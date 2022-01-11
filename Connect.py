import mysql.connector
import sys

db = mysql.connector.connect(host="localhost",
                             user='root',
                             passwd="",
                             db='reddit4')
cursor = db.cursor()
