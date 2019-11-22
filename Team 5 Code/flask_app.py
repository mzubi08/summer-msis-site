#######
# Base provided by Tom Gregory
# For use by MSIS Tech Bootcamp / ISF Project


####################################################################
# Team 5: Dell Executives                                          #
# Michael I. Zubi, Yashil Kalyani, Ni Pan, Grace Liu, John Fannin  #
####################################################################

#In collaboration with FLASK, Team Dell Executives is proud to 
#present the basic Version 1.0 of......


#    BBBB        I       PPPP               I     M           M       SSSSS
#    B    B      I       P    P             I     M M       M M      S
#    B    B      I       P    P             I     M   M   M   M      S
#    B B B       I       P P P     =====    I     M     M     M       S S S
#    B    B      I       P                  I     M           M            S
#    B    B      I       P                  I     M           M            S
#    BBBB        I       P                  I     M           M       SSSSS

###################################################################
# Any relation to persons living or dead is probably coincidental.#
###################################################################

# You may need to install the Flask module for this code to work
# `pip3 install flask` may do it

import math
from datetime import date

from ISF_Model import *
from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

#from models import * # This is a model class definition file I made

# Global Variable
new_cohortID = 0
studentCount = 0
courses = []
sections = {}
numOfSections = 0
newStudents = []



def cleanData(data):
    
    cleaned = data.replace('"','') #remove the "
    cleaned = cleaned.replace('\r','') #remove the carriage returns
    cleaned = cleaned.replace('\n',',') #remove the new lines and replace with commas
    cleaned = cleaned.split(",") #split the string into a list on the commas
    
    cleanedList = []
    while True:
        temp = []
        for i in range (1,5):
            # extract 4 from the cleaned data, and put into their own list within a list to make it easier
            # to add to the students table
            # do this for every record until the cleaned list is empty
            #The data is stored as a list within a list, each sub-list is an individual records
            # Ex. [ [1,2,3,4] , [1,2,3,4] ]
            temp2 = cleaned.pop(0)
            temp.append(temp2)
        cleanedList.append(temp)
        
        # just being sure it will break on time
        if cleaned == []:
            break
    
    return cleanedList



@app.route('/')               # A "route" is the path the user sees in the browser
@app.route('/home')           # A controller may have more than one route
def home():
    return render_template(
        'home.html',          # This file needs to be in the 'templates' folder
    )


@app.route('/students')
def add_students_page():
    return render_template(
        'students.html'
    )


@app.route('/processStudents', methods=["POST"])
def add_students():
    #Get the data from the form
    cohortStartDate = request.form['startDate']
    stuData = request.form['studentsList']
    
    #Send it to the cleaners
    entries = cleanData(stuData)
    #get the global variables and make suer they're reset
    global newStudents
    newStudents = []
    
    #Count the number of students we are adding
    global studentCount
    studentCount = 0
    studentCount= len(entries)
    
    # Create a new cohort and grab the new cohort ID for use later
    c = CohortModel({'StartDate':cohortStartDate})
    c.create()
    global new_cohortID
    new_cohortID = 0
    new_cohortID = c.CohortID
        
        
    ## Add records in cleaned to database
    s = StudentModel()
    
    #Get employee IDs for checking if people are new or not
    allRecords = s.fetch_all()
    eIds = []
    for item in allRecords:
        eIds.append(item.EmployeeID)
    
    #Go through the entries, make a studentModel with their infotmation,
    # and check if they exist already based on their Employee IDs. If they
    # are already in, then we are updating their name (F and L) and cohort ID
    for student in entries:
        tempModel = StudentModel({'CohortID':new_cohortID,'StudentFname':student[1],'StudentLname':student[0],'StudentEmail':student[2],'EmployeeID':student[3]})
        
        if student[3] in eIds:
            #update the data if the student is already in the table
            tempModel.update()
            
            response = tempModel.fetch_by_empID(student[3])
            
            #this newStudents variable is collecting the new people we are uploading
            #so that we know who to assign and register to courses later on
            newStudents.append(response.StudentID)
            
        else:
            #If not in the table already, just add to the table a new records
            tempModel.create()
            
            # Storing the new student IDs in the controller for the registration later
            newStudents.append(tempModel.StudentID)
    
    #Just checking for errors, don't mind me
    if entries != [] or entries != '':
        return redirect(url_for('students_confirm'))
    else:
        return redirect(url_for('students_error'))
    

@app.route('/students-message')
def students_confirm():
    return render_template(
        'students-message.html',
        result = "confirm"
    )

def students_error():
    return render_template(
        'students-message.html',
        result = "error"
    )


@app.route('/courses')
def view_courses():
    return render_template(
        'courses.html'
    )



