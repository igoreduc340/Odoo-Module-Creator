# Standard Module Generator for Odoo

Este script Python ajuda a gerar um módulo Odoo básico, incluindo arquivos essenciais como modelos, visões, arquivos de inicialização e manifesto. O script cria os diretórios necessários, configura os arquivos com as informações fornecidas e abre o arquivo Python do modelo no VSCode para facilitar o desenvolvimento.

## Pré-requisitos

- **Python 3.x**  
  O script requer a versão 3.x do Python para funcionar corretamente.

- **VSCode**  
  O script utiliza o comando `code` para abrir arquivos no Visual Studio Code.

## Instalar dependências

Para instalar as dependências necessárias, crie um ambiente virtual ou use o Python global e execute o seguinte comando:

```bash
pip install -r requirements.txt
´´´

Configuração do ambiente

Antes de executar o script, você precisa configurar um arquivo .env contendo as variáveis de ambiente necessárias para o script. Essas variáveis definem os caminhos de destino onde o módulo será gerado, no projeto existe um arquivo chamado env.example , apos a configuração troque o nome dele para .env

Exemplo de arquivo:

```ini
DESTINO_VSCODE_SYLVIA=/caminho/para/o/vscode/sylvia
DESTINO_MODULOS_SYLVIA=/caminho/para/o/modulo/sylvia

DESTINO_VSCODE_ASISTO_BASE=/caminho/para/o/vscode/asisto-base
DESTINO_MODULOS_ASISTO_BASE=/caminho/para/o/modulo/asisto-base

DESTINO_VSCODE_NAVE=/caminho/para/o/vscode/nave
DESTINO_MODULOS_NAVE=/caminho/para/o/modulo/nave
```
Uso

``` python3 app.py```


O que o script faz

Cria a estrutura de diretórios:

Cria os diretórios necessários, como views/, models/, etc.

Cria o arquivo Python do modelo:

Gera o arquivo models/my_model.py com um esqueleto básico de modelo Odoo,

Cria o arquivo de visão (XML):

Após a criação do arquivo do modelo, o script abre automaticamente o arquivo Python no VSCode, usando o comando code.