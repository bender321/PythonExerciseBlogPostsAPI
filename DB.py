import databases
import sqlalchemy

#database setup
DATABASE_URL = "sqlite:///./store.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

post = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String(20)),
    sqlalchemy.Column("content", sqlalchemy.String(500)),
    sqlalchemy.Column("date_creation", sqlalchemy.DateTime())
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
