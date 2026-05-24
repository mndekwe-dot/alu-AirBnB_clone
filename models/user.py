#!/usr/bin/python3
"""User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents an AirBnB user."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
