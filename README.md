# Address book API

A book application where API users can create, update and delete
addresses

## Installation

- Clone the repository

`git clone https://github.com/tsankotsanev/address_book_api`

- Navigate to the project's folder

`cd address_book_api`

- Create a virtual environment

`python3 -m venv venv`

- Activate the virtual environment

`source venv/bin/activate`

- Install the dependencies

`pip install -r requirements.txt`

## Usage

- Run the server

`uvicorn main:app --reload`

- Open the browser and go to

`http://localhost:8000/docs`

## Logging

Each request made on the API is being logged in the project's folder `log.txt` in the following format:

`[timestamp] call (create/read/update/delete): status (success/failure)`

## Testing

- **IMPORTANT: Before proceeding into testing make sure that your database file (address_book.db) is empty/non-existant**

`rm address_book.db`

- Run pytest

`pytest test_address.py`
