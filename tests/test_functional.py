from datetime import datetime

import pytest

from met_api import get_object, get_objects, get_departments, search
from met_api.response_objects import ObjectResponse, ObjectsResponse, DepartmentsResponse
from met_api.utils import logical_xnor


def test_get_departments():
    response = get_departments()
    assert type(response) == DepartmentsResponse

@pytest.mark.parametrize("date", [datetime(year=1992, month=1, day=13), None])
@pytest.mark.parametrize("department_ids", [[1, 2, 3, 4], None])
def test_get_objects(date, department_ids):
    response = get_objects(date=date, department_ids=department_ids)
    assert type(response) is ObjectsResponse


@pytest.mark.parametrize("id_", list(range(15)))
def test_get_object(id_):
    if id_ == 0:
        with pytest.raises(ValueError):
            get_object(id_)
    else:
        response = get_object(id_)
        assert type(response) is ObjectResponse


@pytest.mark.parametrize("q", ["sunflowers"])
@pytest.mark.parametrize("is_highlight", [None])
@pytest.mark.parametrize("department_id", [None])
@pytest.mark.parametrize("is_on_view", [None])
@pytest.mark.parametrize("artist_or_culture", [None])
@pytest.mark.parametrize("medium", [None])
@pytest.mark.parametrize("has_images", [None])
@pytest.mark.parametrize("geo_location", [None])
@pytest.mark.parametrize("date_begin", [1700, 1900, None])
@pytest.mark.parametrize("date_end", [1800, None])
def test_search(q, is_highlight, department_id, is_on_view, artist_or_culture, medium, has_images, geo_location,
                date_begin, date_end):
    only_one_date_present = not logical_xnor(date_begin, date_end)
    begin_date_after_end_date = (date_begin and date_end) and (date_begin > date_end)
    if only_one_date_present or begin_date_after_end_date:
        with pytest.raises(ValueError):
            search(q, is_highlight, department_id, is_on_view, artist_or_culture, medium, has_images, geo_location,
                   date_begin, date_end)
    else:
        response = search(q, is_highlight, department_id, is_on_view, artist_or_culture, medium, has_images, geo_location,
                       date_begin, date_end)
        assert type(response) == ObjectsResponse
