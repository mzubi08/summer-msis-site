from isf_db_helper import DbHelper

import sqlite3

#################################################
############# Class for Cohort Table
#################################################

class CohortModel:
    """
    A simple example class. Attributes match the database
       table `Sushi` exactly: id, name, price
    
    Modifying this class to match a different entity is easy:
    1. Change the file name
    2. Change the class name. Suggest something that ends in ___Model,
       like VehicleModel or PersonModel.
    3. Update the constructor (the `__init__` method) with your desired
       default values.
    4. Update the SQL statements in the `create()`, `update()`, `delete()`,
       `fetch_by_id()`, and `fetch_all()` methods. Only the SQL statements and
       the parameters to the `cursor.execute()` call need to be changed.
    5. Update the `__str__()` method so the class can be printed easily. This
       will help with debugging.
    """

    def __init__(self, data = {}):
        """
        Populates class fields, if available, or uses default values
        """
        if isinstance(data, sqlite3.Row):
            data = dict(data)

        # Assign the values in the dict to the instance variables in the ISF_Cohort Table
        self.CohortID = data.get('CohortID', None)
        self.StartDate = data.get('StartDate', '#######')

    ####################
    # Method definitions
    # These require the instance variables already be populated
    
    def create(self):
        """ () -> sushi
        Creates a new sushi record in the databse, and returns the
        newly created object.
        No id is passed, as that's assigned by the database
        """
        cursor = DbHelper.get_cursor()
        cursor.execute(
            'INSERT INTO ISF_Cohort (StartDate) VALUES (?)',
            (self.StartDate,)
        )
        self.CohortID = cursor.lastrowid
        return self
    
##    def update(self):
##        cursor = DbHelper.get_cursor()
##        cursor.execute(
##            'UPDATE ISF_Cohort SET StartDate=? WHERE CohortID=?',
##            (self.StartDate, self.CohortID)
##        )
##        return self
##    
##    def delete(self):
##        cursor = DbHelper.get_cursor()
##        cursor.execute(
##            'DELETE FROM ISF_Cohort WHERE CohortID = ?,
##            (self.CohortID,) # need the trailing comma
##        )
##        return None



    ####################
    # Static methods
    # These don't require an instance already exist

    #Select the information about the Cohort based on the CohortID user choose
    @staticmethod
    def fetch_by_id(find_me):
        cursor = DbHelper.get_cursor()
        cursor.execute(
            'SELECT CohortID, StartDate FROM ISF_Cohort WHERE CohortID = ?',
            (find_me,) # need the trailing comma
        )
        s = cursor.fetchone()
        return CohortModel(s) if s is not None else None

    @staticmethod
    def fetch_all():
        """ () -> [SushiModel, ...]
        Fetches all sushi from the database, and returns as a list
        of SushiModel objects.
        """
        cur = DbHelper.get_cursor()
        cur.execute('SELECT CohortID, StartDate FROM ISF_Cohort')
        result = [CohortModel(row) for row in cur.fetchall()]
        return result
        
    # Override what an instance looks like when printed
    def __str__(self):
        """ This method allows you to print instances """
        return f'{self.CohortID}: {self.StartDate}'

#########################################
################# Class for Course Table
#########################################

class CourseModel:
    """
    A simple example class. Attributes match the database
       table `Sushi` exactly: id, name, price
    
    Modifying this class to match a different entity is easy:
    1. Change the file name
    2. Change the class name. Suggest something that ends in ___Model,
       like VehicleModel or PersonModel.
    3. Update the constructor (the `__init__` method) with your desired
       default values.
    4. Update the SQL statements in the `create()`, `update()`, `delete()`,
       `fetch_by_id()`, and `fetch_all()` methods. Only the SQL statements and
       the parameters to the `cursor.execute()` call need to be changed.
    5. Update the `__str__()` method so the class can be printed easily. This
       will help with debugging.
    """

    def __init__(self, data = {}):
        """
        Populates class fields, if available, or uses default values
        """
        if isinstance(data, sqlite3.Row):
            data = dict(data)

        # Assign the values in the dict to the instance variables in the ISF_Cohort Table
        self.CourseID = data.get('CourseID', None)
        self.CourseTitle = data.get('CourseTitle', '')
        self.CourseDescription = data.get('CourseDescription', 'This is a course')
        self.CreditHours = data.get('CreditHours', 3)
        
    ####################
    # Method definitions
    # These require the instance variables already be populated
    
    def create(self):
        """ () -> sushi
        Creates a new sushi record in the databse, and returns the
        newly created object.
        No id is passed, as that's assigned by the database
        """
        cursor = DbHelper.get_cursor()
        cursor.execute(
            'INSERT INTO ISF_Course (CourseTitle, CourseDescription, CreditHours) VALUES (?,?,?)',
            (self.CourseTitle,self.CourseDescription,self.CreditHours)
        )
        self.CourseID = cursor.lastrowid
        return self
    
