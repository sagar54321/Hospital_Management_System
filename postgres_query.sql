SET zero_damaged_pages = off;
SET TIME ZONE 'UTC';

CREATE TABLE billing (
  bid serial PRIMARY KEY,
  Pname varchar(20) NOT NULL,
  Disease varchar(20) NOT NULL,
  AddmissionDate date NOT NULL,
  DischargeDate date,
  "Doctor Name" varchar(20) NOT NULL,
  "Doctor Charge" int NOT NULL,
  "Room Type" varchar(20) NOT NULL,
  "Room cost" int NOT NULL,
  "Total Bill" int NOT NULL
);

select * from billing

CREATE TABLE doctor (
  did serial PRIMARY KEY,
  dname varchar(20) NOT NULL,
  "Speciality" varchar(20) NOT NULL,
  "Joining" date,
  "Experince" int NOT NULL,
  "Status" int NOT NULL,
  "Charge" int NOT NULL
);

select * from doctor

INSERT INTO doctor (did, dname, "Speciality", "Joining", "Experince", "Status", "Charge")
VALUES
  (1, 'Dr.Jayant', 'Cardiologist', '2022-06-15', 5, 1, 2000),
  (2, 'Dr.Abhishek', 'MS', '2022-06-15', 6, 1, 2500);

select charge from doctor where did=1


CREATE TABLE login (
  username varchar(10),
  password varchar(10)
);

INSERT INTO login (username, password)
VALUES
  ('Ram', 'ram123'),
  ('Sam', 'sam12'),
  ('Sham', 'sham1');

select * from login

CREATE TABLE patient (
  Pid serial PRIMARY KEY,
  Pname varchar(20) NOT NULL,
  AddmissionDate date,
  rid int NOT NULL,
  did int NOT NULL,
  Diseases varchar(20) NOT NULL
);

INSERT INTO patient (Pid, Pname, AddmissionDate, rid, did, Diseases)
VALUES
  (1, 'Preeti', '2022-06-06', 3, 1, 'HBP'),
  (2, 'Kritika', '2022-06-12', 2, 2, 'GRP'),
  (4, 'haja', '2022-08-15', 3, 1, 'asd');

select * from patient

INSERT INTO patient (Pid, Pname, AddmissionDate, rid, did, Diseases)
VALUES
  (7, 'Pre', '2023-06-06', 3, 1, 'HP')
	
CREATE TABLE rooms (
  rid serial PRIMARY KEY,
  type varchar(20) NOT NULL,
  cost int NOT NULL,
  count int NOT NULL
);

INSERT INTO rooms (rid, type, cost, count)
VALUES
  (1, 'General', 250, 10),
  (2, 'Deluxe Non AC', 500, 20),
  (3, 'Deluxe AC', 1000, 10);

select * from rooms

select * from doctor

