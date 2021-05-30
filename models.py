from pydantic import BaseModel, Field
from datetime import datetime


class OnePost(BaseModel):

    id: int
    name: str
    content: str
    date_creation: datetime


class AllPosts(BaseModel):
    id: int
    name: str


class PostCreation(BaseModel):

    name: str = Field(..., example="Write name of your post here.")
    content: str = Field(..., example="Write content of your post here.")


class PostUpdate(BaseModel):

    id: int = Field(..., example="Write ID of post you wish to update here.")
    name: str = Field(..., example="Write name of post you wish to update here.")
    content: str = Field(..., example="Write content of post you wish to update here.")


class PostDelete(BaseModel):

    id: int = Field(..., example="Write ID of post you wish to delete here.")
