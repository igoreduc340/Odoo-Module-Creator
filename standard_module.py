import subprocess
import os
import sys

# Verifica se o nome da pasta destino foi passado como argumento
if len(sys.argv) != 3:
    print("Uso: python3 standard_module.py <nome_do_modulo> <nome_do_modelo>")
    sys.exit(1)
    
nome_do_modulo = sys.argv[1]
nome_do_modelo = sys.argv[2]
caminho_conf = '/home/user/Projects/scripts/config.txt'

# Lendo o arquivo de configuração e criando um dicionário
caminhos = {}
with open(caminho_conf, 'r') as arquivo:
    for linha in arquivo:
        # Dividindo a linha em chave e valor
        chave, valor = linha.strip().split(' = ')
        caminhos[chave] = valor

try:
    destino_vscode = caminhos.get('destino_vscode',False)
    destino = caminhos.get('destino',False) + f'/{nome_do_modulo}'

except Exception as e:
    print(f"Ocorreu um erro no arquivo de configurações: {e}")

# Tenta executar o script
try:  
    os.mkdir(destino)
    os.mkdir(destino + "/views")
    os.mkdir(destino + "/models")
    
     #Configura o arquivo __init__
    with open(destino + '/models/__init__.py', 'w') as arquivo:
        arquivo.write(f"from . import {nome_do_modelo}")
        
    #Configura o arquivo python
    with open(destino + f'/models/{nome_do_modelo}.py', 'w') as arquivo:
        arquivo.write(
f"""# -*- coding: utf-8 -*-    
from odoo import api, fields, models

class {"".join(word.capitalize() for word in nome_do_modelo.split('_'))}(models.Model):
    _inherit = '{nome_do_modelo.replace('_',".")}'

    godoo_field = fields.Char()""")
        
        
    #Configura o arquivo xml
    with open(destino + f'/views/{nome_do_modelo}.xml', 'w') as arquivo:
        arquivo.write(
f"""<odoo>
    <data>
            <!-- View Form para modificar -->
            <record id="view_{nome_do_modelo}_form_inherit" model="ir.ui.view">
                <field name="name">view.{nome_do_modelo.replace('_','.')}.form.inherit</field>
                <field name="model">{nome_do_modelo.replace('_',".")}</field>
                <field name="inherit_id" ref=""/>
                <field name="arch" type="xml">

                    <xpath expr="//field[@name='name']" position="">
                         <field name="name"/>
                    </xpath>

                </field>
            </record>

            <!-- View Tree para modificar -->
             <record id="view_{nome_do_modelo}_tree_inherit" model="ir.ui.view">
                <field name="name">view.{nome_do_modelo.replace('_','.')}.tree.inherit</field>
                 <field name="model">{nome_do_modelo.replace('_',".")}</field>
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
    with open(destino + '/__manifest__.py', 'w') as arquivo:
        arquivo.write(
f"""{{
    'name': '{" ".join(word.capitalize() for word in nome_do_modulo.split('_'))}',
    'version': '1.0',
    'description': '',
    'author': 'Asisto - Igor Carvalho',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        
        ],
    'data': ['views/{nome_do_modelo}.xml'],
    'installable': True,
    'application': True,
}}"""
        )
    subprocess.run(['code', destino_vscode ], check=True)
    
except subprocess.CalledProcessError as e:
    print(f"Ocorreu um erro ao criar o diretório: {e}")
