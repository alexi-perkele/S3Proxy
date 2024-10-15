from minio import Minio
class S3proxy:
    def __init__(self):
        self.client = Minio("127.0.0.1:9000",
                       access_key="user",
                       secret_key="zuf+qwerty123",
                       )

    def get(self, bucket_name:str, obj_name:str):
        print("Hello proxy!")
        return None

    def upload(self, file, bucket_name:str, obj_name:str):
        # Make the bucket if it doesn't exist.
        found = self.client.bucket_exists(bucket_name)
        if not found:
            self.client.make_bucket(bucket_name)
            print("Created bucket", bucket_name)
        else:
            print("Bucket", bucket_name, "already exists")

        # Upload the file, renaming it in the process
        self.client.fput_object(
            bucket_name, obj_name, file,
        )
        print(
            file, " successfully uploaded as object ",
            obj_name, " to bucket ", bucket_name,
        )

        return None