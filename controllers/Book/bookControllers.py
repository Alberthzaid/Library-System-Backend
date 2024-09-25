from flask import jsonify , request
from objects import Book
from config.index import Connect
from objects.Book import Book

supabase = Connect.connect()
tableBook = supabase.table("Books")

class BookControllers:
    def __init__(self):
        pass

    def addBook(req:request) -> jsonify:
        book = Book(req.get("name") , req.get("gender") , req.get("version") , req.get("disable"))
        response = tableBook.insert(book.getBody()).execute()
        print(f"==== BOOK ADDED {book.getName()} =====")
        return jsonify(response.data)

    def getBooks() -> jsonify:
        response = tableBook.select("*").execute()
        print("=== GETTING BOOKS ===")
        return jsonify(response.data)

    def deleteBook(id:int) -> jsonify:
        response = tableBook.delete().eq("id",id).execute()
        print("=== BOOK DELETED ===")
        return jsonify(response.data)

    def getBookById(id:int) -> jsonify:
        response = tableBook.select("*").eq("id",id).execute()
        print(f"=== BOOK WITH ID {id} FOUND ===")
        return jsonify(response.data)

    def updateBook(id:int , req:request) -> jsonify:
        book = Book(req.get("name") ,req.get("version"),req.get("gender") ,req.get("disable"))
        response = tableBook.update(book.getBody()).eq("id",id).execute()
        print(f"=== BOOK WITH {id} UPDATE ===")
        return jsonify(response.data)