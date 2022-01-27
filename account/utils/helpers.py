import hashlib
import hmac
import json
import re
import uuid
from urllib.parse import parse_qs, urlparse


def generate_hash_signature(secret_key, value):
    signature = hmac.new(secret_key.encode(), bytes(value, encoding='utf-8'), digestmod=hashlib.sha256).hexdigest()
    return signature


def verify_hash_signature(secret, msg, digest):
    signature = hmac.new(secret.encode("utf-8"), msg.encode("utf-8"), hashlib.sha256)
    return hmac.compare_digest(signature.hexdigest(), digest)


def search_string_match(pattern, value):
    try:
        return re.match(pattern, value).group(0)
    except AttributeError:
        return None


def get_host_url(url):
    parsed_uri = urlparse(url)
    return f'{parsed_uri.scheme}://{parsed_uri.netloc}'


def generate_unique_key():
    return uuid.uuid4().hex


def response_to_dictionary(text):
    return json.loads(text)


def get_url_params(url):
    parsed = urlparse(url)
    return parse_qs(parsed.query)
