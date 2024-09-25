class Library:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location

    def getName(self):
        return self.__name

    def getLocation(self):
        return self.__location

    def getBody(self):
        body = {
            "name":self.getName(),
            "location":self.getLocation()
        }
        return body
