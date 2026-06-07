import streamlit as st

st.set_page_config(
    page_title="Matematika Geometri",
    page_icon=":fire: ",
)

with st.sidebar:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.logo("geometry.png",)
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilih Bangun Datar", ["Persegi", "Persegi Panjang", "Lingkaran"])
    st.caption("Dibuat dengan :fire: oleh **Aulia Assyahro**")
    st.caption("Aplikasi untuk menghitung luas dan keliling bangun datar")


match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung `luas` dan `keliling` persegi")
        sisi = st.number_input("Masukkan panjang sisi")
        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            # st.info(f"Luas Persegi: {luas :.2f} dan keliling: {keliling :.2f}")
            col1, col2,= st.columns([2,2])
            with col1:
                st.metric("Luas Persegi", value=luas, border=True)
            with col2:
                st.metric("Keliling Persegi", value=keliling, border=True)
            st.balloons()
    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung `luas` dan `keliling` persegi panjang")
        panjang = st.number_input("Masukkan panjang")
        lebar = st.number_input("Masukkan lebar")
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            # st.info(f"Luas Persegi Panjang: {luas :.2f} dan keliling: {keliling :.2f}")
            col1, col2,= st.columns([2,2])
            with col1:
                st.metric("Luas Persegi Panjang", value=luas, border=True)
            with col2:
                st.metric("Keliling Persegi Panjang", value=keliling, border=True)
            st.balloons()
    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung `luas` dan `keliling` lingkaran")
        jari_jari = st.number_input("Masukkan jari-jari")
        if st.button("Hitung", type="primary"):
            luas = 3.14 * jari_jari * jari_jari
            keliling = 2 * 3.14 * jari_jari
            # st.info(f"Luas Lingkaran: {luas :.2f} dan keliling: {keliling :.2f}")
            col1, col2,= st.columns([2,2])
            with col1:
                st.metric("Luas Lingkaran", value=luas, border=True)
            with col2:
                st.metric("Keliling Lingkaran", value=keliling, border=True)
            st.balloons()
    case _:
        st.error("terjadi kesalahan")