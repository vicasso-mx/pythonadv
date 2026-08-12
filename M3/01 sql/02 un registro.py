import mysql.connector

connection = mysql.connector.connect(
    host='lahman.csw1rmup8ri6.us-east-1.rds.amazonaws.com',
    user='python',
    passwd='python',
    db='lahmansbaseballdb'
)

varid = 'jeterde01'

query = """SELECT nameFirst, nameLast, birthCity, birthState, birthYear
           FROM people
           WHERE playerID = '""" + varid + "';"""

cursor = connection.cursor()

cursor.execute(query)

result = cursor.fetchone()

if result:
    player_name = result[0] + ' ' + result[1]
    birth_place = result[2] + ', ' + result[3]
    birth_year = result[4]
    print(f'{player_name} nació en {birth_place} en el año {birth_year}.')
else:
    print('No se encontró ningún jugador con ese ID.')

cursor.close()

connection.close()