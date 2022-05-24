"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
import os
from pprint import pprint
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine

from jsonplaceholder_requests import fetch_posts_data, fetch_users_data
from models import User, Post
from models.base import Session as async_session, async_engine, Base


async def create_tables(async_engine: AsyncEngine):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(session: AsyncSession, users_data: List[dict]) -> List[User]:
    users = []
    for user_data in users_data:
        user = User(
            id=user_data["id"],
            name=user_data["name"],
            username=user_data["username"],
            email=user_data["email"],
        )
        users.append(user)
    session.add_all(users)
    return users


async def create_posts(session: AsyncSession, posts_data: List[dict]) -> List[Post]:
    posts = []
    for post_data in posts_data:
        post = Post(
            id=post_data["id"],
            title=post_data["title"],
            body=post_data["body"],
            user_id=post_data["userId"],
        )
        posts.append(post)
    session.add_all(posts)
    return posts


async def create_users_and_posts_in_db(
    users_data: List[dict], posts_data: List[dict]
) -> (List[Post], List[User]):
    async with async_session() as session:  # type: AsyncSession
        posts, users = await asyncio.gather(
            create_posts(session, posts_data), create_users(session, users_data)
        )
        await session.commit()
        return posts, users


async def async_main():
    if "PYTEST_CURRENT_TEST" in os.environ:
        await create_tables(async_engine)

    posts, users = await asyncio.gather(fetch_posts_data(), fetch_users_data())
    # print(">>>>>>> posts:")
    # pprint(posts)
    # print(">>>>>>> users:")
    # pprint(users)

    await create_users_and_posts_in_db(users, posts)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
