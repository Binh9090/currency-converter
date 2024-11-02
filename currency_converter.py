import requests

# Thay YOUR_API_KEY bằng API key của bạn
API_KEY = "db8f9bcff8936e9f1d7a8b8a"
BASE_URL = "https://v6.exchangerate-api.com/v6"  # Đổi link nếu bạn dùng API khác

def get_exchange_rate(from_currency, to_currency):
    url = f"{BASE_URL}/{API_KEY}/pair/{from_currency}/{to_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data["result"] == "success":
        return data["conversion_rate"]
    else:
        print("Error fetching exchange rate.")
        return None

def main():
    print("Currency Converter")
    from_currency = input("Enter the currency you have (e.g., USD): ").upper()
    to_currency = input("Enter the currency you want (e.g., VND): ").upper()
    amount = float(input("Enter the amount: "))

    rate = get_exchange_rate(from_currency, to_currency)

    if rate:
        converted_amount = amount * rate
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        print("Conversion failed. Please try again later.")

if __name__ == "__main__":
    main()
