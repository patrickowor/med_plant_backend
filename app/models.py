from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    ''' this is an example user model for sqlmodel'''
    id: int = Field(default=None, primary_key=True)
    name : str
    email: str = Field(unique=True)
    password : str 

class Token(SQLModel, table=True):
    ''' this is an example user model for sqlmodel'''
    id: int = Field(default=None, primary_key=True)
    token: str
    user_id: int
