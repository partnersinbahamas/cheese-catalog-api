from pydantic import BaseModel, ConfigDict


class CheeseTypeBase(BaseModel):
    name: str
    description: str


class CheeseTypeCreate(CheeseTypeBase):
    pass


class CheeseTypeRead(CheeseTypeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)