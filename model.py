from peewee import Model, CharField, MySQLDatabase

db = MySQLDatabase(
    user='root',
    password='Password08',
    host='localhost',
    database='database'
)


class BaseModel(Model):
    class Meta:
        database = db


class Course(BaseModel):
    name = CharField(255)
    title = CharField(255)
