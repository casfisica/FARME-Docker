from fastapi import APIRouter

#To create new routes 
user = APIRouter()

@user.get("/users")
def tryUser():
    return "tryUser function called"