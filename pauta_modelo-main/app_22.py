import pandas as pd
import streamlit as st
import numpy as np
from pycaret.regression import load_model, predict_model

st.set_page_config(page_title="Modelo de Predicción de Resultados de Anuncios")

@st.cache(allow_output_mutation=True)
def get_model():
    return load_model("final_rf_pauta")

def predict(model, df):
    predictions = predict_model(model, data = df)
    return predictions['Label'][0]

model = get_model()

st.title("Modelo de Predicción de Resultados de Anuncios")
st.markdown("Elija los valores para pronosticar el Resultado del Anuncio")

form = st.form("anuncios")
importe_gastado = form.number_input('importe_gastado', min_value = 0.0, max_value = 20000.00,value=0.0, format = '%f', step = 0.01)
clasificacion_list = ['Atributos','Especiales','Estratégicas','Estratégico','Spots','Territorio']
clasificacion_descripcion = form.selectbox('clasificacion_descripcion', clasificacion_list)
objetivo_list = ['Interacción','ThruPlay']
objetivo_descripcion = form.selectbox('objetivo_descripcion', objetivo_list)
redsocial_list = ['Dark Post', 'Facebook','Instagram']
redsocial_descripcion = form.selectbox('redsocial_descripcion', redsocial_list)

predict_button = form.form_submit_button('Predict')

input_dict = {'importe_gastado': importe_gastado, 'clasificacion_descripcion': clasificacion_descripcion, 'objetivo_descripcion': objetivo_descripcion, 'redsocial_descripcion': redsocial_descripcion}

input_df = pd.DataFrame([input_dict])

if predict_button: 
    out = predict(model, input_df)
    out = '{0:,.2f}'.format(out)
    st.success(f'La prediccion del Resultado Alcanzado es {out}.')
