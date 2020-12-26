insert into STAFF (staffEmail) values ('rlynnett0@histats.com');
insert into STAFF (staffEmail) values ('lspilsbury1@ftc.gov');
insert into STAFF (staffEmail) values ('fiverson2@1688.com');
insert into STAFF (staffEmail) values ('mthewles3@is.gd');
insert into STAFF (staffEmail) values ('cpundy4@xrea.com');
insert into STAFF (staffEmail) values ('clelievre5@addthis.com');
insert into STAFF (staffEmail) values ('gdiggins6@stumbleupon.com');
insert into STAFF (staffEmail) values ('dabbots7@shareasale.com');
insert into STAFF (staffEmail) values ('bmaxworthy8@geocities.jp');
insert into STAFF (staffEmail) values ('tellams9@hc360.com');


insert into USER (userID, fName, mName, lName, email, pwd, streetAddr, district, state, pinCode, phoneNum, USN, course, sem) values 
(1101, 'Nikaniki', 'Léone', 'Cool', 'ncool0@sitemeter.com', '3ORxsy2LDZWI', '8905 Melody Center', 'Delhi', 'Bulgaria', 8216, 3046308781, '1BY18IS001', 'CSE', 1);

insert into USER (userID, fName, mName, lName, email, pwd, streetAddr, district, state, pinCode, phoneNum, USN, course, sem) values 
(1102, 'Elke', 'Laurène', 'Feakins', 'efeakins1@hp.com', 'i2AiUhswUhSI', '61 Crownhardt Drive', 'Östergötland', 'Sweden', 60181, 3374545615, '1BY18IS002', 'ISE', 2);

insert into USER (userID, fName, mName, lName, email, pwd, streetAddr, district, state, pinCode, phoneNum, USN, course, sem) values 
(1103, 'Josiah', 'Michèle', 'Jahnke', 'jjahnke2@bravesites.com', 'nXWczjm5Zi', '1464 Bultman Park', 'London', 'Brazil', 18950000, 3252956567, '1BY18IS003', 'ME', 3);

insert into USER (userID, fName, mName, lName, email, pwd, streetAddr, district, state, pinCode, phoneNum, USN, course, sem) values 
(1104, 'Dell', 'Lèi', 'Chstney', 'dchstney3@drupal.org', 'XAYdpsHU', '914 Graedel Point', 'London', 'Tunisia', 45651, 8609499794, '1BY18IS004', 'ISE', 4);

insert into USER (userID, fName, mName, lName, email, pwd, streetAddr, district, state, pinCode, phoneNum, USN, course, sem) values 
(1105, 'Zoe', 'Adélaïde', 'Fishe', 'zfishe4@parallels.com', 'MH5Xdu', '17462 Shopko Park', 'London', 'Russia', 152891, 3846088471, '1BY18IS005', 'ECE', 5);


insert into LIBRARIAN (librarianID, fName, mName, lName, email, pwd, streetAddr, district, state, pinCode, phoneNum, salary) values 
(2101, 'Gibb', 'Angélique', 'Trenfield', 'gtrenfield0@histats.com', 'D0n9XLxr', '0 Talisman Street', 'Wuhan', 'China', 671323, 2392292409, 20000);

insert into LIBRARIAN (librarianID, fName, mName, lName, email, pwd, streetAddr, district, state, pinCode, phoneNum, salary) values 
(2102, 'Giselle', 'Mylène', 'Milliere', 'gmilliere1@bloglovin.com', 'beI0fa', '6 Macpherson Lane', 'Wuhan', 'China', 671323, 9336291402, 25000);

insert into LIBRARIAN (librarianID, fName, mName, lName, email, pwd, streetAddr, district, state, pinCode, phoneNum, salary) values 
(2103, 'Amelita', 'Régine', 'Garfit', 'agarfit2@tinypic.com', 'KNK5leC4Z', '535 Southridge Point', 'Wuhan', 'China', 671323, 5381835516, 20000);


insert into PUBLISHER (pubID, pubName, streetAddr, district, state, pinCode, phoneNum) values 
(3101, 'Hunfredo', '831 Eagle Crest Park', 'Florida', 'California', 33963, 2395328200);

insert into PUBLISHER (pubID, pubName, streetAddr, district, state, pinCode, phoneNum) values 
(3102, 'Glynda', '26404 Larry Alley', 'Ohio', 'New York', 44485, 3308272176);

insert into PUBLISHER (pubID, pubName, streetAddr, district, state, pinCode, phoneNum) values 
(3103, 'Marion', '359 Bluestem Circle', 'New Hampshire', 'Indiana', 03105, 6037966569);

insert into PUBLISHER (pubID, pubName, streetAddr, district, state, pinCode, phoneNum) values 
(3104, 'Cecily', '02 Goodland Point', 'Nevada', 'Washington', 89140, 7027844834);

insert into PUBLISHER (pubID, pubName, streetAddr, district, state, pinCode, phoneNum) values 
(3105, 'Thea', '64814 Doe Crossing Avenue', 'California', 'Arizona', 93794, 5597595882);


insert into BOOK (bookID, librarianID, pubID, title, pubYear, genre, ISBN) values 
	(4101, 2101, 3101, 'Egyptian cobra', 2008, 'Drama|War', 1975233514);

insert into BOOK (bookID, librarianID, pubID, title, pubYear, genre, ISBN) values 
	(4102, 2102, 3102, 'Little heron', 1989, 'Drama|Romance', 0210621795);

insert into BOOK (bookID, librarianID, pubID, title, pubYear, genre, ISBN) values 
	(4103, 2103, 3103, 'Crowned hawk-eagle', 2007, 'Drama|Romance', 4305841541);

