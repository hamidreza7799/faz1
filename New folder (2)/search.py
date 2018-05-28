from flask import Flask, flash, jsonify, render_template, request
import sqlite3
def compare(a,b):
    if len(a)>=len(b):
        counter1=0
        counter2=0
        while a[counter1]!=b[0]:
            if counter1<len(a):
                counter1+=1
            break
        counter2=counter1+len(b)
        m=a[counter1:counter2]
        if m==b:
            return 1
        else:
            return 0
    else:
        counter1=0
        counter2=0
        while b[counter1]!=a[0]:
            if counter1<len(b):
                counter1+=1
            break
        counter2=counter1+len(a)
        m=b[counter1:counter2]
        #print(m,counter1,counter2)
        if m==a:
            return 1
        else:
            return 0
def transfor(string):
    for i in string:
        if ord(i) in range(65,91):
            string=string.replace(i,chr(ord(i)+32))

        if  ord(i)==1610 or ord(i)==1574:
            string=string.replace(i,chr(1740))
            
    return string

sql='''SELECT ID,NAME FROM name_id'''
sql2='''SELECT * FROM BAZAAR WHERE ID=(?) '''
app = Flask(__name__)
@app.route("/hello", methods=['POST'])
def hello():
    con=sqlite3.connect('test.db')
    data = request.form['q']
    data=transfor(data)
    cursor=con.execute(sql)
    for row in cursor:
        name=row[1]
        com_result=compare(data,name)
        if com_result==1:
            id2=row[0]
            rows=con.execute(sql2,(id2,))
            for row1 in rows:
                return render_template('result.html', result = row1)
    return 'FILE NOT FOUND'

app.run(debug=True)
