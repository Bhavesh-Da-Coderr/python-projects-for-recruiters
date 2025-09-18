import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fetch_stock(symbol="AAPL", period="6mo"):
    data = yf.download(symbol, period=period)
    return data

def predict_stock(data):
    data = data.reset_index()
    data["Days"] = range(len(data))
    X = data[["Days"]]
    y = data["Close"]

    model = LinearRegression().fit(X, y)
    future = pd.DataFrame({"Days": range(len(data), len(data)+30)})
    preds = model.predict(future)
    return preds

if __name__ == "__main__":
    symbol = input("Enter stock symbol (e.g. AAPL, TSLA): ").strip().upper()
    data = fetch_stock(symbol)
    print(data.tail()) # pyright: ignore[reportOptionalMemberAccess]

    preds = predict_stock(data)

    plt.plot(data["Close"], label="Historical") # type: ignore
    plt.plot(range(len(data), len(data)+30), preds, label="Prediction") # pyright: ignore[reportArgumentType]
    plt.title(f"{symbol} Price Prediction")
    plt.legend()
    plt.show()
