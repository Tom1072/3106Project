import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


# import to use this
DATABASE_URI = os.environ.get("DATABASE_URL")
