CREATE TABLE STAFF
(
  staffEmail varchar(30) NOT NULL
);

CREATE TABLE USER
(
  userId INT NOT NULL,
  fName INT NOT NULL,
  mName INT,
  lName INT,
  email INT NOT NULL,
  pwd INT NOT NULL,
  streetAddr INT NOT NULL,
  district INT NOT NULL,
  state INT NOT NULL,
  pinCode INT NOT NULL,
  phoneNum INT NOT NULL,
  USN INT NOT NULL,
  course INT NOT NULL,
  sem INT NOT NULL,
  PRIMARY KEY (userId)
);

CREATE TABLE LIBRARIAN
(
  librarianId INT NOT NULL,
  fName INT NOT NULL,
  mName INT,
  lName INT,
  email INT NOT NULL,
  pwd INT NOT NULL,
  streetAddr INT NOT NULL,
  district INT NOT NULL,
  state INT NOT NULL,
  pinCode INT NOT NULL,
  phoneNum INT NOT NULL,
  salary INT NOT NULL,
  PRIMARY KEY (librarianId)
);

CREATE TABLE PUBLISHER
(
  pubId INT NOT NULL,
  pubName INT NOT NULL,
  streetAddr INT NOT NULL,
  district INT NOT NULL,
  state INT NOT NULL,
  pinCode INT NOT NULL,
  phoneNum INT NOT NULL,
  PRIMARY KEY (pubId)
);

CREATE TABLE BOOK
(
  bookId INT NOT NULL,
  librarianId INT NOT NULL,
  pubId INT NOT NULL,
  title INT NOT NULL,
  pubYear INT NOT NULL,
  genre INT NOT NULL,
  ISBN INT NOT NULL,
  PRIMARY KEY (bookId),
  FOREIGN KEY (librarianId) REFERENCES LIBRARIAN(librarianId) on delete cascade,
  FOREIGN KEY (pubId) REFERENCES PUBLISHER(pubId) on delete cascade
);

CREATE TABLE AUTHOR
(
  authorId INT NOT NULL,
  fName INT NOT NULL,
  mName INT NOT NULL,
  lName INT NOT NULL,
  PRIMARY KEY (authorId)
);

CREATE TABLE STOCK
(
  bookId INT NOT NULL,
  librarianId INT NOT NULL,
  bookCopies INT NOT NULL,
  primary key(bookid),
  FOREIGN KEY (bookId) REFERENCES BOOK(bookId) on delete cascade,
  FOREIGN KEY (librarianId) REFERENCES LIBRARIAN(librarianId) on delete cascade
);

CREATE TABLE WrittenBy
(
  bookId INT NOT NULL,
  authorId INT NOT NULL,
  PRIMARY KEY (bookId, authorId),
  FOREIGN KEY (bookId) REFERENCES BOOK(bookId) on delete cascade,
  FOREIGN KEY (authorId) REFERENCES AUTHOR(authorId) on delete cascade
);

CREATE TABLE BORROWED_BOOKS
(
  bookId INT NOT NULL,
  userId INT NOT NULL,
  checkOut INT NOT NULL,
  dueDate INT NOT NULL,
  checkIn INT NOT NULL,
  PRIMARY KEY (userId, bookId),
  FOREIGN KEY (userId) REFERENCES USER(userId) on delete cascade,
  FOREIGN KEY (bookId) REFERENCES BOOK(bookId) on delete cascade
);