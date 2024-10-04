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

## Features

### Overview

Grab and check all data you need using the **Main Function**.

### Price Plots

Generate nice looking charts with Plotly.

#### Current Price vs. All-Time-High Comparison for Multiple Symbols

#### Price Comparison for Multiple Symbols

#### Price & Volume Figures for a Symbol

### Explore DataFrames in Tabulate

Display data in Tabulate and apply filters if necessary.

### Interactive Widgets

Use interactive widgets to explore data in **Jupyter Notebook** or build a **Dashboard App** using **Panel**.

## Resources

- [**JupyterLab - Scientific Python Notebook Suite**](https://jupyter.org/)
- [**HoloViz Panel Data Exploration & Web App Framework for Python **](https://panel.holoviz.org/index.html)
- [**Plotly Open Source Graphing Library for Python **](https://plotly.com/python/)
