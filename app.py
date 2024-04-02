import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Iris Flower Explorer", 
    page_icon="🐧", 
    layout="centered",
)

st.title("Iris Flower Explorer")

st.markdown("""
## Observations
- The Adelie species has the highest bill length.

""")

st.divider()

df = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

with st.sidebar:
    # Input filter options
    bill_length_slider = st.slider(
        "Bill Length (mm)",
        min(df["bill_length_mm"]),
        max(df["bill_length_mm"]),
    )
    species_filter = st.selectbox(
        "Species",
        df["species"].unique(),
        index=None
    )
    islands_filter = st.multiselect("Island", df["island"].unique())

# Filter data
if islands_filter:
    df = df[df["island"].isin(islands_filter)]
if species_filter:
    df = df[df["species"] == species_filter]
df = df[df["bill_length_mm"] > bill_length_slider]

with st.expander("RAW Data"):
    st.write(df)

fig = px.histogram(
    df, 
    x="bill_length_mm"
)
st.plotly_chart(fig)

fig2 = px.scatter(
    df, 
    x="bill_length_mm", 
    y="bill_depth_mm"
)
st.plotly_chart(fig2)