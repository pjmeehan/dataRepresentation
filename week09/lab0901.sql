create table student(
    id int NOT NULL AUTO_INCREMENT,
    firstname varchar(100),
    age int (3),
    PRIMARY KEY(id)
    );

insert into student (firstname, age) values (’joe’,56);	

select * from student;

update student set firstname=’mary’ where id = 1;