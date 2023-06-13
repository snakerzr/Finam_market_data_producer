from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

CLIENT_IDS = os.getenv("CLIENT_IDS")
TOKEN = os.getenv("TOKEN")
RABBIT_MQ_HOST = os.getenv('RABBIT_MQ_HOST')