"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.7
"""
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn import metrics
import logging


def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> KNeighborsClassifier:
    clf = KNeighborsClassifier()
    clf.fit(X_train, y_train)
    return clf


def evaluate_model(clf: KNeighborsClassifier, X_test: pd.DataFrame, y_test: pd.Series):
    y_pred = clf.predict(X_test)
    accuracy = metrics.accuracy_score(y_pred, y_test)
    logger = logging.getLogger(__name__)
    logger.info("Model has a accuracy score of %.3f on test data.", accuracy)
