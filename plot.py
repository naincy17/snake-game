import sqlite3

conn = sqlite3.connect("schooldata.db")
cur = conn.cursor()

# data = "DELETE FROM student_info"
# cur.execute(data)
# conn.commit()

# data = "CREATE TABLE student_info (roll_no int ,Name varchar(30),Fname varchar(30),Mname varchar(30),Fees int)"
# cur.execute(data)
# conn.commit()

print("Welcome to WsCube School!")
print('''Press:
1. To enter student info.
2. To enter fee info.
3. for Principal access.
4. Exit!''')

access_code = 112233
info_dict1 = {}
while True:
    x = int(input("Enter: "))
    if x == 1:
        y = int(input("Enter number of students: "))
        for i in range(1, y + 1):
            print("Enter info for Student no: ", i)
            roll_no = int(input("Enter roll no: "))
            name = input("Enter student name: ")
            Fname = input("Enter father's name: ")
            Mname = input("Enter mother's name: ")
            info_list = [roll_no, name, Fname, Mname, "null"]
            data = "INSERT INTO student_info values (?,?,?,?,?)"
            cur.execute(data, info_list)
            conn.commit()
            info_dict1[roll_no] = [name, Fname, Mname, "fee"]
            print(info_dict1)
    elif x == 2:
        y = int(input("Enter student roll no: "))
        print("Please Enter fee for ", info_dict1[y][0], ".")
        if y in info_dict1:
            fee = int(input("Enter: "))
            info_dict1[y][3] = fee
            print(info_dict1)
            temp_list = [fee, y]
            data = "UPDATE student_info SET fee = (?) where roll_no==(?)"
            cur.execute(data, temp_list)
            conn.commit()
        else:
            print("DO NOT EXIST!")
    elif x == 3:
        code = int(input("Enter access code: "))
        if code == access_code:
            x = int(input("Enter student roll no: "))
            data = "SELECT roll_no FROM student_info"
            l = cur.execute(data)
            a = cur.fetchone()
            print (a)
            if x in a:
                print ("roll_no_exists")
    elif x == 4:
        print("Thank You for using the system.")
        break
    else:
        print("Invalid key, try again!")

conn.close()