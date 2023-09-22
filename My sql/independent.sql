create database independent;
use independent;
create table voterlist(id int unique not null,adhar_number bigint not null unique,
Name varchar(55) not null default "pulakesh",age int ,address varchar(244) not null,
phno bigint default "0000000000",country varchar(55) default "india",
check (age>10));
desc voterlist;
/* modify the table*/
alter  table voterlist modify dob date default "1999-12-07";

insert into  voterlist(id,adhar_number,age,address) values(12,365845333999,24,"pune");
select * from voterlist;
alter  table voterlist  add lname varchar(55);
