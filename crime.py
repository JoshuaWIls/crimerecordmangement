# Crime record management system
import mysql.connector 
import time
from datetime import date


global conn,cursor
conn = mysql.connector.connect(host='localhost',database='crime',user='root',password='casper9088')
cursor = conn.cursor()

def clear():
  for _ in range(65):
     print()



def introduction():
    msg = '''
          C R I M E   R E C O R D    I N F O R M A T I O N    S Y S T E M 
          
          - An Introduction
          
          Crime record are the most important part of any modern society for better controlling crime. Crime database 
          database help us to recognise the type of crime right now happending in the system and how to overcome that. 

          This project is also trying to solve this simple but very useful information of the crime. The whole 
          database is store in MySQL table alumni that stores their current position as well as some other useful
          information like higher education, current position, passout year etc.

          The whole project is divided into four major parts ie addition of data, modification, searching and 
          reporting. all these part are further divided into menus for easy navigation

          NOTE: Python is case-SENSITIVE so type exact Column Name wherever required.

          If you have any query or suggestions please contact me at joshua@kesri.in \n\n\n\n'''
    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait=input('Press any key to continue.....')


def made_by():
    msg = ''' 
            Crime Record information system made by     : Aditya Singh,Mohit Monappa,Joshua Wilson
            Roll No                                     : ---
            School Name                                 : Kensri School
            Session                                     : 2021-22
            
            
            Thanks for evaluating my Project.
            \n\n\n
        '''

    for x in msg:
        print(x, end='')
        time.sleep(0.002)

    wait = input('Press any key to continue.....')



def display_complaint_records():
    cursor.execute('select * from complaint_record;')
    records = cursor.fetchall()
    for row in records:
        print(row)



def admin_login():
    while True:
        clear()
        uname = input('Enter your Admin id :')
        upass = input('Enter your Admin Password :')
        cursor.execute('select * from admin_login where Name="{}" and Passwd ="{}"'.format(uname,upass))
        cursor.fetchall();
        rows = cursor.rowcount
        if rows!=1:
            print('Invalid Login details..... Try again')
        else:
            print('You are eligible for operating this system............')
            print('\n\n\n')
            print('Press any key to continue...............')
            break



def user_login():
    while True:
        clear()
        uname = input('Enter your User id :')
        upass = input('Enter your User Password :')
        cursor.execute('select * from User_login where Name="{}" and Passwd ="{}"'.format(uname,upass))
        cursor.fetchall()
        rows = cursor.rowcount
        if rows!=1:
            print('Invalid Login details..... Try again')
        else:
            print('You are eligible for operating this system............')
            print('\n\n\n')
            print('Press any key to continue...............')
            break



def add_crime_type():
    clear()
    offence_name = input('Enter offence Name : ')
    ipc_section =  input('Enter IPC section applied for this offence : ')
    comment = input('Enter Any other information : ')
    sql = 'insert into crime_type(offence_name,ipc_section, description) values("{}","{}","{}");'.format(offence_name,ipc_section,comment)
    cursor.execute(sql)
    conn.commit()
    print('\n\n New Offence Type added....')
    wait= input('\n\n\nPress any key to continue............')



def add_record():
    clear()
    crime_date = input('Enter Crime Date (yyyy/mm/dd) : ')
    # this is coming from the crime type table 
    offence_id = input('Enter Offence_id : ')
    complaint_by = input('Enter Name of complainee : ')
    address  = input('Enter Complainee Address :')
    phone  = input('Enter Complainee Phone No :')
    status  = input('Enter current status :')
    update_date = date.today()
    sql = 'insert into complaint_record(c_date,offence_type,complaint_by,address,phone_no,status,update_date) values \
            ("{}",{},"{}","{}","{}","{}","{}");'.format(crime_date, offence_id,complaint_by,address,phone,status,update_date) 
    cursor.execute(sql)
    print('\n\n New Crime Record added....')

    cursor.execute('select max(id) from complaint_record;')
    no = cursor.fetchone()
    print(' Your complaint  No is : {} \n\n\n'.format(no[0]))
    wait = input('\n\n\nPress any key to continue............')



