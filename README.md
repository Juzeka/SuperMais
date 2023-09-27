
# Teste para vaga FullStack Jr.

Um simples e-commece de mercadinho feito em django.


## Instalação

Para a Instalação execute os seguintes comandos no terminal.

- Clone o projeto em:
```bash
git clone https://github.com/Juzeka/SuperMais.git
```

- Ativando o ambiente:
```bash
. venv/bin/activate
```

- Instalação das dependências:
```bash
pip install -r requirements.txt
```

### Criação das variáveis de ambiente
Crie um arquivo .env na pasta do projeto (onde o arquivo manage.py se encontra) e no terminal execute:

- Execute o comando:
```bash
python3
```

- Entre com:
```bash
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```
com a chave exibida pelo print cole no arquivo .env:
```bash
SECRET_KEY = 'chave gerada aqui!'
DEBUG = True
...
```


## Rodando o server

- Rode as makemigrations:
```bash
python3 manage.py makemigrations
```
- Rode as migrations:
```bash
python3 manage.py migrate
```
- Rode o servidor:
```bash
python3 manage.py runserver
```
