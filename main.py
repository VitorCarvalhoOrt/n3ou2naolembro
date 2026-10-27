from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def main():
    data_path = Path(__file__).resolve().parent / "Maths.csv"
    df = pd.read_csv(data_path).drop_duplicates()

    y = df["G3"]
    X = pd.get_dummies(df.drop(columns=["G3"]), drop_first=True, dtype=int)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    print("R²:", r2_score(y_test, y_pred))
    print("MSE:", mse)
    print("RMSE:", mse**0.5)


if __name__ == "__main__":
    main()
