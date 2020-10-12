from typing import List, Optional, Dict, Union
from datetime import datetime

from pydantic import BaseConfig

class ObjectsResponse(BaseConfig):
    total: int
    objectIDs: List[int]


class ObjectResponse(BaseConfig):
    objectID: int
    isHighlight: bool
    accessionNumber: str  # todo might be parsed to float by python
    accessionYear: str  # todo might be parsed to int by python
    isPublicDomain: bool
    primaryImage: str
    primaryImageSmall: str
    additionalImages: List[str]
    constituents: List[Dict[str, str]]
    department: str
    objectName: str
    title: str
    culture: str
    period: str
    dynasty: str
    reign: str
    portfolio: str
    artistRole: int
    artistPrefix: str
    artistDisplayName: str
    artistDisplayBio: str
    artistSuffix: str
    artistAlphaSort: str
    artistNationality: str
    artistBeginDate: str
    artistEndDate: str
    artistGender: str
    artistWikidata_URL: str
    artistULAN_URL: str
    objectDate: str
    objectBeginDate: int
    objectEndDate: int
    medium: str
    dimensions: str
    creditLine: str
    geographyType: str
    city: str
    state: str
    county: str
    country: str
    region: Optional[str]
    subregion: Optional[str]
    locale: Optional[str]
    locus: Optional[str]
    excavation: Optional[str]
    river: Optional[str]
    classification: str
    rightsAndReproduction: str
    linkResource: str
    metadataDate: datetime
    repository: str
    objectURL: str
    tags: List[Dict[str, str]]
    objectWikidata_URL: str
    isTimelineWork: bool
    GalleryNumber: Optional[int]


class DepartmentsResponse(BaseConfig):
    departments: List[Dict[str, Union[str, int]]]