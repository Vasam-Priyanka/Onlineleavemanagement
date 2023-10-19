from datetime import datetime as dt
lt=["sick leave","earn leave","maternity leave","casual leave"]
userid='admin'
password='one'
l={
    1:{
        "name":"user1",
        "psw":"pwd1"
    },
    2:{
        "name":"user2",
        "psw":"pwd2"
    }
}
d={1:{"name":"user1","post":"asst professor","Dept":"CSE","sick leave":3,"earn leave":1,"maternity leave":0,"casual leave":2},
   2:{"name":"user2","post":"asst professor","Dept":"Civil","sick leave":4,"earn leave":3," maternity leave":0,"casual leave":1}
}
p=["user1","user2"]

print('                           CBIT ONLINE LEAVE MANAGEMENT SYSTEM')
print('----------------------------------------------------------------------------------------------------------')
print()
print('''Press 1 or 2 to proceed:
    1.Admin Login
    2.User Login''')
print()
q=int(input('Enter your choice: '))
print()
if q==1:                             #admin
    print('***** ADMIN LOGIN *****')
    print()
    i = True
    while i:
        id = input('Enter username:')
        if id == userid:
            pwd = input('Enter password: ')
            if pwd != password:
                print('Enter correct password.......')
                print()
            else:
                print('Logged in.......')
                i = False
                k = True
                while k:
                    print()
                    print('1.to add  2.to delete  3.to modify  4.to quit')
                    print()
                    n = int(input('Enter option to proceed: '))
                    print()
                    if n == 1:
                        d[len(d) + 1] = {}
                        d[len(d)]["name"] = input('Enter name: ')
                        if d[len(d)]["name"] in p:
                            print('User with given name exists already........')

                        else:
                            d[len(d)]["post"] = input('Enter post: ')
                            d[len(d)]["dept"] = input('Enter Department: ')
                            d[len(d)]["sick leave"] = int(input('Enter no.of sick leaves taken: '))
                            d[len(d)]["earn leave"]= int(input('Enter no.of earn leaves taken: '))
                            d[len(d)]["maternity leave"]=int(input('Enter no.of maternity leaves taken: '))
                            d[len(d)]["casual leave"]=int(input('Enter no.of casual leaves taken: '))
                            p.append(d[len(d)]["name"])
                            print('User added.......')
                            f = open('user.txt', 'w')
                            for i in range(1, len(d) + 1):
                                f.write(str(i) + ' ' + '=' + ' ' + repr(d[i]))
                                f.write('\n')
                            f.close()
                            # create file and store data
                        print()
                    elif n == 2:
                        s = input('Enter userid to be deleted: ')
                        for i in range(1, len(d) + 1):
                            if s == d[i]["name"]:
                                d[i].clear()
                                print('deleted......')
                                f = open('user.txt', 'w')
                                for i in range(1, len(d) + 1):
                                    f.write(str(i) + ' ' + '=' + ' ' + repr(d[i]))
                                    f.write('\n')
                                f.close()
                                break

                        else:
                            print('Entered user doesnt exist.......')
                            # if selected then delete this from created file
                        print()
                    elif n == 3:
                        u = input('Enter userid to be modified:')
                        print()
                        for i in range(1, len(d) + 1):
                            if u == d[i]["name"]:
                                d[i]["name"] = input('enter name:')
                                d[i]["post"] = input('enter post:')
                                d[i]["dept"] = input('enter department:')
                                d[i]["sick leave"] = int(input('enter no.of sick leaves taken: '))
                                d[i]["earn leave"] = int(input('enter no.of earn leaves taken: '))
                                d[i]["maternity leave"] = int(input('enter no.of maternity leaves taken: '))
                                d[i]["casual leave"] = int(input('enter no.of casual leaves taken: '))
                                print('Details modified.......')
                                f = open('user.txt', 'w')
                                for i in range(1, len(d) + 1):
                                    f.write(str(i) + ' ' + '=' + ' ' + repr(d[i]))
                                    f.write('\n')
                                f.close()

                                break
                        else:
                            print('User doesnt exist.........')
                            # modify
                        # same here
                        print()
                    elif n == 4:
                        print('Logged out........')
                        quit()
                        print()
                    elif n>4:
                        print('Choose a valid option.......')
                        print()
        else:
            print('Enter correct id........')
            print()
elif q==2:
    print('****** USER LOGIN *******')
    print()
    i = True
    while i:
        n = input('Enter username: ')
        j = 1

        while j <= len(l):
            if n in l[j]["name"]:
                pd = input('Enter password: ')
                if pd not in l[j]["psw"]:
                    print('Enter correct passowrd')
                    print()
                else:
                    print('Successfully logged in.......')

                    i = False
                    k = True
                    while k:
                        print()
                        print("1.view details 2.check no of leaves remaining 3.apply for leave 4.exit")
                        print()
                        n = int(input('Enter option to proceed:'))
                        print()
                        if n == 1:
                            print('name:',d[j]["name"])
                            print('post:',d[j]["post"])
                            print('department:',d[j]["Dept"])
                            print('No.of sick leaves taken=',d[j]["sick leave"])
                            print('No.of earn leaves taken=',d[j]["earn leave"])
                            print('No.of materinity leaves taken=',d[j]["maternity leave"])
                            print('No.of casual leaves taken=',d[j]["casual leave"])
                            print()
                        if n == 2:
                            print('No of sick leaves remaining= ',20-d[j]["sick leave"])
                            print('No of earn leaves remaining=', 6-d[j]["earn leave"])
                            print('No of maternity leaves remaining=', 180 - d[j]["maternity leave"])
                            print('No of casual leaves remaining=  ',20-d[j]["casual leave"])
                            print()
                        elif n == 3:
                            print('''choose leave option and check no.of leaves alloted for each leave type:
                            1. sick leave - 20 days per annum
                            2. earn leave - 6 days per annum
                            3. casual leave - 20 days per annum
                            4. maternity leave - 6 months''')
                            print()
                            m = int(input('Enter no of leaves:'))
                            p = input('Enter reason for leave:')
                            day1,m1,y1=map(int,input("From(as dd mm yyyy): ").split())
                            date1=dt(y1,m1,day1)
                            day2,m2,y2=map(int,input("To(as dd mm yyyy): ").split())
                            date2=dt(y2,m2,day2)
                            print("FROM: ",date1," TO:",date2)
                            
                            if p == "sick leave":
                                if m + d[j]["sick leave"] > 20:
                                    print('cant apply for leave.....')
                                else:
                                    print('leave application sent......')
                            elif p == "casual leave":
                                if m + d[j]["casual leave"] > 20:
                                    print('cant apply for leave.....')
                                else:
                                    print('leave application sent......')
                            elif p == 'maternity leave':
                                if m + d[j]["maternity leave"] > 180:
                                    print('cant apply for leave......')
                                else:
                                    print('leave application sent......')
                            elif p == "earn leave":
                                if m + d[j]["earn leave"] > 6:
                                    print('cant apply for leave......')
                                else:
                                    print('leave application sent.......')
                            else:
                                print('entered leave type doesnt exist')
                            print()
                        elif n == 4:
                            print('logged out......')
                            quit()

                        elif n>4:
                            print('choose correct option........')
                            print()
                break
            j = j + 1
        else:
            print('enter correct userid')
            print()
else:
    print('choose correct option........')
    print()


