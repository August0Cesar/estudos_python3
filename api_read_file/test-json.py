import json

string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr)

dados = {
    "nome": 'b"Renato Lelis"',
    "profissao": "Desenvolvedor de sistemas"
}
with open("dados.json", "w") as json_file:
    json.dump(dados, json_file, indent=4)

# print(str.encode("my_str"))