import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns   
import streamlit as st

ruta = "https://github.com/maurogdodata23/Proyecto_siniestros/raw/refs/heads/main/Siniestros_nacionales_aleatorio_trim6.csv"
df = pd.read_csv(ruta, encoding='latin-1')
imagen = "imagen1.png"
imagen3 = plt.imread(imagen)
plt.imshow(imagen3)
plt.axis('off')

##Configuracion streamlit
st.set_page_config(page_title="Análisis de Siniestros", page_icon=":⚠️:", layout="wide")
st.title("Análisis de Siniestros Nacionales")
st.markdown("Este proyecto analiza los siniestros nacionales utilizando un conjunto de datos aleatorio. A continuación, se presentan algunos gráficos y análisis basados en los datos disponibles.")
st.image(imagen3, caption="Análisis de Siniestros", use_column_width=True)




