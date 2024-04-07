import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Iris Flower Explorer", 
    page_icon="🌷", 
    layout="centered",
)

st.title("🌷 Iris Flower Explore 🌷")

st.markdown("""
## Observations
- The Adelie species has the highest bill length.

""")

st.divider()

df = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

# Sidebar filters
with st.sidebar:
    st.markdown("## Filters")
    species = st.selectbox("Species", options=["All"] + list(df['species'].unique()))
    sepal_length_slider = st.slider("Sepal Length (cm)", min(df["sepal_length"]), max(df["sepal_length"]), (min(df["sepal_length"]), max(df["sepal_length"])))
    sepal_width_slider = st.slider("Sepal Width (cm)", min(df["sepal_width"]), max(df["sepal_width"]), (min(df["sepal_width"]), max(df["sepal_width"])))
    petal_length_slider = st.slider("Petal Length (cm)", min(df["petal_length"]), max(df["petal_length"]), (min(df["petal_length"]), max(df["petal_length"])))
    petal_width_slider = st.slider("Petal Width (cm)", min(df["petal_width"]), max(df["petal_width"]), (min(df["petal_width"]), max(df["petal_width"])))


# Filter data
df_filtered = df[
    (df["sepal_length"] >= sepal_length_slider[0]) & (df["sepal_length"] <= sepal_length_slider[1]) &
    (df["sepal_width"] >= sepal_width_slider[0]) & (df["sepal_width"] <= sepal_width_slider[1]) &
    (df["petal_length"] >= petal_length_slider[0]) & (df["petal_length"] <= petal_length_slider[1]) &
    (df["petal_width"] >= petal_width_slider[0]) & (df["petal_width"] <= petal_width_slider[1])
]

if species != "All":
    df_filtered = df_filtered[df_filtered['species'] == species]


# Display filtered data
with st.expander("Filtered Data"):
    st.write(df_filtered)

# Visualization
st.subheader("Distribution of Sepal Length and Width")
fig_sepal = px.scatter(df_filtered, x="sepal_length", y="sepal_width", color="species", title="Sepal Measurements")
st.plotly_chart(fig_sepal)

st.subheader("Distribution of Petal Length and Width")
fig_petal = px.scatter(df_filtered, x="petal_length", y="petal_width", color="species", title="Petal Measurements")
st.plotly_chart(fig_petal)

# Classifier
X = df_filtered[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df_filtered['species']
