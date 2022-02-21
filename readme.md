===criei um formulario para registrar funcionarios, dessa forma a empresa tenha os dados organizados dos seus funcionarios e mantendo a organização.===


Endpoints + METODOS GET/PUT/DELETE

api/v1/funcionario = cadastrar um funcionario
api/v1/funcionario/id = editar ou deletar o cadastro de um funcionario

#MODELO_DE_CADASTRO (JSON)

{
    "nome":"",
    "usuario":"",
    "identificador":null,
    "ano": null
    "image":null
}

* A IMPLEMENTAR
-status: 'empregado' ou 'demitido'

#EXECUTANDO_O_PROJETO:

* executando pelo:
python manage.py runserver
o endereço será 127.0.0.1:8000

*HEROKU
cads-06.herokuapp.com


