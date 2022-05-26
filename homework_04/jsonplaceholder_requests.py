from typing import Any

import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(data_url) -> Any:
    """
    Fetch json data from url.
    :param data_url:
    :return:
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(data_url) as response:
            data: dict = await response.json()
            return data


async def fetch_users_data() -> dict:
    """
    Fetch users
    :return:
    """
    return await fetch_json(USERS_DATA_URL)


async def fetch_posts_data() -> dict:
    """
    Fetch posts
    :return:
    """
    return await fetch_json(POSTS_DATA_URL)
