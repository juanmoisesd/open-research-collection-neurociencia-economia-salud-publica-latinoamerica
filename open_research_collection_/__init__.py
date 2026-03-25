"""Open Research Collection — Juan Moisés de la Serna Tuya: Neurociencia, Economía 
DOI:10.5281/zenodo.19151868"""
__version__="1.0.0"
import pandas as pd,io,requests
def load_data(f=None):
  rid="10.5281/zenodo.19151868".split(".")[-1];m=requests.get("https://zenodo.org/api/records/"+rid,timeout=30).json();csvs=[x for x in m.get("files",[]) if x["key"].endswith(".csv")]
  if not csvs:raise ValueError("No CSV")
  tgt=next((x for x in csvs if f and x["key"]==f),csvs[0]);return pd.read_csv(io.StringIO(requests.get(tgt["links"]["self"],timeout=60).text))
def cite():return "de la Serna, Juan Moisés (2025). Open Research Collection — Juan Moisés de la Serna Tuya: Neu"
def info():print("DOI: 10.5281/zenodo.19151868\nGitHub: https://github.com/juanmoisesd/open-research-collection-neurociencia-economia-salud-publica-latinoamerica")
