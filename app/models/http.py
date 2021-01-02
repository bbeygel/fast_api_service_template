from typing import Optional, List

from pydantic import BaseModel


class ItemModel(BaseModel):
    detail_1: Optional[str] = None
    detail_2: Optional[bool] = None
    detail_3: Optional[int] = None


class GetAllModel(BaseModel):
    data: Optional[List[ItemModel]] = None
    error: Optional[Exception] = None

    class Config:
        arbitrary_types_allowed = True


class GetItemModel(BaseModel):
    data: Optional[ItemModel] = None
    error: Optional[Exception] = None

    class Config:
        arbitrary_types_allowed = True


class CreateItemModel(BaseModel):
    data: Optional[ItemModel] = None
    error: Optional[Exception] = None

    class Config:
        arbitrary_types_allowed = True


class EditItemModel(BaseModel):
    data: Optional[ItemModel] = None
    error: Optional[Exception] = None

    class Config:
        arbitrary_types_allowed = True


class DeleteItemModel(BaseModel):
    data: bool = False
    error: Optional[Exception] = None

    class Config:
        arbitrary_types_allowed = True
