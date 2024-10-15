import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock

import sys
sys.path.append('../..')

from src.main import app

# Mock the S3 client
client = AsyncMock()

# Create a test client
test_client = TestClient(app)

@pytest.mark.parametrize(
    "file_path, bucket_name, object_name, expected_status, expected_response",
    [
        ("/tmp/mega", "pastebin", "top_secret", 200, {"msg": "file uploaded!!!11"}),  # happy path
        ("", "emptybucket", "emptyobject", 200, {"msg": "file uploaded!!!11"}),  # edge case: empty file
        ("/tmp/mega", "", "top_secret", 200, {"msg": "file uploaded!!!11"}),  # edge case: empty bucket name
        ("/tmp/mega", "pastebin", "", 200, {"msg": "file uploaded!!!11"}),  # edge case: empty object name
        ("/tmp/mega", None, "top_secret", 422, {"detail": "Unprocessable Entity"}),  # error case: None bucket name
        ("/tmp/mega", "pastebin", None, 422, {"detail": "Unprocessable Entity"}),  # error case: None object name
    ],
    ids=[
        "happy_path",
        "empty_file",
        "empty_bucket_name",
        "empty_object_name",
        "none_bucket_name",
        "none_object_name",
    ]
)
def test_upload_file(file_path, bucket_name, object_name, expected_status, expected_response):
    # Act
    response = test_client.post(
        "/upload",
        files={"file": file_path},
        data={"bucket_name": bucket_name, "object_name": object_name}
    )

    # Assert
    assert response.status_code == expected_status
    assert response.json() == expected_response

