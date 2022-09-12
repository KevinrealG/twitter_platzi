
# Python
import json
from typing import Optional, List

# Pydantic

from pydantic import Field

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body
#From modules
from models.users import UserRegister, User 
from models.tweet import Tweet


app = FastAPI()


# operations


## Users


### Create User
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    tags=["Users"]

    )
def signup(user: UserRegister = Body(...)):
    """
    Register a new user
    This path is used to register a new user in the system.

    parameters:
        - user: UserRegister

    responses:
        201: return a JSON with the basic user data:
                -   user_id: UUID
                -  email: EmailStr
                -  first_name: str
                -  last_name: str
                -  birth_date: Optional[date]
        400: Bad Request
    """
    
    with open("users.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read()) #Read the file, convert to JSON
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict) #Agregamos el nuevo usuario a la lista
        f.seek(0)# rewind to the beginning of the file
        f.write(json.dumps(results))# write the new data, converts dumps() the list of dictionarie  to JSON
        return user 
### Login User
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a new user",
    tags=["Users"]

    )
def login():
    pass 
### Get all users
@app.get(
    path="/users",
    response_model=list[User],
    status_code=status.HTTP_200_OK,
    summary="Show all  user",
    tags=["Users"]

    )
def show_all_users():
    """
        This Path is used to show all users in the system
        Parameters:
            - None
        Returns a JSON list with all users, with the following keys   
                    -   user_id: UUID
                -  email: EmailStr
                -  first_name: str
                -  last_name: str
                -  birth_date: Optional[date]
    """
    with open("users.json", "r", encoding="utf-8") as f: 
        results = json.loads(f.read())
        return results

### Get a user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a particular user",
    tags=["Users"]

    )
def show_a_user():
    pass 

### Delete a user
@app.delete(
    path="/login/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a  user",
    tags=["Users"]

    )
def delete_a_user():
    pass 
### Update a user
@app.put(
    path="/login/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a  user",
    tags=["Users"]

    )
def delete_a_user():
    pass 
## tweets

### Show al tweet
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
    )
def home():
    return {"Twitter Api": "Working"}

### Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
    )
def post():
    pass

### show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
)
def show_a_tweet():
    pass

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,   
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_a_tweet():
    pass
