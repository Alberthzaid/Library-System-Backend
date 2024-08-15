from typing import Type

from supabase._sync.client import SyncClient
from env import key, url
from supabase import create_client, Client


class connectDB:
    def __init__(self, key: str, url: str):
        self.__key: str = key
        self.__url: str = url

    def connect(self) -> SyncClient | Type[ConnectionError]:
        try:
            client: Client = create_client(self.url, self.key)
            print("=== Success ===")
            return client
        except ConnectionError:
            print("Connection error")
            return ConnectionError


Connect = connectDB(key, url)

