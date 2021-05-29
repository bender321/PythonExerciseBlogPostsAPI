from fastapi import FastAPI, Depends, HTTPException
from fastapi_pagination import PaginationParams, Page
from fastapi_pagination.paginator import paginate
from DB import post, database
import models as pmodels
import datetime


app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get('/posts', response_model=Page[pmodels.AllPosts], tags=['Posts'])
async def get_all_posts(params: PaginationParams = Depends()):
    query = post.select()
    res = await database.fetch_all(query)
    return paginate(res, params)


@app.get('/post{post_id}', response_model=pmodels.OnePost, tags=['Posts'])
async def get_one_post(post_id: int):
    query = post.select().where(post.c.id == post_id)
    res = await database.fetch_one(query)
    if res is None:
        raise HTTPException(status_code=404, detail="Item not found.")
    else:
        return res


@app.post('/newpost', response_model=pmodels.PostCreation, tags=['Posts'])
async def create_post(p: pmodels.PostCreation):

    gDate = datetime.datetime.utcnow()

    query = post.insert().values(

        name=p.name,
        content=p.content,
        date_creation=gDate
    )
    await database.execute(query)
    return {
            **p.dict(),
            "date_creation": gDate
    }


@app.put('/post{post_id}', response_model=pmodels.PostUpdate, tags=['Posts'])
async def edit_post(p: pmodels.PostUpdate):

    gDate = datetime.datetime.utcnow()

    query = post.update().where(post.c.id == p.id).values(
        id=p.id,
        name=p.name,
        content=p.content,
        date_creation=gDate
    )
    await database.execute(query)
    return await get_one_post(p.id)


@app.delete('/post{post_id}', tags=['Posts'])
async def delete_post(p: pmodels.PostDelete):
    query = post.delete().where(post.c.id == p.id)
    await database.execute(query)
    return {
        "status": True,
        "message": "This post has been deleted successfully."
    }
