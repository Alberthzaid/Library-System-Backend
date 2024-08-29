from config.env import url
from config.env import key
from config.connectDB import connectDB

Connect = connectDB(key, url)
