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