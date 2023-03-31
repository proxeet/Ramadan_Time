import pandas as pd
import numpy as np
from datetime import datetime
import streamlit as st


def imsakiye ():
    site = pd.read_html('https://www.namazvakitleri.mobi/wroclaw-ramazan-imsakiyesi')[0]
    takvim = site.drop(['Güneş', 'Öğle', 'İkindi', 'Yatsı', 'Unnamed: 0' ], axis = 1)
    takvim = takvim.drop (5, axis = 0)
    tarih = takvim['Tarih'].str.split(".", expand = True) 
    takvim['Tarih'] = tarih[2] + '-' + tarih[1] + '-'+ tarih[0]
    takvim['Tarih'] = pd.to_datetime(takvim['Tarih'])
    return takvim
    
def today():
    df=imsakiye()
    Today = datetime.today().date().strftime("%Y-%m-%d")
    iftar = df[df["Tarih"]==Today]
    return iftar
    
def iftarKalan():
    df = imsakiye()
    Today = datetime.today().date().strftime("%Y-%m-%d")
    Now = datetime.now().time().strftime("%H:%M:%S")
    iftar = df[df["Tarih"]==Today]["Akşam"].values[0]
    kalan = pd.Timedelta(pd.to_datetime(iftar)-pd.to_datetime(Now))
    return kalan


st.header("Welcome Ramadan")

st.subheader("Iftar Kalan Sure")
st.write(iftarKalan())
st.subheader("Today")
st.table(today())
st.subheader('Imsakiye')
st.table(imsakiye())