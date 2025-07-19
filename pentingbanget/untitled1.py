import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ==== STYLING ==== #
st.markdown("""
    <style>
        /* Global background */
        .stApp {
            background-color: #F0F4EF;
            font-family: 'Segoe UI', sans-serif;
        }

        /* General title */
        .main-title {
            font-size: 34px;
            font-weight: bold;
            color: #114B5F;
            background-color: #E4FDE1;
            padding: 16px;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 20px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        }

        /* Section content */
        .section-box {
            background-color: #F3E9D2;
            padding: 18px 24px;
            border-radius: 10px;
            margin-bottom: 24px;
            font-size: 17px;
            color: #333333;
            line-height: 1.7;
            box-shadow: 1px 1px 6px rgba(0,0,0,0.08);
        }

        ul {
            margin-top: 10px;
        }

        li {
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ==== DRAW TRIANGLE FUNCTION ==== #
def draw_triangle(a, b):
    c = round((a**2 + b**2)**0.5, 2)
    fig, ax = plt.subplots()
    ax.plot([0, a, 0, 0], [0, 0, b, 0], color='#114B5F')
    ax.fill([0, a, 0], [0, 0, b], '#88D498', alpha=0.4)
    ax.text(a / 2, -1, f"a = {a}", ha='center')
    ax.text(-1, b / 2, f"b = {b}", va='center', rotation='vertical')
    ax.text(a / 2.5, b / 2.5, f"c = {c}", fontsize=12, color='#E76F51')
    ax.set_xlim(-2, max(10, a+2))
    ax.set_ylim(-2, max(10, b+2))
    ax.set_aspect('equal')
    ax.set_title("Visualisasi Segitiga Pythagoras", fontsize=14, color='#114B5F')
    return fig, c

# ==== SIDEBAR MENU ==== #
st.sidebar.title("📘 Laboratorium Interaktif")
menu = st.sidebar.radio("Pilih fitur:", ["🎯 Tujuan Pembelajaran", "🧭 Petunjuk Penggunaan", "🧪 Jelajah Teorema Pythagoras"])

# ==== PAGE 1 ==== #
if menu == "🎯 Tujuan Pembelajaran":
    st.markdown("<div class='main-title'>Tujuan Pembelajaran</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-box'>
        Setelah menggunakan laboratorium ini, kamu diharapkan dapat:
        <ul>
            <li>Menemukan rumus Pythagoras melalui visualisasi segitiga siku-siku secara konkret.</li>
            <li>Memahami dan menjelaskan hubungan antara panjang sisi-sisi segitiga tersebut.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)

# ==== PAGE 2 ==== #
elif menu == "🧭 Petunjuk Penggunaan":
    st.markdown("<div class='main-title'>Petunjuk Penjelajahan Pythagenius</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-box'>
        Untuk memulai penjelajahan teorema Pythagoras menggunakan aplikasi <strong>Pythagenius</strong>, ikuti langkah-langkah berikut:
        <ol>
            <li>Buka menu <strong>Jelajah Teorema Pythagoras</strong> di sisi kiri layar.</li>
            <li>Gunakan <em>slider</em> untuk memilih panjang sisi <code>a</code> dan <code>b</code>.</li>
            <li>Amati visualisasi segitiga yang muncul lengkap dengan panjang ketiga sisinya.</li>
            <li>Nilai sisi miring <code>c</code> akan dihitung secara otomatis.</li>
            <li>Ulangi eksperimen dengan panjang sisi berbeda untuk memperkuat pemahaman.</li>
        </ol>
        </div>
    """, unsafe_allow_html=True)

# ==== PAGE 3 ==== #
elif menu == "🧪 Jelajah Teorema Pythagoras":
    st.markdown("<div class='main-title'>Eksperimen: Jelajahi Teorema Pythagoras</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='section-box'>
        Gunakan penggeser di bawah ini untuk menentukan panjang sisi <strong>a</strong> dan <strong>b</strong> pada segitiga siku-siku. Perhatikan bagaimana sisi miring <strong>c</strong> dihitung dan divisualisasikan secara otomatis!
        </div>
    """, unsafe_allow_html=True)

    a = st.slider("Panjang sisi a (horizontal)", 1, 20, 5)
    b = st.slider("Panjang sisi b (vertikal)", 1, 20, 5)

    fig, c = draw_triangle(a, b)
    st.pyplot(fig)
    st.markdown(f"""
        <div class='section-box'>
        Diketahui:
        <ul>
            <li>Sisi a = {a}</li>
            <li>Sisi b = {b}</li>
            <li>Maka sisi miring (c) = {c}</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)
