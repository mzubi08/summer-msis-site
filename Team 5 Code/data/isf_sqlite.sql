CREATE TABLE ISF_Cohort (
	CohortID int NOT NULL PRIMARY KEY,
	CohortDescription varchar(100)
);

CREATE TABLE ISF_Course (
	CourseID int NOT NULL PRIMARY KEY,
	CourseTitle varchar(20),
	CourseDecription varchar(100),
	CreditHours int NOT NULL
);

CREATE TABLE ISF_Student (
	StudentID int NOT NULL PRIMARY KEY,
	CohortID int NOT NULL,
	StudentFname varchar(30),
	StudentLname varchar(30),
	StudentDOB date,
	StudentEmail varchar(50),
	StudentPhone varchar(15),
	StudentAddress varchar(50),
	FOREIGN KEY (CohortID) REFERENCES ISF_Cohort(CohortID)		
);

CREATE TABLE ISF_Section (
	SectionNum int NOT NULL PRIMARY KEY,
	CourseID int NOT NULL,
	CohortID int NOT NULL,
	SectionDetail varchar(50),
	StartDate date,
	EndDate date,
	Schedule varchar(50),
	FOREIGN KEY (CourseID) REFERENCES ISF_Course(CourseID),
	FOREIGN KEY (CohortID) REFERENCES ISF_Cohort(CohortID)
);

CREATE TABLE ISF_StudentEnroll (
	EnrollmentID int NOT NULL PRIMARY KEY,
	StudentID int NOT NULL,
	SectionNum int NOT NULL,
	EnrollmentDate date,
	FOREIGN KEY (StudentID) REFERENCES ISF_Student(StudentID),
	FOREIGN KEY (SectionNum) REFERENCES ISF_Section(SectionNum)
);

