import psycopg2

cursor = None
connection = None

try:
    connection = psycopg2.connect(
        "dbname='Database-Name' user='Database-User' host='localhost' password='Password-Database'")
    print("Successful connection to the Bank")
    cursor = connection.cursor()

except (Exception, psycopg2.Error) as Error:
    print('connection fail', Error)


def select(fields, tables, where=None):
    query = " SELECT " + fields + " FROM " + tables

    global cursor

    if (where):
        query = query + " WHERE " + where

    cursor.execute(query)
    return cursor.fetchall()


def insert(values, table, fields=None):
    global cursor, connection

    query = " INSERT INTO " + table

    if (fields):
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

    cursor.execute(query)
    connection.commit()


def update(sets, table, where=None):
    global connection, cursor

    query = " UPDATE " + table
    query = query + " SET " + ",".join([field + "= '" + value + "'" for field, value in sets.items()])
    if (where):
        query = query + " WHERE " + where

    cursor.execute(query)
    connection.commit()


def delete(table, where):
    global connection, cursor
    query = " DELETE FROM " + table + " WHERE " + where

    cursor.execute(query)
    connection.commit()
