import pytest
from jsonschema import validate

USER_PAYLOAD = {
		"name": "Tom E",
		"username": "OliveCrane",
		"email": "test@test.com",
		"address": {
		  "street": "West Street",
		  "suite": "Apt. 519",
		  "city": "Sheffield",
		  "zipcode": "92998-3874",
		  "geo": {
			"lat": "-37.3159",
			"lng": "81.1496"
		  }
		},
		"phone": "1-770-736-8031 x56442",
		"website": "burl.org",
		"company": {
		  "name": "Lunch Stop",
		  "catchPhrase": "Lovely Sandwiches",
		  "bs": "harness real-time sandwiches"
		}
	}
	

def test_get_single_user(api_client, load_schema):

	response = api_client.get("/users/1")
	response_data = response.json()

	assert response.status_code == 200
	schema = load_schema("user_schema")
	validate(instance=response_data, schema=schema)

	assert response_data["id"] == 1


def test_get_all_users(api_client, load_schema):

	response = api_client.get("/users")
	response_data = response.json()

	assert response.status_code == 200
	schema = load_schema("multiple_user_schema")

	validate(instance=response_data, schema=schema)

	assert len(response_data) == 10


def test_create_user(api_client, load_schema):
	
	response = api_client.post("/users", USER_PAYLOAD)
	response_data = response.json()

	assert response.status_code == 201
	
	schema = load_schema("user_schema")
	validate(instance=response_data, schema=schema)


def test_put_a_user(api_client, load_schema):

	response = api_client.put("/users/1", USER_PAYLOAD)
	response_data = response.json()

	assert response.status_code == 200

	schema = load_schema("user_schema")
	validate(instance=response_data, schema=schema)

	assert response_data["name"] == "Tom E"


def test_patch_a_user(api_client, load_schema):
	patch_payload = {
		"name": "Tom E",
	}

	response = api_client.patch("/users/1", patch_payload)
	response_data = response.json()

	assert response.status_code == 200

	schema = load_schema("user_schema")
	validate(instance=response_data, schema=schema)

	assert response_data["name"] == "Tom E" and response_data["username"] == "Bret"


def test_delete_user(api_client, load_schema):

	response = api_client.delete("/users/1")
	response_data = response.json()

	assert response.status_code == 200
	assert response_data == {}