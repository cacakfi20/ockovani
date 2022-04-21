import sqlite3 as sql
import tkinter as tk

con = sql.connect('example.db')
cur = con.cursor()
curr = con.cursor()
window = tk.Tk()
window.geometry("320x250")
window.title("Přihlášení očkování")


def register():
    error = 0
    text = rodnycislo.get()
    rodnycislo.delete(0, tk.END)
    text_tel = telefon.get()
    telefon.delete(0, tk.END)
    if len(text) == 0 or len(text_tel) == 0:
        error += 1
        label_err = tk.Label(
            text='Některý z údajů je prázdný',
            fg='red'
        )
        label_err.pack()
    if len(text) != 10 and len(text) != 11:
        error += 1
        label_err = tk.Label(
            text='Rodné číslo nemá správnou délku',
            fg='red'
        )
        label_err.pack()
    if len(text_tel) != 9:
        error += 1
        label_err = tk.Label(
            text='Telefonní číslo nemá správnou délku',
            fg='red'
        )
        label_err.pack()
    if len(text) == 11:
        cs = len(text)
        print(cs)
        text.replace("\n", "")
        text2 = text.replace("/","")
        pocet = len(text2)
        print(text2)
        vysledek = 0
        for i in range(0, pocet, 2):
            vysledek = vysledek + int(text2[i] + text2[i+1])
        if vysledek % 11 == 0:
            print("ok")
        else:
            error += 1
            label_err = tk.Label(
                text='Toto není rodné číslo',
                fg='red'
            )
            label_err.pack()
    if error == 0:
        reg_continue(text, text_tel)


def reg_continue(text, text_tel):
    insert_rodny = text
    insert_tel = text_tel
    checkos = curr.execute(
        """
        SELECT * FROM osoba WHERE rodne_cislo = ?
        """, (insert_rodny,)
    )
    row = checkos.fetchone()
    if row == None:
        window.destroy()
        con2 = sql.connect('example.db')
        cur2 = con.cursor()
        curr2 = con.cursor()
        window2 = tk.Tk()
        window2.geometry("600x350")
        window2.title("Registrace očkování 1.1")

        main_label = tk.Label(
            text='Registrace',
            font=("Helvetica", 18),
        )
        main_label.pack()

        label = tk.Label(
            text='Rodné číslo'
        )
        label.pack()

        rodnycislo = tk.Entry(
            width=20,
            relief="solid",
            justify="center"
        )
        rodnycislo.pack()
        rodnycislo.insert(0, insert_rodny)
        rodnycislo.configure(state='disabled')

        jmeno_lbl = tk.Label(
            text='Jméno'
        )
        jmeno_lbl.pack()

        jmeno_ent = tk.Entry(
            width=20,
            relief="solid",
            justify="center"
        )
        jmeno_ent.pack()

        prijmeni_lbl = tk.Label(
            text='Příjmení'
        )
        prijmeni_lbl.pack()

        prijmeni_ent = tk.Entry(
            width=20,
            relief="solid",
            justify="center"
        )
        prijmeni_ent.pack()

        email_lbl = tk.Label(
            text='Email'
        )
        email_lbl.pack()

        email_ent = tk.Entry(
            width=20,
            relief="solid",
            justify="center"
        )
        email_ent.pack()

        label_tel = tk.Label(
            text='Telefonní číslo',
        )
        label_tel.pack()

        telefon = tk.Entry(
            width=20,
            relief="solid",
            justify="center"
        )
        telefon.pack()
        telefon.insert(0, insert_tel)
        telefon.configure(state='disabled')

        odeslat = tk.Button(
            width=15,
            height=2,
            text="REGISTROVAT",
            relief="solid",
            command=send
        )
        odeslat.pack(pady=10)


def send():
    text = rodnycislo.get()
    rodnycislo.delete(0, tk.END)
    text_tel = telefon.get()
    telefon.delete(0, tk.END)
    check(text, text_tel)

def check(text, text_tel):
    check_text = text
    check_tel = text_tel
    checkos = curr.execute(
        """
        SELECT * FROM osoba WHERE rodne_cislo = ? AND telefon = ?
        """,(check_text, check_tel, )
    )
    row = checkos.fetchone()
    if row == None:
        print("There are no results for this query")
    else:
        print("existuje")
        window.destroy()
        con2 = sql.connect('example.db')
        cur2 = con.cursor()
        curr2 = con.cursor()
        window2 = tk.Tk()
        window2.geometry("600x600")
        window2.title("Registrace očkování 1.1")

        listos = ('Rodné číslo:', 'Jméno:', 'Příjmení:', 'Email:', 'Telefon:')

        curr2.execute(
            """
            SELECT * FROM osoba WHERE rodne_cislo = ?
            """,(check_text,)
        )
        for row in curr2.execute('SELECT * FROM osoba WHERE rodne_cislo = ?',(check_text,)):
            i = 0
            textbox = tk.Listbox(
                height=5,
            )
            for vec in row:
                text = '{} {}'.format(listos[i], vec)
                textbox.insert(tk.END, text)
                i += 1

            textbox.pack()

        window.mainloop()

main_label = tk.Label(
    text='Přihlašte se nebo začněte registraci',
    font=("Helvetica", 18),
)
main_label.pack()
label = tk.Label(
    text='Rodné číslo'
)
label.pack()

rodnycislo = tk.Entry(
    width=20,
    relief="solid",
    justify="center"
)
rodnycislo.pack()

label_tel = tk.Label(
    text='Telefonní číslo'
)
label_tel.pack()

telefon = tk.Entry(
    width=20,
    relief="solid",
    justify="center"
)
telefon.pack()

odeslat = tk.Button(
    width=15,
    height=1,
    text="PŘIHLÁSIT",
    relief="solid",
    command= send
)
odeslat.pack(pady=10)

registrovat = tk.Button(
    width=15,
    height=1,
    text="REGISTROVAT",
    relief="solid",
    command= register
)
registrovat.pack()

window.mainloop()


