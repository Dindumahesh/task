introduction of sql

#create table
create table employee(emp_name varchar(20),location varchar(20));

# add column in employee table 
alter table employee add address varchar(20);

#add column emp_id in first 
alter table employee add emp_int first;

#add column at specific postion 
alter table employee add email varchar(25) after emp_id;

#modify empname char to varchar
alter table employee modify column emp_name char to varchar(20);

# add sid and department at a time 
alter table employee add sid int, department varchar(50);

#rename emp_name to employeename.
alter table employee rename column emp_name to employeename;

#drop sid column
alter table employee drop sid; 


