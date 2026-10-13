from pydantic import BaseModel, ConfigDict

from db.models import PackagingType


class CheeseTypeBase(BaseModel):
    name: str
    description: str


class CheeseTypeCreate(CheeseTypeBase):
    pass


class CheeseTypeRead(CheeseTypeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class CheeseBase(BaseModel):
    title: str
    price: float
    packaging_type: PackagingType


class CheeseCreate(CheeseBase):
    cheese_type_id: int


class CheeseRead(CheeseBase):
    id: int
    cheese_type: CheeseTypeRead

    model_config = ConfigDict(from_attributes=True)
