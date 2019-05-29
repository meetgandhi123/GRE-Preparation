# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 06:49:45 2019

@author: meet
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="python_project"
)
mycursor = mydb.cursor()

 
def add_words():
    word1=input("Adding words to DataBase:")
    print(word1)
    if(word1=='quit' or word1=='QUIT' or word1=='Quit'):
        ask()
    meaning1=input("Meaning and Expected answer:")
    print(meaning1)
    sql = "INSERT INTO vocab (word,meaning) VALUES (%s,%s)"
    val = (word1,meaning1)
    mycursor.execute(sql, val)    
    mydb.commit()
    print("Record Saved !!")
    add_words()
#    ask()
def sequential_words(srno):
    count=0;
    srno=srno+1        
    sql = "SELECT word FROM vocab where sr_no = '{}'".format(srno)
    mycursor.execute(sql)    
    myquestion = mycursor.fetchone()
    str1 = ''.join(myquestion)
    ans1=(input("Enter similar word for {}:".format(str1)))  
    print(ans1)
    ans3=ans1
    sql = "SELECT meaning FROM vocab WHERE word LIKE '{}'".format(str1)
    mycursor.execute(sql)    
    myresult = mycursor.fetchone()
    correct_answer = ''.join(myresult)  
    ans2=correct_answer
    if(ans1 ==correct_answer):
        print('Perfectely Correct')
    elif(ans1=='QUIT'):
        ask()
    elif(ans1!=''):
        ans1=ans1.split(' ')
        showans=correct_answer
        correct_answer=correct_answer.split(' ')
        for i in ans1:
            if i in correct_answer:
                count=1;
        if(count==1):
            print('correct answer')
            print('Answer according to database:',showans)        
        if(count!=1):
            print('incorrect')                
            print('Answer according to database:',showans)
            reply=(input("Are this words similar?"))
            if(reply=='YES'):
                space=" "
                add=ans2+space+ans3
                query="update vocab set meaning ='{}' where word like '{}'".format(add,str1)
                db = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  passwd="root",
                  database="python_project"
                  )
                mycursor1 = db.cursor()
                mycursor1.execute(query)
                db.commit()
                print(mycursor1.rowcount, "record(s) affected")
            else:
                reply1=(input("Add this to difficult words?"))
                if(reply1=='YES'):
                    sql = "INSERT INTO gre_words (word,meaning) VALUES (%s,%s)"
                    val = (str1,ans2)
                    mycursor.execute(sql, val)    
                    mydb.commit()
                    print("Record Saved !!")
    else:
        print('incorrect')
        print('Answer according to database:',correct_answer) 
    sequential_words(srno)
    
def random_words():
    count=0
    sql = "SELECT word FROM vocab ORDER BY RAND() LIMIT 1"
    mycursor.execute(sql)    
    myquestion = mycursor.fetchone()
    str1 = ''.join(myquestion)
    ans1=(input("Enter similar word for {}:".format(str1)))  
    print(ans1)
    ans3=ans1
    sql = "SELECT meaning FROM vocab WHERE word LIKE '{}'".format(str1)
    mycursor.execute(sql)    
    myresult = mycursor.fetchone()
    correct_answer = ''.join(myresult)
    ans2=correct_answer
    if(ans1 ==correct_answer):
        print('Perfectely Correct')
    elif(ans1=='QUIT'):
        ask()
    elif(ans1!=''):
        ans1=ans1.split(' ')
        showans=correct_answer
        correct_answer=correct_answer.split(' ')
        for i in ans1:
            if i in correct_answer:
                count=1;
        if(count==1):
            print('correct answer')
            print('Answer according to database:',showans)         
        if(count!=1):
            print('incorrect')                
            print('Answer according to database:',showans)        
            reply=(input("Are this words similar?"))
            if(reply=='YES'):
                space=" "
                add=ans2+space+ans3
                query="update vocab set meaning ='{}' where word like '{}'".format(add,str1)
                db = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  passwd="root",
                  database="python_project"
                  )
                mycursor1 = db.cursor()
                mycursor1.execute(query)
                db.commit()
                print(mycursor1.rowcount, "record(s) affected")
            else:
                reply1=(input("Add this to difficult words?"))
                if(reply1=='YES'):
                    sql = "INSERT INTO gre_words (word,meaning) VALUES (%s,%s)"
                    val = (str1,ans2)
                    mycursor.execute(sql, val)    
                    mydb.commit()
                    print("Record Saved !!")
    else:
        print('incorrect')
        print('Answer according to database:',correct_answer)        
    random_words()
    
