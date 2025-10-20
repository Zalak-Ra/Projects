import pandas as pd
import smtplib

def main():
    subject = input("Enter a subject name: ").lower()
    subject_name = ["maths","dsa","ml"]
    if subject not in subject_name:
        raise ValueError("Please enter valid subject")
    stu_roll = input("Enter a list of roll numbers separated by space: ").split()
    rollno = ["23BCP001", "23BCP002", "23BCP003", "23BCP004", "23BCP005"]
    for roll in stu_roll:
        if roll not in rollno:
            raise ValueError("Please enter valid rollno separated by space: ")
    leave = input("Enter number of leaves: ").split()
    if len(stu_roll) != len(leave) or all(list_ele.isdigit() for list_ele in leave) == False:
        raise ValueError("Please enter valid amount of list")
    leave_check(subject,stu_roll,leave)
    check()

def leave_check(subject , stu_roll , leaves):
    data = pd.read_excel(r"C:\Users\devsm\OneDrive\Desktop\CS\Zode\python\cs50\final project\stu_list.xlsx", index_col=0)

    for i in range(len(stu_roll)):
        if stu_roll[i] in data.index:
            data.at[stu_roll[i], subject] = int(data.at[stu_roll[i], subject]) + int(leaves[i])
        else:
            print(f"Roll number {stu_roll[i]} not found in the data")

    data.to_excel(r"C:\Users\devsm\OneDrive\Desktop\CS\Zode\python\cs50\final project\stu_list.xlsx")
    

def check():
    data = pd.read_excel(r"C:\Users\devsm\OneDrive\Desktop\CS\Zode\python\cs50\final project\stu_list.xlsx", index_col=0)
    for roll_no in ["23BCP001", "23BCP002", "23BCP003", "23BCP004", "23BCP005"]:
        for subject in ["maths", "dsa", "ml"]:
            if data.at[roll_no, subject] == 2:
                email(subject, roll_no,2)

    for roll_no in ["23BCP001", "23BCP002", "23BCP003", "23BCP004", "23BCP005"]:
        for subject in ["maths", "dsa", "ml"]:
            if data.at[roll_no, subject] >= 3:
                email(subject, roll_no,3)

        


def email(subject, roll_no,no):
    data = pd.read_excel(r"C:\Users\devsm\OneDrive\Desktop\CS\Zode\python\cs50\final project\stu_list.xlsx", index_col=0)
    HOST = "smtp-mail.outlook.com"
    PORT = 587
    sender_email = "zalakranparia@outlook.com"
    receiver_email = data.at[roll_no, "email"]  
    password = input("Enter password: ")
    server = smtplib.SMTP(HOST, PORT)
    server.starttls()
    server.login(sender_email, password)
    if no == 2:
        message = f"""\
Subject: Leave Alert for {subject}

This is to inform you that the leave count for {subject} has reached 2 for roll number {roll_no}.
"""
        server.sendmail(sender_email, receiver_email, message)

    else:
        message = f"""\
Subject: Leave Alert for {subject}

This is to inform you that the leave count for {subject} has reached 3 so you are not allow to sit in exam. So please meet you course co-ordinater.
"""
        server.sendmail(sender_email, receiver_email, message)
    print("Email has been sent.")
    server.quit()





if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)
