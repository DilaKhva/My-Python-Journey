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
