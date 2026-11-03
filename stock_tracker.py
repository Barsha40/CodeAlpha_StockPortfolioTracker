
import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock name! Try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity

    total_investment += investment

    portfolio.append([
        stock_name,
        quantity,
        price,
        investment
    ])

    print(f"Investment in {stock_name}: ${investment}")

# Display portfolio
print("\n========== PORTFOLIO SUMMARY ==========")

for stock, quantity, price, investment in portfolio:
    print(f"{stock} | Quantity: {quantity} | "
          f"Price: ${price} | Value: ${investment}")

print("---------------------------------------")
print(f"Total Investment: ${total_investment}")

# Save data to CSV
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Stock Name",
        "Quantity",
        "Price",
        "Investment Value"
    ])

    writer.writerows(portfolio)

    writer.writerow(["", "", "Total", total_investment])

print("\nPortfolio saved successfully in portfolio.csv")
