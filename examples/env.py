from dotenv import load_dotenv
import os


def load_env():
    load_dotenv()
    username = os.getenv('GEO_USERNAME')
    password = os.getenv('GEO_PASSWORD')
    token = os.getenv('GEO_TOKEN')
    return username, password, token
