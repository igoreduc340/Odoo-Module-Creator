import subprocess
import os
import sys
from dotenv import load_dotenv  # type: ignore

load_dotenv()
# Verifica se todos os argumentos foram passados
if len(sys.argv) != 4:
    print("Uso: python3 standard_module.py <module_name> <model_name> <odoo_instance>")
    sys.exit(1)

module_name = sys.argv[1]
model_name = sys.argv[2]
odoo_instance = sys.argv[3]

try:
    if odoo_instance == 'Sylvia Design':
        vscode_destination = os.getenv('DESTINO_VSCODE_SYLVIA')
        modules_destination = os.path.join(os.getenv('DESTINO_MODULOS_SYLVIA'), module_name)

    elif odoo_instance == 'Asisto Base':
        vscode_destination = os.getenv('DESTINO_VSCODE_ASISTO_BASE')
        modules_destination = os.path.join(os.getenv('DESTINO_MODULOS_ASISTO_BASE'), module_name)

    elif odoo_instance == 'Nave':
        vscode_destination = os.getenv('DESTINO_VSCODE_NAVE')
        modules_destination = os.path.join(os.getenv('DESTINO_MODULOS_NAVE'), module_name)
    
except Exception as e:
    print(f"Ocorreu um erro ao capturar as variáveis de ambiente: {e}")
    sys.exit()

# Tenta executar o script
try:
    os.makedirs(modules_destination)
    os.makedirs(os.path.join(modules_destination, "views"))
    os.makedirs(os.path.join(modules_destination, "models"))
    
    # Configura o arquivo __init__.py
    with open(os.path.join(modules_destination,'__init__.py'), 'w') as file:
        file.write(f"from . import models")

    # Configura o arquivo __init__.py
    with open(os.path.join(modules_destination, 'models', '__init__.py'), 'w') as file:
        file.write(f"from . import {model_name}")

    # Configura o arquivo Python
    with open(os.path.join(modules_destination, 'models', f'{model_name}.py'), 'w') as file:
        file.write(
f"""# -*- coding: utf-8 -*-
from odoo import api, fields, models

class {"".join(word.capitalize() for word in model_name.split('_'))}(models.Model):
    _inherit = '{model_name.replace('_', ".")}'

    godoo_field = fields.Char()""")

    # Configura o arquivo XML
    with open(os.path.join(modules_destination, 'views', f'{model_name}.xml'), 'w') as file:
        file.write(
f"""<odoo>
    <data>
            <!-- View Form para modificar -->
            <record id="view_{model_name}_form_inherit" model="ir.ui.view">
                <field name="name">view.{model_name.replace('_', '.').replace(' ', '_')}.form.inherit</field>
                <field name="model">{model_name.replace('_', ".")}</field>
                <field name="inherit_id" ref=""/>
                <field name="arch" type="xml">

                    <xpath expr="//field[@name='name']" position="">
                         <field name="name"/>
                    </xpath>

                </field>
            </record>

            <!-- View Tree para modificar -->
             <record id="view_{model_name}_tree_inherit" model="ir.ui.view">
                <field name="name">view.{model_name.replace('_', '.').replace(' ', '_')}.tree.inherit</field>
                 <field name="model">{model_name.replace('_', ".")}</field>
                <field name="inherit_id" ref=""/>
                <field name="arch" type="xml">

                    <xpath expr="//field[@name='name']" position="">
                         <field name="name"/>
                    </xpath>

                </field>
            </record>
    </data>
</odoo>""")

    # Configura o arquivo __manifest__.py
    with open(os.path.join(modules_destination, '__manifest__.py'), 'w') as file:
        file.write(
f"""{{
    'name': '{" ".join(word.capitalize() for word in module_name.split('_'))}',
    'version': '1.0',
    'description': '',
    'author': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [],
    'data': ['views/{model_name}.xml'],
    'installable': True,
    'application': True,
}}"""
        )
    subprocess.run(['code', vscode_destination,os.path.join(modules_destination, 'models', f'{model_name}.py')], check=True)

except subprocess.CalledProcessError as e:
    print(f"Ocorreu um erro ao criar o diretório: {e}")
