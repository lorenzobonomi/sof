## Modules for project

# Standard modules
import numpy as np
import pandas as pd
import streamlit as st

from google.oauth2 import service_account
from google.cloud import bigquery

## App

# Streamlit layout main parameters
st.set_page_config(layout = 'wide')
st.title('Sof')
st.subheader('')

# Create API client
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

# Query the data
@st.experimental_memo(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.experimental_memo to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

rows = run_query("SELECT * FROM peppy-archive-358819.dbt_lbonomi.dim_list_tables LIMIT 10")

results = pd.DataFrame(rows)

# Print results
st.write(results)




