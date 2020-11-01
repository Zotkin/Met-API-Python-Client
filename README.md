# The Metropolitan Museum Of Art Python API Client

[![CI to docker hub Actions Status](https://github.com/{userName}/{repoName}/workflows/{workflowName}/badge.svg)](https://github.com/{userName}/{repoName}/actions)

An unofficial python client for The Metropolitan Museum of Art Collection API.
This client fully implements a convinient python interface for the methods described [here](https://metmuseum.github.io/).
Build using [requests](https://github.com/psf/requests) and [pydantic](https://github.com/samuelcolvin/pydantic). 

Examples:
 
```python
>>> from met_api
>>> from datetime import datetime

 # requests all object ids 
>>> objects = met_api.get_objects()
>>> objects.total
474566
>>> len(objects.objectIDs):
474566

# request objects modified since 1st 2020

>>> objects = met_api.get_objects(date=datetime(year=2020, month=5, day=1))
>>> objects.total
270396

# get object with objectID=10
>>> object = met_api.get_object(id_=10)
>>> object
ObjectResponse(objectID=10, isHighlight=False, accessionNumber='1979.486.3', accessionYear='1979', isPublicDomain=False, primaryImage='', primaryImageSmall='', additionalImages=[], constituents=[{'constituentID': '1080', 'role': 'Maker', 'name': 'Bela Lyon Pratt', 'constituentULAN_URL': 'http://vocab.getty.edu/page/ulan/500095555', 'constituentWikidata_URL': '', 'gender': ''}], department='The American Wing', objectName='Coin', title='Two-and-a-half-dollar Indian Head Coin', culture='', period='', dynasty='', reign='', portfolio='', artistRole='Maker', artistPrefix='', artistDisplayName='Bela Lyon Pratt', artistDisplayBio='1867–1917', artistSuffix='', artistAlphaSort='Pratt, Bela Lyon', artistNationality='', artistBeginDate='1867', artistEndDate='1917', artistGender='', artistWikidata_URL='', artistULAN_URL='http://vocab.getty.edu/page/ulan/500095555', objectDate='1912', objectBeginDate=1912, objectEndDate=1912, medium='Gold', dimensions='Dimensions unavailable', creditLine='Gift of Heinz L. Stoppelmann, 1979', geographyType='', city='', state='', county='', country='', region='', subregion='', locale='', locus='', excavation='', river='', classification='Metal', rightsAndReproduction='', linkResource='', metadataDate='2020-03-02T21:50:01.377Z', repository='Metropolitan Museum of Art, New York, NY', objectURL='https://www.metmuseum.org/art/collection/search/10', tags=None, objectWikidata_URL='', isTimelineWork=False, GalleryNumber='')

# get all available departments

>>> departments = met_api.get_departments()
>>> departments
DepartmentsResponse(departments=[{'departmentId': '1', 'displayName': 'American Decorative Arts'}, {'departmentId': '3', 'displayName': 'Ancient Near Eastern Art'}, {'departmentId': '4', 'displayName': 'Arms and Armor'}, {'departmentId': '5', 'displayName': 'Arts of Africa, Oceania, and the Americas'}, {'departmentId': '6', 'displayName': 'Asian Art'}, {'departmentId': '7', 'displayName': 'The Cloisters'}, {'departmentId': '8', 'displayName': 'The Costume Institute'}, {'departmentId': '9', 'displayName': 'Drawings and Prints'}, {'departmentId': '10', 'displayName': 'Egyptian Art'}, {'departmentId': '11', 'displayName': 'European Paintings'}, {'departmentId': '12', 'displayName': 'European Sculpture and Decorative Arts'}, {'departmentId': '13', 'displayName': 'Greek and Roman Art'}, {'departmentId': '14', 'displayName': 'Islamic Art'}, {'departmentId': '15', 'displayName': 'The Robert Lehman Collection'}, {'departmentId': '16', 'displayName': 'The Libraries'}, {'departmentId': '17', 'displayName': 'Medieval Art'}, {'departmentId': '18', 'displayName': 'Musical Instruments'}, {'departmentId': '19', 'displayName': 'Photographs'}, {'departmentId': '21', 'displayName': 'Modern Art'}])

# search all objects with "sunflower" which have images 
>>> search_result = met_api.search(q="sunflower", has_images=True)
>>> search_result
ObjectsResponse(total=90, objectIDs=[551786, 472562, 317877, 544740, 329077, 459028, 459027, 544320, 39901, 207397, 824771, 438821, 435848, 460281, 820022, 437422, 53660, 452102, 237451, 207157, 549236, 451725, 435997, 436098, 192770, 436529, 201957, 437984, 383883, 39895, 811771, 811772, 436102, 452032, 437059, 430812, 736196, 822751, 759529, 435621, 452740, 40080, 436530, 764636, 437585, 228995, 626692, 435702, 60470, 437878, 436534, 452364, 200840, 228990, 436144, 53238, 53162, 452651, 436803, 436838, 201718, 453385, 437980, 437174, 437508, 436607, 439327, 712539, 435991, 436884, 436885, 435864, 437868, 436658, 44759, 435844, 436105, 451287, 437159, 453895, 437173, 436099, 733847, 448280, 437936, 450761, 450605, 435678, 437061, 437873])




```
