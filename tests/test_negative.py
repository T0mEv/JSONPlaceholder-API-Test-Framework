import pytest
from jsonschema import validate

INVALID_NAME_USER_PAYLOAD = {
		"name": 12,
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

MISSING_NAME_USER_PAYLOAD = {
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


@pytest.mark.parametrize("bad_id", [999, 0, -1, "test"])
def test_get_users_with_invalid_id(api_client, bad_id):
	response = api_client.get(f"/users/{bad_id}")
	assert response.status_code == 404


@pytest.mark.xfail(reason="Backend allows integer in name field, should be string")
def test_invalid_name_during_creation_of_user(api_client, load_schema):
	
	# The api accepts this input despite being invalid
	# It converts the integer to a string
	response = api_client.post("/users", INVALID_NAME_USER_PAYLOAD)
	assert response.status_code == 400

	# But this check catches it as it's directly compared to the schema
	response_data = response.json()

	schema = load_schema("user_schema")
	validate(instance=response_data, schema=schema)


@pytest.mark.xfail(reason="Backend allows user with no name to be created")
def test_create_user_with_no_name(api_client, load_schema):

	response = api_client.post("/users", MISSING_NAME_USER_PAYLOAD)
	response_data = response.json()
	
	assert response.status_code == 400

	schema = load_schema("user_schema")
	validate(instance=response_data, schema=schema)