# Unit test for plot.py
def test_plot_scatter_with_degradation():
    import pandas as pd
    import os
    from Src.plot import plot_scatter_with_degradation

    # Sample DataFrame
    data = {
        "discharge_capacity": [1.0, 1.1, 1.2],
        "voltage": [3.7, 3.6, 3.5],
        "cycle_index": [1, 2, 3],
        "cell_index": [1, 1, 1],
    }
    cleaned_data = pd.DataFrame(data)

    # Call the function
    save_path = "test_plot.png"
    plot_scatter_with_degradation(
        cleaned_data,
        x_col="discharge_capacity",
        y_col="voltage",
        color_col="cycle_index",
        group_col="cell_index",
        save_path=save_path,
        title="Test Plot"
    )

    # Check if the file was created
    assert os.path.exists(save_path)

    # Clean up
    os.remove(save_path)
