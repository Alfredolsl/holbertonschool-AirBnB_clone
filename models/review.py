#!/usr/bin/python3
"""Defines a Review Class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents Review, inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
