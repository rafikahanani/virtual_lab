import streamlit as st

st.set_page_config(
    page_title="Virtual Lab Bangun Datar",
    page_icon="🟦",
    layout="wide",
)

# Inline CSS for styling & animations
st.markdown(
    """
    <style>
    /* Reset and base */
    body, .main {
        background-color: #ffffff;
        color: #374151;
        font-family: 'Poppins', sans-serif;
        margin: 0; padding: 0;
    }
    h1, h2, h3 {
        font-weight: 700;
        color: #111827;
    }
    h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    h2 {
        font-size: 2rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    p {
        color: #6b7280;
        font-size: 1.1rem;
        line-height: 1.5;
    }
    /* Container cards */
    .card {
        background: #f9fafb;
        border-radius: 0.75rem;
        box-shadow: 0 10px 15px -3px rgb(100 116 139 / 0.1), 0 4px 6px -4px rgb(100 116 139 / 0.1);
        padding: 2rem;
        margin-bottom: 3rem;
        transition: box-shadow 0.3s ease;
    }
    .card:hover {
        box-shadow: 0 12px 20px -5px rgb(59 130 246 / 0.3), 0 8px 14px -7px rgb(59 130 246 / 0.3);
    }
    /* Layout container */
    .container {
        max-width: 1200px;
        margin-left: auto;
        margin-right: auto;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    /* Button styling (not used here but can be for CTA) */
    .btn-primary {
        background-color: #2563eb;
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
        font-weight: 600;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .btn-primary:hover {
        background-color: #1d4ed8;
    }

    /* Shape container centers */
    .shape-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 1.5rem;
    }

    /* Animations for shapes */

    /* Square animation - scaling pulse */
    @keyframes pulse-scale {
      0%, 100% {transform: scale(1);}
      50% {transform: scale(1.1);}
    }

    /* Rectangle animation - horizontal stretch */
    @keyframes stretch-horizontal {
      0%, 100% {transform: scaleX(1);}
      50% {transform: scaleX(1.2);}
    }

    /* Triangle animation - bounce */
    @keyframes bounce {
      0%, 100% {transform: translateY(0);}
      50% {transform: translateY(-15px);}
    }

    /* Circle animation - glow */
    @keyframes glow {
      0%, 100% {box-shadow: 0 0 10px 4px #3b82f6;}
      50% {box-shadow: 0 0 20px 8px #60a5fa;}
    }

    /* Parallelogram animation - rotate */
    @keyframes rotate-shape {
      0%, 100% {transform: rotate(0deg);}
      50% {transform: rotate(10deg);}
    }

    /* Shape base styles */
    .shape {
        background: linear-gradient(135deg, #60a5fa, #3b82f6);
        border-radius: 0.5rem;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.5);
        transition: all 0.3s ease;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page Header
st.markdown(
    """
    <div class="container">
        <h1>💠 Virtual Lab Bangun Datar</h1>
        <p>Pelajari sifat-sifat bangun datar dengan cara interaktif yang penuh animasi dan menyenangkan untuk anak SMP!</p>
    </div>
    """, unsafe_allow_html=True
)

def draw_square(side):
    side_px = side * 10
    shape_html = f"""
    <div class="shape-container">
      <div class="shape" style="
        width: {side_px}px; height: {side_px}px;
        animation: pulse-scale 2s infinite ease-in-out;
      "></div>
    </div>
    """
    st.markdown(shape_html, unsafe_allow_html=True)

def draw_rectangle(width, height):
    width_px = width * 10
    height_px = height * 10
    shape_html = f"""
    <div class="shape-container">
      <div class="shape" style="
        width: {width_px}px; height: {height_px}px;
        animation: stretch-horizontal 2.5s infinite ease-in-out;
        border-radius: 0.5rem;
      "></div>
    </div>
    """
    st.markdown(shape_html, unsafe_allow_html=True)

def draw_triangle(base, height):
    # Create triangle using CSS clip-path polygon
    base_px = base * 10
    height_px = height * 10
    shape_html = f"""
    <div class="shape-container">
      <div style="
        width: {base_px}px;
        height: {height_px}px;
        background: linear-gradient(135deg, #fbbf24, #f97316);
        clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
        animation: bounce 3s infinite ease-in-out;
        border-radius: 0.5rem;
        box-shadow: 0 4px 15px rgba(251, 191, 36, 0.5);
      ">
      </div>
    </div>
    """
    st.markdown(shape_html, unsafe_allow_html=True)

def draw_circle(radius):
    diameter_px = radius * 20
    shape_html = f"""
    <div class="shape-container">
      <div style="
        width: {diameter_px}px;
        height: {diameter_px}px;
        background: radial-gradient(circle at center, #34d399, #047857);
        border-radius: 50%;
        box-shadow: 0 0 15px #10b981;
        animation: glow 3.5s infinite ease-in-out;
      ">
      </div>
    </div>
    """
    st.markdown(shape_html, unsafe_allow_html=True)

def draw_parallelogram(base, height):
    base_px = base * 10
    height_px = height * 10
    shape_html = f"""
    <div class="shape-container">
      <div style="
        width: {base_px}px;
        height: {height_px}px;
        background: linear-gradient(135deg, #a78bfa, #7c3aed);
        clip-path: polygon(25% 0%, 100% 0%, 75% 100%, 0% 100%);
        animation: rotate-shape 4s infinite ease-in-out;
        border-radius: 0.5rem;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.5);
      ">
      </div>
    </div>
    """
    st.markdown(shape_html, unsafe_allow_html=True)

# Main interactive lab
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Persegi (Square)")
    st.write("Sisi-sisi memiliki panjang yang sama, sudut semua siku-siku (90°).")
    side = st.slider("Panjang sisi (cm)", 1, 20, 5)
    draw_square(side)
    luas = side * side
    st.markdown(f"**Luas Persegi:** {side} cm × {side} cm = {luas} cm²")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Persegi Panjang (Rectangle)")
    st.write("Dua pasang sisi sejajar dan sama panjang, sudut semua siku-siku (90°).")
    width = st.slider("Panjang (cm)", 1, 30, 10)
    height = st.slider("Lebar (cm)", 1, 20, 5)
    draw_rectangle(width, height)
    luas = width * height
    st.markdown(f"**Luas Persegi Panjang:** {width} cm × {height} cm = {luas} cm²")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Segitiga (Triangle)")
    st.write("Bangun dengan tiga sisi dan tiga sudut yang jumlahnya selalu 180°.")
    base = st.slider("Alas (cm)", 1, 30, 10)
    height = st.slider("Tinggi (cm)", 1, 20, 7)
    draw_triangle(base, height)
    luas = 0.5 * base * height
    st.markdown(f"**Luas Segitiga:** ½ × {base} cm × {height} cm = {luas:.2f} cm²")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Lingkaran (Circle)")
    st.write("Setiap titik pada lingkaran berjarak sama terhadap titik pusat.")
    radius = st.slider("Jari-jari (cm)", 1, 15, 7)
    draw_circle(radius)
    import math
    luas = math.pi * radius * radius
    st.markdown(f"**Luas Lingkaran:** π × {radius} cm × {radius} cm = {luas:.2f} cm²")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("Jajar Genjang (Parallelogram)")
    st.write("Dua pasang sisi sejajar, sudut berpasangan sama besar.")
    base = st.slider("Alas (cm)", 1, 30, 12)
    height = st.slider("Tinggi (cm)", 1, 20, 6)
    draw_parallelogram(base, height)
    luas = base * height
    st.markdown(f"**Luas Jajar Genjang:** {base} cm × {height} cm = {luas} cm²")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer with credit
st.markdown(
    """
    <div style="text-align:center; margin-top:3rem; color:#9ca3af;">
        &copy; 2024 Virtual Lab Bangun Datar - Created with ❤️ using Streamlit
    </div>
    """, unsafe_allow_html=True
)

