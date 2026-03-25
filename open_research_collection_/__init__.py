"""Open Research Collection — Juan Moisés de la Serna Tuya: Neurociencia, Economía Conductual, Salud Pú
DOI: 10.5281/zenodo.19151868 | GitHub: https://github.com/juanmoisesd/open-research-collection-neurociencia-economia-salud-publica-latinoamerica"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd,io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="10.5281/zenodo.19151868".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs:raise ValueError("No CSV found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite():return f'de la Serna, Juan Moisés (2025). Open Research Collection — Juan Moisés de la Serna Tuya: Neurociencia, Economía . Zenodo. https://doi.org/10.5281/zenodo.19151868'
def info():print(f"Dataset: Open Research Collection — Juan Moisés de la Serna Tuya: Neurociencia, Economía \nDOI: 10.5281/zenodo.19151868\nGitHub: https://github.com/juanmoisesd/open-research-collection-neurociencia-economia-salud-publica-latinoamerica")