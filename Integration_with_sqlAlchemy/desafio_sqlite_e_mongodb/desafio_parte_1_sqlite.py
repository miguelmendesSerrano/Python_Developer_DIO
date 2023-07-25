"""
    Implementando um Banco de Dados Relacional com SQLAlchemy.
    Implementar uma aplicação de integração com SQLite com base em um esquema relacional
     dentro do contexto de cliente e conta (sistema bancário)
"""
from sqlalchemy.orm import (
    relationship,
    declarative_base,
    Session
)
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    create_engine,
    inspect,
    select,
    Float
)

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    cpf = Column(String(9), nullable=False)
    address = Column(String(40))

    conta = relationship("Conta", back_populates="cliente")

    def __repr__(self):
        return f"Cliente(id={self.id}, name={self.name}, cpf={self.cpf} address={self.address})"


class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("cliente.id"))
    tipo_conta = Column(String, default="conta corrente")
    agencia = Column(String, default="0001")
    num_conta = Column(Integer, unique=True)
    saldo = Column(Float, default=0)

    cliente = relationship("Cliente", back_populates="conta")

    def __repr__(self):
        return f"Conta(id={self.id},tipo_conta={self.tipo_conta}, " \
               f"agencia={self.agencia}, num_conta={self.num_conta}, saldo={self.saldo})"


print(Cliente.__tablename__)
print(Conta.__tablename__)

# Conexão com o banco de dados
engine = create_engine("sqlite://")

# Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# Investigando o esquema do banco de dados
inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("cliente"))
print(inspetor_engine.get_table_names())

# Criando Sessão para persistir registros no banco de dados
with Session(engine) as session:
    joao = Cliente(
        name="Joao da Silva",
        cpf="000.000.000",
        address="Rua Zero",
        conta=[Conta(id=1)]
    )

    maria = Cliente(
        name="Maria da Silva",
        cpf="111.000.000",
        address="Rua Um",
        conta=[Conta(id=2)]
    )
    session.add_all([joao, maria])

    session.commit()
# Recuperando usuários a partir de condição de filtragem
    stmt = select(Cliente).where(Cliente.name.in_(["Joao da Silva", "Maria da Silva"]))
    for cliente in session.scalars(stmt):
        print(cliente)
# # Recuperando contas por id
    stmt_conta = select(Conta).where(Conta.id.in_([1, 2]))
    for conta in session.scalars(stmt_conta):
        print(conta)

    session.close()
