# Book Management
# Flask Books REST API

A simple RESTful API built using Flask that performs CRUD (Create, Read, Update, Delete) operations on a collection of books. The application stores book data in memory using a Python list and exposes endpoints for managing books.

---

## Project Overview

This project demonstrates the fundamentals of:

* Building REST APIs using Flask
* Handling HTTP requests and responses
* Working with JSON data
* Implementing CRUD operations
* Using route parameters and request methods

---

## Features

* Add a new book
* Retrieve all books
* Retrieve a specific book by ID
* Update book details
* Delete a book
* Basic input validation and error handling
* JSON-based API responses

---

## Technologies Used

* Python 3
* Flask
* JSON
* REST API Principles

---

## Project Structure

```text
flask_projects/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Home Endpoint

**GET /**

Returns a welcome message.

#### Response

```json
{
  "message": "Welcome to API"
}
```

---

### Add a Book

**POST /books**

Adds a new book to the collection.

#### Request Body

```json
{
  "title": "The Alchemist",
  "author": "Paulo Coelho"
}
```

#### Response

```json
{
  "id": 1,
  "title": "The Alchemist",
  "author": "Paulo Coelho"
}
```

Status Code: `201 Created`

---

### Get All Books

**GET /books**

Returns all books stored in the application.

#### Response

```json
[
  {
    "id": 1,
    "title": "The Alchemist",
    "author": "Paulo Coelho"
  }
]
```

Status Code: `200 OK`

---

### Get Book by ID

**GET /books/<book_id>**

Returns the details of a specific book.

#### Example

```text
GET /books/1
```

#### Response

```json
{
  "id": 1,
  "title": "The Alchemist",
  "author": "Paulo Coelho"
}
```

If the book does not exist:

```json
{
  "error": "Book not found"
}
```

Status Code: `404 Not Found`

---

### Update a Book

**PUT /books/<book_id>**

Updates the title and/or author of an existing book.

#### Request Body

```json
{
  "title": "The Kite Runner",
  "author": "Khaled Hosseini"
}
```

#### Response

```json
{
  "id": 1,
  "title": "The Kite Runner",
  "author": "Khaled Hosseini"
}
```

Status Code: `200 OK`

---

### Delete a Book

**DELETE /books/<book_id>**

Deletes a book from the collection.

#### Response

```json
{
  "message": "Book deleted successfully"
}
```

If the book does not exist:

```json
{
  "error": "Book not found"
}
```

Status Code: `404 Not Found`

---

## Running the Application

### Clone the Repository

```bash
git clone <repository-url>
cd flask_projects
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start the Server


python app.py


The application will run on:


http://127.0.0.1:5000/


---

## Testing the API

The API can be tested using:

* Postman
* Thunder Client (VS Code Extension)
* cURL commands
* Web browsers for GET requests

---

## Learning Objectives

This project was developed to practice:

* Flask application development
* REST API design
* CRUD operations
* JSON request and response handling
* Route parameters and HTTP methods
* Basic validation and error handling

---


###Sample output

<img width="1043" height="865" alt="image" src="https://github.com/user-attachments/assets/7884e7da-1896-4d9b-8f33-ec1b78837930" />
<img width="1063" height="737" alt="image" src="https://github.com/user-attachments/assets/6df4acb2-380e-4021-88fe-75956eb457db" />


## Author

**Adithya K.S.**

This project was created as a practice project to strengthen Flask development skills and gain hands-on experience in building RESTful APIs using Python.
