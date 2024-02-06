import sqlite3

conn = sqlite3.connect("my_database.db")
conn.execute('''
    CREATE TABLE IF NOT EXISTS istoric (
        id INTEGER PRIMARY KEY,
        nume TEXT NOT NULL,
        varsta INTEGER NOT NULL
    );
''')

conn.execute('''
    CREATE TABLE IF NOT EXISTS persoane (
        id INTEGER PRIMARY KEY,
        nume TEXT NOT NULL,
        varsta INTEGER NOT NULL
    );
''')

persoane = [
    ("Alice", 25),
    ("Bob", 30),
    ("Carol", 22),
    ("David", 28),
    ("Eve", 35)
]

for p in persoane:
    conn.execute("INSERT INTO persoane (nume, varsta) VALUES (?, ?)", p)

conn.execute('''
    CREATE TRIGGER IF NOT EXISTS before_delete_history
    BEFORE DELETE ON persoane
    BEGIN
        INSERT INTO istoric (id, nume, varsta)
        SELECT OLD.id, OLD.nume, OLD.varsta;
    END;
''')

conn.commit()
conn.close()

print("Baza de date a fost actualizată cu succes!")
