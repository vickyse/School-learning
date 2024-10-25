CREATE TABLE IF NOT EXISTS dept_manager (
  dept_no char(4) NOT NULL,
  emp_no int NOT NULL,
  from_date date NOT NULL,
  to_date date NOT NULL,
  PRIMARY KEY (emp_no, dept_no),
  CONSTRAINT dept_manager_emp_no_fk FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
  CONSTRAINT dept_manager_dept_no_fk FOREIGN KEY (dept_no) REFERENCES departments (dept_no)
);

-- Dumping data for table employee.dept_manager: ~24 rows (approximately)
INSERT INTO dept_manager (dept_no, emp_no, from_date, to_date) VALUES
	('d001', 110022, '1985-01-01', '1991-10-01'),
	('d001', 110039, '1991-10-01', '9999-01-01'),
	('d002', 110085, '1985-01-01', '1989-12-17'),
	('d002', 110114, '1989-12-17', '9999-01-01'),
	('d003', 110183, '1985-01-01', '1992-03-21'),
	('d003', 110228, '1992-03-21', '9999-01-01'),
	('d004', 110303, '1985-01-01', '1988-09-09'),
	('d004', 110344, '1988-09-09', '1992-08-02'),
	('d004', 110386, '1992-08-02', '1996-08-30'),
	('d004', 110420, '1996-08-30', '9999-01-01'),
	('d005', 110511, '1985-01-01', '1992-04-25'),
	('d005', 110567, '1992-04-25', '9999-01-01'),
	('d006', 110725, '1985-01-01', '1989-05-06'),
	('d006', 110765, '1989-05-06', '1991-09-12'),
	('d006', 110800, '1991-09-12', '1994-06-28'),
	('d006', 110854, '1994-06-28', '9999-01-01'),
	('d007', 111035, '1985-01-01', '1991-03-07'),
	('d007', 111133, '1991-03-07', '9999-01-01'),
	('d008', 111400, '1985-01-01', '1991-04-08'),
	('d008', 111534, '1991-04-08', '9999-01-01'),
	('d009', 111692, '1985-01-01', '1988-10-17'),
	('d009', 111784, '1988-10-17', '1992-09-08'),
	('d009', 111877, '1992-09-08', '1996-01-03'),
	('d009', 111939, '1996-01-03', '9999-01-01');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
