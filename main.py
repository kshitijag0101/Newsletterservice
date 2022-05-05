import mysql.connector as m
conn = m.connect(host="localhost", user="root", passwd="kshitij", database="newsletter")
c = conn.cursor()
c.execute("create table if not exists admin(emailid varchar(50),password varchar(30))")
c.execute("create table if not exists user(emailid varchar(50),password varchar(30),subscribed varchar(100))")
c.execute("create table if not exists topic(name varchar(50))")
c.execute("create table if not exists news(tname varchar(50),content varchar(2000),time datetime)")
while True:
    ch = int(input("Press \n 1- Admin login\n 2- User login\n 3- Exit\n"))
    if ch == 1:
        email = input("Enter emailid :- ")
        password = input("Enter password :- ")
        c.execute("select * from admin where emailid='{}' and password='{}'".format(email, password))
        b = c.fetchall()
        if b!=[]:
            print("\nHello Admin\n")
            while True:
                ch1 = int(input("Press \n 1- Add Topic\n 2- Add News\n 3- Sign out\n"))
                if ch1 == 1:
                    top = input("Enter Topic Name:- ")
                    c.execute("select * from topic where name='{}'".format(top))
                    b = c.fetchall()
                    if b == []:
                        c.execute("insert into topic values('{}')".format(top))
                        conn.commit()
                        print("\nTopic added successfully\n")
                    else:
                        print("\nTopic already exists\n")
                elif ch1 == 2:
                    top = input("Enter topic:- ")
                    cont = input("Enter content:- ")
                    dt = input("Enter Date and Time :- ")
                    c.execute("insert into news values('{}','{}','{}')".format(top, cont, dt))
                    conn.commit()
                    print("\nNews added succesfully\n")
                else:
                    break

        else:
            print("\nInvalid login\n")
    elif ch == 2:
        email = input("Enter emailid:- ")
        password = input("Enter password :- ")
        c.execute("select emailid from user where emailid='{}'".format(email))
        b = c.fetchall()
        if b != []:
            print("\nUser already exists\n")
        else:
            print("\nSelect topic\n")
            c.execute("select * from topic")
            b = c.fetchall()
            for i in b:
                for j in i:
                    print(j, end="\n")
            tp = input("Enter topic:- ")
            c.execute("insert into user values('{}','{}','{}')".format(email, password, tp))
            conn.commit()
            print("\nYou have subscribed successfully\n")
    else:
        break
