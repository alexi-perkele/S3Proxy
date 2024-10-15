from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" :  "Gsooooommmm"}

@app.post("/upload")
async def upload_file():
    '''
    The service receives a file,
    a bucket name and an object name.
    It should store the file in the respective bucket and object in S3.

    :return:
    '''
    return {"msg" : "file uploaded"}

@app.get("/get")
async def get_file():
    '''
    The service receives a bucket name and an object name.
    It should return the respective object from S3 to the caller.
    :return:
    '''
    return {"message" : "file from s3"}
