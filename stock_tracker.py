stock_prices = {
    "AAPL": 1802,
    "TSLA": 2408,
    "MSFT": 4205,
    "GOOG": 1756,
    "AMZN": 1858
}

def calculate_total_investment(investments, prices):
    """
    Calculates the total investment value based on quantities and prices.
    Returns the total investment and a list of detailed investment lines.
    """
    total_value = 0
    investment_details = []
    
    investment_details.append("--- Investment Summary ---")
    investment_details.append(f"{'Stock':<10} {'Quantity':<10} {'Price':<10} {'Value':<10}")
    investment_details.append("-" * 40)

    for stock, quantity in investments.items():
        if stock in prices:
            price_per_share = prices[stock]
            stock_value = quantity * price_per_share
            total_value += stock_value
            investment_details.append(f"{stock:<10} {quantity:<10} ${price_per_share:<9.2f} ${stock_value:<9.2f}")
        else:
            investment_details.append(f"{stock:<10} {quantity:<10} {'N/A':<10} {'N/A':<10} (Price not found)")
            print(f"Warning: Price for {stock} not found in our hardcoded list.")
    
    investment_details.append("-" * 40)
    investment_details.append(f"Total Investment: ${total_value:.2f}")
    
    return total_value, investment_details

def save_results_to_file(details, filename="investment_summary.txt"):
    """
    Writes the investment summary to a specified file.
    """
    try:
        with open(filename, 'w') as f:
            for line in details:
                f.write(line + '\n')
        print(f"\nInvestment summary saved to {filename}")
    except IOError:
        print(f"Error: Could not save file to {filename}")

# Main execution flow (simulated user input)
if __name__ == "__main__":
    # Simulate user input for investments
    # Format: {"STOCK_SYMBOL": QUANTITY, ...}
    simulated_user_investments = {
        "AAPL": 10,
        "MSFT": 5,
        "TSLA": 3,
        "GOOG": 7,
        "XYZ": 2 # Example of a stock not in our hardcoded prices
    }

    print("Simulating the following stock investments:")
    for stock, quantity in simulated_user_investments.items():
        print(f"- {stock}: {quantity} shares")
    
    total_investment_value, investment_summary_lines = calculate_total_investment(
        simulated_user_investments, stock_prices
    )
    
    # Display the summary to the user
    for line in investment_summary_lines:
        print(line)
    
    # Automatically save results to a file
    save_results_to_file(investment_summary_lines)