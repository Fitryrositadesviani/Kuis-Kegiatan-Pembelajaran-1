import streamlit as st
import joblib

# Judul
st.title("Kuis Interaktif: Peluang - Cublak-Cublak Suweng")
st.write("Modul pembelajaran matematika berbasis etnomatematika")

# Input nama siswa
nama = st.text_input("Masukkan nama kamu:")

if nama:
    st.success(f"Halo, {nama}! Yuk mulai kuisnya ✨")

    # Soal pilihan ganda
    soal_pilgan = [
        {
            "soal": "1. Ruang sampel dari permainan Cublak-Cublak Suweng dengan pemain Fahri (penebak), Gilang, Hana, dan Laila, adalah...",
            "opsi": ["A. {Gilang, Fahri, Hana}", 
                     "B. {Hana, Laila, Fahri}", 
                     "C. {Gilang, Hana, Laila}", 
                     "D. {Gilang, Fahri, Hana, Laila}"],
            "jawaban": "C"
        },
        {
            "soal": "2. Banyaknya anggota ruang sampel dalam permainan Cublak-Cublak Suweng dengan 8 pemain adalah...",
            "opsi": ["A. 8", "B. 7", "C. 6", "D. 9"],
            "jawaban": "B"
        },
        {
            "soal": "3. Dalam permainan dengan 5 pemain, jika kejadian A adalah 'suweng ada di tangan pemain perempuan' dan terdapat 2 pemain perempuan (Sari dan Tini), maka A = ...",
            "opsi": ["A. {Sari}", "B. {Tini}", "C. {Sari, Tini}", "D. {Sari, Tini, penebak}"],
            "jawaban": "C"
        },
        {
            "soal": "4. Seorang siswa melempar sebuah dadu bermata enam sekali. Ruang sampel dari percobaan ini adalah...",
            "opsi": ["A. 1", "B. {1, 2, 3, 4, 5, 6}", "C. Angka genap", "D. Salah satu dari {1, 2, 3}"],
            "jawaban": "B"
        },
        {
            "soal": "5. Manakah kejadian yang paling mungkin terjadi dalam undian bola merah, biru, kuning (4:3:2)?",
            "opsi": ["A. Bola merah", "B. Bola biru", "C. Bola kuning", "D. Bola putih"],
            "jawaban": "A"
        }
    ]

    # Soal uraian
    soal_uraian = [
        {
            "soal": "6. (Uraian) Pada percobaan pelemparan tiga koin sekaligus:\n a. Tentukan ruang sampel dan banyaknya elemen ruang sampel\n b. Tentukan kejadian A yaitu muncul paling sedikit dua angka",
            "pembahasan": "a. Ruang sampel S = {AAA, AAG, AGA, AGG, GAA, GGA, GAG, GGG}, jadi n(S) = 8\nb. A = {AAA, AAG, AGA, GAA}, karena ini kejadian muncul minimal dua angka. Jadi n(A) = 4"
        },
        {
            "soal": "7. (Uraian) Pada percobaan melambungkan dua buah dadu secara bersamaan:\n a. Tentukan ruang sampel dan banyaknya elemen ruang sampel\n b. Tentukan kejadian A yaitu muncul angka-angka yang berjumlah 9",
            "pembahasan": "a. Ruang sampel pelemparan dua dadu = 36 kombinasi, jadi n(S) = 36\nb. A = {(3,6), (4,5), (5,4), (6,3)}, karena jumlahnya 9. Jadi n(A) = 4"
        }
    ]

    skor = 0
    jawaban_uraian = []

    st.header("📘 Soal Pilihan Ganda")

    for i, soal in enumerate(soal_pilgan):
        pilihan = st.radio(soal["soal"], soal["opsi"], key=f"pg{i}")
        if pilihan.startswith(soal["jawaban"]):
            skor += 1

    st.header("📝 Soal Uraian")
    for i, soal in enumerate(soal_uraian):
        jawaban = st.text_area(f"{soal['soal']}", key=f"essay{i}")
        jawaban_uraian.append(jawaban)
        if jawaban:
            with st.expander("🔍 Lihat Pembahasan"):
                st.write(soal["pembahasan"])

    if st.button("Selesai dan Simpan Hasil"):
        st.success(f"🎓 KUIS SELESAI! {nama}, skor kamu adalah {skor} dari {len(soal_pilgan)} soal.")
        hasil = {
            "nama": nama,
            "skor": skor,
            "jawaban_uraian": jawaban_uraian
        }
        joblib.dump(hasil, "hasil_kuis.pkl")
        st.download_button("📥 Unduh Hasil Kuis (.pkl)", data=open("hasil_kuis.pkl", "rb"), file_name="hasil_kuis.pkl")
