import os

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = f"Expected environment variable '{name}' not set."
        raise Exception(message)

POSTGRES_URL = get_env_variable('POSTGRES_URL')
POSTGRES_USER = get_env_variable('POSTGRES_USER')
POSTGRES_PASS = get_env_variable('POSTGRES_PASS')
POSTGRES_DB = get_env_variable('POSTGRES_DB')
DB_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_URL}/{POSTGRES_DB}'

config = {
    'POSTGRES_URL': POSTGRES_URL,
    'POSTGRES_USER': POSTGRES_USER,
    'POSTGRES_PASS': POSTGRES_PASS,
    'POSTGRES_DB': POSTGRES_DB,
    'DB_URI': DB_URI
}


