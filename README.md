# Frameworks_Assignment


**Task**: Basic analysis of the CORD-19 `metadata.csv` file and a simple Streamlit app.


## Contents
- `analysis_script.py` — Python script with data loading, cleaning, analysis, and plot-generation. (Can be run as a script or used inside a Jupyter notebook.)
- `app.py` — Streamlit application to explore the cleaned dataset and visualizations.
- `requirements.txt` — Python dependencies.
- `.gitignore` — ignores `__pycache__` and large data files.


## Instructions
1. Place `metadata.csv` inside this folder.
2. Create a virtualenv and install requirements:


```bash
python -m venv venv
source venv/bin/activate # on mac/linux
venv\Scripts\activate # on Windows
pip install -r requirements.txt
