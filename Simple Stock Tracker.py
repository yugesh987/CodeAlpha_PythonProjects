# Simple Stock Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190
}

total_investment = 0

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stock_prices:
    price = stock_prices[stock_name]
    investment = price * quantity
    total_investment += investment

    print("\nStock:", stock_name)
    print("Price per share: $", price)
    print("Quantity:", quantity)
    print("Investment value: $", investment)
    print("Total Investment: $", total_investment)

    # Save result to a text file
    with open("stock_tracker.txt", "w") as file:
        file.write("Stock: " + stock_name + "\n")
        file.write("Quantity: " + str(quantity) + "\n")
        file.write("Total Investment: $" + str(total_investment))

    print("\nResult saved in stock_tracker.txt")

else:
    print("Stock not found!")