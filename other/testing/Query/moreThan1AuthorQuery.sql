select BOOK.bookId, BOOK.title
from WrittenBy, BOOK, AUTHOR
WHERE BOOK.bookId = WrittenBy.bookId AND WrittenBy.authorId = AUTHOR.authorId
GROUP by BOOK.bookId
HAVING count(*) > 1;
