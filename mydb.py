import pymysql
dataBase = pymysql.connect(
    host='localhost',
    user='root',
    passwd='Mehulvs@99',
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS re_crm")

print("All Done!")

# import pyodbc
#
# # Define the connection string
# conn_str = (
#     "DRIVER={ODBC Driver 17 for SQL Server};"
#     "SERVER=localhost;"
#     "DATABASE=master;"
#     "UID=your_username;"
#     "PWD=your_password;"
# )
#
# # Connect to the SQL Server instance
# connection = pyodbc.connect(conn_str)
#
# # Create a cursor object
# cursor = connection.cursor()
#
# # Create a new database if it doesn't exist
# cursor.execute("CREATE DATABASE IF NOT EXISTS re_crm")
#
# # Commit the transaction
# connection.commit()
#
# # Close the cursor and connection
# cursor.close()
# connection.close()
#
# print("All Done!")
