from fastapi import FastAPI, APIRouter

router = APIRouter()

class


@router.get('/my-library/books/{book_id}') # book_id is embedded in the link where the book photo is
def photos(book_id):
    if book_id:
        return 'Available'
    return 'Not available'


@router.get('my-library/books/search')
def search(author: str, genre: str, year: int, name, str):