@app.route('/process_courses', methods=['POST'])
def add_courses():
    # establish global variabls for use here
    # Yes it's neater this time!
    # Hint: global variabls are located OUTSIDE
    # these functions and can be shared across
    # functions and updated in a really useful way
    # Global Variabls = Mr. Worldwide
    global courses
    global sections
    global new_cohortID
    global studentCount
    global numOfSections
    
    # more variables 
    #VariableLove
    course = []
    numOfSections = 0
    sections = {}
    
    c = CourseModel()
    allCourses = c.fetch_all()
    cNames = []
    for item in allCourses:
        cNames.append(item.CourseTitle)
        
    # Get the course data from the page
    courseData = request.form['courseData']
    
    #Create the courses and store the course IDs created
    if courseData != [] or courseData != '':
        #clean the data and make it nicely sorted into a list 
        #by splitting on the commas, and adding commas where there was a carriage return
        courseData = courseData.replace("\n","")
        courseData = courseData.replace("\r",",")
        courseData = courseData.split(",")
        
        #Grab the course ID numbers for use later
        for line in courseData:
            if line not in cNames:
                tempModel = CourseModel({'CourseTitle':line})
                tempModel.create()
                courses.append(tempModel.CourseID)

            else:
                tempModel = CourseModel({'CourseTitle':line})
                qResponse = tempModel.fetch_by_name(line)
                courses.append(qResponse.CourseID)
        
    
        #Calculate how many sections needed per course based on how
        #many students were added earlier
        numOfSections = math.ceil(studentCount/35)

        tempList = []
        #For each course
        for course in courses:
            #Create a section N times 
            tempList = []
            for num in range(0,numOfSections):
                tempModel = SectionModel({'CourseID':course,'CohortID':new_cohortID})
                tempModel.create()
                #Store the section numbers in a list
                print(tempModel.SectionNum)
                tempList.append(tempModel.SectionNum)

            #Add this section number list as a dict entry associated with that course number
            print(tempList)
            sections[course] = tempList


        # Example dictionary
        # {8866:[2589,4563], ... }
        
    if sections != []:
        return redirect(url_for('courses_confirm'))
    else:
        return redirect(url_for('courses_error'))
    
    

@app.route('/courses_message')
def courses_confirm():
    return render_template(
        'course-confirm.html',
        result = 'confirm'
    )

def courses_error():
    return render_template(
        'course-confirm.html',
        result = 'error'
    )



@app.route('/register')
def register_page():
    return render_template(
    'register_students.html'
    )


@app.route('/registration_process')
def register_students():
    global courses
    global sections
    global studentCount
    global newStudents
    global numOfSections
    Today = date.today()
    
    print(1, sections)
    
    # Determining the max number of students to have per section
    maxStudents = math.ceil(studentCount/numOfSections)
    studentCounter = 0
    
    #register the students using the dict I created earlier
    for course_id in courses: #6688
        print(2,course_id)
        studentIndex = 0 #This counter is prarily used to index through the newStudents list
        for section_id in sections[course_id]: #6688: [52,64]
            print(3, section_id)
            enrolledCounter = 0
            #^^This is counting the number of students enrolled in a section
            while enrolledCounter < maxStudents:
                student_id = newStudents[studentIndex] 
                #the student counter is being used to index the student we added earlier
                print(4,student_id)
                #Create the record
                tempModel = StudentEnrollModel({'StudentID':student_id,'SectionNum':section_id, 'EnrollmentDate':Today})
                tempModel.create()
                
                
                studentIndex += 1
                enrolledCounter += 1
                
                # an extra failsafe because you can't be too safe #AmIRight?
                if studentIndex == studentCount:
                    print("break")
                    break
                    
    return redirect(url_for('register_confirm'))


@app.route('/register_message')
def register_confirm():
    return render_template(
        'register_confirm.html'
    )


@app.route('/report')
def generate_report():
    # Grab the records from the course, section, and StudentEnroll tables
    cResults = CourseModel.fetch_all()
    sResults = SectionModel.fetch_all()
    eResults = StudentEnrollModel.fetch_all()
    
    #Try and run some basic checking to avoid an empty report table
    if cResults == '' or sResults == '' or eResults == '' or cResults == [] or sResults == [] or eResults == []:
        appended = ["There are","No","Values"]
        return render_template(
            'report_view.html',
            dataSet = appended,
            status = "error"
        )
    else:
        
        #sort through the reported data
        allCourses = []
        for row in cResults:
            allCourses.append([row.CourseID,row.CourseTitle])


        allSections = []
        for row in sResults:
            allSections.append([row.SectionNum,row.CourseID])


        allEnrolls = []
        for row in eResults:
            allEnrolls.append(row.SectionNum)


        ##Count number of times a section number was mentioned in enrollments
        sectionDict = {}
        for section in allSections:
            secounter = 0
            for enroll in allEnrolls:
                if enroll == section[0]:
                    secounter += 1
            sectionDict[section[0]] = [secounter,section[1]]

        appended = []

        # Now sum the section number enrollment count by 
        # course ID, like a SELECT -> GROUP BY
        courseDict = {}
        for course in allCourses:
            ccounter = 0

            for entry in sectionDict:
                if sectionDict[entry][1] == course[0]:
                    ccounter += sectionDict[entry][0]

            appended.append([course[0],course[1],ccounter])
        
        #Take them to the report page after processing
        return render_template(
            'report_view.html',
            dataSet = appended,
            status = "good"
        )
#    
## This route/function processes HTML forms
## Forms should use the POST method. This page has no View. The controller
## processes the form, then redirects to a regular page.

if __name__ == '__main__':
    app.run()
