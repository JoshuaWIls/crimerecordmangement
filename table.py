# Crime record management system data
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")
mycursor=mydb.cursor()

mycursor.execute("create database if not exists crime;")
mycursor.execute("use crime;")

mycursor.execute("DROP TABLE IF EXISTS crime_type;")
mycursor.execute("CREATE table if not exists crime_type (crime_id int(10) primary key auto_increment, offence_name char(50) not null, ipc_section char(60) not null, description varchar(100) not null)")
mycursor.execute("INSERT into crime_type values (1, 'Attempt to murder', '403', 'murder by parents'), (2, 'Stolen', '1243', 'When owner was away'), (3, 'Burgulary', '454-1234', 'sendhmari'), (4, 'Sexual assualt', '345-C', 'Sexual assualt on adult women')")
mycursor.execute("INSERT into crime_type values (5, 'EVE-Teasing', '254-B', 'Following or harassing adult women'), (6, 'Online Fraud', '68-A', 'Online fraud using spam phishing or other means'), (7, 'Molestation', '3434-C', 'Molestation of minor')")
mycursor.execute("INSERT into crime_type values (8, 'Financial cheating', '420', 'Simple finacial cheating')")
mydb.commit()


mycursor.execute("DROP table if exists admin_login")
mycursor.execute("CREATE TABLE IF NOT EXISTS admin_login (id int(10) Primary key,Name char(20) Not null,Passwd char(10) Not Null);")
mycursor.execute("INSERT into admin_login values (101,'Aditya','123'),(102,'Mohit','123'),(103,'Joshua','123');")
mydb.commit()


mycursor.execute("DROP table if exists user_login")
mycursor.execute("CREATE TABLE IF NOT EXISTS user_login (id int(10) Primary key auto_increment, Name char(20) Not null,Passwd char(10) Not Null);")
mycursor.execute("INSERT into user_login values (101,'Joey','123'),(102,'Chandler','123'),(103,'Ross','123');")
mydb.commit()


mycursor.execute("DROP TABLE IF EXISTS complaint_record;")
mycursor.execute("CREATE TABLE IF NOT EXISTS complaint_record (id int(10) PRIMARY KEY auto_increment,c_date date ,offence_type int(10),complaint_by char(30),address varchar(100),phone_no char(11),status char(15),update_date date)")
mycursor.execute("INSERT INTO complaint_record VALUES (1, '2021-02-04', 4, 'rakesh kumar', 'c-4 brij vihar', '9871816902', 'open', '2021-02-03'),(2, '2021-02-03', 4, 'anuj bhati', 'b-100 surya nagar', '9565652302', 'open', '2021-02-04'),(3, '2021-02-01', 8, 'amar singh', 'c-102 ramprastha', '9675652302', 'open', '2021-01-04'),(4, '2021-03-05', 12, 'ramji', '100 shrestha vihar', '34534534', 'open', '2021-03-05'),(5, '2021-03-05', 11, 'ramji', 'c-122 mayur vihar', '1122334455', 'open', '2021-03-05'),(6, '2021-03-05', 13, 'suresh sharma', 'cf-5 vivek vihar delhi', '4433221111', 'open', '2021-03-05')")
mydb.commit()




mycursor.execute("DROP TABLE IF EXISTS offenders_record;")
mycursor.execute("CREATE TABLE IF NOT EXISTS offenders_record (id int(10) PRIMARY KEY auto_increment, offender_name varchar(30) NOT NULL, crime_id int(10) NOT NULL, crime_name char(30) NOT NULL )")
mycursor.execute("INSERT INTO offenders_record (id, offender_name, crime_id, crime_name) VALUES(1, 'joey singh', 4, 'null'),(2, 'mohit bing', '4', 'null'),(3, 'rachel agarwal', 6, 'null'),(4, 'josh tribbiani', 8, 'null'),(5, 'monica shetty', 12, 'null')")
mydb.commit()
