import streamlit as st

# Inisialisasi Session State
if 'submitted_pg' not in st.session_state:
    st.session_state.submitted_pg = False
if 'skor_pg' not in st.session_state:
    st.session_state.skor_pg = 0

# Data soal pilihan ganda
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

soal_uraian = [
    {
        "soal": "6. (Uraian) Pada percobaan pelemparan tiga koin sekaligus:\n a. Tentukan ruang sampel dan banyaknya elemen ruang sampel\n b. Tentukan kejadian A yaitu muncul paling sedikit dua angka",
        "pembahasan": "a. S = {AAA, AAG, AGA, AGG, GAA, GGA, GAG, GGG}, n(S) = 8\nb. A = {AAA, AAG, AGA, GAA}, n(A) = 4"
    },
    {
        "soal": "7. (Uraian) Pada percobaan melambungkan dua dadu:\n a. Tentukan ruang sampel dan banyaknya elemen ruang sampel\n b. Kejadian A yaitu muncul angka-angka yang berjumlah 9",
        "pembahasan": "a. n(S) = 36\nb. A = {(3,6), (4,5), (5,4), (6,3)}, n(A) = 4"
    }
]

st.title("📘 Kuis Interaktif: Titik sampel, Ruang sampel, Percobaan, dan Kejadian - Cublak-Cublak Suweng")

# Input nama siswa
nama = st.text_input("Masukkan nama kamu:")

if nama:
    st.subheader("Soal Pilihan Ganda")

    jawaban_siswa = []
    skor = 0

    with st.form("form_pilgan"):
        for i, soal in enumerate(soal_pilgan):
            pilihan = st.radio(soal["soal"], soal["opsi"], key=f"pg{i}")
            jawaban_siswa.append(pilihan)
        submitted = st.form_submit_button("Kirim Jawaban Pilihan Ganda")

    if submitted:
        benar = 0
        pembahasan = []
        for i, soal in enumerate(soal_pilgan):
            jawaban_benar = soal["jawaban"]
            jawaban_siswa_i = jawaban_siswa[i][0]  # A/B/C/D

            if jawaban_siswa_i == jawaban_benar:
                benar += 1
                pembahasan.append(f"✅ Soal {i+1}: Benar")
            else:
                pembahasan.append(f"❌ Soal {i+1}: Salah. Jawaban yang benar adalah {jawaban_benar}")

        nilai = int((benar / len(soal_pilgan)) * 100)
        st.session_state.submitted_pg = True
        st.session_state.skor_pg = nilai

        st.success(f"📊 Kamu menjawab benar {benar} dari {len(soal_pilgan)} soal.")
        st.info(f"Nilai kamu: {nilai}/100")

        with st.expander("🔍 Lihat Pembahasan Pilihan Ganda"):
            for p in pembahasan:
                st.write(p)

# Setelah submit PG, tampilkan soal uraian
if st.session_state.submitted_pg:
    st.subheader("📝 Soal Uraian")
    for i, soal in enumerate(soal_uraian):
        jawaban = st.text_area(soal["soal"], key=f"essay{i}")
        if jawaban:
            with st.expander("💡 Lihat Pembahasan"):
                st.write(soal["pembahasan"])
