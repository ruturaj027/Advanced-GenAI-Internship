from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

# Home Route
@app.get("/")
def home():
    return {"message": "Welcome to City Public Library"}


# Initial Book Data
books = [
    {"id": 1, "title": "Python Basics", "author": "John Smith", "genre": "Tech", "is_available": True},
    {"id": 2, "title": "World History", "author": "Emma Brown", "genre": "History", "is_available": True},
    {"id": 3, "title": "Space Science", "author": "Alan White", "genre": "Science", "is_available": True},
    {"id": 4, "title": "Mystery House", "author": "David Clark", "genre": "Fiction", "is_available": True},
    {"id": 5, "title": "AI Future", "author": "Sophia Lee", "genre": "Tech", "is_available": True},
    {"id": 6, "title": "Ancient Wars", "author": "Mark Hall", "genre": "History", "is_available": True}
]

borrow_records = []
queue = []
record_counter = 1


# Helper Functions
def find_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return None


def calculate_due_date(days: int, member_type: str):
    if member_type == "premium":
        if days > 60:
            days = 60
        return f"Return by: Day {30 + days}"
    else:
        if days > 30:
            days = 30
        return f"Return by: Day {15 + days}"


def filter_books_logic(genre, author, is_available):
    result = books

    if genre:
        result = [b for b in result if b["genre"] == genre]

    if author:
        result = [b for b in result if b["author"] == author]

    if is_available is not None:
        result = [b for b in result if b["is_available"] == is_available]

    return result


# Pydantic Models
class BorrowRequest(BaseModel):
    member_name: str = Field(..., min_length=2)
    book_id: int = Field(..., gt=0)
    borrow_days: int = Field(..., gt=0, le=30)
    member_id: str = Field(..., min_length=4)
    member_type: str = "regular"


class NewBook(BaseModel):
    title: str
    author: str
    genre: str
    is_available: bool = True


# Get All Books
@app.get("/books")
def get_books():
    available = [b for b in books if b["is_available"]]

    return {
        "books": books,
        "total": len(books),
        "available_count": len(available)
    }


# Get Single Book
@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    return book


# Books Summary
@app.get("/books/summary")
def books_summary():
    genre_count = {}
    borrowed = 0

    for book in books:
        g = book["genre"]
        genre_count[g] = genre_count.get(g, 0) + 1

        if not book["is_available"]:
            borrowed += 1

    available = len([b for b in books if b["is_available"]])

    return {
        "total_books": len(books),
        "available": available,
        "borrowed": borrowed,
        "genre_breakdown": genre_count
    }


# Borrow Book
@app.post("/borrow")
def borrow_book(request: BorrowRequest):
    global record_counter

    book = find_book(request.book_id)

    if not book:
        return {"error": "Book not found"}

    if not book["is_available"]:
        return {"error": "Book already borrowed"}

    book["is_available"] = False

    due = calculate_due_date(
        request.borrow_days,
        request.member_type
    )

    record = {
        "record_id": record_counter,
        "member_name": request.member_name,
        "book_id": request.book_id,
        "due_date": due
    }

    borrow_records.append(record)
    record_counter += 1

    return record


# Return Book
@app.post("/return/{book_id}")
def return_book(book_id: int):
    global record_counter

    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    book["is_available"] = True

    for person in queue:
        if person["book_id"] == book_id:

            queue.remove(person)

            book["is_available"] = False

            record = {
                "record_id": record_counter,
                "member_name": person["member_name"],
                "book_id": book_id,
                "due_date": "Auto-assigned"
            }

            borrow_records.append(record)
            record_counter += 1

            return {
                "message": "Returned and re-assigned",
                "record": record
            }

    return {"message": "Returned and available"}


# Borrow Records
@app.get("/borrow-records")
def get_records():
    return {
        "records": borrow_records,
        "total": len(borrow_records)
    }


# Add New Book
@app.post("/books")
def add_book(book: NewBook):
    for b in books:
        if b["title"].lower() == book.title.lower():
            return {"error": "Duplicate title"}

    new_id = max(b["id"] for b in books) + 1

    new_book = {
        "id": new_id,
        **book.dict()
    }

    books.append(new_book)

    return new_book


# Update Book
@app.put("/books/{book_id}")
def update_book(
    book_id: int,
    genre: Optional[str] = None,
    is_available: Optional[bool] = None
):
    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    if genre:
        book["genre"] = genre

    if is_available is not None:
        book["is_available"] = is_available

    return book


# Delete Book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    books.remove(book)

    return {"message": "Book deleted successfully"}


# Filter Books
@app.get("/books/filter")
def filter_books(
    genre: Optional[str] = None,
    author: Optional[str] = None,
    is_available: Optional[bool] = None
):
    result = filter_books_logic(
        genre,
        author,
        is_available
    )

    return {
        "count": len(result),
        "books": result
    }


# Queue System
@app.post("/queue/add")
def add_to_queue(member_name: str, book_id: int):
    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    if book["is_available"]:
        return {"message": "Book available — borrow directly"}

    queue.append({
        "member_name": member_name,
        "book_id": book_id
    })

    return {"message": "Added to queue"}


@app.get("/queue")
def get_queue():
    return {
        "queue": queue,
        "total": len(queue)
    }


# Search Books
@app.get("/books/search")
def search_books(keyword: str):
    keyword = keyword.lower()

    results = [
        b for b in books
        if keyword in b["title"].lower()
        or keyword in b["author"].lower()
    ]

    return {
        "results": results,
        "total_found": len(results)
    }


# Sort Books
@app.get("/books/sort")
def sort_books(
    sort_by: str = "title",
    order: str = "asc"
):
    reverse = order == "desc"

    sorted_books = sorted(
        books,
        key=lambda x: x[sort_by],
        reverse=reverse
    )

    return {
        "sorted_by": sort_by,
        "order": order,
        "books": sorted_books
    }


# Pagination
@app.get("/books/page")
def paginate_books(
    page: int = 1,
    limit: int = 3
):
    start = (page - 1) * limit
    end = start + limit

    total = len(books)
    total_pages = (total + limit - 1) // limit

    return {
        "total": total,
        "total_pages": total_pages,
        "current_page": page,
        "books": books[start:end]
    }


# Borrow Records Search
@app.get("/borrow-records/search")
def search_records(member_name: str):
    results = [
        r for r in borrow_records
        if member_name.lower()
        in r["member_name"].lower()
    ]

    return {
        "results": results,
        "total_found": len(results)
    }


# Borrow Records Pagination
@app.get("/borrow-records/page")
def paginate_records(
    page: int = 1,
    limit: int = 2
):
    start = (page - 1) * limit
    end = start + limit

    total = len(borrow_records)
    total_pages = (total + limit - 1) // limit

    return {
        "total": total,
        "total_pages": total_pages,
        "current_page": page,
        "records": borrow_records[start:end]
    }


# Browse Books (Search + Sort + Pagination)
@app.get("/books/browse")
def browse_books(
    keyword: Optional[str] = None,
    sort_by: str = "title",
    order: str = "asc",
    page: int = 1,
    limit: int = 3
):
    result = books

    if keyword:
        keyword = keyword.lower()

        result = [
            b for b in result
            if keyword in b["title"].lower()
            or keyword in b["author"].lower()
        ]

    reverse = order == "desc"

    result = sorted(
        result,
        key=lambda x: x[sort_by],
        reverse=reverse
    )

    start = (page - 1) * limit
    end = start + limit

    total = len(result)
    total_pages = (total + limit - 1) // limit

    return {
        "page": page,
        "total_pages": total_pages,
        "results": result[start:end]
    }
