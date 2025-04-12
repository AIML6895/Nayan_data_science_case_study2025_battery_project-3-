# Integration test for main.py
def test_main():
    import os
    from main import main

    # Sample UI parameters
    ui_parameters = {
        "anomaly_removal": {
            "group_col": "cell_index",
            "threshold": 1.5
        },
        "save_cleaned_data": True,
        "cleaned_data_path": "test_cleaned_data.csv",
        "plotting": {
            "x_col": "discharge_capacity",
            "y_col": "voltage",
            "color_col": "cycle_index",
            "save_path": "test_scatter_plot.png",
            "title": "Test Plot"
        }
    }

    # Sample DataFrame
    import pandas as pd
    data = {
        "cell_index": [1, 1, 1, 2, 2],
        "discharge_capacity": [1.0, 1.1, 10.0, 0.9, 1.2],
        "voltage": [3.7, 3.6, 3.8, 3.5, 3.4],
        "cycle_index": [1, 2, 3, 1, 2]
    }
    df = pd.DataFrame(data)

    # Mock file path
    file_path = "test_data.parquet"

    # Save DataFrame to Parquet file
    df.to_parquet(file_path)

    # Run the main function
    main(file_path, ui_parameters)

    # Check if cleaned data file and plot were created
    assert os.path.exists("test_cleaned_data.csv")
    assert os.path.exists("test_scatter_plot.png")

    # Clean up
    os.remove(file_path)
    os.remove("test_cleaned_data.csv")
    os.remove("test_scatter_plot.png")