#!/usr/bin/python3
"""Defines a City Class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents City, inherits from BaseModel"""
    state_id = ""
    name = ""
