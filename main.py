#Python
from typing import Optional, List

#FastAPI
from fastapi import FastAPI
from fastapi import status

#From modules
from models.users import User
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
def signup():
    pass 
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
    pass 

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
    status_code=status.HTTP_201_OK,
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
