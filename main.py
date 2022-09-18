
# Python
import json
from typing import Optional, List
from urllib import response

# Pydantic

from pydantic import Field

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Query
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
def login(
    email: str = Body(...),
    password: str = Body(...)

):
    """
    Login a old user
    This path is used to login registeed user in the system.

    parameters:
        - user: UserRegister

    responses:
        200: return a JSON with the basic user data:
                -   user_id: UUID
                -  email: EmailStr
                -  first_name: str
                -  last_name: str
                -  birth_date: Optional[date]
        400: Bad Request
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        for user in results:
            if user["email"] == email and user["password"] == password:
                return {"message": "Login"}
        return "User not found"
 


### Get all users
@app.get(
    path="/users",
    response_model=list[User],
    status_code=status.HTTP_200_OK,
    summary="Show all  user",
    tags=["Users"]

    )
def show_all_users(

):
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
def show_a_user(
    user_id: str = Query(..., description="The ID of the user to get")


):
    """
        This Path is used to show a user in the system
        Parameters:
            - user_id: str
        Returns a JSON with the following keys   
                    -   user_id: UUID
                -  email: EmailStr
                -  first_name: str
                -  last_name: str
                -  birth_date: Optional[date]
    """
    with open("users.json", "r", encoding="utf-8") as f: 
        results = json.loads(f.read())
        for user in results:
            if user["user_id"] == user_id:
                return user
        return {"message": "User not found"}


### Delete a user
@app.delete(
    path="/login/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a  user",
    tags=["Users"]

    )
def delete_a_user():
    """
        This Path is used to delete a user in the system

        Parameters:
            - user_id: UUID
        Returns a JSON with the following keys
                    -   user_id: UUID
                -  email: EmailStr
                -  first_name: str
                -  last_name: str
                -  birth_date: Optional[date]
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        for user in results:
            if user["user_id"] == user_id:
                results.remove(user)
                f.seek(0)
    return status.HTTP_201_CREATED
     
### Update a user
@app.put(
    path="/login/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a  user",
    tags=["Users"]

    )
def update_a_user(
    user_id: str = Query(..., description="The ID of the user to get"),
    user: UserRegister = Body(...)

):
    """
        This Path is used to update a user in the system

        Parameters:
            - user_id: UUID
        Returns a JSON with the following keys
                    -   user_id: UUID
                -  email: EmailStr
                -  first_name: str
                -  last_name: str
                -  birth_date: Optional[date]
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        for user in results:
            if user["user_id"] == user_id:
                results.remove(user)
                user_dict = user.dict()
                user_dict["user_id"] = str(user_dict["user_id"])
                user_dict["birth_date"] = str(user_dict["birth_date"])
                results.append(user_dict)
                f.seek(0)
    return status.HTTP_201_CREATED


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
    """
    This path is used to show all tweets in the system

    
    parameters:
        - None


    Returns a JSON list with all tweets, with the following keys:
        
        - tweet_id: UUID

        - user_id: UUID

        - tweet: str

        - created_at: datetime

        - updated_at: Optional[datetime]

        - by_user: User
    """
    with open("tweets.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results
    

### Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
    )
def post(tweet: Tweet = Body(...)):
    """
    Post a tweet
    This path is used to post a tweet in the system.


    parameters:
        Reuest Body:
        - tweer: Tweet
        

    Returns a JSON with the basic tweet data:
                -   tweet_id: UUID

                -  user_id: UUID

                -  tweet: str

                -  created_at: datetime

                -  updated_at: Optional[datetime]

                - by: User
        
    """
    with open("tweets.json", "r+", encoding="utf-8") as f: 
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        
        results.append(tweet_dict ) #Agregamos el nuevo usuario a la lista
        f.seek(0)# rewind to the beginning of the file
        f.write(json.dumps(results))# write the new data, converts dumps() the list of dictionarie  to JSON
        return tweet

### show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
)
def show_a_tweet(
    tweet_id: str = Query(..., description="The ID of the tweet to get")
):
    """
    This path is used to show a tweet in the system


    parameters:
        - tweet_id: UUID


    Returns a JSON with the basic tweet data:
                -   tweet_id: UUID

                -  user_id: UUID

                -  tweet: str

                -  created_at: datetime

                -  updated_at: Optional[datetime]

                - by: User
    """
    with open("tweets.json", "r", encoding="utf-8") as f: 
        results = json.loads(f.read())
        for tweet in results:
            if tweet["tweet_id"] == tweet_id:
                return tweet
        return {"message": "Tweet not found"}
    

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,   
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def delete_a_tweet(
    tweet_id: str = Query(..., description="The ID of the tweet to get")
):
    """
    This path is used to delete a tweet in the system


    parameters:
        - tweet_id: UUID


    Returns a JSON with the basic tweet data:
                -   tweet_id: UUID

                -  user_id: UUID

                -  tweet: str

                -  created_at: datetime

                -  updated_at: Optional[datetime]

                - by: User
    """
    with open("tweets.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        for tweet in results:
            if tweet["tweet_id"] == tweet_id:
                results.remove(tweet)
                f.seek(0)
    return status.HTTP_201_CREATED

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_a_tweet(
    tweet_id: str = Query(..., description="The ID of the tweet to get"),
    tweet: Tweet = Body(..., description="The new tweet")
):
    """
    This path is used to update a tweet in the system


    parameters:
        - tweet_id: UUID


    Returns a JSON with the basic tweet data:
                -   tweet_id: UUID

                -  user_id: UUID

                -  tweet: str

                -  created_at: datetime

                -  updated_at: Optional[datetime]

                - by: User
    """
    with open("tweets.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        for tweet in results:
            if tweet["tweet_id"] == tweet_id:
                results.remove(tweet)
                tweet_dict = tweet.dict()
                tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
                tweet_dict["created_at"] = str(tweet_dict["created_at"])
                tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
                tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
                tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
                results.append(tweet_dict)
                f.seek(0)
    return status.HTTP_201_CREATED
