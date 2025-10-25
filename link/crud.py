from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Link
from .schemas import LinkSchema
from hashids import Hashids

hashids = Hashids()


async def get_link_by_old(session: AsyncSession, old_url: str) -> Link | None:
    stmt = select(Link).where(Link.old == old_url)
    result = await session.execute(stmt)
    return result.scalar()


async def get_link_by_new(session: AsyncSession, new_url: str) -> Link | None:
    stmt = select(Link).where(Link.new == new_url)
    result = await session.execute(stmt)
    await increment_click_link(session, new_url)
    return result.scalar()


async def create_link(session: AsyncSession, link_in: LinkSchema) -> Link:
    link = Link(**link_in.model_dump())
    hashid = hashids.encode(len(link.old))
    link.new = f"http://127.0.0.1:8000/{hashid}"

    check_cache = await get_link_by_old(session, link.old)
    if check_cache is None:

        session.add(link)
        await session.commit()
        await session.refresh(link)

        return link
    else:
        return check_cache


async def increment_click_link(session: AsyncSession, new_url: str) -> Link:
    stmt = select(Link).where(Link.new == new_url)
    result = await session.execute(stmt)
    link = result.scalar_one()

    # Обновляем счетчик
    link.click_count += 1

    # Сохраняем изменения
    await session.commit()

    return link
