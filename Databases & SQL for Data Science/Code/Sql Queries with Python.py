import pymysql as sql


try:
    con=sql.connect(host='localhost',user='root',password='ayaan1234')
    mycursor=con.cursor()

except:
    messagebox.showerror('Error','Database Connectivity Issue,Please Try Again.')

try:
    query='create database Chicago'
    mycursor.execute(query)
    query='use Chicago'
    mycursor.execute(query)
    query='CREATE TABLE Chicago_Crime_Data (ID INT Primary Key NOT NULL AUTO_INCREMENT,CASE_NUMBER VARCHAR(25) NOT NULL,Date_Reg DATE NOT NULL,BLOCK_NUMBER VARCHAR(50) NOT NULL,IUCR INT(25) NOT NULL,PRIMARY_TYPE VARCHAR(20) NOT NULL,Description_crime VARCHAR(25) NOT NULL,LOCATION_DESCRIPTION VARCHAR(25) NOT NULL,ARREST VARCHAR(6) NOT NULL,DOMESTIC VARCHAR(6) NOT NULL,BEAT INT(10),DISTRICT INT(10),WARD INT(10),COMMUNITY_AREA_NUMBER INT(10),FBI_CODE INT(10),X_CORDINATE INT(15) not NUll,Y_CORDINATE INT(15) not NUll,Year_Crime INT(4) not NUll,LATITUDE INT(20) not NUll,LONGITUDE INT(20) not NUll,LOCATION VARCHAR(30) not NUll)'
    mycursor.execute(query)
except:
    mycursor.execute('use Chicago')
try:
    query1='use Chicago'
    mycursor.execute(query1)
    query1='CREATE TABLE Chicago_Census_Data (COMMUNITY_AREA_NUMBER Primary key Foreign Key int(10) Not Null,COMMUNITY_AREA_NAME Char(25) not null,PERCENT_OF_HOUSING_CROWDED varchar(10),PERCENT_HOUSEHOLDS_BELOW_POVERTY varchar(10),PERCENT_AGED_16__UNEMPLOYED varchar(10),PERCENT_AGED_25__WITHOUT_HIGH_SCHOOL_DIPLOMA varchar(10),PERCENT_AGED_UNDER_18_OR_OVER_64 varchar(10),PER_CAPITA_INCOME int(10),HARDSHIP_INDEX int(6))'
    mycursor.execute(query1)
except:
    mycursor.execute('use Chicago')

try:
    query2='use Chicago'
    mycursor.execute(query2)
    query2='CREATE TABLE Chicago_Public_Schools (COMMUNITY_AREA_NUMBER Primary key Foreign Key int(10) Not Null,COMMUNITY_AREA_NAME Char(25) not null,PERCENT_OF_HOUSING_CROWDED varchar(10),PERCENT_HOUSEHOLDS_BELOW_POVERTY varchar(10),PERCENT_AGED_16__UNEMPLOYED varchar(10),PERCENT_AGED_25__WITHOUT_HIGH_SCHOOL_DIPLOMA varchar(10),PERCENT_AGED_UNDER_18_OR_OVER_64 varchar(10),PER_CAPITA_INCOME int(10),HARDSHIP_INDEX int(6))'
    mycursor.execute(query2)
except:
    mycursor.execute('use Chicago')
    

try:
    con=sql.connect(host='localhost',user='root',password='ayaan1234',database='Chicago')
    mycursor=con.cursor()
    #query='select COMMUNITY_AREA_NUMBER,count(*) as number_of_crimes from Chicago_Crime_Data group by COMMUNITY_AREA_NUMBER order by number_of_crimes desc limit 1'
    #query='select distinct(CASE_NUMBER),PRIMARY_TYPE from Chicago_Crime_Data where PRIMARY_TYPE="OTHER OFFENSE" '
    #query='select CASE_NUMBER,PRIMARY_TYPE from Chicago_Crime_Data where PRIMARY_TYPE="KIDNAPPING" and Description_Crime like "%CHILD%" '
    #query='select PRIMARY_TYPE,Description_Crime from Chicago_Crime_Data where LOCATION_DESCRIPTION like "%SCHOOL%"'
    query='select count(*) from Chicago_Crime_Data'
    mycursor.execute(query)
    rows=mycursor.fetchall()
    print("Crimes at school are ",rows)
    #query1='select COMMUNITY_AREA_NAME from Chicago_Census_Data where HARDSHIP_INDEX=(select distinct(HARDSHIP_INDEX) from Chicago_Census_Data order by HARDSHIP_INDEX DESC limit 1)'
    query1='select COMMUNITY_AREA_NAME from Chicago_Census_Data where COMMUNITY_AREA_NUMBER\
=(select COMMUNITY_AREA_NUMBER from Chicago_Crime_Data group by COMMUNITY_AREA_NUMBER order by count(COMMUNITY_AREA_NUMBER) desc limit 1)'
    mycursor.execute(query1)
    rows1=mycursor.fetchall()
    print("Community area with most number of crimes: ",rows1)
    query2='select "ELementry,Middle, or High School" as Schools_Type,AVG(SAFETY_SCORE) as Average_Safety_Score from \
Chicago_Public_Schools group by "ELementry,Middle, or High School"'
    mycursor.execute(query2)
    rows2=mycursor.fetchall()
    print("Average Safety Score for al types of Schools is ",rows2)
    
except:
    print("There is some error Please Try Again!!")
