
import csv, sqlite3

con = sqlite3.connect("mark_list.db")
cur = con.cursor()
#cur.execute("DROP TABLE MARKS")

cur.execute("CREATE TABLE MARKS(name, maths, biology, english, physics, chemistry, hindi);") # use your column names here

with open('Student_marks_list.csv','r') as f:

    dr = csv.DictReader(f)

    to_db = [(i['Name'], i['Maths'], i['Biology'], i['English'], i['Physics'], i['Chemistry'], i['Hindi']) for i in dr]

cur.executemany("INSERT INTO MARKS (Name, Maths, Biology, English, Physics, Chemistry, Hindi) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)

for row in cur.execute('SELECT Name FROM MARKS ORDER BY maths DESC LIMIT 1'):
        print("The topper in Maths is ", [i for i in row])

for row in cur.execute('SELECT Name FROM MARKS ORDER BY biology DESC LIMIT 1'):
        print("The topper in Biology is ", [i for i in row])

for row in cur.execute('SELECT Name FROM MARKS ORDER BY english DESC LIMIT 1'):
        print("The topper in English is ", [i for i in row])

for row in cur.execute('SELECT Name FROM MARKS ORDER BY physics DESC LIMIT 1'):
        print("The topper in Physics is ", [i for i in row])

for row in cur.execute('SELECT Name FROM MARKS ORDER BY chemistry DESC LIMIT 1'):
        print("The topper in Chemistry is ", [i for i in row])

for row in cur.execute('SELECT Name FROM MARKS ORDER BY hindi DESC LIMIT 1'):
        print("The topper in Hindi is ", [i for i in row])

toppers = []
for row in cur.execute('SELECT Name, (maths + biology + english + physics + Chemistry + hindi) AS total FROM MARKS ORDER BY total DESC LIMIT 3'):
    toppers.append(row)

print("Best students in class are: ", toppers)

con.commit()
con.close()
#
