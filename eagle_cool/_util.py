from typing import Optional
import requests


def get(*args, **kwargs):
    if not "allow_redirects" in kwargs:
        kwargs["allow_redirects"] = True
    return requests.get(*args, **kwargs).json()


def post(*args, **kwargs):
    if not "allow_redirects" in kwargs:
        kwargs["allow_redirects"] = True
    return requests.post(*args, **kwargs).json()

def dict2query(d: Optional[dict[str, str]]):
    if d is None: return ""
    return "?" + "&".join(f"{k}={v}" for k, v in d.items())
    
def reject_none(d: dict):
    return {k:v for k, v in d.items() if not v is None}