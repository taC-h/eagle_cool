from __future__ import annotations
from typing import Literal, Optional, List, Dict
from dataclasses import dataclass
from functools import wraps


Color = Literal[
    "red",
    "orange",
    "green",
    "yellow",
    "aqua",
    "blue",
    "purple",
    "pink",
    ]


@dataclass
class URLItem():
    name: str
    url: str
    website: Optional[str] = None
    annotation: Optional[str] = None
    tags: Optional[List[str]] = None
    modificationTime: Optional[int] = None
    headers: Optional[Dict[str,str]] = None

@dataclass
class PathItem():
    name: str
    path: str
    website: Optional[str] = None
    annotation: Optional[str] = None
    tags: Optional[List[str]] = None
    modificationTime: Optional[int] = None
    headers: Optional[Dict[str,str]] = None
