"""
This is a boilerplate pipeline 'data_process'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import process_iris


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=process_iris,
                inputs="iris_data",
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="preprocess_iris_node",
            ),
        ]
    )
