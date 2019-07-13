
import datetime
import hashlib

import sqlalchemy


URL = 'sqlite:///teste.db'
engine = sqlalchemy.create_engine(URL, echo=True)

metadata = sqlalchemy.MetaData(bind=engine)

user_table = sqlalchemy.Table(
    'usuarios',
    metadata,
    sqlalchemy.Column(
        'id', 
        sqlalchemy.Integer, 
        primary_key=True
    ),
    sqlalchemy.Column(
        'nome', 
        sqlalchemy.String(40), 
        index=True,
    ),
    sqlalchemy.Column(
        'idade', 
        sqlalchemy.Integer, 
        nullable=False
    ),
    sqlalchemy.Column(
        'senha', 
        sqlalchemy.String
    ),
    sqlalchemy.Column(
        'criado_em', 
        sqlalchemy.DateTime, 
        default=datetime.datetime.now
    ),
    sqlalchemy.Column(
        'atualizado_em', 
        sqlalchemy.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now
    )
)

metadata.create_all(engine)

con = engine.connect()
insert = user_table.insert()

con.execute(
    insert.values(
        idade=26,
        nome='Lucas Ricciardi de Salles',
        senha='4linux'
    )
)

for result in sqlalchemy.select([ user_table ]).execute():
    print(result)

def cadastrar_usuario(nome, idade, senha):
    con.execute(
    insert.values(
            idade=idade,
            nome=nome,
            senha=hashlib.md5(senha.encode()).hexdigest()
        )
    )

# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))
# senha = input('Digite sua senha: ')

# cadastrar_usuario(nome, idade, senha)

res = sqlalchemy.update(user_table).where(
    user_table.c.nome == 'Lucas Ricciardi de Salles'
).values(nome='Professor').execute()

def selecionar_usuarios_por_idade():

    resultados = 0
    idade = int(input('Digite uma idade: '))

    # Lógica aqui
    resultados = len([ r for r in sqlalchemy.select(
        [ user_table ]
    ).where(user_table.c.idade == idade).execute() ])

    print('Temos {} usuários com a idade {}'.format(
        resultados, idade
    ))

selecionar_usuarios_por_idade()

res = sqlalchemy.delete(user_table).where(
    user_table.c.idade == 26
).execute()

print('{} registros deletdos'.format(res.rowcount))


sqlalchemy.insert(user_table).where().execute()
sqlalchemy.update(user_table).where().execute()
sqlalchemy.select(user_table).where().execute()
sqlalchemy.delete(user_table).where().execute()