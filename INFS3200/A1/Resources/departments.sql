CREATE TABLE IF NOT EXISTS departments (
  dept_no char(4) NOT NULL,
  dept_name varchar(40) NOT NULL,
  PRIMARY KEY (dept_no),
  CONSTRAINT departments_dept_name_unique UNIQUE (dept_name)
);

-- Dumping data for table employee.departments: ~9 rows (approximately)
INSERT INTO departments (dept_no, dept_name) VALUES
	('d009', 'Customer Service'),
	('d005', 'Development'),
	('d002', 'Finance'),
	('d003', 'Human Resources'),
	('d001', 'Marketing'),
	('d004', 'Production'),
	('d006', 'Quality Management'),
	('d008', 'Research'),
	('d007', 'Sales');

