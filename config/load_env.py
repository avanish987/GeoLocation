import os

from dotenv import load_dotenv

load_dotenv()
env = os.getenv

def get_bool_env(name):
    env_value = env(name)
    if env_value.lower() == "true":
        return True
    else:
        return False

