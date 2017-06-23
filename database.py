# https://oracle.github.io/python-cx_Oracle/

import cx_Oracle
conn = cx_Oracle.connect('TPACARE/tpacare@172.16.112.202/thaire')
curs = conn.cursor()
curs.execute('SELECT COUNT(1) FROM members.member_detail')
for row in curs.fetchall():
	print(row)
conn.close()