# JsonPlaceholder API Test Framework

A small API testing project built with **python**, **PyTest** and **JSON Schema** for practising CRUD, contract and negative testing against JSONPlaceholder.

## Features

* **API Client:** Wrapped `requests` implementation in `conftest.py` to abstract the base URLs and make the codebase cleaner while calling routes.
* **Contract Testing:** Uses **JSON Schema (Draft-07)** to ensure responses from the API match the expected data types and structure, catching "silent" backend type coercion bugs.
* **Advanced PyTest Logic:**
	* **Fixtures:** Modular setup for clients and loading JSON schemas.
	* **Parametrization:** Used to test multiple invalid inputs in payloads while adhering to DRY principles.
	* **XFAIL Tracking:** Used to highlight "silent" backend bugs where the api should fail yet doesn't.
* **Negative Testing** Covers typical negative tests such as `404 Not Found` and `400 Bad Request`.

## Installation & Setup

1. ### **Clone the repo:**
```bash
	git clone
```

2. ### **Install Dependencies**
```bash
	pip install -r requirements.txt
```

3. ### **Run the tests!**
```bash
	pytest
```