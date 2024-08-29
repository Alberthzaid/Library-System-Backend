from flask import Flask , request
from controllers.Book.bookControllers import libraryControllers

controllers = libraryControllers()
app = Flask(__name__)


@app.route('/')
def getBooks():
    return controllers.getBooks()

@app.route('/add/Book', methods=['POST'])
def addBook():
    data = request.json
    name = data.get("name")
    version = data.get("version")
    gender = data.get("gender")
    disable = data.get("disable")
    return controllers.addBook(name,version , gender,disable)


@app.route('/get/<id>')
def getBookById(id):
    data = controllers.getBookById(id)
    return data

@app.route('/delete/book/<id>' , methods=['DELETE'])
def deleteBook(id):
    data = controllers.deleteBook(id)
    return data

@app.route('/update/book/<id>' , methods=['PUT'])
def updateBook(id):
    data = request.json
    name = data.get("name")
    gender = data.get("gender")
    version = data.get("version")
    disable = data.get("disable")

    response = controllers.updateBook(id, name, gender, version, disable)
    return response


if __name__ == '__main__':
    app.run()
