import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Pythagoras Explorer", layout="wide", page_icon="🎉")

st.markdown("""
    <style>
        .main {
            background-color: #fdf6f0;
        }
        .block-container {
            padding: 2rem 2rem;
        }
        h1, h2, h3, h4, h5, h6, .stMarkdown {
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔺 Pythagoras Explorer")
st.subheader("Visualisasikan dan temukan sendiri rumusnya!")

st.markdown("""
**Langkah 1:** Geser panjang sisi siku-siku (a dan b) untuk membentuk segitiga.

**Langkah 2:** Amati luas persegi di setiap sisi.

**Langkah 3:** Temukan sendiri hubungan antara a² + b² dan c²!
""")

# Input sisi a dan b
a = st.slider("Panjang sisi a:", 1, 20, 3)
b = st.slider("Panjang sisi b:", 1, 20, 4)
c = round(np.sqrt(a**2 + b**2), 2)

st.markdown(f"**Sisi miring (c)** akan dihitung otomatis: **{c}**")

# Visualisasi segitiga dan persegi
def plot_triangle(a, b):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    
    # Titik-titik segitiga
    A = [0, 0]
    B = [a, 0]
    C = [0, b]

    # Gambar segitiga
    triangle = plt.Polygon([A, B, C], closed=True, fill=True, color="#a0d8ef", edgecolor="black")
    ax.add_patch(triangle)

    # Tambahkan persegi pada sisi-sisi
    ax.add_patch(plt.Rectangle((0, 0), a, a, fill=True, color="#ffeb99", alpha=0.4))  # a²
    ax.add_patch(plt.Rectangle((0, 0), -b, b, fill=True, color="#caffbf", alpha=0.4))  # b²
    ax.add_patch(plt.Rectangle((a, 0), b, b, angle=np.degrees(np.arctan(b/a)), fill=True, color="#ffb3c1", alpha=0.4))  # c² (kira-kira)

    # Label
    ax.text(a/2, -1, f"a = {a}", ha='center')
    ax.text(-1, b/2, f"b = {b}", va='center', rotation='vertical')
    ax.text(a/2, b/2, f"c = {c}", ha='center')

    ax.set_xlim(-b - 5, a + b + 5)
    ax.set_ylim(-5, b + a + 5)
    ax.axis('off')
    return fig

fig = plot_triangle(a, b)
st.pyplot(fig)

# Refleksi siswa
st.markdown("---")
st.header("🧠 Refleksi")
st.markdown("Apa yang kamu amati dari luas persegi a², b², dan c²?")
user_input = st.text_area("Tuliskan kesimpulanmu di sini:")

if user_input:
    st.success("Keren! Sekarang coba bandingkan dengan rumus Pythagoras berikut:")
    st.latex(r"a^2 + b^2 = c^2")
    st.balloons()

st.markdown("""
---
📌 **Catatan:**
- Aplikasi ini bertujuan mengajak kamu berpikir kritis dan bereksperimen.
- Cobalah berbagai nilai a dan b!
""")
