from typing import Union, List

from fastapi import APIRouter, Query, Path
from pydantic import BaseModel, Required


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


router = APIRouter(tags=["Items"], prefix="/items")

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@router.get("")
def read_items(skip: int = 0, limit: int = Query(default=Required)):
    return fake_items_db[skip : skip + limit]


@router.get("/{item_id}")
def root(
    # * allows use any order of default and non-default params
    *,
    item_id: int = Path(
        default=Required, title="The ID of the item to get", ge=1, lt=1000
    ),
    needy: str,
    q: Union[str, None] = Query(
        default=None,
        min_length=3,
        max_length=50,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        alias="item-query",
        deprecated=True,
    ),
    short: bool = False,
    list_param: List[str] = Query(default=["foo", "bar"]),
    hidden_query: Union[str, None] = Query(default=None, include_in_schema=False),
):
    """

    :param list_param:
    :param item_id:
    :param needy:
    :param q:
    :param short:
    :return:
    """
    item = {"item_id": item_id, "needy": needy}
    item.update({"l": list_param})
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
    return item


@router.post("")
def create_item(item: Item):
    """

    :param item:
    :return:
    """
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@router.put("/{item_id}")
def create_item_with_id(
    item_id: int,
    item: Item,
    # ... - Ellipsis declare that a value is required.
    # In this case you must pass the None value.
    q: Union[str, None] = Query(
        default=..., min_length=3, max_length=50, regex="^fixedquery$"
    ),
):
    """

    :param item_id:
    :param item:
    :param q:
    :return:
    """
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


@router.patch("/{item_id}")
def update_item(
    *,
    item_id: int = Path(title="The ID of item to get", ge=0, lt=1000),
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
    user: Union[User, None] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})

    return results
