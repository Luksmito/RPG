import json



with open("criaturas","r") as json_file:
    lista = json.load(json_file)
    print(lista)