def add_offenders_record():
    clear()
    
    name = input("Enter offender name: ")
    crime_id = input("Enter crime id: ")
    crime_name = input("Enter crime name: ")
    sql = 'insert into offenders_record(offender_name,crime_id,crime_name) values \
            ("{}",{},"{}");'.format(name, crime_id, crime_name) 
    cursor.execute(sql)
    conn.commit()
    print("\n\n New Offender's  Record added....")

    cursor.execute('select max(id) from offenders_record;')
    no = cursor.fetchone()
    print(' Your record  No is : {} \n\n\n'.format(no[0]))
    wait = input('\n\n\nPress any key to continue............')



def modify_crime_type_record():
    clear()
    print(' M O D I F Y    C R I M E  T Y P E  S C R E E N ')
    print('1.  Offence Name \n')
    print('2.  IPC Section \n')
    print('3.  Description  \n')
    choice = int(input('Enter your choice :'))
    field=''
    if choice==1:
        field='offence_name'
    if choice==2:
        field='ipc_section'
    if choice==3:
        field='Description'

    crime_id = input('Enter Crime Type ID :')
    value = input('Enter new values :')
    sql = 'update crime_type set '+ field +' = "' + value +'" where crime_id ='+ crime_id +';'
    
    cursor.execute(sql)
    conn.commit()
    print('Record updated successfully................')
    wait = input('\n\n\nPress any key to continue............')



