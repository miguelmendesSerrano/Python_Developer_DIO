"""
    Implementar banco de dados NoSQL com MongoDB via pyMongo, persistir e manipular documentos no DB.
"""
import pymongo as pyM
import pprint

# Conectando com banco de dados
client = pyM.MongoClient("mongodb+srv://pymongo:pymongo@cluster1.yoczfda.mongodb.net/?retryWrites=true&w=majority")

db = client.test
bank = db.test_bank

# Definindo infos para compor o docmento
cliente = {
    "name": "Joao da Silva",
    "Cpf": "000.000.000",
    "Endereço": "Rua Zero",
    "Tipo conta": "Corrente",
    "Agencia": "0001",
    "Num_conta": "1",
    "Saldo": 0
}

# Preparando para submeter as infos
clientes = db.clientes
cliente_id = clientes.insert_one(cliente).inserted_id
print(cliente_id)

pprint.pprint(db.clientes.find_one())

# Bulk inserts
new_clientes = [{
        "name": "Joao da Silva",
        "Cpf": "000.000.000",
        "Endereço": "Rua Zero",
        "Tipo conta": "Corrente",
        "Agencia": "0001",
        "Num_conta": "1",
        "Saldo": 0},
        {
        "name": "Maria da Silva",
        "Cpf": "111.000.000",
        "Endereço": "Rua Um",
        "Tipo conta": "Corrente",
        "Agencia": "0001",
        "Num_conta": "2",
        "Saldo": 0}]

result = clientes.insert_many(new_clientes)
print(result.inserted_ids)

# Recuperando primeira instância
pprint.pprint(db.clientes.find_one())

# Recuperando a partir de um parâmetro específico
pprint.pprint(db.clientes.find_one({"name": "Joao da Silva"}))

# Recuperando documentos dentro da coleção clientes
for cliente in clientes.find():
    pprint.pprint(cliente)

# Contando quantos documentos foram persistidos
print(clientes.count_documents({}))

# Recuperando info de maneira ordenada
for cliente in clientes.find({}).sort("name"):
    pprint.pprint(cliente)

# Inserindo indices para otimizar a recuperação de infos
results = db.profiles.create_index([("name", pyM.ASCENDING)], unique=True)

print(sorted(list(db.profiles.index_information())))

# Criando profiles de usuários

user_profile = [
    {"user_id": 100, "name": "Pedro"},
    {"user_id": 101, "name": "Julia"}]

# Criando coleção profiles
profiles = db.profile_user.insert_many(user_profile)

# Recuperando coleções armazenadas
collections = db.list_collection_names()

for collection in collections:
    print(collection)

# Removendo coleção
db.profiles.drop()

# Removendo documentos
clientes.delete_one({"name": "Joao da Silva"})

# Deletando banco de dados
client.drop_database("test")
