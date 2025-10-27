import cx_Oracle

conn = cx_Oracle.connect('DBMS128/matsushima@//tetraserver.thddns.net:4421/orcl')
print(conn.version)



