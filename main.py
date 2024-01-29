# from fastapi import FastAPI, status, HTTPException
# from pydantic import BaseModel
# from typing import List


# from data.users import users_list

# class User( BaseModel):
#     id: int
#     username: str
#     password: str
#     is_admin: bool

# class UsersResponse( BaseModel ):
#     status: int
#     users: List [User]

# class UserResponse( BaseModel ):
#     status: int
#     user: User


# app = FastAPI()

# @app.get('/')
# def index():
#     return {
#         'messagge': 'Hello, grettings!!!'
#     }

# @app.get('/users', status_code = status.HTTP_200_OK, response_model = UsersResponse )
# def get_users():
#     return {
#         'status': 200,
#         'users': users_list
#     }

# @app.get ('/users/{ user_id }', status_code = status.HTTP_200_OK, response_model = UserResponse )
# def get_user(user_id: int ):
#     for user in users_list:
#         if user ['id'] == user_id:
#             return{
#                 'status': 200,
#                 'user': user
#             }
#     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'User not Found')

# @app.post ('/users', status_code = status.HTTP_201_CREATED, response_model = UserResponse)
# def create_user( user_data: User ):
#     new_user = user_data.model_dump()
#     password = new_user [ 'password']
#     new_user ['password'] = f'{ password }#password'
#     users_list.append( new_user )


#     return{
#         'status': 201,
#         'user': new_user
#     }

# @app.put ('/users/ {user_id}', status_code = status.HTTP_200_OK, response_model = UserResponse)
# def update_user ( user_id: int, user_data: User):
#     for user in users_list:
#         if user [ 'id' ] == user_id:
#             user [ 'username' ] == user_data.username
#             user [ 'password' ] == user_data.password
#             user [ 'is_admin' ] == user_data.is_admin

#             return {
#                 'status': 200,
#                 'user': user
#             }
#     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'User not Found')
        
        
# @app.delete ('/users/ { user_id }', status_code = status.HTTP_204_NO_CONTENT)
# def delete_user(user_id: int):
#     for user in users_list:
#         if user ['id'] == user_id:
#                 users_list.remove(user)
#                 return{
#                 'status': 200,
#                 'user': user
#                 }
#     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'User not Found')
        