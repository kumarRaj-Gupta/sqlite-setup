from typing import Annotated

from fastapi import FastAPI, Query, HTTPException, Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int| None = Field(default=None, index=True)
    secret_name:str
    
sql_filename = "database.db"
sql_url = f"sqlite:///{sql_filename}" 

connection_args = {"check_same_thread":False}
engine = create_engine(sql_url,connect_args=connection_args)

def createdb_and_tables():
    SQLModel.metadata.create_all(engine)

"""
Next we need to create Session.
Session is what hold the object in memeory and communicates with the db
through the engine    

To ensure that we use single Session per Request, we'll have to use yield.
Then we create an Annotated dependency SessionDep to simplify the rest of the code that will use this dependency. 
"""
