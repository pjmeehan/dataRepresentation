create table book(
    id int NOT NULL AUTO_INCREMENT,
    title varchar(100),
	author varchar(100)
	price int (10),
    PRIMARY KEY(id)
    );

insert into book (id, title, author, price) values (01,"McCarthy's Bar","Pete McCarthy", 10);	

