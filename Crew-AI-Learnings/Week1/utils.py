import os

from dotenv import load_dotenv, find_dotenv


def _load_env():
    """Load variables from the nearest .env file (searches parent dirs)."""
    load_dotenv(find_dotenv())


def get_openai_api_key() -> str:
    _load_env()
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError(
            "OPENAI_API_KEY not found. Add it to your .env file at the repo root."
        )
    return key
