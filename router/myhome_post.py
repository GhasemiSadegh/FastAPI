from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix='/myhome', tags=['posts'])


class PydanticValidator(BaseModel):
    name: str
    age: int
    postalcode: Optional[int] = None
    present: bool = True


@router.post('/posts')
def my_post(myhome: PydanticValidator):
    print(myhome.name)
    print(myhome.age)
    return {'Msg': 'ok', "data": myhome}