##    def update(self):
##        cursor = DbHelper.get_cursor()
##        cursor.execute(
##            'UPDATE ISF_Course SET CourseTitle=?, CourseDescription=?, CreditHours=? WHERE CourseID=?',
##            (self.CourseTitle, self.CourseDescription, self.CreditHours, self.CourseID)
##        )
##        return self
##    
##    def delete(self):
##        cursor = DbHelper.get_cursor()
##        cursor.execute(
##            'DELETE FROM ISF_Course WHERE CourseID = ?,
##            (self.CourseID,) # need the trailing comma
##        )
##        return None



    ####################
    # Static methods
    # These don't require an instance already exist

    @staticmethod
    def fetch_by_name(find_me):
        cursor = DbHelper.get_cursor()
        cursor.execute(
            'SELECT CourseID, CourseTitle, CourseDescription, CreditHours FROM ISF_Course WHERE CourseTitle = ?',
            (find_me,) # need the trailing comma
        )
        s = cursor.fetchone()
        return CourseModel(s) if s is not None else None

    @staticmethod
    def fetch_all():
        """ () -> [SushiModel, ...]
        Fetches all sushi from the database, and returns as a list
        of SushiModel objects.
        """
        cur = DbHelper.get_cursor()
        cur.execute('SELECT CourseID, CourseTitle, CourseDescription, CreditHours FROM ISF_Course')
        result = [CourseModel(row) for row in cur.fetchall()]
        return result
    
    
    #This did not work
#    @staticmethod
#    def generateReport():
#        """ 
#        Performs the requested count of students enrolled per coursefor the report
#        """
#        cur = DbHelper.get_cursor()
#        cur.execute('SELECT c.CourseID,c.CourseTitle, COUNT(se.StudentID) as numEnrolled FROM ISF_Section s INNER JOIN ISF_Course c ON s.CourseID = c.CourseID INNER JOIN ISF_StudentEnroll se on s.SectionNum = se.SectionNum GROUP BY c.CourseID,c.CourseTitle ORDER BY COUNT(se.StudentID);')
#        result = [CourseModel(row) for row in cur.fetchall()]
#        
#        cleaned = []
#        for row in result:
#            cleaned.append([row.CourseID, row.CourseTitle, row.numEnrolled])
#        
#        return cleaned
        
    # Override what an instance looks like when printed
    def __str__(self):
        """ This method allows you to print instances """
        return f'{self.CourseID}: {self.CourseTitle}, {self.CourseDescription}, {self.CreditHours}'

