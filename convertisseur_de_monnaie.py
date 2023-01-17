#script réalisé avec Remi Vidal-Michel
#import
from tkinter import *
from tkinter import ttk

#dict
RATE_CURR={
    "EUR":1,
    "USD":1.08,
    "GBP":0.89,
    "JPY":138.88
}

#colors
blue = "#88d7ff"
white = "#ffffff"

#window
window = Tk()
window.geometry("300x280")
window.title("Convert")
window.resizable(height=False, width=False)

#function
def convert():
    currency1 = menu1.get()
    currency2 = menu2.get()
    amount = value.get()
    output = float(amount)*(float(RATE_CURR[currency2])/float(RATE_CURR[currency1]))
    result.config(text=round(output, 2))

#gui
value_txt = Label(window, text="AMOUNT")
value_txt.place(x=40, y=20)
value = Entry(window, relief="solid", justify=CENTER, width=10)
value.place(x=40, y=40)

currency = ['EUR', 'USD', 'GBP', 'JPY']

menu1_txt = Label(window, text="FROM")
menu1_txt.place(x=190, y=20)
menu1 = ttk.Combobox(window, justify=CENTER, width=7)
menu1["values"] = (currency)
menu1.place(x=190, y=38)

menu2_txt = Label(window, text="TO")
menu2_txt.place(x=40, y=100)
menu2 = ttk.Combobox(window, justify=CENTER, width=7)
menu2["values"] = (currency)
menu2.place(x=40, y=118)

button = Button(window, text="Convert", width=8, bg=blue, command=convert)
button.place(x=190, y=112)

result = Label(window, text="", relief="solid", width=30, height=2, bg=white)
result.place(x=40, y=200)

window.mainloop()