insert into BOOK (bookID, librarianID, pubID, title, pubYear, genre, ISBN) values 
	(4104, 2101, 3104, 'Black spider monkey', 2003, 'Drama|Fantasy', 9744602678);

insert into BOOK (bookID, librarianID, pubID, title, pubYear, genre, ISBN) values 
	(4105, 2101, 3105, 'Skink, african', 2004, 'Adventure|Children|Drama', 3245019327);

insert into BOOK (bookID, librarianID, pubID, title, pubYear, genre, ISBN) values 
	(4106, 2102, 3101, 'Glossy starling (unidentified)', 2004, 'Drama', 0453069681);

insert into BOOK (bookID, librarianID, pubID, title, pubYear, genre, ISBN) values 
	(4107, 2102, 3101, 'Duck, white-faced whistling', 2012, 'Comedy|Romance', 7895422316);

insert into BOOK (bookID, librarianID, pubID, title, pubYear, genre, ISBN) values 
	(4108, 2103, 3101, 'Buffalo, wild water', 1992, 'Documentary', 1526453800);

insert into BOOK (bookID, librarianID, pubID, title, pubYear, genre, ISBN) values 
	(4109, 2103, 3102, 'Gull, dusky', 1997, 'Comedy|Crime|Drama|Western', 7564049103);

insert into BOOK (bookID, librarianID, pubID, title, pubYear, genre, ISBN) values 
	(4110, 2103, 3105, 'Radiated tortoise', 2004, 'Comedy|Thriller', 9642044110);


insert into AUTHOR (authorId, fName, mName, lName) values (5101, 'Herbie', 'Görel', 'Mettricke');
insert into AUTHOR (authorId, fName, mName, lName) values (5102, 'Roth', 'Béatrice', 'Norfolk');
insert into AUTHOR (authorId, fName, mName, lName) values (5103, 'Raven', 'André', 'Grossman');
insert into AUTHOR (authorId, fName, mName, lName) values (5104, 'Chip', 'Bécassine', 'Trythall');
insert into AUTHOR (authorId, fName, mName, lName) values (5105, 'Eli', 'Noëlla', 'Hovey');
insert into AUTHOR (authorId, fName, mName, lName) values (5106, 'Cayla', 'Yáo', 'Pickavant');
insert into AUTHOR (authorId, fName, mName, lName) values (5107, 'Amalle', 'Frédérique', 'Stallard');
insert into AUTHOR (authorId, fName, mName, lName) values (5108, 'Eldon', 'Séréna', 'Bortoluzzi');
insert into AUTHOR (authorId, fName, mName, lName) values (5109, 'Bari', 'Zoé', 'Milkins');
insert into AUTHOR (authorId, fName, mName, lName) values (5110, 'Arlee', 'Cécile', 'Pyer');


insert into STOCK (bookID, librarianID, bookCopies) values (4101, 2101, 6);
insert into STOCK (bookID, librarianID, bookCopies) values (4102, 2102, 15);
insert into STOCK (bookID, librarianID, bookCopies) values (4103, 2103, 4);
insert into STOCK (bookID, librarianID, bookCopies) values (4104, 2101, 10);
insert into STOCK (bookID, librarianID, bookCopies) values (4105, 2101, 20);
insert into STOCK (bookID, librarianID, bookCopies) values (4106, 2102, 2);
insert into STOCK (bookID, librarianID, bookCopies) values (4107, 2102, 12);
insert into STOCK (bookID, librarianID, bookCopies) values (4108, 2102, 7);
insert into STOCK (bookID, librarianID, bookCopies) values (4109, 2103, 4);
insert into STOCK (bookID, librarianID, bookCopies) values (4110, 2103, 8);


insert into WrittenBy (bookID, authorId) values (4101, 5104);
insert into WrittenBy (bookID, authorId) values (4105, 5102);
insert into WrittenBy (bookID, authorId) values (4102, 5107);
insert into WrittenBy (bookID, authorId) values (4104, 5108);
insert into WrittenBy (bookID, authorId) values (4104, 5109);


insert into BORROWED_BOOKS (bookID, userID, checkOut, checkIn, dueDate) values (4101, 1101, '5/2/2020', '12/6/2019', '9/23/2020');
insert into BORROWED_BOOKS (bookID, userID, checkOut, checkIn, dueDate) values (4102, 1102, '7/20/2020', '5/12/2020', '3/15/2020');
insert into BORROWED_BOOKS (bookID, userID, checkOut, checkIn, dueDate) values (4103, 1103, '8/15/2020', '1/16/2020', '7/31/2020');
insert into BORROWED_BOOKS (bookID, userID, checkOut, checkIn, dueDate) values (4104, 1104, '7/21/2020', '6/17/2020', '7/11/2020');
insert into BORROWED_BOOKS (bookID, userID, checkOut, checkIn, dueDate) values (4105, 1105, '3/15/2020', '8/23/2020', '8/1/2020');
insert into BORROWED_BOOKS (bookID, userID, checkOut, checkIn, dueDate) values (4106, 1101, '12/15/2019', '9/9/2020', '1/24/2020');
insert into BORROWED_BOOKS (bookID, userID, checkOut, checkIn, dueDate) values (4107, 1101, '1/21/2020', '3/14/2020', '2/7/2020');
insert into BORROWED_BOOKS (bookID, userID, checkOut, checkIn, dueDate) values (4101, 1102, '5/20/2020', '8/6/2020', '1/24/2020');
insert into BORROWED_BOOKS (bookID, userID, checkOut, checkIn, dueDate) values (4101, 1103, '8/30/2020', '12/26/2019', '10/22/2020');
insert into BORROWED_BOOKS (bookID, userID, checkOut, checkIn, dueDate) values (4102, 1103, '7/28/2020', '5/9/2020', '8/29/2020');