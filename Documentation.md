# Key-Value Store Application : Documentation

This documentation provides information about the Key-Value Store application. The application is built using FastAPI, Redis, and Huey to create a simple key-value store with support for asynchronous task execution.

## API Endpoints

1. Get Value by Key
Endpoint: GET /get/{key}

Retrieve the value for a given key.
![Get Endpoint Image](<Screenshot 2024-03-06 at 5.24.04 PM.png>)


2. Set Value for Key
Endpoint: POST /set
Body : {
    "key": "hey",
    "value": "hello"
}

Set a key-value pair.
![Set Endpoint Image](<Screenshot 2024-03-06 at 5.24.14 PM.png>)


3. Delete Value by Key
Endpoint: DELETE /delete/{key}

Delete a key-value pair.
![Delete Endpint Image](<Screenshot 2024-03-06 at 5.25.15 PM.png>)