#############################################
################ Class for Student Table
#############################################
class StudentModel:
    """
    A simple example class. Attributes match the database
       table `Sushi` exactly: id, name, price
    
    Modifying this class to match a different entity is easy:
    1. Change the file name
    2. Change the class name. Suggest something that ends in ___Model,
       like VehicleModel or PersonModel.
    3. Update the constructor (the `__init__` method) with your desired
       default values.
    4. Update the SQL statements in the `create()`, `update()`, `delete()`,
       `fetch_by_id()`, and `fetch_all()` methods. Only the SQL statements and
       the parameters to the `cursor.execute()` call need to be changed.
    5. Update the `__str__()` method so the class can be printed easily. This
       will help with debugging.
    """

    def __init__(self, data = {}):
        """
        Populates class fields, if available, or uses default values
        """
        if isinstance(data, sqlite3.Row):
            data = dict(data)

        # Assign the values in the dict to the instance variables
        self.StudentID = data.get('StudentID', None)
        self.CohortID = data.get('CohortID', '')
        self.StudentFname = data.get('StudentFname', '')
        self.StudentLname = data.get('StudentLname', '')
        self.StudentEmail = data.get('StudentEmail', '')
        self.EmployeeID = data.get('EmployeeID','')

    ####################
    # Method definitions
    # These require the instance variables already be populated
    def lastCohort(self):
        ##To get the last cohort created
        self.StudentID = cursor.lastrowid
        result = fetch_by_id(self.studentID)
        return result.CohortID
        
    def create(self):
        """ () -> sushi
        Creates a new sushi record in the databse, and returns the
        newly created object.
        No id is passed, as that's assigned by the database
        """
        cursor = DbHelper.get_cursor()
        cursor.execute(
            'INSERT INTO ISF_Student (CohortID, StudentFName, StudentLName, StudentEmail, EmployeeID) VALUES (?,?,?,?,?)',
            (self.CohortID, self.StudentFname, self.StudentLname, self.StudentEmail, self.EmployeeID)
        )
        self.StudentID = cursor.lastrowid
        return self
    
    def update(self):
        cursor = DbHelper.get_cursor()
        cursor.execute(
            'UPDATE ISF_Student SET CohortID=?,StudentFname=?,StudentLname=? WHERE EmployeeID=?',
            (self.CohortID, self.StudentFname, self.StudentLname, self.EmployeeID)
        )
        return self
    
    ####################
    # Static methods
    # These don't require an instance already exist
    
    @staticmethod
    def fetch_by_empID(find_me):
        cursor = DbHelper.get_cursor()
        cursor.execute(
            'SELECT * FROM ISF_Student WHERE EmployeeID = ?',
            (find_me,) # need the trailing comma
        )
        s = cursor.fetchone()
        return StudentModel(s) if s is not None else None

    @staticmethod
    def fetch_all():
        """ () -> [SushiModel, ...]
        Fetches all sushi from the database, and returns as a list
        of SushiModel objects.
        """
        cur = DbHelper.get_cursor()
        cur.execute('SELECT * FROM ISF_Student')
        result = [StudentModel(row) for row in cur.fetchall()]
        return result
        
    # Override what an instance looks like when printed
    def __str__(self):
        """ This method allows you to print instances """
        return f'{self.StudentID}: {self.CohortID}, {self.StudentFname}, {self.StudentLname}, {self.StudentEmail}, {self.EmployeeID}'


#############################################
################ Class for Section Table
#############################################

class SectionModel:
    """
    A simple example class. Attributes match the database
       table `Sushi` exactly: id, name, price
    
    Modifying this class to match a different entity is easy:
    1. Change the file name
    2. Change the class name. Suggest something that ends in ___Model,
       like VehicleModel or PersonModel.
    3. Update the constructor (the `__init__` method) with your desired
       default values.
    4. Update the SQL statements in the `create()`, `update()`, `delete()`,
       `fetch_by_id()`, and `fetch_all()` methods. Only the SQL statements and
       the parameters to the `cursor.execute()` call need to be changed.
    5. Update the `__str__()` method so the class can be printed easily. This
       will help with debugging.
    """

    def __init__(self, data = {}):
        """
        Populates class fields, if available, or uses default values
        """
        if isinstance(data, sqlite3.Row):
            data = dict(data)

        # Assign the values in the dict to the instance variables in the ISF_Cohort Table
        self.SectionNum = data.get('SectionNum', None)
        self.CourseID = data.get('CourseID', '')
        self.CohortID = data.get('CohortID', '')
        self.SectionDetail = data.get('SectionDetail', 'This is a section for that course')
        self.Schedule = data.get('Schedule', 'MWF')
        
    ####################
    # Method definitions
    # These require the instance variables already be populated
    
    def create(self):
        """ () -> sushi
        Creates a new sushi record in the databse, and returns the
        newly created object.
        No id is passed, as that's assigned by the database
        """
        cursor = DbHelper.get_cursor()
        cursor.execute(
            'INSERT INTO ISF_Section (CourseID, CohortID, SectionDetail, Schedule) VALUES (?,?,?,?)',
            (self.CourseID,self.CohortID,self.SectionDetail,self.Schedule)
        )
        self.SectionNum = cursor.lastrowid
        return self

    ####################
    # Static methods
    # These don't require an instance already exist

    @staticmethod
    def fetch_by_id(find_me):
        cursor = DbHelper.get_cursor()
        cursor.execute(
            'SELECT SectionNum, CourseID, CohortID, SectionDetail, Schedule FROM ISF_Section WHERE SectionNum = ?',
            (find_me,) # need the trailing comma
        )
        s = cursor.fetchone()
        return SectionModel(s) if s is not None else None

    @staticmethod
    def fetch_all():
        """ () -> [SushiModel, ...]
        Fetches all sushi from the database, and returns as a list
        of SushiModel objects.
        """
        cur = DbHelper.get_cursor()
        cur.execute('SELECT SectionNum, CourseID, CohortID, SectionDetail, Schedule FROM ISF_Section')
        result = [SectionModel(row) for row in cur.fetchall()]
        return result
        
    # Override what an instance looks like when printed
