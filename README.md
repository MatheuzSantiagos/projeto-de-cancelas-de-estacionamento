# Projeto de cancelas de estacionamento

## Ambiente local

Na raiz do repositório, crie e ative o ambiente virtual e instale as dependências:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Prepare o banco SQLite e inicie o servidor:

```bash
python projsala/manage.py migrate
python projsala/manage.py runserver
```

A aplicação fica disponível em http://127.0.0.1:8000/ e o admin em http://127.0.0.1:8000/admin/.

Para criar um usuário administrador, execute `python projsala/manage.py createsuperuser`.

## Configuração

O projeto usa português do Brasil e o fuso horário `America/Sao_Paulo`. Para desenvolvimento, `DEBUG` fica ligado por padrão. As opções podem ser definidas por variáveis de ambiente:

- `DJANGO_SECRET_KEY`: segredo da aplicação; defina um valor próprio fora do desenvolvimento local.
- `DJANGO_DEBUG`: use `true` ou `false`.
- `DJANGO_ALLOWED_HOSTS`: hosts permitidos separados por vírgula; por padrão, `localhost,127.0.0.1`.

Não use o valor de segredo padrão nem `DEBUG=true` em produção.
