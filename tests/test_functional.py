from datetime import datetime

import pytest

from met_api import get_object, get_objects, get_departments, search
from met_api.response_objects import ObjectResponse, ObjectsResponse, DepartmentsResponse

pytestmark = pytest.mark.asyncio


async def test_get_object(event_loop):
    pass

@pytest.mark.parametrize("date",[datetime(year=1992, month=1, day=13), None])
@pytest.mark.parametrize("department_ids", [[1,2,3,4], None])
async def test_get_objects(event_loop, date, department_ids):
    response = await get_objects(date=date, department_ids=department_ids)
    assert type(response) is ObjectsResponse


async def test_get_departments(event_loop):
    pass


async def test_search(event_loop):
    pass



