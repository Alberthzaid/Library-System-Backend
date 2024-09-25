from abc import ABC, abstractmethod
from typing import List

class User(ABC):
    def __init__(self, name: str, lastname:str, status: bool, types: str):
        self.name: str = name
        self.lastname:str = lastname
        self.status: bool = status
        self.types: str = types

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_status(self) -> bool:
        pass