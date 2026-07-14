
from typing import Optional
from pydantic import BaseModel

class Boo(BaseModel):
    int: Optional[int] = None
    print(int)

me = Boo(int=123)