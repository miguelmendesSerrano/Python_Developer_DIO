"""
    Implementar banco de dados NoSQL com MongoDB via pyMongo, persistir e manipular documentos no DB.
"""
import pymongo as pyM

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
