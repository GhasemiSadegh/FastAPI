from fastapi import APIRouter

router = APIRouter(prefix='/blog', tags=['posts'])


@router.post('/new')
def my_post():
    return {'Jason': 'ok'}
