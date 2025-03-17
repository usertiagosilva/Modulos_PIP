# JSON é um formato de dados muito utilizado para comunicação entre sistemas. Ele é muito parecido com um dicionário em Python, com chaves e valores. O JSON é uma string, então para manipulá-lo em Python, é necessário convertê-lo para um dicionário. Para isso, utilizamos a função loads() do módulo json.
import json

# 1 - Strings para dicionários:
person = '{"name": "Rodrigo", "languages": ["Python", "Java"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languages'])

# 2 - Dicionários para json:
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))
print(type(person_dict))

# 3 - Formatando json:
print(json.dumps(person_dict, indent=4, sort_keys=True))

# 4 - Salvando json em arquivo txt:
with open("person.txt", "w") as json_file:
    json.dump(person_dict, json_file)
   
# 5 - Lendo json externo:
with open("iris.json", "r") as f:
    data = json.load(f)
    print(data)
    print(type(data))