# Cryptocurrency Dashboard

Simple finance dashboard to track and compare cryptocurrency prices written in Python. 

**Update:**
Complete overhaul in v1.2!
- Extensive Jupyter Notebook with full documentation.
- Use as a basis and create your own python script using the components you need.  

**Features:**
- Fetch cryptocurrency data from *Binance*.
- Store API-Keys securely using *dotenv*.
- Helper functions to extract data and save to *CSV*.
- Explore dataframes in *Tabulate*.
- Create plots in *Plotly*. 
- Build dashboard in *Panel*.

## WebApp

Currently not available.

## Requirements & Installation

### List of Python packages

- load_dotenv
- datetime
- pandas
- panel
- plotly
- matplotlib

### Installation

Install with **pip**:

``pip install <PACKAGE_NAME>``

Install with **conda**:

``conda install --channel=conda-forge <PACKAGE_NAME>``

### Binance API Key

Store your Public Binance API-Key in **keys.env**. 

![howto_add_api_key.png](https://raw.githubusercontent.com/kuranez/Krypto-Dashboard/refs/heads/v.1.2/screenshots/howto_add_api_key.png)

### Add Cryptocurrency Symbols

Go to **Add Symbol** section of the notebook and add custom Crypto-USDT-pairs.

![howto_add_symbols.png](https://raw.githubusercontent.com/kuranez/Krypto-Dashboard/refs/heads/v.1.2/screenshots/howto_add_symbols.png)

Pick custom colors for plotly using the matplotlib colors library and add to colors dictionaries. 

[https://matplotlib.org/stable/gallery/color/named_colors.html](https://matplotlib.org/stable/gallery/color/named_colors.html)

![howto_add_symbols_customize.png](https://raw.githubusercontent.com/kuranez/Krypto-Dashboard/refs/heads/v.1.2/screenshots/howto_add_symbols_customize.png)


### Example Datasets

Example data sets are available.

![howto_example_datasets](https://raw.githubusercontent.com/kuranez/Krypto-Dashboard/refs/heads/v.1.2/screenshots/howto_example_datasets.png)

### Run Notebook

Run all cells first to guarantee full functionality.

![howto_run_notebook.png](https://raw.githubusercontent.com/kuranez/Krypto-Dashboard/refs/heads/v.1.2/screenshots/howto_run_notebook.png)

## Features

### Overview 

Grab and check all data you need using the **Main Function**. 

![features_main.png](https://raw.githubusercontent.com/kuranez/Krypto-Dashboard/refs/heads/v.1.2/screenshots/features_main.png)

### Save Data to CSV

Save data locally as a csv file.

![features_CSV.png](https://raw.githubusercontent.com/kuranez/Krypto-Dashboard/refs/heads/v.1.2/screenshots/features_CSV.png)

### Price Plots

Generate nice looking charts with Plotly.

#### Market Overview Figures

![fig_market_overview_comparison_1.png](https://raw.githubusercontent.com/kuranez/Krypto-Dashboard/refs/heads/v.1.2/screenshots/fig_market_overview_comparison_1.png)

![fig_market_overview_comparison_2.png](https://raw.githubusercontent.com/kuranez/Krypto-Dashboard/refs/heads/v.1.2/screenshots/fig_market_overview_comparison_2.png)

#### Interactive Price Charts

![fig_detail.png](https://raw.githubusercontent.com/kuranez/Krypto-Dashboard/refs/heads/v.1.2/screenshots/fig_detail.png)

### Explore DataFrames in Tabulate

Explore & Compare data tables and apply filters if necessary.

![features_compare_filter_data.png](https://raw.githubusercontent.com/kuranez/Krypto-Dashboard/refs/heads/v.1.2/screenshots/features_compare_filter_data.png)

### Interactive Widgets

Use interactive widgets to explore data in **Jupyter Notebook** or build a **Dashboard App** using **Panel**. 

![features_dashboard.png](https://raw.githubusercontent.com/kuranez/Krypto-Dashboard/refs/heads/v.1.2/screenshots/features_dashboard.png)

## Resources

- [JupyterLab - Scientific Python Notebook Suite](https://jupyter.org/)
- [HoloViz Panel Data Exploration & Web App Framework for Python](https://panel.holoviz.org/index.html)
- [Plotly Open Source Graphing Library for Python](https://plotly.com/python/)
- [Matplotlib Color Gallery](https://matplotlib.org/stable/gallery/color/named_colors.html)

![matplotlib_named_colors.png](https://raw.githubusercontent.com/kuranez/Krypto-Dashboard/refs/heads/v.1.2/screenshots/matplotlib_named_colors.png)
