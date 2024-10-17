from instagrapi import Client
# from instagrapi.types import StoryMedia
import os

# Create a client instance
cl=Client()

# Login
def login(user,passw):
    try:
        cl.login(user,passw)
        print("Login Success")
    except Exception as e:
        print(e)

print("Enter your username and password")
user=input("Username: ")
passw=input("Password: ")
login(user,passw)