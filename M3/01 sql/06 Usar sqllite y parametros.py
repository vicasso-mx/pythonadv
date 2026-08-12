import sqlite3
from pathlib import Path

def main():
    db = Path("data/lahmansbaseballdb.sqlite")
    
    if not db.exists():
        print(
            "debe descargar la base de datos desde https://github.com/WebucatorTraining/lahman-baseball-mysql/blob/master/lahmansbaseballdb.sqlite?raw=true y guardarla en la carpeta data."
        )
        return

    connection = sqlite3.connect(db)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    query = """SELECT p.nameFirst, p.nameLast, b.HR,
                    t.name AS team, b.yearID
                FROM batting b
                    JOIN people p ON p.playerID = b.playerID
                    JOIN teams t ON t.ID = b.team_ID
                WHERE b.yearID = ?
                ORDER BY b.HR DESC
                LIMIT 5;"""

    checking = True
    
    while checking:
        year_id = int(input('Escriba un año (0 para salir): '))
        if year_id == 0:
            break

        cursor.execute(query, [year_id])
        results = cursor.fetchall()

        for i, result in enumerate(results , 1):
            name = f"{result['nameFirst']} {result['nameLast']}"
            print(f"{i}. {name}: {result['HR']}")

    cursor.close()
    connection.close()

main()