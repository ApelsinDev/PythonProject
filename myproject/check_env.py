import os

import environ

env = environ.Env()
environ.Env.read_env(os.path.join(os.path.dirname(__file__), '.env'))

print("DB_NAME:", env('DB_NAME'))
print("DB_USER:", env('DB_USER'))
print("DB_PASSWORD:", env('DB_PASSWORD'))
print("DB_HOST:", env('DB_HOST'))
print("DB_PORT:", env('DB_PORT'))
