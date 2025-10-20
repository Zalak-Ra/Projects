# Simple Attendance Tracker
#### Video Demo:  https://www.youtube.com/watch?v=nteGDEGb2Fw
This project is about an Attendance Tracker and how it works. In every college, there are two basic criteria to pass a course:
* Clear the exam with a certain percentage of marks.
* Have a minimum percentage of attendance to sit for the exam.

If a student exceeds a certain number of leaves, they can't sit for the exam. It is hard to remember the total number of leaves you take in every course. So in this program, you can input the number of leaves and it reminds you by email.

## Introduction
The simple attendance tracker takes three inputs: subject, roll number, and number of leaves, and updates it into an Excel file which collects all data. In this case, we consider that if a student takes more than 3 leaves, they can't sit for the exam.

Based on that, we remind the student three times:
* After 2 leaves, we warn them they have only one leave left.
* After 3 leaves, we inform them they have no more leaves and cannot take any more.
* After more than 3 leaves, we notify them they cannot sit for the exam.

If the leaves are 0 or 1, then the student has plenty of leaves so no email is sent.

In this project, I have made a total of four files:
* `requirement.txt`
* `project.py`
* `test_project.py`
* `stu_list.xlsx`

Now let's see all the files one by one.

## 1. requirement.txt
This is a text file that contains all libraries that are imported and their usage.

### Libraries
* **pandas**: `pandas` is an open-source data analysis and manipulation library for Python. It provides data structures and functions needed to efficiently manipulate structured data, making it a crucial tool for data analysis and data science tasks.
* **smtplib**: `smtplib` is a built-in Python module used for sending emails using the Simple Mail Transfer Protocol (SMTP). It allows Python programs to connect to an SMTP server, authenticate, and send emails.
* **openpyxl**: `openpyxl` is a Python library for reading and writing Excel files (with the .xlsx file extension). It allows you to create, modify, and manipulate Excel files directly from Python code.
* **pytest**: `pytest` is a powerful and easy-to-use testing framework for Python. It is used to write simple as well as scalable test cases for small and complex applications.

## 2. project.py
This is the main Python file containing our primary code. This code contains four functions:
 1. `main()`
 2. `leave_check()`
 3. `check()`
 4. `email()`

### main()
The `main` function takes three inputs:
* **Subject**: In this case, we have three subjects: maths, dsa, and ml. If the user inputs other than these three subjects, then a ValueError is thrown stating "Please enter a valid subject".
* **Roll number**: This takes a list of inputs. If the input roll number doesn't match, then a ValueError is thrown stating "Please enter a valid roll number separated by space".
* **Number of leaves**: This also takes a list as input and checks that every element is an integer and that the length of roll numbers is equal to the length of leaves. If these conditions are not satisfied, it throws a ValueError stating "Please enter a valid leaves".

### leave_check()
This function adds data into Excel using the `pandas` library. It is called by the `main` function and takes three arguments: subject, roll number, and number of leaves. Based on the received arguments, it adds the number of leaves in the Excel file.

### check()
This function checks if the number of leaves is 2, 3, or more than 3 and accordingly calls the `email` function. It essentially reviews all leaves and calls the function based on the conditions.

### email()
This function takes three arguments. It sends an email to the student according to their number of leaves. To send an email, we use the `smtplib` library's functions and methods.

## test_project.py
This is a Python code that tests all functions of `project.py`. We import functions from `project.py` and test them using the `assert` function.

We also use `monkeypatch` and it has the `@pytest.fixture(autouse=True)` property. We don't want to actually send an email or check the SMTP server, which is why we use this property. Since our function depends on other functions, we use this property to test it effectively.

## stu_list.xlsx
This is an Excel file that stores information about students and their number of leaves. It takes information from the `leave_check()` function and then the `check()` function reviews all the leaves.<br>
It contains roll numbers, email addresses of students, and three subjects.

