# -*- coding: utf-8 -*-
"""
APP positivos negativos COVID-19

@author: mirkos@gmail.com
"""

import streamlit as st
import joblib

classes = ['COVID-19 negativo','COVID-19 positivo']
st.title('Preditor para COVID-19')
modelo = joblib.load('giane-pn.sav')
mono = st.number_input('Monócitos (/mm3)')
linf = st.number_input('Linfócitos (/mm3)')
plaq = st.number_input('Plaquetas (/mm3)')
pcr = st.number_input('PCR (mg/dL)')
ferr = st.number_input('Ferritina (ng/mL)')
pac = [mono,linf,plaq,pcr,ferr]

pred = modelo.predict([pac])
if st.button('Analisar'):
    st.write(classes[int(pred)])
