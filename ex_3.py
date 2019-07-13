
# Criar uma tabela times que contenha as colunas
# nome,
# estadio,
# ano_de_fundacao,

import sqlalchemy


URL = 'sqlite:///teste.db'
engine = sqlalchemy.create_engine(URL, echo=True)

metadata = sqlalchemy.MetaData(bind=engine)

times = sqlalchemy.Table('times', metadata,

    sqlalchemy.Column(
        'id',
        sqlalchemy.Integer,
        primary_key=True
    ),

    sqlalchemy.Column(
        'nome',
        sqlalchemy.String(255),
        index=True   
    ),

    sqlalchemy.Column(
        'estadio',
        sqlalchemy.String(255),
    ),

    sqlalchemy.Column(
        'ano_de_fundacao',
        sqlalchemy.Integer
    )

)

res = sqlalchemy.insert(times).values(
    nome='Corinthians',
    estadio='Itaquerão',
    ano_de_fundacao=1910
)

print(res)