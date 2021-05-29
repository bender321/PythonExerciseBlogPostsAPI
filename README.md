# PythonExerciseBlogPostsAPI
### Job Interview task: 
- Create an easy blog management Rest API in Python using Fast API.
### Main functions:
- Creating a new blog post
- Editing blog post
- Deleting blog post
- List all blog posts
- View blog post detail

## Requirements:
- Python >= 3.7
- databases >= 0.4.3
- SQLAlchemy >= 1.3.24
- fastapi >= 0.65.1
- fastapi-pagination >= 0.7.3
- pydantic >= 1.8.2
- aiosqlite >= 0.17.0

## Dev server:
- uvicorn >= 0.13.4

## Database used (optional):
- sqlite

## Instalation:
- create virtual enviroment 
- make sure that all requirements are satisfied
- install uvicorn for running dev server
- use your prefered database, do setup of it and then in file: DB.py on line 5: DATABASE_URL = "sqlite:///./store.db" (Change option in quotations marks according to your database that you wish to use. More details here: https://docs.sqlalchemy.org/en/14/core/engines.html
- then in terminal run this command: ```uvicorn main:app --reload```
- if server is running and there is no error message then everything is OK
- otherwise error messages should be explanatory enough to give a solution for fix (missing packages etc.)
## Test usage:
- if server is running you can go on this default adress: http://127.0.0.1:8000/docs
- it is an interactive documentation for FastAPI where you can test functions via GUI (you can also use raw url in browser).
### there is five main functions for working with API:
#### GET /posts (Get all posts):
- for listing names of all posts in database, there is a pagination that you can manage with how many items should be in body of one response
- for example: page: 0 with number of items: 2 -> URL: http://127.0.0.1:8000/posts?page=0&size=2
#### GET /post{post_id} (Get one post):
- for getting details about one specific post defined by it's ID
- for example: 1 -> URL: http://127.0.0.1:8000/post1
#### PUT /post{post_id} (Edit post):
- for updating name and content of specific post defined by it's ID (date of change is generated automaticaly)
####  DELETE /post{post_id} (Delete post):
- for deleting specific post defined by it's ID
##### Important: 
- if you delete for example post{1} then pagination is starting from next post which has ID{2}, but you can no longer search for or edit post with ID{1}
- if you try so in case of search you will recive null 
- if you try edit deleted post you will recive null
#### POST /newpost (Create post):
- for creating a new post (name of post and it's content, ID and date of creation is generated automaticaly) and storing it in database
