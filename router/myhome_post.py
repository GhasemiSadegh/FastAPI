from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix='/blog', tags=['posts'])


class PydanticValidator(BaseModel):
    name: str
    age: int
    postalcode: int
    street: str


@router.post('/new')
def my_post(myhome: BaseModel):
    return {'Msg': 'ok', "data": myhome}
