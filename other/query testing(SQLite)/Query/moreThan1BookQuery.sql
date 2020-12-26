select AUTHOR.fName, AUTHOR.authorId
from BOOK, AUTHOR, WrittenBy
WHERE BOOK.bookId = WrittenBy.bookID and WrittenBy.authorId = AUTHOR.authorId
GROUP by AUTHOR.authorId
HAVING count(*) > 1;