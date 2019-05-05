import pyodbc

connection = 'Microsoft SQL Server'
server = 'localhost,1433'
database = 'pokemon'
username = 'SA'
password = 'Passw0rd2018'

docker_pokemon = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL SERVER};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = docker_pokemon.cursor()


def sql_query_no_transaction(sql_query):
    return cursor.execute(sql_query)