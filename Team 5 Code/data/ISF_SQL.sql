CREATE TABLE ISF_Cohort (
	CohortID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	StartDate DATE NOT NULL DEFAULT (datetime('now','localtime'))
);

CREATE TABLE ISF_Course (
	CourseID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	CourseTitle varchar(20),
	CourseDescription varchar(100),
	CreditHours int NOT NULL DEFAULT 3
);

CREATE TABLE ISF_Student (
	StudentID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	CohortID int NOT NULL,
	StudentFname varchar(30),
	StudentLname varchar(30),
	StudentEmail varchar(50),
	EmployeeID varchar(30) NOT NULL DEFAULT '',
	FOREIGN KEY (CohortID) REFERENCES ISF_Cohort(CohortID)		
);

CREATE TABLE ISF_Section (
	SectionNum INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	CourseID int NOT NULL,
	CohortID int NOT NULL,
	SectionDetail varchar(50),
	Schedule varchar(50),
	FOREIGN KEY (CourseID) REFERENCES ISF_Course(CourseID),
	FOREIGN KEY (CohortID) REFERENCES ISF_Cohort(CohortID)
);

CREATE TABLE ISF_StudentEnroll (
	EnrollmentID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	StudentID int NOT NULL,
	SectionNum int NOT NULL,
	EnrollmentDate date,
	FOREIGN KEY (StudentID) REFERENCES ISF_Student(StudentID),
	FOREIGN KEY (SectionNum) REFERENCES ISF_Section(SectionNum)
);

