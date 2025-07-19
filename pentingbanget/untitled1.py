import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Pythagenius", layout="centered")
st.markdown("""
    <style>
    /* Warna latar dan teks utama */
    body {
        background-color: #FDFCF9;
        color: #333333;
    }
    
    /* Judul dan header */
    .css-10trblm {
        color: #2D4059;
    }

    /* Sidebar */
    .css-1d391kg, .css-1d391kg:hover {
        background-color: #F4F6F6;
        color: #2D4059;
    }

    /* Slider dan widget lainnya */
    .stSlider > div {
        color: #3B3B98;
    }

    /* Teks konten */
    .css-1cpxqw2 p, .css-1cpxqw2 li {
        font-size: 16px;
        color: #444444;
    }
    </style>
""", unsafe_allow_html=True)

menu = st.sidebar.selectbox("Pilih Halaman", ["BERANDA", "PETUNJUK PENGGUNAAN", "JELAJAH TEOREMA PYTHAGORAS"])

def draw_triangle(a, b):
    c = round((a**2 + b**2)**0.5, 2)
    fig, ax = plt.subplots()

    # Koordinat titik
    x = [0, a, 0, 0]
    y = [0, 0, b, 0]

    # Gambar segitiga
    ax.plot(x, y, color='#3B3B98', linewidth=2)
    ax.fill([0, a, 0], [0, 0, b], '#74b9ff', alpha=0.4)

    # Teks sisi a (horizontal)
    ax.text(a / 2, -0.8, f"a = {a}", ha='center', fontsize=12, color='black')

    # Teks sisi b (vertikal)
    ax.text(-0.8, b / 2, f"b = {b}", va='center', ha='right', rotation='vertical', fontsize=12, color='black')

    # Teks sisi c (miring)
    mid_c_x = a / 2
    mid_c_y = b / 2
    ax.text(mid_c_x + 0.2, mid_c_y + 0.2, f"c = {c}",
            fontsize=12, color='red',
            rotation=-np.degrees(np.arctan2(b, a)) / 2)

    # Atur tampilan
    ax.set_xlim(-2, max(a, b) + 3)
    ax.set_ylim(-2, max(a, b) + 3)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title("Visualisasi Segitiga Pythagoras")

    return fig, c

if menu == "BERANDA":
    st.title("Selamat Datang di Pythagenius")
    st.write("""
    Aplikasi ini dirancang sebagai laboratorium virtual interaktif untuk membantu kamu mengeksplorasi dan memahami Teorema Pythagoras melalui visualisasi langsung. Selamat belajar dan bereksperimen!
    """)

elif menu == "PETUNJUK PENGGUNAAN":
    st.title("Petunjuk Penjelajahan Pythagenius")
    st.write("""
Untuk memulai penjelajahan teorema Pythagoras menggunakan aplikasi **Pythagenius**, ikuti langkah-langkah berikut: 
1. Buka menu **Jelajah Teorema Pythagoras** yang tersedia di sisi kiri layar atau bagian atas aplikasi. 
2. Gunakan **slider** untuk memilih panjang dua sisi siku-siku, yaitu sisi `a` dan sisi `b`. Silakan geser sesuai angka yang diinginkan.
Pilihan ini akan membentuk segitiga siku-siku secara otomatis. 
3. Amati perubahan visual segitiga yang ditampilkan di layar. Aplikasi akan menampilkan bentuk segitiga lengkap dengan panjang sisi `a`, `b`, dan `c`, serta sudut siku-sikunya.
4. Nilai sisi miring `c` (hipotenusa) akan dihitung dan ditampilkan secara otomatis berdasarkan input yang diberikan. Proses ini menunjukkan bagaimana teorema Pythagoras bekerja secara langsung.
5. Lakukan pengulangan dengan memilih nilai yang berbeda untuk `a` dan `b`, agar kamu bisa melihat pola yang terbentuk dan memahami hubungan antar sisi dalam berbagai kondisi segitiga.

Melalui langkah-langkah ini, kamu dapat mempelajari dan menemukan sendiri bagaimana teorema Pythagoras bekerja secara nyata dan menyenangkan.
""")

elif menu == "JELAJAH TEOREMA PYTHAGORAS":
    st.title("🧪 Eksperimen Segitiga Pythagoras")

    a = st.slider("Panjang sisi a", 1, 20, 5)
    b = st.slider("Panjang sisi b", 1, 20, 5)

    fig, c = draw_triangle(a, b)
    st.pyplot(fig)
    st.markdown(f"<p style='font-size:18px;'>Sisi miring \(c\) dihitung menggunakan rumus \(c = \sqrt{{a^2 + b^2}}\): <br><strong>c = {c}</strong></p>", unsafe_allow_html=True)
