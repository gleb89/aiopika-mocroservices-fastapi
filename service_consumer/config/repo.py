from typing import List, Optional, Union

import ormar

from .db import metadata, database



class Case(ormar.Model):
    class Meta:
        tablename = "cases"
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    title:str = ormar.String(max_length=100)