# Unit test for data_processing.py
def test_get_column_types():
    import pandas as pd
    from Src.data_processing import get_column_types

    # Sample DataFrame
    data = {
        "Category": ["A", "B", "C"],
        "Value": [1.5, 2.3, 3.7],
    }
    df = pd.DataFrame(data)

    # Call the function
    categorical_columns, numerical_columns = get_column_types(df)

    # Assertions
    assert categorical_columns == ["Category"]
    assert numerical_columns == ["Value"]