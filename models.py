from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None


m = User.model_validate({'id': 123, 'name': 'James'})
print(m)

try:
    m = User.model_validate_json('{"id": 123, "name" : "Cristian"}')
except ValidationError as e:
    print(e)