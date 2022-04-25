import sqlite3 as sql
import tkinter as tk
import re

def reg_continue(text, text_tel):

    def reg_final():

        rodnecislo = reg_rc_ent.get()
        jmeno = reg_jmeno_ent.get()
        prijmeni = reg_prijmeni_ent.get()
        email = reg_email_ent.get()
        telcislo = reg_telefon_ent.get()
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        errors_reg = 0
        tries = 0

        if tries != 0:
            label_err.remove()

        if not jmeno.isalpha() or jmeno == ' ':
            label_err = tk.Label(
                text='Jméno musí obsahovat pouze písmena',
                fg='red'
            )
            label_err.pack()
            errors_reg += 1
        if not prijmeni.isalpha() or prijmeni == ' ':
            label_err = tk.Label(
                text='Příjmení musí obsahovat pouze písmena',
                fg='red'
            )
            label_err.pack()
            errors_reg += 1
        if not (re.search(regex, email)):
            label_err = tk.Label(
                text='Email není validní',
                fg='red'
            )
            label_err.pack()
            errors_reg += 1

        if errors_reg != 0:
            tries += 1

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

        reg_rc_ent = tk.Entry(
            width=30,
            relief="solid",
            justify="center"
        )
        reg_rc_ent.pack()
        reg_rc_ent.insert(0, insert_rodny)
        #reg_rc_ent.configure(state='disabled')

        jmeno_lbl = tk.Label(
            text='Jméno'
        )
        jmeno_lbl.pack()

        reg_jmeno_ent = tk.Entry(
            width=20,
            relief="solid",
            justify="center"
        )
        reg_jmeno_ent.pack()

        prijmeni_lbl = tk.Label(
            text='Příjmení'
        )
        prijmeni_lbl.pack()

        reg_prijmeni_ent = tk.Entry(
            width=20,
            relief="solid",
            justify="center"
        )
        reg_prijmeni_ent.pack()

        email_lbl = tk.Label(
            text='Email'
        )
        email_lbl.pack()

        reg_email_ent = tk.Entry(
            width=20,
            relief="solid",
            justify="center"
        )
        reg_email_ent.pack()

        label_tel = tk.Label(
            text='Telefonní číslo',
        )
        label_tel.pack()

        reg_telefon_ent = tk.Entry(
            width=20,
            relief="solid",
            justify="center"
        )
        reg_telefon_ent.pack()
        reg_telefon_ent.insert(0, insert_tel)
        #reg_telefon_ent.configure(state='disabled')

        odeslat = tk.Button(
            width=15,
            height=2,
            text="REGISTROVAT",
            relief="solid",
            command=reg_final
        )
        odeslat.pack(pady=10)

    else:
        pass


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
        window2.title("Vaše údaje")

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

con = sql.connect('example.db')
cur = con.cursor()
curr = con.cursor()
window = tk.Tk()
window.geometry("400x230")
window.title("Přihlášení očkování")


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
    width=40,
    relief="solid",
    justify="center"
)
rodnycislo.pack()

label_tel = tk.Label(
    text='Telefonní číslo'
)
label_tel.pack()

telefon = tk.Entry(
    width=40,
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


