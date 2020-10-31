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
    date: Optional[datetime], department_ids: Optional[List[int]]
) -> ObjectsResponse:
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
    is_highlight: Optional[bool],
    department_id: Optional[int],
    is_on_view: Optional[bool],
    artist_or_culture: Optional[bool],
    medium: Optional[str],
    has_images: Optional[bool],
    geo_location: Optional[str],
    date_begin: Optional[str],
    date_end: Optional[str],
) -> ObjectsResponse:
    if (date_begin and date_end) and date_begin > date_end:
        raise ValueError(f"date_end {date_end} > date_begin {date_begin}")
    if not logical_xnor(date_begin, date_end):
        raise ValueError(
            "Both date_begin and date_end have to be present if one of is present."
        )

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
