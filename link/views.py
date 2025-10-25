from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from link.schemas import LinkSchema
from core.models import db_helper
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get("/")
async def redirect_link():
    return {"status_code": 200}


@router.get("/{link}")
async def redirect_link(
    link: str,
    session: AsyncSession = Depends(db_helper.async_session_dependency),
):
    link_new = await crud.get_link_by_new(session, f"http://127.0.0.1:8000/{link}")
    if link_new is None:
        return RedirectResponse("/")
    return RedirectResponse(link_new.old)


@router.post("/create/")
async def create_link(
    link: LinkSchema,
    session: AsyncSession = Depends(db_helper.async_session_dependency),
):
    return await crud.create_link(session=session, link_in=link)


@router.get("/get_link/")
async def get_link(
    link: str,
    session: AsyncSession = Depends(db_helper.async_session_dependency),
):
    return await crud.get_link_by_old(session=session, old_url=link)
