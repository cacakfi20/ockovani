import sqlite3 as sql
import tkinter as tk
import re

# funkce na vytvoření formuláře pro registraci
def reg_continue(text, text_tel):

    # funkce na kontrolu dat při registraci
    def reg_final():

        # funkce na přeposlání dat ke kontrole
        def send_2():
            text = rodnycislo.get()
            text_tel = telefon.get()
            check_2(text, text_tel)

        # funkce na kontrolu dat při registraci a následném přihlášení
        def check_2(text, text_tel):
            check_text = text
            check_tel = text_tel
            checkos = curr.execute(
                """
                SELECT * FROM osoba WHERE rodne_cislo = ? AND telefon = ?
                """, (check_text, check_tel,)
            )
            row = checkos.fetchone()
            if row == None:
                print("There are no results for this query")
                rodnycislo.config(highlightbackground = "red", highlightcolor= "red")
                telefon.config(highlightbackground = "red", highlightcolor= "red")
            else:
                def update_jmeno2():
                    jmeno_up = up_jmeno.get()
                    if not jmeno_up.isalpha() or jmeno_up == ' ':
                        up_jmeno.delete(0, tk.END)
                        up_jmeno.config(highlightbackground="red", highlightcolor="red")
                    else:
                        up_jmeno.config(highlightbackground="black", highlightcolor="black")
                        up_jmeno.delete(0, tk.END)
                        con = sql.connect('example.db')
                        c = con.cursor()
                        c.execute(""" UPDATE osoba SET jmeno = ? WHERE rodne_cislo = ?""", (jmeno_up, check_text))
                        con.commit()

                        c.execute(
                            """
                            SELECT * FROM osoba WHERE rodne_cislo = ?
                            """, (check_text,)
                        )
                        updated_window = tk.Toplevel(window2)
                        updated_window.geometry("600x300")
                        updated_window.title("Upravené údaje")
                        for row in c.execute('SELECT * FROM osoba WHERE rodne_cislo = ?', (check_text,)):
                            i = 0
                            textbox = tk.Listbox(
                                updated_window,
                                height=5,
                                width=50,
                            )
                            for vec in row:
                                text = '{} {}'.format(listos[i], vec)
                                textbox.insert(tk.END, text)
                                i += 1

                            textbox.pack(pady=20)

                # funkce na update prijmeni
                def update_prijmeni2():
                    prijmeni_up = up_prijmeni.get()
                    if not prijmeni_up.isalpha() or prijmeni_up == ' ':
                        up_prijmeni.config(highlightbackground="red", highlightcolor="red")
                        up_prijmeni.delete(0, tk.END)
                    else:
                        up_prijmeni.delete(0, tk.END)
                        up_prijmeni.config(highlightbackground="black", highlightcolor="black")
                        con = sql.connect('example.db')
                        c = con.cursor()
                        c.execute(""" UPDATE osoba SET prijmeni = ? WHERE rodne_cislo = ?""", (prijmeni_up, check_text))
                        con.commit()

                        c.execute(
                            """
                            SELECT * FROM osoba WHERE rodne_cislo = ?
                            """, (check_text,)
                        )
                        updated_window = tk.Toplevel(window2)
                        updated_window.geometry("600x300")
                        updated_window.title("Upravené údaje")
                        for row in c.execute('SELECT * FROM osoba WHERE rodne_cislo = ?', (check_text,)):
                            i = 0
                            textbox = tk.Listbox(
                                updated_window,
                                height=5,
                                width=50,
                            )
                            for vec in row:
                                text = '{} {}'.format(listos[i], vec)
                                textbox.insert(tk.END, text)
                                i += 1

                            textbox.pack(pady=20)

                # funkce na update telefonu
                def update_telefon2():
                    telefon_up = up_telefon.get()
                    num_error = 0
                    if not telefon_up.isdigit():
                        up_telefon.config(highlightbackground="red", highlightcolor="red")
                        num_error += 1
                    if len(telefon_up) != 9:
                        up_telefon.config(highlightbackground="red", highlightcolor="red")
                        num_error += 1
                    if num_error == 0:
                        up_telefon.config(highlightbackground="black", highlightcolor="black")
                        up_telefon.delete(0, tk.END)
                        con = sql.connect('example.db')
                        c = con.cursor()
                        c.execute(""" UPDATE osoba SET telefon = ? WHERE rodne_cislo = ?""", (telefon_up, check_text))
                        con.commit()

                        c.execute(
                            """
                            SELECT * FROM osoba WHERE rodne_cislo = ?
                            """, (check_text,)
                        )
                        updated_window = tk.Toplevel(window2)
                        updated_window.geometry("600x300")
                        updated_window.title("Upravené údaje")
                        for row in c.execute('SELECT * FROM osoba WHERE rodne_cislo = ?', (check_text,)):
                            i = 0
                            textbox = tk.Listbox(
                                updated_window,
                                height=5,
                                width=50,
                            )
                            for vec in row:
                                text = '{} {}'.format(listos[i], vec)
                                textbox.insert(tk.END, text)
                                i += 1

                            textbox.pack(pady=20)

                #funkce na update emailu
                def update_mail2():
                    mail_up = up_mail.get()
                    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                    if not (re.search(regex, mail_up)):
                        up_mail.config(highlightbackground="red", highlightcolor="red")
                    else:
                        up_mail.config(highlightbackground="black", highlightcolor="black")
                        up_mail.delete(0, tk.END)
                        con = sql.connect('example.db')
                        c = con.cursor()
                        c.execute(""" UPDATE osoba SET email = ? WHERE rodne_cislo = ?""", (mail_up, check_text))
                        con.commit()

                        c.execute(
                            """
                            SELECT * FROM osoba WHERE rodne_cislo = ?
                            """, (check_text,)
                        )
                        updated_window = tk.Toplevel(window2)
                        updated_window.geometry("600x300")
                        updated_window.title("Upravené údaje")
                        for row in c.execute('SELECT * FROM osoba WHERE rodne_cislo = ?', (check_text,)):
                            i = 0
                            textbox = tk.Listbox(
                                updated_window,
                                height=5,
                                width=50,
                            )
                            for vec in row:
                                text = '{} {}'.format(listos[i], vec)
                                textbox.insert(tk.END, text)
                                i += 1

                            textbox.pack(pady=20)

                def delete_all2():
                    con = sql.connect('example.db')
                    c = con.cursor()
                    c.execute(""" DELETE FROM osoba WHERE rodne_cislo = ?""", (check_text,))
                    con.commit()

                    updated_window = tk.Tk()
                    updated_window.geometry("400x100")
                    updated_window.title("Upravené údaje")

                    exit_message = tk.Label(
                        updated_window,
                        text='Vaše data byla úspěšně smazána',
                        font=("Helvetica", 18),
                    )

                    exit_message.pack(pady=20)

                    window2.destroy()

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
                    """, (check_text,)
                )
                for row in curr2.execute('SELECT * FROM osoba WHERE rodne_cislo = ?', (check_text,)):
                    i = 0
                    textbox = tk.Listbox(
                        height=5,
                        width=50,
                    )
                    for vec in row:
                        text = '{} {}'.format(listos[i], vec)
                        textbox.insert(tk.END, text)
                        i += 1

                    textbox.pack(pady=20)
                zmena = tk.Label(
                    text='Můžete změnit své údaje',
                    font=("Helvetica", 18),
                )
                zmena.pack()

                jmeno_lbl = tk.Label(
                    text='Jméno',
                    font=("Helvetica", 12),
                )
                jmeno_lbl.pack()
                up_jmeno = tk.Entry(
                    width=30,
                    relief="solid",
                    justify="center",
                    highlightthickness=2
                )
                up_jmeno.pack()
                jmeno_btn = tk.Button(
                    text='Změnit',
                    command=update_jmeno2
                )
                jmeno_btn.pack(pady=10)

                prijmeni_lbl = tk.Label(
                    text='Přijímení',
                    font=("Helvetica", 12),
                )
                prijmeni_lbl.pack()
                up_prijmeni = tk.Entry(
                    width=30,
                    relief="solid",
                    justify="center",
                    highlightthickness=2
                )
                up_prijmeni.pack()
                prijmeni_btn = tk.Button(
                    text='Změnit',
                    command=update_prijmeni2
                )
                prijmeni_btn.pack(pady=10)

                telefon_lbl = tk.Label(
                    text='Telefonní číslo',
                    font=("Helvetica", 12),
                )
                telefon_lbl.pack()
                up_telefon = tk.Entry(
                    width=30,
                    relief="solid",
                    justify="center",
                    highlightthickness=2
                )
                up_telefon.pack()
                telefon_btn = tk.Button(
                    text='Změnit',
                    command=update_telefon2
                )
                telefon_btn.pack(pady=10)

                mail_lbl = tk.Label(
                    text='Email',
                    font=("Helvetica", 12),
                )
                mail_lbl.pack()
                up_mail = tk.Entry(
                    width=30,
                    relief="solid",
                    justify="center",
                    highlightthickness=2
                )
                up_mail.pack()
                mail_btn = tk.Button(
                    text='Změnit',
                    command=update_mail2
                )
                mail_btn.pack(pady=10)

                delete = tk.Button(
                    text='Smazat vše',
                    width=20,
                    command = delete_all2
                )
                delete.pack(pady=10)

        rodnecislo = reg_rc_ent.get()
        jmeno = reg_jmeno_ent.get()
        prijmeni = reg_prijmeni_ent.get()
        email = reg_email_ent.get()
        telcislo = reg_telefon_ent.get()
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        errors_reg = 0

        if not jmeno.isalpha() or jmeno == ' ':
            reg_jmeno_ent.config(highlightbackground = "red", highlightcolor= "red")
            reg_jmeno_ent.delete(0, tk.END)
            errors_reg += 1
        if not prijmeni.isalpha() or prijmeni == ' ':
            reg_prijmeni_ent.config(highlightbackground = "red", highlightcolor="red")
            errors_reg += 1
            reg_prijmeni_ent.delete(0, tk.END)
        if not (re.search(regex, email)):
            reg_email_ent.config(highlightbackground = "red", highlightcolor= "red")
            errors_reg += 1
            reg_email_ent.delete(0, tk.END)
        if errors_reg == 0:
            con = sql.connect('example.db')
            c = con.cursor()
            c.execute(""" INSERT INTO osoba(rodne_cislo, jmeno, prijmeni, email, telefon) VALUES(?,?,?,?,?) """, (rodnecislo, jmeno, prijmeni, email, telcislo, ))
            con.commit()

            window2.destroy()
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
                justify="center",
                highlightthickness=2
            )
            rodnycislo.pack()

            label_tel = tk.Label(
                text='Telefonní číslo'
            )
            label_tel.pack()

            telefon = tk.Entry(
                width=40,
                relief="solid",
                justify="center",
                highlightthickness=2
            )
            telefon.pack()

            odeslat = tk.Button(
                width=15,
                height=1,
                text="PŘIHLÁSIT",
                relief="solid",
                command=send_2
            )
            odeslat.pack(pady=10)

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
            justify="center",
            highlightthickness=2
        )
        reg_rc_ent.pack()
        reg_rc_ent.insert(0, insert_rodny)
        reg_rc_ent.configure(state='disabled')

        jmeno_lbl = tk.Label(
            text='Jméno'
        )
        jmeno_lbl.pack()

        reg_jmeno_ent = tk.Entry(
            width=20,
            relief="solid",
            justify="center",
            highlightthickness=2
        )
        reg_jmeno_ent.pack()

        prijmeni_lbl = tk.Label(
            text='Příjmení'
        )
        prijmeni_lbl.pack()

        reg_prijmeni_ent = tk.Entry(
            width=20,
            relief="solid",
            justify="center",
            highlightthickness=2
        )
        reg_prijmeni_ent.pack()

        email_lbl = tk.Label(
            text='Email'
        )
        email_lbl.pack()

        reg_email_ent = tk.Entry(
            width=20,
            relief="solid",
            justify="center",
            highlightthickness=2
        )
        reg_email_ent.pack()

        label_tel = tk.Label(
            text='Telefonní číslo',
        )
        label_tel.pack()

        reg_telefon_ent = tk.Entry(
            width=20,
            relief="solid",
            justify="center",
            highlightthickness=2
        )
        reg_telefon_ent.pack()
        reg_telefon_ent.insert(0, insert_tel)
        reg_telefon_ent.configure(state='disabled')

        odeslat = tk.Button(
            width=15,
            height=2,
            text="REGISTROVAT",
            relief="solid",
            command=reg_final
        )
        odeslat.pack(pady=10)

    else:
        rodnycislo.config(highlightbackground = "red", highlightcolor= "red")

# funkce na kontrolu dat při registraci
def register():
    error = 0
    text = rodnycislo.get()
    #rodnycislo.delete(0, tk.END)
    text_tel = telefon.get()
    #telefon.delete(0, tk.END)
    if len(text) == 0 or len(text_tel) == 0:
        error += 1
        rodnycislo.config(highlightbackground = "red", highlightcolor= "red")
        telefon.delete(0, tk.END)
    if len(text) != 10 and len(text) != 11:
        error += 1
        rodnycislo.config(highlightbackground = "red", highlightcolor= "red")
        telefon.delete(0, tk.END)
    if len(text_tel) != 9:
        error += 1
        telefon.config(highlightbackground = "red", highlightcolor= "red")
        telefon.delete(0, tk.END)
    if len(text) == 11:
        cs = len(text)
        print(cs)
        if text.find("/") != 6:
            error += 1
            rodnycislo.config(highlightbackground = "red", highlightcolor= "red")
            rodnycislo.delete(0, tk.END)
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
            rodnycislo.config(highlightbackground = "red", highlightcolor= "red")
            rodnycislo.delete(0, tk.END)
    if len(text) == 10:
        cs = len(text)
        print(cs)
        if text.find("/") != 6:
            error += 1
            rodnycislo.config(highlightbackground="red", highlightcolor="red")
            rodnycislo.delete(0, tk.END)
        else:
            text.replace("\n", "")
            text2 = text.replace("/", "")
            pocet = len(text2)
            print(text2)
            strtext = str(text2)
            rok = strtext[0] + strtext[1]
            if 46 <= int(rok) <= 54:
                print('ok')
            else:
                error += 1
                rodnycislo.config(highlightbackground="red", highlightcolor="red")
                rodnycislo.delete(0, tk.END)
    if error == 0:
        reg_continue(text, text_tel)

#funkce na odesílání dat při přihlášení
def send():
    text = rodnycislo.get()
    text_tel = telefon.get()
    check(text, text_tel)

#funkce na výpis dat při správném zapsání údajů
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
        rodnycislo.config(highlightbackground="red", highlightcolor="red")
        telefon.config(highlightbackground="red", highlightcolor="red")
    else:

        # funkce pro update jména
        def update_jmeno():
            jmeno_up = up_jmeno.get()
            if not jmeno_up.isalpha() or jmeno_up == ' ':
                up_jmeno.delete(0, tk.END)
                up_jmeno.config(highlightbackground="red", highlightcolor="red")
            else:
                up_jmeno.config(highlightbackground="black", highlightcolor="black")
                up_jmeno.delete(0, tk.END)
                con = sql.connect('example.db')
                c = con.cursor()
                c.execute(""" UPDATE osoba SET jmeno = ? WHERE rodne_cislo = ?""",(jmeno_up, check_text))
                con.commit()

                # výpis po updatu jména
                c.execute(
                    """
                    SELECT * FROM osoba WHERE rodne_cislo = ?
                    """,(check_text,)
                )
                updated_window = tk.Toplevel(window2)
                updated_window.geometry("600x300")
                updated_window.title("Upravené údaje")
                for row in c.execute('SELECT * FROM osoba WHERE rodne_cislo = ?',(check_text,)):
                    i = 0
                    textbox = tk.Listbox(
                        updated_window,
                        height=5,
                        width= 50,
                    )
                    for vec in row:
                        text = '{} {}'.format(listos[i], vec)
                        textbox.insert(tk.END, text)
                        i += 1

                    textbox.pack(pady=20)

        # funkce na update prijmeni
        def update_prijmeni():
            prijmeni_up = up_prijmeni.get()
            if not prijmeni_up.isalpha() or prijmeni_up == ' ':
                up_prijmeni.config(highlightbackground="red", highlightcolor="red")
                up_prijmeni.delete(0, tk.END)
            else:
                up_prijmeni.delete(0, tk.END)
                up_prijmeni.config(highlightbackground="black", highlightcolor="black")
                con = sql.connect('example.db')
                c = con.cursor()
                c.execute(""" UPDATE osoba SET prijmeni = ? WHERE rodne_cislo = ?""", (prijmeni_up, check_text))
                con.commit()

                # výpis po updatu prijmeni
                c.execute(
                    """
                    SELECT * FROM osoba WHERE rodne_cislo = ?
                    """, (check_text,)
                )
                updated_window = tk.Toplevel(window2)
                updated_window.geometry("600x300")
                updated_window.title("Upravené údaje")
                for row in c.execute('SELECT * FROM osoba WHERE rodne_cislo = ?', (check_text,)):
                    i = 0
                    textbox = tk.Listbox(
                        updated_window,
                        height=5,
                        width=50,
                    )
                    for vec in row:
                        text = '{} {}'.format(listos[i], vec)
                        textbox.insert(tk.END, text)
                        i += 1

                    textbox.pack(pady=20)
        # funkce na update telefonního čísla
        def update_telefon():
            telefon_up = up_telefon.get()
            num_error = 0
            if not telefon_up.isdigit():
                up_telefon.config(highlightbackground="red", highlightcolor="red")
                num_error += 1
            if len(telefon_up) != 9:
                up_telefon.config(highlightbackground="red", highlightcolor="red")
                num_error += 1
            if num_error == 0:
                up_telefon.config(highlightbackground="black", highlightcolor="black")
                up_telefon.delete(0, tk.END)
                con = sql.connect('example.db')
                c = con.cursor()
                c.execute(""" UPDATE osoba SET telefon = ? WHERE rodne_cislo = ?""", (telefon_up, check_text))
                con.commit()

                # výpis po updatu telefonu
                c.execute(
                    """
                    SELECT * FROM osoba WHERE rodne_cislo = ?
                    """, (check_text,)
                )
                updated_window = tk.Toplevel(window2)
                updated_window.geometry("600x300")
                updated_window.title("Upravené údaje")
                for row in c.execute('SELECT * FROM osoba WHERE rodne_cislo = ?', (check_text,)):
                    i = 0
                    textbox = tk.Listbox(
                        updated_window,
                        height=5,
                        width=50,
                    )
                    for vec in row:
                        text = '{} {}'.format(listos[i], vec)
                        textbox.insert(tk.END, text)
                        i += 1

                    textbox.pack(pady=20)

        def update_mail():
            mail_up = up_mail.get()
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not (re.search(regex, mail_up)):
                up_mail.config(highlightbackground="red", highlightcolor="red")
            else:
                up_mail.config(highlightbackground="black", highlightcolor="black")
                up_mail.delete(0, tk.END)
                con = sql.connect('example.db')
                c = con.cursor()
                c.execute(""" UPDATE osoba SET email = ? WHERE rodne_cislo = ?""", (mail_up, check_text))
                con.commit()

                #výpis po updatu emailu
                c.execute(
                    """
                    SELECT * FROM osoba WHERE rodne_cislo = ?
                    """, (check_text,)
                )
                updated_window = tk.Toplevel(window2)
                updated_window.geometry("600x300")
                updated_window.title("Upravené údaje")
                for row in c.execute('SELECT * FROM osoba WHERE rodne_cislo = ?', (check_text,)):
                    i = 0
                    textbox = tk.Listbox(
                        updated_window,
                        height=5,
                        width=50,
                    )
                    for vec in row:
                        text = '{} {}'.format(listos[i], vec)
                        textbox.insert(tk.END, text)
                        i += 1

                    textbox.pack(pady=20)

        #funkce na vymazání dat
        def delete_all():
            con = sql.connect('example.db')
            c = con.cursor()
            c.execute(""" DELETE FROM osoba WHERE rodne_cislo = ?""", (check_text,))
            con.commit()

            updated_window = tk.Tk()
            updated_window.geometry("400x100")
            updated_window.title("Upravené údaje")

            exit_message = tk.Label(
                updated_window,
                text='Vaše data byla úspěšně smazána',
                font = ("Helvetica", 18),
            )

            exit_message.pack(pady=20)

            window2.destroy()


        print("existuje")
        window.destroy()
        con2 = sql.connect('example.db')
        cur2 = con.cursor()
        curr2 = con.cursor()
        window2 = tk.Tk()
        window2.geometry("600x600")
        window2.title("Vaše údaje")

        listos = ('Rodné číslo:', 'Jméno:', 'Příjmení:', 'Email:', 'Telefon:')

        # výpis uživatelových dat a možností úprav dat

        curr2.execute(
            """
            SELECT * FROM osoba WHERE rodne_cislo = ?
            """,(check_text,)
        )
        for row in curr2.execute('SELECT * FROM osoba WHERE rodne_cislo = ?',(check_text,)):
            i = 0
            textbox = tk.Listbox(
                height=5,
                width= 50,
            )
            for vec in row:
                text = '{} {}'.format(listos[i], vec)
                textbox.insert(tk.END, text)
                i += 1

            textbox.pack(pady=20)

        zmena = tk.Label(
            text='Můžete změnit své údaje',
            font=("Helvetica", 18),
        )
        zmena.pack()

        jmeno_lbl = tk.Label(
            text='Jméno',
            font=("Helvetica", 12),
        )
        jmeno_lbl.pack()
        up_jmeno = tk.Entry(
            width=30,
            relief="solid",
            justify="center",
            highlightthickness=2
        )
        up_jmeno.pack()
        jmeno_btn = tk.Button(
            text='Změnit',
            command=update_jmeno
        )
        jmeno_btn.pack(pady=10)

        prijmeni_lbl = tk.Label(
            text='Přijímení',
            font=("Helvetica", 12),
        )
        prijmeni_lbl.pack()
        up_prijmeni = tk.Entry(
            width=30,
            relief="solid",
            justify="center",
            highlightthickness=2
        )
        up_prijmeni.pack()
        prijmeni_btn = tk.Button(
            text='Změnit',
            command=update_prijmeni
        )
        prijmeni_btn.pack(pady=10)

        telefon_lbl = tk.Label(
            text='Telefonní číslo',
            font=("Helvetica", 12),
        )
        telefon_lbl.pack()
        up_telefon = tk.Entry(
            width=30,
            relief="solid",
            justify="center",
            highlightthickness=2
        )
        up_telefon.pack()
        telefon_btn = tk.Button(
            text='Změnit',
            command=update_telefon
        )
        telefon_btn.pack(pady=10)

        mail_lbl = tk.Label(
            text='Email',
            font=("Helvetica", 12),
        )
        mail_lbl.pack()
        up_mail = tk.Entry(
            width=30,
            relief="solid",
            justify="center",
            highlightthickness=2
        )
        up_mail.pack()
        mail_btn = tk.Button(
            text='Změnit',
            command=update_mail
        )
        mail_btn.pack(pady=10)

        delete = tk.Button(
            text='Smazat vše',
            width=20,
            command=delete_all
        )
        delete.pack(pady=10)


# tkinter pro registraci a prihlaseni (základní okno)
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
    justify="center",
    highlightthickness=2
)
rodnycislo.pack()

label_tel = tk.Label(
    text='Telefonní číslo'
)
label_tel.pack()

telefon = tk.Entry(
    width=40,
    relief="solid",
    justify="center",
    highlightthickness=2
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


