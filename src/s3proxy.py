from minio import Minio


class S3proxy:
    def __init__(self):
        self.client = Minio("127.0.0.1:9000",
                            access_key="user",
                            secret_key="qwerty123",
                            secure=False
                            )
        print("Hello proxy ctr!!!")

    def get(self, bucket_name: str, obj_name: str):
        print("Hello get proxy!")
        return None

    def upload(self, file_path:str, bucket_name: str, obj_name: str):
        # Make the bucket if it doesn't exist.
        print("Hello proxy upload")
        try:
            if found := self.client.bucket_exists(bucket_name):
                print("Bucket", bucket_name, "already exists")

            else:
                self.client.make_bucket(bucket_name)
                print("Created bucket", bucket_name)
        except Exception as ex:
            print("Exception occured: ", ex)
        # Upload the file, renaming it in the process
        self.client.fput_object(
            bucket_name, obj_name, file_path,
        )
        print(
            file_path, " successfully uploaded as object ",
            obj_name, " to bucket ", bucket_name,
        )

        return None
