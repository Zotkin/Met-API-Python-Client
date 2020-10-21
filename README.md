# The Metropolitan Museum Of Art Python API Client

An unofficial python client for The Metropolitan Museum of Art Collection API.
This client fully implements a convinient python interface for the methods described [here](https://metmuseum.github.io/).
Build using [requests](https://github.com/psf/requests) and [pydantic](https://github.com/samuelcolvin/pydantic). 

Examples:
 
```python
from met_api import get_objects
from datetime import datetime

objects = get_object()
```
