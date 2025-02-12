# Pagamentos API - Sistema de Cobrança de Clientes

## Descrição
Um sistema completo para controle de pagamentos a receber de clientes, desenvolvido com Django REST Framework, React, MySQL e integração com PIX.

## Tecnologias Utilizadas
- Backend: Django REST Framework (DRF)
- Banco de Dados: MySQL
- Autenticação: Token JWT
- Controle de Acessos: Django Groups & Permissions
- Pagamentos: Integração com PIX
- Notificações: Envio de e-mails para cobrança
- Logs e Auditoria: Middleware para rastrear transações
- Agendamento de Cobranças: Jobs automáticos via Django Commands
- Frontend: React.js


## Funcionalidades da API

- Cadastro e Gerenciamento de Clientes
  - Criar, listar, editar e excluir clientes
  - Clientes têm nome, e-mail, telefone e endereço
- Produtos e Vendas
  - Cadastro de produtos com preço de compra e venda
  - Registro de vendas associadas a clientes
- Controle de Pagamentos
  - Pesquisa de pagamentos por data
  - Filtro de clientes com vencimento no dia
- Autenticação e Controle de Acessos
  - Autenticação via JWT Token
  - Controle de permissões por grupos (Admin, Financeiro, Vendedor)
- Logs e Auditoria de Transações
  - Registro automático de ações no sistema
  - Middleware para salvar logs de acessos
- Integração com PIX
  - Geração automática de QR Code para pagamento
  - Verificação de status do pagamento
- Agendamento de Cobranças Automáticas
  - Envio de lembretes de pagamento via e-mail
  - Agendamento de tarefas com Django Commands


## Como Rodar o Projeto

- git clone https://github.com/douglasinforj/pagamentosAPI_Sistema_de_cobranca_de_clientes.git
- cd pagamentosAPI_Sistema_de_cobranca_de_clientes

##  Configurar o Backend (Django)

- Criar o ambiente virtual:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

- Instalar as dependências:
pip install -r requirements.txt

- Criar o banco de dados e rodar as migrações:
python manage.py migrate

- Criar um superusuário para login:
python manage.py createsuperuser

- Rodar o Servidor
python manage.py runserver

## Endpoints da API









## Estrutura do Projeto Inicialmente

`
/backend
 ├── api
 │   ├── models.py      # Modelos do banco de dados
 │   ├── views.py       # Endpoints da API
 │   ├── serializers.py # Serializadores DRF
 │   ├── urls.py        # Rotas da API
 │   ├── middlewares.py # Logs e auditoria
 │   ├── tasks.py       # Agendador de tarefas
 │
 ├── payments
 │   ├── services.py    # Integração com PIX
 │
 ├── users
 │   ├── authentication.py # Login e permissões
 │
 ├── manage.py
 ├── README.md
/frontend
 ├── src
 │   ├── components/
 │   ├── pages/
 │   ├── services/
 ├── package.json
 ├── index.js

`