import numpy as np
import matplotlib.pyplot as plt

balance = 10000

stocks = {
    "TCS": 2400,
    "Reliance": 1400,
    "HDFC": 800,
    "Infosys": 1300,
    "ITC": 300
}

portfolio = {}
portfolio_history = []


def update_prices():
    for stock in stocks:

        change_percent = np.random.normal(0, 0.02)

        new_price = stocks[stock] * (1 + change_percent)

        stocks[stock] = round(new_price, 2)


def show_stocks():

    print("\nCurrent Market Prices ")

    for stock, price in stocks.items():
        print(stock, ":", price)


def buy_stock():

    global balance

    stock = input("Enter stock name: ")

    if stock not in stocks:
        print("Stock not available")
        return

    qty = int(input("Enter quantity: "))

    cost = stocks[stock] * qty

    if cost > balance:
        print("Not enough balance")
        return

    balance -= cost

    portfolio[stock] = {
        "qty": portfolio.get(stock, {}).get("qty", 0) + qty,
        "buy_price": stocks[stock]
    }

    print("Stock bought successfully")


def sell_stock():

    global balance

    stock = input("Enter stock name: ")

    if stock not in portfolio:
        print("You don't own this stock")
        return

    qty = int(input("Enter quantity: "))

    if qty > portfolio[stock]["qty"]:
        print("Not enough shares")
        return

    sell_price = stocks[stock]
    buy_price = portfolio[stock]["buy_price"]

    profit_loss = (sell_price - buy_price) * qty

    balance += sell_price * qty

    portfolio[stock]["qty"] -= qty

    if portfolio[stock]["qty"] == 0:
        del portfolio[stock]

    print("Trade Result:", round(profit_loss,2))


def show_portfolio():

    total_value = 0

    print("\nYour Portfolio ")

    for stock, data in portfolio.items():

        current_price = stocks[stock]

        value = current_price * data["qty"]

        pnl = (current_price - data["buy_price"]) * data["qty"]

        total_value += value

        print(stock,
              "Qty:", data["qty"],
              "Buy:", data["buy_price"],
              "Current:", current_price,
              "P/L:", round(pnl,2))

    portfolio_history.append(total_value)

    print("Total Portfolio Value:", round(total_value,2))


def show_graph():

    if len(portfolio_history) == 0:
        print("No data yet")
        return

    plt.plot(portfolio_history)

    plt.title("Portfolio Value Over Time")

    plt.xlabel("Trades")

    plt.ylabel("Value")

    plt.show()


while True:

    update_prices()

    print("\nBalance:", round(balance,2))

    print("""
1 View Market Prices
2 Buy Stock
3 Sell Stock
4 View Portfolio
5 Portfolio Graph
6 Exit
""")

    choice = input("Choose option: ")

    if choice == "1":
        show_stocks()

    elif choice == "2":
        buy_stock()

    elif choice == "3":
        sell_stock()

    elif choice == "4":
        show_portfolio()

    elif choice == "5":
        show_graph()

    elif choice == "6":
        break