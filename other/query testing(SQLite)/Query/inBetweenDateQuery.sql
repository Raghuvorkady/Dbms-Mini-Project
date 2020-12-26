select USER.fName, BOOK.title, BOOK.bookId
from BORROWED_BOOKS, USER, BOOK
where BOOK.bookId = BORROWED_BOOKS.bookId AND BORROWED_BOOKS.userId = USER.userId
GROUP BY BOOK.bookId
HAVING checkOut between '12-15-2019' and '3/15/2020' ;