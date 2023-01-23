#script réalisé avec Remi Vidal-Michel
#import de la librairie graphique
from tkinter import *
from tkinter import ttk

#création d'un dictionnaire qui associe une devise à son taux de change ex : 1€ = 1.08$
rates={
    "EUR":1,
    "USD":1.08,
    "GBP":0.89,
    "JPY":140.92
}

#variables couleurs
blue = "#88d7ff"
white = "#ffffff"
red = "#b60000"
cyan = "#9effe3"
green = "#149c00"

#paramètres de la fenêtre tkinter
window = Tk()
window.geometry("290x300")
window.title("Convert")
window.resizable(height=False, width=False)

#les fonctions
def convert():
    currency1 = menu1.get()
    currency2 = menu2.get()
    try:
        amount = float(value.get())
        if type(amount) == float:
            fail.config(text="")
    except:
        fail.config(text="Please enter the amount as a number", fg=red)
    try:
        if currency1 not in rates or currency2 not in rates:
            fail.config(text="Please ADD the currency", fg=red)
    except:
        fail.config(text="")
    try:
        if currency1 == "" or currency2 == "":
            fail.config(text="Please write the new currency", fg=red)
    except:
        fail.config(text="")
    output = float(amount)*(float(rates[currency2])/float(rates[currency1]))
    result.config(text=round(output, 2))
    historic.insert(END ,(amount, currency1, "=", round(output, 2), currency2))

def add1():
    try:
        var_rate1 = float(rate1.get())
        if type(var_rate1) == float:
            fail.config(text="")
    except:
        fail.config(text="Please enter a number for the 1st rate", fg=red)
    if menu1.get() not in rates and menu1.get() != "":
        rates.update({menu1.get():var_rate1})
        fail.config(text="ADDED!", fg=green)
        print(rates)
        menu1["values"] = [i for i in rates]
        menu2["values"] = [i for i in rates]
    elif menu1.get() == "" :
        fail.config(text="Please write the new currency", fg=red)
    else:
        fail.config(text="This currency is already in the database", fg=red)

def add2():
    try:
        var_rate2 = float(rate2.get())
        if type(var_rate2) == float:
            fail.config(text="")
    except:
        fail.config(text="Please enter a number for the 2nd rate", fg=red)
    if menu2.get() not in rates and menu2.get() != "":
        rates.update({menu2.get():var_rate2})
        fail.config(text="ADDED!", fg=green)
        menu1["values"] = [i for i in rates]
        menu2["values"] = [i for i in rates]
    elif menu2.get() == "" :
        fail.config(text="Please write the new currency", fg=red)
    else:
        fail.config(text="This currency is already in the database", fg=red)

#gui
value_txt = Label(window, text="AMOUNT")
value_txt.place(x=40, y=20)
value = Entry(window, relief="solid", justify=CENTER, width=10)
value.place(x=40, y=40)

fail = Label(window, text="")
fail.place(x=37, y=172)

btn_add1 = Button(window, text="ADD", width=18, bg=cyan, command=add1)
btn_add1.place(x=110, y=65)

btn_add2 = Button(window, text="ADD", width=18, bg=cyan, command=add2)
btn_add2.place(x=110, y=145)

menu1_txt = Label(window, text="FROM")
menu1_txt.place(x=110, y=20)
menu1 = ttk.Combobox(window, justify=CENTER, width=7)
menu1["values"] = [i for i in rates]
menu1.place(x=110, y=39)

menu2_txt = Label(window, text="TO")
menu2_txt.place(x=110, y=100)
menu2 = ttk.Combobox(window, justify=CENTER, width=7)
menu2["values"] = [i for i in rates]
menu2.place(x=110, y=119)

btn_conv = Button(window, text="Convert", width=8, bg=blue, command=convert)
btn_conv.place(x=40, y=116)

rate1_txt = Label(window, text="RATE")
rate1_txt.place(x=180, y=20)
rate1 = Entry(window, relief="solid", justify=CENTER, width=10)
rate1.place(x=180, y=40)

rate2_txt = Label(window, text="RATE")
rate2_txt.place(x=180, y=100)
rate2 = Entry(window, relief="solid", justify=CENTER, width=10)
rate2.place(x=180, y=120)

historic = Listbox(window, width=34, height=2, justify=CENTER)
historic.place(x=40, y=250)

result = Label(window, text="", relief="solid", width=29, height=2, bg=white)
result.place(x=40, y=200)

window.mainloop()