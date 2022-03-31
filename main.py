from tkinter import *
import requests
import json

pycrypto = Tk()
pycrypto.title("my crypto portfolio")
img = PhotoImage(file='giphy.gif')
pycrypto.tk.call('wm', 'iconphoto', pycrypto._w, img)


def font_color(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"    

def my_portfolio():

    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=3889ce63-c733-403d-8b7d-c41a2438b4ea")
    api = json.loads(api_request.content)

    coins =[
        {
            "symbol":"BTC",
            "amount_owned":2,
            "price_per_coin":3200
        },
        {
            "symbol":"EOS",
            "amount_owned":100,
            "price_per_coin":2.75
        },
        {
            "symbol":"LTC",
            "amount_owned":75,
            "price_per_coin":25
        },
        {    
            "symbol":"XMR",
            "amount_owned":10,
            "price_per_coin":48.05
        }    
    ]

    total_pl = 0
    coin_row = 1
    total_current_value = 0

    for i in range(0, 300):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                total_paid = coin["amount_owned"] * coin["price_per_coin"]
                current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
                pl_percoin = api["data"][i]["quote"]["USD"]["price"]-coin["price_per_coin"]
                total_per_coin = pl_percoin* coin["amount_owned"]

                total_pl = total_pl + total_per_coin
                total_current_value = total_current_value + current_value

                name = Label(pycrypto, text = api["data"][i]["symbol"], bg = "#F3F4F6", fg ="black", font = "lato 12", borderwidth= 2, relief= "groove", padx= "2", pady= "2")
                name.grid(row = coin_row, column = 0, sticky = N+S+E+W)

                price = Label(pycrypto, text = "${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"], bg = "black", fg = "black", font = "lato 12", borderwidth= 2, relief= "groove", padx= "2", pady= "2"))
                price.grid(row = coin_row, column = 1, sticky = N+S+E+W)

                no_coins = Label(pycrypto, text = coin["amount_owned"], bg = "#F3F4F6", fg = "black", font="lato 12", borderwidth= 2, relief= "groove",padx= "2", pady= "2")
                no_coins.grid(row = coin_row, column = 2, sticky = N+S+E+W)

                amount_paid = Label(pycrypto, text = total_paid, bg = "#F3F4F6", fg = "black", font = "lato 12", borderwidth= 2, relief= "groove", padx= "2", pady= "2" )
                amount_paid.grid(row = coin_row, column = 3, sticky = N+S+E+W)

                current_value = Label(pycrypto, text = "${0:.2f}".format(current_value), bg ="#F3F4F6", fg = "black", font = "lato 12", borderwidth= 2, relief= "groove", padx= "2", pady= "2")
                current_value.grid(row = coin_row, column = 4, sticky = N+S+E+W)

                pl_coin = Label(pycrypto, text = "${0:.2f}".format(pl_percoin), bg = "#F3F4F6", fg = "black", font = font_color(float("{0:.2f}".format(pl_percoin))), borderwidth= 2, relief= "groove", padx= "2", pady= "2")
                pl_coin.grid(row = coin_row, column = 5, sticky = N+S+E+W)

                totalpl = Label(pycrypto, text = "${0:.2f}".format(total_per_coin), bg = "#F3F4F6", fg = "black", font = font_color(float("{0:.2f}".format(total_per_coin))), borderwidth= 2, relief= "groove", padx= "2", pady= "2")
                totalpl.grid(row = coin_row, column = 6, sticky = N+S+E+W)

                coin_row = coin_row + 1

                total_cv = Label(pycrypto, text = "${0:.2f}".format(total_current_value), bg = "#F3F4F6", fg= font_color(float("{0:.2f}".format(total_pl))))
                total_cv.grid(row = coin_row, column = 4, sticky= N+S+E+W)

                totalpl = Label(pycrypto, text = "${0:.2f}".format(total_pl), bg = "#F3F4F6")
                totalpl.grid(row = coin_row, column = 6, sticky= N+S+E+W)

                update = Button(pycrypto, text = "update", bg= "#142E54", fg= "white", command = my_portfolio, font= "lato 12", borderwidth= 2, relief= "groove", padx= "2", pady="2")
                update.grid(row= coin_row + 1, column= 6, sticky= N+S+E+W)

    name = Label(pycrypto, text = "coin name", bg = "#142E54", fg ="white",font = "lato 12 bold", padx= "2", pady= "2", borderwidth= 2, relief= "groove")
    name.grid(row = 0, column = 0, sticky = N+S+E+W)

    price = Label(pycrypto, text = "price", bg = "#142E54", fg = "white", font = "lato 12 bold", padx= "2", pady= "2", borderwidth= 2, relief= "groove")
    price.grid(row = 0, column = 1, sticky = N+S+E+W)

    no_coins = Label(pycrypto, text = "coin owned", bg = "#142E54", fg = "white", font = "lato 12 bold", padx= "2", pady= "2", borderwidth= 2, relief= "groove")
    no_coins.grid(row = 0, column = 2, sticky = N+S+E+W)

    amount_paid = Label(pycrypto, text = "total amount paid", bg = "#142E54", fg = "white", font = "lato 12 bold", padx= "2", pady= "2", borderwidth= 2, relief= "groove")
    amount_paid.grid(row = 0, column = 3, sticky = N+S+E+W)


    current_value = Label(pycrypto, text = "current value paid", bg = "#142E54", fg = "white", font = "lato 12 bold", padx= "2", pady= "2", borderwidth= 2, relief= "groove")
    current_value.grid(row = 0, column = 4, sticky = N+S+E+W)

    # current_val = Label(pycrypto, text="${0:.2f}".format(current_value), bg="#F3F4F6", fg="black", font="Lato 12", borderwidth=2, relief="groove", padx="2", pady="2")
    # current_val.grid(row=coin_row, column=5, sticky=N+S+E+W)

    pl_coin = Label(pycrypto, text = "p/l per coin", bg = "#142E54", fg = font_color(float("{0:.2f}".format(pl_percoin))), font = "lato 12 bold", padx= "2", pady= "2", borderwidth= 2, relief= "groove")
    pl_coin.grid(row = 0, column = 5, sticky = N+S+E+W)

    totalpl = Label(pycrypto, text = "total p/l with coin", bg = "#142E54", fg = font_color(float("{0:.2f}".format(total_per_coin))), font = "lato 12 bold", padx= "2", pady= "2", borderwidth= 2, relief= "groove")
    totalpl.grid(row = 0, column = 6, sticky = N+S+E+W)

    pycrypto.mainloop()
    print("program completed")

my_portfolio()



