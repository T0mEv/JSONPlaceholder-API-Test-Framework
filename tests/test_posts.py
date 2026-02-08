import pytest
from jsonschema import validate

def test_get_single_post(api_client, load_schema):
	response = api_client.get("/posts/1")
	response_data = response.json()

	assert response.status_code == 200
	schema = load_schema("post_schema")
	validate(instance=response_data, schema=schema)

	assert response_data["id"] == 1


def test_get_all_posts(api_client, load_schema):
	response = api_client.get("/posts")
	response_data = response.json()

	assert response.status_code == 200
	schema = load_schema("multiple_posts_schema")
	validate(instance=response_data, schema=schema)

	# Known that there's 100 posts total
	assert len(response_data) == 100


def test_create_a_post(api_client, load_schema):
	post_payload = {
		"title": "Time for testing",
		"body": "You are being tested mwahahaha",
		"userId": 1
	}

	response = api_client.post("/posts", post_payload)
	response_data = response.json()

	assert response.status_code == 201
	schema = load_schema("post_schema")
	validate(instance=response_data, schema=schema)

	assert response_data["id"] == 101


def test_put_a_post(api_client, load_schema):
	post_payload = {
		"id": 1,
		"title": "Time for testing",
		"body": "You are being tested mwahahaha",
		"userId": 1
	}

	response = api_client.put("/posts/1", post_payload)
	response_data = response.json()

	assert response.status_code == 200
	schema = load_schema("post_schema")
	validate(instance=response_data, schema=schema)

	assert response_data["title"] == "Time for testing"


def test_patch_a_post(api_client, load_schema):
	post_payload = {
		"title": "New Title"
	}

	response = api_client.patch("/posts/1", post_payload)
	response_data = response.json()

	assert response.status_code == 200
	schema = load_schema("post_schema")
	validate(instance=response_data, schema = schema)

	assert response_data["title"] == "New Title"


def test_delete_a_post(api_client, load_schema):

	response = api_client.delete("/posts/1")
	response_data = response.json()

	assert response.status_code == 200
	assert response_data == {}


def test_get_posts_comments(api_client, load_schema):

	response = api_client.get("/posts/1/comments")
	response_data = response.json()

	assert response.status_code == 200
	schema = load_schema("multiple_comment_schema")
	validate(instance=response_data, schema = schema)

	assert len(response_data) == 5