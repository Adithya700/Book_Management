from flask import Flask, request 
 
app = Flask(__name__) 
 
books = [] 
 
@app.route("/") 
def home(): 
    return { 
        "message": "Welcome to  API" 
    } 
 
@app.route("/books", methods=["POST"]) 
def add_book(): 
    data = request.get_json() 
    book = { 
        "id": len(books) + 1, 
        "title": data["title"], 
        "author": data["author"]
    } 
 
    books.append(book) 
 
    return book, 201 
 
@app.route("/books", methods=["GET"]) 
def getall_book(): 
    return books
 
@app.route("/books/<int:book_id>", methods=["GET"]) 
def get_book(book_id): 
    for book in books: 
        if book["id"] == book_id: 
            return book
 
    return {"error": "Book not found"}, 404 
 
@app.route("/books/<int:book_id>", methods=["PUT"]) 
def update_book(book_id): 
    data = request.get_json() 
    for book in books: 
        if book["id"] == book_id: 
            book["title"] = data.get( 
                "title", 
                book["title"] 
            ) 
            book["author"] = data.get( 
                "author", 
                book["author"] 
            ) 
 
            return book
 
    return {"error": "Book not found"}, 404 

@app.route("/books", methods=["POST"]) 
def create_book(): 
    data = request.get_json() 
    if not data: 
        return { 
            "error": "Request body required" 
        }, 400 
    if not data.get("title"): 
        return { 
            "error": "Book title required" 
        }, 400 
 
    book = { 
        "id": len(books) + 1, 
        "title": data["title"], 
        "author": data["author"]
    } 
 
    books.append(book)
 
@app.route("/books/<int:book_id>", methods=["DELETE"]) 
def delete_book(book_id): 
 
    for book in books: 
 
        if book["id"] == book_id: 
 
            books.remove(book) 
 
            return { 
                "message": "Book deleted successfully" 
            } 
 
    return {"error": "Book not found"}, 404 
 
if __name__ == "__main__": 
    app.run(debug=True) 