from fastapi import FastAPI, APIRouter

router = APIRouter()


@router.get('/myhome/users/photos')
def photos():
    return 'show photos'
