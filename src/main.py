from fastapi import FastAPI
from src.s3proxy import S3proxy
#from .s3proxy import S3proxy

from pydantic import BaseModel


class Item(BaseModel):
    file_path: str   | None = None
    bucket_name: str | None = None
    object_name: str | None = None




app = FastAPI()
client = S3proxy() # S3Proxy()

@app.get("/")
async def root():
    return {"message" :  "Gsooooommmm"}

@app.post("/upload")
async def upload_file(item: Item):
    '''
    The service receives a file,
    a bucket name and an object name.
    It should store the file in the respective bucket and object in S3.

    :return:
    '''
    print("Item dict: ", item.model_dump())
    print("Item file path: ", item.file_path)
    client.upload("/tmp/mega", "pastebin", "top_secret")
    return {"msg" : "file uploaded!!!11"}

@app.get("/get")
async def get_file():
    '''
    The service receives a bucket name and an object name.
    It should return the respective object from S3 to the caller.
    :return:
    '''
    client.get()
    return {"message" : "file from s3"}
