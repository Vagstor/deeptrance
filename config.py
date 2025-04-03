import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    TOKEN = os.getenv("deepseek_token") #Create an .env file and add the following line: "deepseek_token=(your personal API token)"


settings: Settings = Settings()