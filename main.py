from fastapi import FastAPI
from data.users import users_list

app = FastAPI()

@app.get('/')
def index():
    return {
        'messagge': 'Hello, grettings!!!'
    }

@app.get('/users')
def get_users():
    return {
        'status': 200,
        'users': users_list
    }