##    def __str__(self):
##        """ This method allows you to print instances """
##        return f'{self.CourseID}: {self.CourseTitle}, {self.CourseDescription}, {self.CreditHours}'


#############################################################
################# Class for StudentEnrollment Table
#############################################################

class StudentEnrollModel:
    """
    A simple example class. Attributes match the database
       table `Sushi` exactly: id, name, price
    
    Modifying this class to match a different entity is easy:
    1. Change the file name
    2. Change the class name. Suggest something that ends in ___Model,
       like VehicleModel or PersonModel.
    3. Update the constructor (the `__init__` method) with your desired
       default values.
    4. Update the SQL statements in the `create()`, `update()`, `delete()`,
       `fetch_by_id()`, and `fetch_all()` methods. Only the SQL statements and
       the parameters to the `cursor.execute()` call need to be changed.
    5. Update the `__str__()` method so the class can be printed easily. This
       will help with debugging.
    """

    def __init__(self, data = {}):
        """
        Populates class fields, if available, or uses default values
        """
        if isinstance(data, sqlite3.Row):
            data = dict(data)

        # Assign the values in the dict to the instance variables in the ISF_Cohort Table
        self.EnrollmentID = data.get('EnrollmentID', None)
        self.StudentID = data.get('StudentID', '')
        self.SectionNum = data.get('SectionNum', '')
        self.EnrollmentDate = data.get('EnrollmentDate', '')
        
    ####################
    # Method definitions
    # These require the instance variables already be populated
    
    def create(self):
        """ () -> sushi
        Creates a new sushi record in the databse, and returns the
        newly created object.
        No id is passed, as that's assigned by the database
        """
        cursor = DbHelper.get_cursor()
        cursor.execute(
            'INSERT INTO ISF_StudentEnroll (StudentID, SectionNum, EnrollmentDate) VALUES (?,?,?)',
            (self.StudentID,self.SectionNum,self.EnrollmentDate)
        )
        self.EnrollmentID = cursor.lastrowid
        return self

    ####################
    # Static methods
    # These don't require an instance already exist

    @staticmethod
    def fetch_by_id(find_me):
        cursor = DbHelper.get_cursor()
        cursor.execute(
            'SELECT EnrollmentID, StudentID, SectionNum, EnrollmentDate FROM ISF_StudentEnroll WHERE EnrollmentID = ?',
            (find_me,) # need the trailing comma
        )
        s = cursor.fetchone()
        return StudentEnrollModel(s) if s is not None else None

    @staticmethod
    def fetch_all():
        """ () -> [SushiModel, ...]
        Fetches all sushi from the database, and returns as a list
        of SushiModel objects.
        """
        cur = DbHelper.get_cursor()
        cur.execute('SELECT EnrollmentID, StudentID, SectionNum, EnrollmentDate FROM ISF_StudentEnroll')
        result = [StudentEnrollModel(row) for row in cur.fetchall()]
        return result
    
        
    # Override what an instance looks like when printed
##    def __str__(self):
##        """ This method allows you to print instances """
##        return f'{self.CourseID}: {self.CourseTitle}, {self.CourseDescription}, {self.CreditHours}'
