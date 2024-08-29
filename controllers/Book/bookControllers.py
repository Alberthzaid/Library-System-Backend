from flask import jsonify
from objects import Book
from config.index import Connect
from objects.Book import Book

supabase = Connect.connect()
tableBook = supabase.table("Books")

class libraryControllers:
    def __init__(self):
        pass

    def addBook(self,name: str, gender: str, version: str, disable: bool):
        book = Book(name, version , gender , disable)
        response = tableBook.insert(book.getBody()).execute()
        print(f"==== BOOK ADDED {name} =====")
        return jsonify(response.data)

    def getBooks(self):
        response = tableBook.select("*").execute()
        print("=== GETTING BOOKS ===")
        return jsonify(response.data)

    def deleteBook(self, id:int):
        response = tableBook.delete().eq("id",id).execute()
        print("=== BOOK DELETED ===")
        return jsonify(response.data)

    def getBookById(self, id:int):
        response = tableBook.select("*").eq("id",id).execute()
        print(f"=== BOOK WITH ID {id} FOUND ===")
        return jsonify(response.data)

    def updateBook(self, id: int, name: str, gender: str, version: str, disable: bool):
        book = Book(name, gender, version, disable)
        response = tableBook.update(book.getBody()).eq("id",id).execute()
        print(f"=== BOOK WITH {id} UPDATE ===")
        return jsonify(response.data)