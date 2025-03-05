from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv()


class ENVReader:
    def __init__(self):
        if not os.path.exists(ENV_PATH):
            raise IOError("Env file not existed")

        self.bot_token = os.getenv("BOT_TOKEN")