def modify_complaint_record():
    clear()

    print(' M O D I F Y    C R I M E  R E C O R D  S C R E E N ')
    print('1.  Crime date \n')
    print('2.  Offence Type  \n')
    print('3.  Complaint By  \n')
    print('4.  Address  \n')
    print('5.  Phone No  \n')
    print('6.  Status  \n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'c_date'
    if choice ==2:
        field = 'offence_type'
    if choice == 3:
        field = 'complaint_by'
    if choice == 4:
        field = 'address'
    if choice == 5:
        field = 'phone_no'
    if choice == 6:
        field = 'status'
    
    print('\n\n\n')
    crime_id = input('Enter Complaint Record ID  :')
    value = input('Enter new values :')
    sql = 'update complaint_record set ' + field + \
        ' = "' + value + '" where id =' + crime_id + ';'
    cursor.execute(sql)
    conn.commit()
    print('Record updated successfully................')
    wait = input('\n\n\nPress any key to continue............')



def modify_offenders_record():
    clear()

    print(' M O D I F Y    C R I M E  R E C O R D  S C R E E N ')
    print('1.  Offender name \n')
    print('2.  Crime ID  \n')
    print('3.  Crime Name  \n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'offender_name'
    if choice ==2:
        field = 'crime_id'
    if choice == 3:
        field = 'crime_name'
    print('\n\n\n')
    record_id = input('Enter Record ID  :')
    value = input('Enter new values :')
    sql = 'update offenders_record set ' + field + \
        ' = "' + value + '" where id =' + record_id + ';'
    cursor.execute(sql)
    conn.commit()
    print('Record updated successfully................')
    wait = input('\n\n\nPress any key to continue............')



def search_menu():
    clear()
    print(' S E A R C H    C R I M E  R E C O R D  S C R E E N ')
    print('1.  Crime date \n')
    print('2.  Offence Type  \n')
    print('3.  Complaint By  \n')
    print('4.  Address  \n')
    print('5.  Phone No  \n')
    print('6.  Status  \n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'c_date'
    if choice == 2:
        field = 'offence_type'
    if choice == 3:
        field = 'complaint_by'
    if choice == 4:
        field = 'address'
    if choice == 5:
        field = 'phone_no'
    if choice == 6:
        field = 'status'
    value = input('Enter value to search :')
    if choice == 2:
        sql = 'select cr.id,c_date,offence_type,complaint_by,address,phone_no,status,update_date \
          from complaint_record cr, crime_type ct where cr.offence_type = ct.crime_id \
          AND ' + field + '= ' + value + ';'
    else:
        sql = 'select cr.id,c_date,offence_type,complaint_by,address,phone_no,status,update_date \
          from complaint_record cr, crime_type ct where cr.offence_type = ct.crime_id \
          AND ' + field + '= "' + value + '";'

    cursor.execute(sql)
    results = cursor.fetchall()
    records = cursor.rowcount
    for row in results:
        print(row)
    if records < 1:
        print('Record not found \n\n\n ')
    wait = input('\n\n\nPress any key to continue......')



def report_menu():
    
    clear()
    print(' C R I M E  R E C O R D  R E P O R T S  ')
    print('1.  Crime date \n')
    print('2.  Offence Type  \n')
    print('3.  Complaint By  \n')
    print('4.  Address  \n')
    print('5.  Phone No  \n')
    print('6.  Status  \n')
    choice = int(input('Enter your choice :'))
    field = ''
    if choice == 1:
        field = 'c_date'
    if choice == 2:
        field = 'offence_type'
    if choice == 3:
        field = 'complaint_by'
    if choice == 4:
        field = 'address'
    if choice == 5:
        field = 'phone_no'
    if choice == 6:
        field = 'status'
    value = input('Enter value  :')

    if choice ==2:
        sql = 'select cr.id,c_date,offence_type,complaint_by,address,phone_no,status,update_date \
          from complaint_record cr, crime_type ct where cr.offence_type = ct.crime_id \
          AND ' + field + '= ' + value + ';'
    else:
        sql ='select cr.id,c_date,offence_type,complaint_by,address,phone_no,status,update_date \
          from complaint_record cr, crime_type ct where cr.offence_type = ct.crime_id \
          AND ' + field + '= "' + value + '";'

    cursor.execute(sql)
    results = cursor.fetchall()
    records = cursor.rowcount
   
    page = 1
    total_pages = records//20
    if records % 20 != 0:
        total_pages += 1
    if records < 1:
        print('Record not found \n\n\n ')
    else:
        clear()
        print('Report on :',field,':',value )
        print('Page :',page,'/',total_pages)
        print('-'*100)
        print('{} {} {} {} {} {} {} {}'.format('id','Crime Date','Crime','Complaint By','Address','Phone','Status','Update On'))
        print('-'*100)
        line=1
        for row in results:
            print('{} {} {} {} {} {} {} {}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
            line = line+1
            if line>=21:
                wait = input('Press any key to continue.........')
                line = 1
                page +=1
                print('Report on :', field, ':', value)
                print('Page :',page,'/',total_pages)
                print('-'*100)
                print('{} {} {} {} {} {} {} {}'.format('id', 'Crime Date', 'Crime',
                                                       'Complaint By', 'Address', 'Phone', 'Status', 'Update On'))
        print('-'*100)
    
    wait = input('\n\n\nPress any key to continue......')
    



def main_menu():
    clear()
    introduction()
    n = input("Login as a user or an admin?(u/a): ")
    if n.lower() == 'a':
        admin_login()
        clear()
        while True:
            clear()
            print(' C R I M E   R E C O R D    I N F O R M A T I O N   S Y S T E M')
            print('*'*100)
            print("\n1.  Add New Complaint Record")
            print("\n2.  Add New Crime Type")
            print("\n3.  Add New Offender Record")
            print('\n4.  Modify Crime Type Record')
            print('\n5.  Modify Complaint Record')
            print("\n6.  Modify Offender Record")
            print('\n7.  Search Crime Database')
            print('\n8.  Report menu')
            print('\n9.  Close application')
            print('\n\n')
            choice = int(input('Enter your choice ...: '))

            if choice == 1:
                add_record()

            if choice == 2:
                add_crime_type()

            if choice == 3:
                add_offenders_record()

            if choice == 4:
                modify_crime_type_record()
      
            if choice == 5:
                modify_complaint_record()

            if choice == 6:
                modify_offenders_record()

            if choice == 7:
                search_menu()

            if choice == 8:
                report_menu()
      
            if choice == 9:
                break
        made_by()


    if n.lower() == 'u':
        user_login()
        clear()
        introduction()
        while True:
            clear()
            print(' C R I M E   R E C O R D    I N F O R M A T I O N   S Y S T E M')
            print('*'*100)
            print("\n1.  Add New Complaint Record")
            print('\n2.  Report menu')
            print('\n3.  Close application')
            print('\n\n')
            choice = int(input('Enter your choice ...: '))

            if choice == 1:
                add_record()
            if choice == 2:
                report_menu()
            if choice == 3:
                break
        made_by()


if __name__ == "__main__":
    main_menu()


