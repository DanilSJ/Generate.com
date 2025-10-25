from pydantic import BaseModel, ConfigDict
from typing import Annotated


class LinkSchema(BaseModel):
    old: str

    model_config = ConfigDict(from_attributes=True)
