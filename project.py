
from datetime import date
print("\t\t\t\t\t\t\t\t ************ Employee Information ***********\t\t\t\t\t\t\t")
print("1. Enter Employee details\n2. Exit")
ch = int(input("Enter your choice : "))
while ch == None:
    print("Choose one Option !")
    print("1. Enter Employee details\n2. Exit")
    ch = int(input("Enter your choice : "))
while ch != " ":
    if ch == 1:
        fname = input("Enter First Name : ")
        lname = input("Enter Last Name : ")
        while fname and lname == None:
            break
            fname = input("Enter First Name : ")
            lname = input("Enter Last Name : ")
        while fname and lname != " ":
            Fullname = (fname + lname)
            gender = input("Enter Male / Female : ")
            if gender != "Male":
                Fullname = ("Ms." + fname + " " + lname)
            else:
                Fullname = ("Mr." + fname + lname)
            dob = input('Enter Birth date - (i.e. yyyy-mm-dd) :')
            year, month, day = map(int, dob.split('-'))
            if year > 2002 < 2122:
                print("The year is not valid !")
            d = date(year, month, day)
            today = date.today()
            check_date = ((today.month, today.day) < (d.month, d.day))
            year_diff = today.year - d.year
            age = year_diff - check_date
            Dept = input("Enter the Departmart : ")
            while Dept == None:
                print("Department name is required !")
                Dept = input("Enter the Departmart : ")
            Mobile = int(input("Enter Mobile number : "))
            while Mobile == None:
                print("Mobile number is required !")
                Mobile = int(input("Enter Mobile number : "))
            while Mobile != None:
                if len(str(Mobile))>10 or len(str(Mobile))<10:
                    print(" Mobile Number is not valid (Enter a 10 digit number)")
                    Mobile = int(input("Enter Mobile number : "))
                else:
                            Mobile = int(Mobile)
                            print("Mobile number is valid")
                            break
            City = input("Enter the City : ")
            if (City == None):
                print("Enter your city !")
                City = input("Enter the City : ")
            basic_salary= float(input("Enter the Salary of the Employee : "))
            da = (float)(15*basic_salary)/100.0
            hra = (float)(20 * basic_salary)/100.0
            lta = (float)(10 * basic_salary)/100.0
            gross_salary = basic_salary + da + hra + lta
            Remarks = input("Enter Pass/Fail : ")
            print("\t\t\t\t\t\t**************Employee Details**************")
            print('\t\t\t\t\t\t\t\t\t\t'"Name : ", Fullname, "\n"'\t\t\t\t\t\t\t\t\t\t' "Gender : ", gender, "\n",
                  '\t\t\t\t\t\t\t\t\t\t'"Date of Birth : ", dob, "\n", '\t\t\t\t\t\t\t\t\t\t'"Age :", age, "\n",
                  '\t\t\t\t\t\t\t\t\t\t'"Mobile Number : +91 ", Mobile, "\n", '\t\t\t\t\t\t\t\t\t\t' "Department :", Dept,
                  "\n", '\t\t\t\t\t\t\t\t\t\t' "Basic Salary : ",basic_salary,"\n"'\t\t\t\t\t\t\t\t\t\t'  "Gross Salary : ",gross_salary,"\n" '\t\t\t\t\t\t\t\t\t\t' "Remarks : ",
                  Remarks, "\n")
            if Remarks == "Pass":
                print("\t\t\t\t\t\t\t\t\t\tCongratulations! Keep Rocking :)")
            else:
                print("\t\t\t\t\t\t\t\t\t\tBetter Luck Next Time :( ")
            break
    elif (ch == 2):
        exit(0)
    else:
        print("Invalid Input")
    break