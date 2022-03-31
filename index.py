from random import *
from faker import Faker
import csv

fake = Faker()

n = 40000000

std_header = ["s_id", "s_name"]
t_header = ["t_id", "t_name"]
sec_header = ["sub_id", "t_id", "sec_id", "ex_date", "room", "time"]
grade_header = ["s_id", "sub_id", "grade", "semester"]
sub_header = ["sub_id", "sub_name", "unit", "t_id"]

student = open('students.csv', 'w')
teacher = open('teachers.csv', 'w')
sec = open("sections.csv", "w")
sub = open('subjects.csv', 'w')
grade = open('have_grade.csv', 'w')

student_write = csv.writer(student)
teacher_write = csv.writer(teacher)
sec_write = csv.writer(sec)
sub_write = csv.writer(sub)
grade_write = csv.writer(grade)

student_write.writerow(std_header)
teacher_write.writerow(t_header)
sec_write.writerow(sec_header)
sub_write.writerow(sub_header)
grade_write.writerow(grade_header)

s_id_li = []
t_id_li = []
sub_id_li = []

for i in range(n-1):
    std_id = i
    t_id = i
    sub_id = i

    s_id_li.append(std_id)
    t_id_li.append(t_id)
    if (i < 1000):
        sub_id_li.append(sub_id)
        sub_write.writerow([sub_id, fake.job(),randint(0,3), t_id_li[randrange(0, len(t_id_li))]])
        
    student_write.writerow([std_id, fake.name()])
    teacher_write.writerow([t_id, fake.name()])
    sec_write.writerow([sub_id_li[randrange(0, len(sub_id_li))], t_id_li[randrange(0, len(t_id_li))], randint(0,6), fake.date(), fake.building_number(), str(fake.time())+"-"+str(fake.time())])
    grade_write.writerow([s_id_li[randrange(0, len(s_id_li))], sub_id_li[randrange(0, len(sub_id_li))], randint(1,4), randint(1,2)])
    print((n-i)/n*100)
