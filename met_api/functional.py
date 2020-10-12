from typing import Optional, List, Dict, Any
from datetime import datetime
from urllib.parse import urljoin

import aiohttp

from .response_objects import ObjectResponse, ObjectsResponse, DepartmentsResponse

OBJECTS_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
DEPARTMENTS_URL = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
SEARCH_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search"

session = aiohttp.ClientSession()


async def get_objects(date: Optional[datetime], department_ids: Optional[List[int]]) -> ObjectsResponse:
    params = {"date": date, "department_ids": department_ids}
    async with session.get(OBJECTS_URL, params=params) as resp:
        # todo add error handling
        data = await resp.json()
        response_object = ObjectsResponse(**data)
        return response_object


async def get_object(id_: int) -> ObjectResponse:
    url = urljoin(OBJECTS_URL, str(id_))
    async with session.get(url) as resp:
        data = await resp.json()
        response_object = ObjectResponse(**data)
    return response_object


async def get_departments() -> DepartmentsResponse:

    async with session.get(DEPARTMENTS_URL) as resp:
        data = await resp.json()
        response_object = DepartmentsResponse(**data)
    return response_object


async def search(q: str,
                 is_highlight: Optional[bool],
                 department_id: Optional[int],
                 is_on_view: Optional[bool],
                 artist_or_culture: Optional[bool],
                 medium: Optional[str],
                 has_images: Optional[bool],
                 geo_location: Optional[str],
                 date_begin: Optional[str],
                 date_end: Optional[str]) -> ObjectsResponse:
    # todo handle the case when only date_begin or date_end is submitted
    parameters = {
        "q": q,
        "isHighlight": is_highlight,
        "departmentId": department_id,
        "isOnView": is_on_view,
        "artistOrCulture": artist_or_culture,
        "medium": medium,
        "hasImages": has_images,
        "geoLocation": geo_location,
        "dateBegin": date_begin,
        "dateEnd": date_end
    }
    async with session.get(SEARCH_URL, parameters=parameters) as resp:
        data = await resp.json()
        response_object = ObjectsResponse(**data)
        return response_object
