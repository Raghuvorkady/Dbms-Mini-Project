SELECT BOOK.title, USER.fName, checkOut FROM BORROWED_BOOKS, USER, BOOK 
WHERE BORROWED_BOOKS.userId = USER.userId and BOOK.bookId = BORROWED_BOOKS.bookId;