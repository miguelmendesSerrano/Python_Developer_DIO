from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
# atributos
    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    fullname = Column(String(30))

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)

# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# investiga o esquema do banco de dados
inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    miguel = User(
        name='miguel',
        fullname='Miguel Mendes Serrano',
        address=[Address(email_address='miguelms@email.com')]
    )

    joao = User(
        name='joao',
        fullname='Joao Silva',
        address=[Address(email_address='joao@email.br'),
                 Address(email_address='joaosilva@email.org')]
    )

    maria = User(name='maria', fullname='Maria do Carmo')

    session.add_all([miguel, joao, maria])

    session.commit()

stmt = select(User).where(User.name.in_(['miguel', 'joao']))
print("Recuperando usuários a partir de condição de filtragem")
for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
print("\nRecuperando os endereços de email de Joao")
for address in session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc())
print("\nRecuperando info de maneira ordenada")
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
print()
for result in session.scalars(stmt_join):
    print(result)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\nExecutando statement a partir da connection")
for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(User)
print("\nTotal de instâncias em User")
for result in session.scalars(stmt_count):
    print(result)

session.close()
