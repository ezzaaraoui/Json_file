import json 

d = {
    "nom": "Ayoub",
    "age": 19,
    "ville": "Marrakech"
}


with open("d.json", "w") as json_file:
    json.dump(d, json_file, indent=2)


with open("d.json", "r") as json_file:
    data = json.load(json_file)
    print("Le contenu est:")
    print(data)


data["langage"] = "js"


with open("d.json", "w") as json_file:
    json.dump(data, json_file, indent=2)


with open("d.json", "r") as json_file:
    m_data = json.load(json_file)
    print("Le contenu après modification est:")
    print(m_data)
