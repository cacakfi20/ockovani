import sqlite3 as sql
import tkinter as tk

con = sql.connect('example.db')
cur = con.cursor()
curr = con.cursor()
window = tk.Tk()
window.geometry("600x600")
window.title("Registrace očkování 1.1")

listos = ('Rodné číslo:', 'Jméno:', 'Příjmení:', 'Email:', 'Telefon:')

curr.executescript(
    """
    SELECT * FROM osoba
    """
)
for row in curr.execute('SELECT * FROM osoba'):
        i = 0
        textbox = tk.Listbox(
            height=5,
        )
        for vec in row:
            textbox.insert(tk.END, listos[i], vec)
            i+=1

        textbox.pack()

window.mainloop()

try:
    cur.executescript("""
    CREATE TABLE osoba
    (
    RODNE_CISLO TEXT PRIMARY KEY,
    JMENO VARCHAR,
    PRIJMENI VARCHAR,
    EMAIL VARCHAR,
    TELEFON INT
    );
    """)
except:
    cur.executescript("""
    INSERT INTO osoba(RODNE_CISLO, JMENO, PRIJMENI, EMAIL, TELEFON) VALUES ('041116/4688' ,'Filip', 'Cacák', 'cacijegoat@seznam.cz', 603768452);
    """)
