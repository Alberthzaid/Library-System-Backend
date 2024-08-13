from User import User

class Admin(User):
    def __init__(self, name: str, id: int, status: bool, types: str):
        super().__init__(name, id, status, types)

    def get_name(self) -> str:
        return self.name

    def get_status(self) -> bool:
        return self.status