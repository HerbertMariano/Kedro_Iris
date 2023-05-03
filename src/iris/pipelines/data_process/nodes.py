"""
This is a boilerplate pipeline 'data_process'
generated using Kedro 0.18.7
"""
import pandas as pd
from sklearn.model_selection import train_test_split


def process_iris(iris_data: pd.DataFrame) -> pd.DataFrame:
    iris_data = iris_data.dropna()
    iris_data.drop(["Id"], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(
        iris_data.drop(["Species"], axis=1),
        iris_data["Species"],
        test_size=0.33,
        random_state=42,
    )
    return X_train, X_test, y_train, y_test
