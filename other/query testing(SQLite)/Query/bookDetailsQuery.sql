select BOOK.bookId, title, PUBLISHER.pubId, PUBLISHER.pubName, AUTHOR.authorId,AUTHOR.fName as AuthorName, STOCK.bookCopies
from BOOK, STOCK, PUBLISHER, AUTHOR, WrittenBy
where BOOK.bookId = WrittenBy.bookID and WrittenBy.authorId = AUTHOR.authorId AND
BOOK.bookId = STOCK.bookId and BOOK.pubId = PUBLISHER.pubId;
