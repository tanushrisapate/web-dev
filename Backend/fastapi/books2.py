from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import Field,BaseModel
from typing import Optional
from starlette import status

app = FastAPI()

class BOOK:
  id: int
  title: str
  author: str
  description: str
  rating: int
  published_date: int
  

  def __init__(self,id,title,author,description,rating,published_date): 
    self.id = id
    self.title = title
    self.author = author
    self.description = description
    self.rating = rating
    self.published_date = published_date

class BookRequest(BaseModel):
  id : Optional[int] = Field(description='ID is not needed on create',default=None)
  title:str = Field(min_length =3)
  author:str = Field(min_length = 1)
  description:str = Field(min_length=1,max_length=100)
  rating:int = Field(gt=0,lt=6)
  published_date:int = Field(gt=1000,lt=2027)

  model_config ={
    "json_schema_extra" : {
      "example" : {
        "title" : "A new book",
        "author" : "authorone",
        "description" :"A new beginning",
        "rating" : 5,
        "published_date" :2012
      }
    }
  }


BOOK1 = [
    BOOK(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5,2000),
    BOOK(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5,1960),
    BOOK(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5,2026),
    BOOK(4, 'HP1', 'Author 1', 'Book Description', 2,2020),
    BOOK(5, 'HP2', 'Author 2', 'Book Description', 3,2026),
    BOOK(6, 'HP3', 'Author 3', 'Book Description', 1,1987)
]

@app.get("/books",status_code = status.HTTP_200_OK)
async def read_all_books():
  return BOOK1

def find_book_id(book:BOOK):
  if len(BOOK1) >0:
    book.id = BOOK1[-1].id + 1
  else:
    book.id =1

  return book

@app.post("/books/create-book",status_code=status.HTTP_201_CREATED)
async def create_book(book_request : BookRequest):
  new_book = BOOK(**book_request.model_dump())
  find_book_id(new_book)
  BOOK1.append(new_book)
  return new_book


@app.get("/books/{book_id}",status_code = status.HTTP_200_OK)
async def fetch_by_book_id(book_id:int = Path(ge=0)):
  for i in range(len(BOOK1)):
    if BOOK1[i].id == book_id:
      return BOOK1[i]
  raise HTTPException(status_code=404, detail='Item Not found')

@app.get("/books/")
async def fetch_by_rating(book_rating :int = Query(ge=0,le=5)):
  books_to_return =[]
  for i in range(len(BOOK1)):
    if BOOK1[i].rating >= book_rating:
      books_to_return.append(BOOK1[i])
  return books_to_return

@app.put("/books/update_books")
async def book_updated(book:BookRequest):
  book_changed = False
  for i in range(len(BOOK1)):
    if BOOK1[i].id == book.id:
      BOOK1[i] = BOOK(**book.model_dump())
      book_changed = True
  if not book_changed:
    raise HTTPException(status_code =404,detail="book not found")
  

@app.delete("/books/delete/{book_id}")
async def book_delete(book_id:int = Path(ge=0)):
  for i in range(len(BOOK1)):
    if BOOK1[i].id == book_id:
      BOOK1.pop(i)
      break

@app.get("/books/publish/")
async def fetch_by_published_date(publish:int = Query(ge=1000,le=2027)):
  books_to_return=[]
  for i in range(len(BOOK1)):
    if BOOK1[i].published_date == publish:
      books_to_return.append(BOOK1[i])

  return books_to_return


