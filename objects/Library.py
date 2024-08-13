

class Library:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__list_users = []
        self.__list_books = []

    def getName(self):
        return self.__name

    def getBooks(self):
        return self.__list_books

    def getLocation(self):
        return self.__location

    def getUsers(self):
        return self.__list_users

    def __string__(self):
        return f"""
            name : {self.getName()},
            location : {self.getLocation()}
            users : {self.getUsers()}
            books : {self.getBooks()}
        """
