from typing import List

class Book():
    def __init__(self , name:str , version:str , gender:str , id:int, disable:bool ):
        self.__name: str = name
        self.__version: str = version
        self.__gender:str = gender
        self.__id:int = id
        self.__disable:bool = disable

    def getName(self)-> str:
        return self.__name

    def getGender(self)-> str:
        return self.__gender

    def getVersion(self)-> str:
        return self.__version

    def getId(self)-> int:
        return self.__id

    def getDisable(self)-> bool:
        return self.__disable
