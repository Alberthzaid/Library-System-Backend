from environs import Env

env = Env()

env.read_env()

url = env.str("URL_PROYECT")
key = env.str("KEY")

