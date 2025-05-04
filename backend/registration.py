import uuid
import re
import os

_BAD_WORDS_FILE = os.path.join(os.path.dirname(__file__), 'bad_words.txt')
_BLACKLISTED_WORDS = set()

with open(_BAD_WORDS_FILE, 'r') as f:
    _BLACKLISTED_WORDS = {line.strip().lower() for line in f if line.strip()}


def generate_uuid_string():
    return str(uuid.uuid4())


def is_valid_username(username):
    if not (3 <= len(username) <= 20):
        return False

    if not re.fullmatch(r'[A-Za-z0-9_-]+', username):
        return False

    # Case-insensitive check for blacklisted substrings
    username_lower = username.lower()
    for word in _BLACKLISTED_WORDS:
        if word in username_lower:
            return False

    return True
