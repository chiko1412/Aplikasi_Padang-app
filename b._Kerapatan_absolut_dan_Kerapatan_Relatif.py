import streamlit as st

st.title('Perhitungan Kerapatan Absolut')
st.markdown('----')
st.subheader('Bagaimana cara mendapatkan data untuk perhitungan kerapatan Absolut? Simak caranya berikut ini:')
st.write('1. Gelas ukur di isi dengan aquadest sebanyak 25,00 mL lalu seka bagian dalam tabung, dicatat sebagai volume awal, setelah itu ditimbang dan catat hasil nilai yang didapat sebagai Wa')
st.write('2. .Gelas ukur ditambahkan sampel (kacang hijau) sebanyak 15,00 mL, sehingga menghasilkan volume akhir sebesar 40,00 mL dicatat sebagai volume akhir, ditimbang kembali gelas ukur berisi air dan sampel dan catat hasil nilai yang didapat sehagai Wb')
st.title('Perhitungan Kerapatan Relatif')
st.markdown('----')
st.subheader('Bagaimana cara mendapatkan data untuk perhitungan kerapatan Relatif? Simak caranya berikut ini:')
st.write('1. Data Hasil perhitungan kerapatan absolut ')
st.write('2. Nilai viskositas air dalam suhu saat melakukan percobaan(Nilai viskositas dapat di lihat pada menu tabel viskositas air).')
st.subheader('Masukkan data data yang telah di dapat agar bisa di hitung dengan kalkulator kami')


# Perhitungan kerapatan absolut dan relatif
def calculate_absolute_density(sample_weight, water_weight, sample_volume, water_volume):
    try:
        absolute_density = ((sample_weight - water_weight) / (sample_volume - water_volume)) 
        return absolute_density
    except ZeroDivisionError:
        st.error("Error: Pembagian dengan nol tidak diizinkan.")
        return None
def calculate_relative_density(absolute_density, nilai_viskositas):
    try:
        relative_density = absolute_density / nilai_viskositas
        return relative_density
    except ZeroDivisionError:
        st.error("Error: Pembagian dengan nol tidak diizinkan.")
        return None
def main():
    sample_weight_abs = st.number_input('Bobot Gelas Ukur Isi Sampel (g):', min_value=0.0, step=0.1, format="%.4f")
    water_weight_abs = st.number_input('Bobot Gelas Ukur Isi Air (g):', min_value=0.0, step=0.1, format="%.4f")
    sample_volume_abs = st.number_input('Volume Gelas Ukur Isi Sampel (mL):', min_value=0.0, step=0.1, format="%.2f")
    water_volume_abs = st.number_input('Volume Gelas Ukur Isi Air (mL):', min_value=0.0, step=0.1, format="%.2f")
    nilai_viskositas_bulk =  st.number_input('Nilai Viskositas air (mPa.s):', min_value=0.0, format="%.4f", key='bulk_nilai_viskositas')
    if st.button('Hitung Kerapatan Absolut'):
        absolute_density = calculate_absolute_density(sample_weight_abs, water_weight_abs, sample_volume_abs, water_volume_abs)
        if absolute_density is not None:
            st.subheader('Hasil Perhitungan Kerapatan Absolut:')
            st.write('Kerapatan Absolut:', absolute_density, 'g/mL')
    if st.button('Hitung Kerapatan Relatif'):
        absolute_density = calculate_absolute_density(sample_weight_abs, water_weight_abs, sample_volume_abs, water_volume_abs)
        if absolute_density is not None:
            relative_density = calculate_relative_density(absolute_density, nilai_viskositas_bulk)
            if relative_density is not None:
                st.subheader('Hasil Perhitungan Kerapatan Relatif:')
                st.write('Kerapatan Relatif:', relative_density)
if __name__ == '__main__':
    main()
