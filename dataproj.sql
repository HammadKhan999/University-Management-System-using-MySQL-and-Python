create table student
(
student_id int NOT NULL primary key,
first_name varchar(50),
last_name varchar(50),
department varchar(50),
addres varchar(50),
semester int,
)
insert into student values(191234,'hammad','khan','bce','xyz',7);
insert into student values(191235,'hammad','khan','bce','xyz',7);
insert into student values(191291,'hammad','khan','bce','xyz',7);
insert into student values(191237,'hammad','khan','bce','xyz',7);
insert into student values(191238,'hammad','khan','bce','xyz',7);
insert into student values(191239,'hammad','khan','bce','xyz',7);
insert into student values(191240,'hammad','khan','bce','xyz',7);
insert into student values(191241,'hammad','khan','bce','xyz',7);
insert into student values(191242,'hammad','khan','bce','xyz',7);
insert into student values(191243,'hammad','khan','bce','xyz',7);
select * from student;

create table faculty
(
fac_id int NOT NULL primary key,
first_name varchar(50),
last_name varchar(50),
designation varchar(50),
department varchar(50),
addres varchar(50),
contract_type varchar(50),
)
select * from faculty;

create table staff
(
staff_id int NOT NULL primary key,
first_name varchar(50),
last_name varchar(50),
designation varchar(50),
department varchar(50),
addres varchar(50),
phone_no varchar(50),
)

