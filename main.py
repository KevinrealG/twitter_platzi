

#FastAPI
from fastapi import FastAPI

#From modules
from models.users import User, UserIn, UserOut




app = FastAPI()


@app.get(path="/")
def home():
    return {"Twitter Api": "Working"}