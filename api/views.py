from django.shortcuts import render
from rest_framework import response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import Bankdata
from .serializers import *
from django.db import connection
import psycopg2
import json
import collections
# Create your views here.
class search_result(APIView):
    def post(self,request):
        # # l = []
        # # for p in Bankdata.objects.raw('SELECT * FROM query_bankdata'):
        # #     l.append(p.id)
        # # # print(l,'idddddddddddddddddddd')
        # # obj = Bankdata.objects.filter(id=[i for i in l])
        # # print(obj,'lllllllllllllllllllllllllll')
        # # #     print(p,'hahahahah')
        # with connection.cursor() as cursor:
        #     print(cursor.execute('SELECT * FROM query_bankdata'),'#####################')
        #     result_query = cursor.execute('SELECT * FROM query_bankdata')

        # input_query = request.data['search']
        # # result_query = Bankdata.objects.all()
        # serializer = MySerializer(result_query, many=True)
        # return response.Response(serializer.data)
        con = psycopg2.connect(database="postgres", user="postgres", password="syedisgreat", host='winningshot.cfrqe0kosfba.us-east-2.rds.amazonaws.com', port="5432")
        print("Database opened successfully")
        cur = con.cursor()
        # cur.execute('''CREATE TABLE STUDENT
        #     (ADMISSION INT PRIMARY KEY     NOT NULL,
        #     NAME           TEXT    NOT NULL,
        #     AGE            INT     NOT NULL,
        #     COURSE        CHAR(50),
        #     DEPARTMENT        CHAR(50));''')
        # print("Table created successfully")
        # cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')");
        
        # my_query=cur.execute("SELECT admission, name, age, course, department from STUDENT")
        # rows = cur.fetchall()
        # objects_list = []
        # for row in rows:
        #     d = collections.OrderedDict()
        #     print("ADMISSION =", row[0])
        #     print("NAME =", row[1])
        #     print("AGE =", row[2])
        #     print("COURSE =", row[3])
        #     print("DEPARTMENT =", row[4], "\n")
        #     objects_list.append(d)
        # j = json.dumps(objects_list)
        # con.commit()
        # con.close()
        # print(objects_list,'##################################')
        cur.execute("SELECT * FROM STUDENT")
        rows = cur.fetchall()

        rowarray_list = []
        for row in rows:
            t = (row[0], row[1], row[2], )
            rowarray_list.append(t)

        j = json.dumps(rowarray_list)

        with open("student_rowarrays.js", "w") as f:
            f.write(j)

        # Convert query to objects of key-value pairs
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d["id"] = row[0]
            d["firstName"] = row[1]
            d["lastName"] = row[2]
            d["Street"] = row[3]
            objects_list.append(d)

        j = json.dumps(objects_list)
        print(j,'33333333333333')
        return response.Response(j)
        with open("student_objects.js", "w") as f:
            f.write(j)

        