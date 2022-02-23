### Criei um formulario para registrar funcionarios, dessa forma a empresa tenha os dados organizados dos seus funcionarios e mantendo a organização.


## Endpoints

| Endpoint | Método | Ação |
|--|--|--|
| /api/v1/funcionario/ | GET | Listar os funcionarios |
| /api/v1/funcionario/:id| GET | Informação de um funcionario |
| /api/v1/funcionario/:id| DELETE | Deletar os dados de um funcionario |

## DEPLOY

- Criar o ambiente virtual
```
python -m venv venv
```
- Ative o ambiente
```
.\Venv\Scripts\activate
```
- instalar os pacotes necessários para executar o projeto
```
pip install -r requirements.txt
```
- Execute a criação de tabela no banco de dados
```
python manage.py makemigrations
python manage.py migrate
```
- criando um super usuario para executar o projeto _(opcional)_
```
python manage.py create superuser
```
- ao final desse passo o projeto sera executado no endereço:

[127.0.0.1:8000](http://127.0.0.1:8000/)
### MODELO_DE_CADASTRO (JSON)
```
{
    "nome":"",
    "usuario":"",
    "identificador":null,
    "ano": null
    "image":null
}
```

### A IMPLEMENTAR
-  status: 'empregado' ou 'demitido'

[link](http://127.0.0.1:8000/) 

*HEROKU
```
cads-06.herokuapp.com
```