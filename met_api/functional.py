from typing import Optional, List
from datetime import datetime
import json

import requests

from .response_objects import ObjectResponse, ObjectsResponse, DepartmentsResponse
from .utils import logical_xnor

OBJECTS_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
DEPARTMENTS_URL = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
SEARCH_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search"


def get_objects(
    date: Optional[datetime] = None, department_ids: Optional[List[int]] = None
) -> ObjectsResponse:
    if date:
        date = date.strftime("%Y-%m-%d")
    params = {"date": date, "department_ids": department_ids}
    response = requests.get(OBJECTS_URL, params=params)
    data = json.loads(response.text)
    response_object = ObjectsResponse(**data)
    return response_object


def get_object(id_: int) -> ObjectResponse:
    url = f"{OBJECTS_URL}/{id_}"
    response = requests.get(url)
    if response.status_code == 404:
        raise ValueError(f"Object with given id {id_} not found on the server.")
    elif response.status_code == 200:
        data = json.loads(response.text)
        response_object = ObjectResponse(**data)
        return response_object


def get_departments() -> DepartmentsResponse:
    response = requests.get(DEPARTMENTS_URL)
    data = json.loads(response.text)
    response_object = DepartmentsResponse(**data)
    return response_object


def search(
    q: str,
    is_highlight: Optional[bool] = None,
    department_id: Optional[int] = None,
    is_on_view: Optional[bool] = None,
    artist_or_culture: Optional[bool] = None,
    medium: Optional[str] = None,
    has_images: Optional[bool] = None,
    geo_location: Optional[str] = None,
    date_begin: Optional[datetime] = None,
    date_end: Optional[datetime] = None,
) -> ObjectsResponse:
    if (date_begin and date_end) and date_begin > date_end:
        raise ValueError(f"date_end {date_end} > date_begin {date_begin}")
    if not logical_xnor(date_begin, date_end):
        raise ValueError(
            "Both date_begin and date_end have to be present if one of is present."
        )
    if date_begin:
        date_begin = date_begin.strftime("%Y-%m-%d")
        date_end = date_end.strftime("%Y-%m-%d")
    params = {
        "q": q,
        "isHighlight": is_highlight,
        "departmentId": department_id,
        "isOnView": is_on_view,
        "artistOrCulture": artist_or_culture,
        "medium": medium,
        "hasImages": has_images,
        "geoLocation": geo_location,
        "dateBegin": date_begin,
        "dateEnd": date_end,
    }
    response = requests.get(SEARCH_URL, params=params)
    data = json.loads(response.text)
    response_object = ObjectsResponse(**data)
    return response_object
