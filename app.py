from flask import Flask , request, render_template
from controllers.Book.bookControllers import BookControllers
from controllers.Library.LibraryControllers import LibraryControllers



app = Flask(__name__)


@app.route('/doc')
def documentation():
    return render_template('Documentation.html')

@app.route('/get/Books' , methods=['GET'])
def getBooksRoute():
    data = BookControllers.getBooks()
    return data

@app.route('/get/Book/<id>' , methods=['GET'])
def getBookByIdRoute(id):
    data = BookControllers.getBookById(id)
    return data

@app.route('/add/Book' , methods=['POST'])
def addBookRoute():
    req = request.json
    return BookControllers.addBook(req)

@app.route('/update/Book/<id>' , methods = ['PUT'])
def updateBookRoute(id):
    req = request.json
    return BookControllers.updateBook(id , req)

@app.route('/delete/Book/<id>' , methods=['DELETE'])
def deleteBookRoute(id):
    return BookControllers.deleteBook(id)


@app.route('/get/Library' , methods =['GET'])
def getLibraryRoute():
    return LibraryControllers.getLibrary()

@app.route('/add/Library' , methods=['POST'])
def addLibraryRoute():
    req = request.json
    return LibraryControllers.addLibrary(req)

@app.route('/update/Library/<id>', methods=['PUT'])
def updateLibraryRoute(id):
    req = request.json
    data = LibraryControllers.updateLibrary(id , req)
    return data

@app.route('/delete/Library/<id>' , methods=['DELETE'])
def deleteLibraryRoute(id):
    data = LibraryControllers.deleteLibrary(id)
    return data


if __name__ == '__main__':
    app.run()
