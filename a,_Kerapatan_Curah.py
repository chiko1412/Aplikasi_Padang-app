import streamlit as st

st.title('Perhitungan Kerapatan Curah')
st.markdown('----')
st.subheader('Bagaimana cara mendapatkan data untuk perhitungan kerapatan curah? Simak caranya berikut ini:')
st.write('1. Gelas ukur kosong ditimbang, catat sebagai Wgu')
st.write('2. Kacang ijo dimasukkan ke dalam gelas ukur sambil diketuk-ketuk sampai tanda tera 25,0 mL. Catat sebagai Vc. (Volume 25 mL tidak standar, bisa diubah ke volume berapa saja).')
st.write('3. Gelas ukur berisi kacang ijo ditimbang, catat sebagai Wgb. Hitung bobot kacang ijo (Wgb-Wgu) dan catat sebagai W.')


# Perhitungan kerapatan curah
st.subheader('Masukkan data data yang telah di dapat agar bisa di hitung dengan kalkulator kami')
def calculate_bulk_density(sample_weight, berat_wadah, sample_volume):
    try:
        bulk_density = ((sample_weight - berat_wadah) / sample_volume)
        return bulk_density
    except ZeroDivisionError:
        st.error("Error: Pembagian dengan nol tidak diizinkan.")
        return None
def main():
    st.subheader('Kalkulator Kerapatan Curah')
    sample_weight_bulk = st.number_input('Bobot Gelas Ukur Isi Sampel (g):', min_value=0.0, format="%.4f", key='bulk_sample_weight')
    berat_wadah_bulk = st.number_input('Bobot Gelas Ukur (g):', min_value=0.0, format="%.4f", key='bulk_berat_wadah')
    sample_volume_bulk = st.number_input('Volume Gelas Ukur Isi Sampel (mL):', min_value=0.0, format="%.4f", key='bulk_sample_volume')
    if st.button('Hitung Kerapatan Curah'):
        bulk_density = calculate_bulk_density(sample_weight_bulk, berat_wadah_bulk, sample_volume_bulk)
        if bulk_density is not None:
            st.subheader('Hasil Perhitungan Kerapatan Curah:')
            st.write('Kerapatan Curah:', bulk_density, 'g/mL')

if __name__ == '__main__':
    main()