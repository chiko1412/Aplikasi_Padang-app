import streamlit as st
import pandas as pd

# Judul
st.header('Nilai Viskositas air berdasarkan suhu ruang')

    
# Fungsi untuk memuat data
def load_data():
     return pd.DataFrame({
        "Temperatur (°C)": [20, 21, 22, 23, 24, 25, 26, 27, 27.5, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        "Kerapatan air": [0.9982, 0.9980, 0.9978, 0.9976, 0.9973, 0.9971, 0.9968, 0.9965, 0.9964, 0.9963, 0.9960, 0.9957, 0.9954, 0.9951, 0.9947, 0.9944, 0.9941, 0.9937, 0.9934, 0.9930, 0.9926, 0.9922]
    })

    # Tampilkan tabel dengan format lebar (opsional)
use_container_width = st.checkbox("Tampilkan tabel dengan format lebar", value=False, key="use_container_width")
df = load_data()
st.dataframe(df.style.format({'Temperatur (°C)': '{:.1f}'}), use_container_width=use_container_width)