def practice():
    p1=int(input('1. Random words \n2. Sequential\n3. Exit'))
    if(p1==1):        
        random_words()     
    elif(p1==2):
        srno=0;
        sequential_words(srno)                               
    elif(p1==3):
        ask()
def hard_sequential_words(srno):
    count=0;
    srno=srno+1        
    sql = "SELECT word FROM gre_words where sr_no = '{}'".format(srno)
    mycursor.execute(sql)    
    myquestion = mycursor.fetchone()
    str1 = ''.join(myquestion)
    ans1=(input("Enter similar word for {}:".format(str1)))  
    print(ans1)
    ans3=ans1
    sql = "SELECT meaning FROM gre_words WHERE word LIKE '{}'".format(str1)
    mycursor.execute(sql)    
    myresult = mycursor.fetchone()
    correct_answer = ''.join(myresult)  
    ans2=correct_answer
    if(ans1 ==correct_answer):
        print('Perfectely Correct')
    elif(ans1=='QUIT'):
        ask()
    elif(ans1!=''):
        ans1=ans1.split(' ')
        showans=correct_answer
        correct_answer=correct_answer.split(' ')
        for i in ans1:
            if i in correct_answer:
                count=1;
        if(count==1):
            print('correct answer')
            print('Answer according to database:',showans)        
        if(count!=1):
            print('incorrect')                
            print('Answer according to database:',showans)
            reply=(input("Are this words similar?"))
            if(reply=='YES'):
                space=" "
                add=ans2+space+ans3
                query="update gre_words set meaning ='{}' where word like '{}'".format(add,str1)
                db = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  passwd="root",
                  database="python_project"
                  )
                mycursor1 = db.cursor()
                mycursor1.execute(query)
                db.commit()
                print(mycursor1.rowcount, "record(s) affected")
    else:
        print('incorrect')
        print('Answer according to database:',correct_answer) 
    hard_sequential_words(srno)
    
def hard_random_words():
    count=0
    sql = "SELECT word FROM gre_words ORDER BY RAND() LIMIT 1"
    mycursor.execute(sql)    
    myquestion = mycursor.fetchone()
    str1 = ''.join(myquestion)
    ans1=(input("Enter similar word for {}:".format(str1)))  
    print(ans1)
    ans3=ans1
    sql = "SELECT meaning FROM gre_words WHERE word LIKE '{}'".format(str1)
    mycursor.execute(sql)    
    myresult = mycursor.fetchone()
    correct_answer = ''.join(myresult)
    ans2=correct_answer
    if(ans1 ==correct_answer):
        print('Perfectely Correct')
    elif(ans1=='QUIT'):
        ask()
    elif(ans1!=''):
        ans1=ans1.split(' ')
        showans=correct_answer
        correct_answer=correct_answer.split(' ')
        for i in ans1:
            if i in correct_answer:
                count=1;
        if(count==1):
            print('correct answer')
            print('Answer according to database:',showans)         
        if(count!=1):
            print('incorrect')                
            print('Answer according to database:',showans)        
            reply=(input("Are this words similar?"))
            if(reply=='YES'):
                space=" "
                add=ans2+space+ans3
                query="update gre_words set meaning ='{}' where word like '{}'".format(add,str1)
                db = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  passwd="root",
                  database="python_project"
                  )
                mycursor1 = db.cursor()
                mycursor1.execute(query)
                db.commit()
                print(mycursor1.rowcount, "record(s) affected")
    else:
        print('incorrect')
        print('Answer according to database:',correct_answer)        
    hard_random_words()
    
def Hard_Words_Practice():
    p1=int(input('1. Random words \n2. Sequential\n3. Exit'))
    if(p1==1):        
        hard_random_words()     
    elif(p1==2):
        srno=0;
        hard_sequential_words(srno)                               
    elif(p1==3):
        ask()
        
def ask():
    n=int(input("Press 1 to add words , 2 to practice , 3 for Hard Words\n"))
    if(n==1):
        add_words()
    elif(n==2):
        practice()        
    elif(n==3):
        Hard_Words_Practice()
    
ask()    
    