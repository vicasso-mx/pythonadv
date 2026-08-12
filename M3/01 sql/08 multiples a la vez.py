import sqlite3
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

create = """CREATE TABLE empleados (
                'nombre' text,
                'apellido' text,
                'area' text
            )"""

cursor.execute(create)

members = [
    ('Abel', 'Benitez', 'Finanzas'),
    ('Claudia', 'Díaz', 'Recursos Humanos'),
    ('Ernesto', 'Fernández', 'Marketing'),
    ('Gloria', 'Hernández', 'Operaciones')
]

query_DML = 'INSERT INTO empleados VALUES (?, ?, ?)'

cursor.executemany(query_DML, members)

select = 'SELECT * FROM empleados'
cursor.execute(select)

results = cursor.fetchall()
cursor.close()
connection.close()

print(results)