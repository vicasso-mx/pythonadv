import sqlite3

connection = sqlite3.connect(':memory:')

cursor = connection.cursor()

queryDDL = """CREATE TABLE empleados (
                'nombre' text,
                'apellido' text,
                'area' text
            )"""

cursor.execute(queryDDL)

members = [
    ('Abel', 'Benitez', 'Finanzas'),
    ('Claudia', 'Díaz', 'Recursos Humanos'),
    ('Ernesto', 'Fernández', 'Marketing'),
    ('Gloria', 'Hernández', 'Operaciones')
]

insert = 'INSERT INTO empleados VALUES (?, ?, ?)'

# Loop through the members list, inserting each member
for member in members:
    cursor.execute(insert, member)

query_select = 'SELECT nombre, apellido, area FROM empleados'

cursor.execute(query_select)

results = cursor.fetchall()

cursor.close()

connection.close()

print(results)