CREATE TABLE teacher(
	id SERIAL PRIMARY KEY, 
	fullname VARCHAR(50) NOT NULL,
	phone VARCHAR(20)
);

CREATE TABLE subject(
	id SERIAL PRIMARY KEY,
	title VARCHAR(50) NOT NULL,
	description VARCHAR(200)
);

CREATE TABLE groupp(
	id SERIAL PRIMARY KEY,
	title VARCHAR(50) NOT NULL,
	academic_year INTEGER CHECK (academic_year>2020),
	teacher_id INT REFERENCES teacher(id),
	subject_id INT REFERENCES subject(id)
);

CREATE TABLE student(
	id SERIAL PRIMARY KEY,
	fullname VARCHAR(50) NOT NULL,
	phone VARCHAR(20)
);

CREATE TABLE teacher_subject(
	id SERIAL PRIMARY KEY,
	teacher_id INT REFERENCES teacher(id),
	subject_id INT REFERENCES subject(id) 
);

CREATE TABLE student_group(
	id SERIAL PRIMARY KEY,
	student_id INT REFERENCES student(id),
	group_id INT REFERENCES groupp(id)
);

CREATE TABLE hometask(
	id SERIAL PRIMARY KEY,
	theme VARCHAR(100) NOT NULL,
	description VARCHAR(200),
	group_id INT REFERENCES groupp(id)
);

CREATE TABLE payment(
	id SERIAL PRIMARY KEY,
	amount INT NOT NULL,
	status VARCHAR(50),
	deadline DATE,
	student_id INT REFERENCES student(id)
);

CREATE TABLE attendance(
	id SERIAL PRIMARY KEY,
	status VARCHAR(50) NOT NULL,
	date_of_a DATE,
	student_id INT REFERENCES student(id)
)


-- https://lucid.app/lucidchart/5a4e23ba-9f9c-4866-9fce-079363175ae3/edit?viewport_loc=197%2C271%2C1606%2C862%2C0_0&invitationId=inv_9e026846-c90a-4d39-99c6-18f287fa0cf0
-- scheme
