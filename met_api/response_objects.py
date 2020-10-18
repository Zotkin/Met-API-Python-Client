from typing import List, Optional, Dict, Union
from datetime import datetime

from pydantic import BaseModel

class ObjectsResponse(BaseModel):
    total: int
    objectIDs: List[int]


class ObjectResponse(BaseModel):
    objectID: int
    isHighlight: bool
    accessionNumber: str
    accessionYear: str
    isPublicDomain: bool
    primaryImage: str
    primaryImageSmall: str
    additionalImages: List[str]
    constituents: Optional[List[Dict[str, Union[str, int]]]]
    department: str
    objectName: str
    title: str
    culture: str
    period: str
    dynasty: str
    reign: str
    portfolio: str
    artistRole: str
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
    region: str
    subregion: str
    locale: str
    locus: str
    excavation: str
    river: str
    classification: str
    rightsAndReproduction: str
    linkResource: str
    metadataDate: str
    repository: str
    objectURL: str
    tags: Optional[List[Dict[str, str]]]
    objectWikidata_URL: str
    isTimelineWork: bool
    GalleryNumber: str


class DepartmentsResponse(BaseModel):
    departments: List[Dict[str, Union[str, int]]]