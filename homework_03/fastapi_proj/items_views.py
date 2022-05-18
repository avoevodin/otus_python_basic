from typing import Union, List, Set

from fastapi import APIRouter, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Required, Field, HttpUrl


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300, example="Foo"
    )
    price: float = Field(gt=0, description="The price must be greater than 0")
    tax: Union[float, None] = (None,)
    tags: list[str] = []
    labels: Set[str] = set()
    images: Union[list[Image], None] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 24.8,
                "tax": 4.8,
                "tags": ["nice", "very nice", "nice"],
                "labels": ["Bazz", "Eggs"],
                "images": [
                    {
                        "url": "https://cdn.pixabay.com/photo/2021/08/25/20/42/field-6574455__340.jpg",
                        "name": "Main image",
                    },
                    {
                        "url": "https://www.gettyimages.com/gi-resources/images/500px/983794168.jpg",
                        "name": "Additional image",
                    },
                ],
            }
        }


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


router = APIRouter(tags=["Items"], prefix="/items")

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@router.get("")
def read_items(skip: int = 0, limit: int = Query(default=Required)):
    return fake_items_db[skip : skip + limit]


@router.get("/cookies")
def read_items_cookies(ads_in: Union[str, None] = Cookie(default=None)):
    return {"ads_in": ads_in}


@router.get("/headers")
def read_items_headers(user_agent: Union[str, None] = Header(default=None)):
    return {"User-Agent": user_agent}


@router.get("/{item_id}")
def root(
    # * allows use any order of default and non-default params
    *,
    item_id: int = Path(
        default=Required,
        title="The ID of the item to get",
        ge=1,
        lt=1000,
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item id works correctly.",
                "value": 1,
            },
            "invalid": {
                "summary": "An invalid example",
                "description": "An **invalid** item id doesn't work correctly.",
                "value": "Foo",
            },
        },
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
    # embed - item will be expected as a key item.
    item: Item = Body(embed=True),
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
    # use that param as a body key
    importance: int = Body(gt=0),
):
    """

    :param item_id:
    :param q:
    :param item:
    :param user:
    :param importance:
    :return:
    """
    results = {"item_id": item_id, "importance": importance}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})

    return results


@router.post("/multiple_creating")
def create_multiple_items(items: list[Item]):
    """

    :param items:
    :return:
    """
    return items
