import streamlit as st
import math
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

# Set page configuration
st.set_page_config(
    page_title="Virtual Lab Teorema Pythagoras",
    page_icon="🔺",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
    }
    .stSlider > div {
        padding: 0 1rem;
    }
    .formula-box {
        background-color: #e3f2fd;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #2196f3;
    }
    .header-section {
        background-color: #1565c0;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
    }
    .triangle-container {
        display: flex;
        justify-content: center;
        margin: 2rem 0;
    }
    .exercise-box {
        background-color: #e8f5e9;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #4caf50;
    }
    .highlight {
        background-color: #fff9c4;
        padding: 2px 4px;
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown("""
<div class="header-section">
    <h1 style="color:white; text-align:center;">Virtual Lab Teorema Pythagoras</h1>
    <p style="color:white; text-align:center;">Eksplorasi segitiga siku-siku dan hubungan antar sisinya</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Menu Navigasi")
section = st.sidebar.radio(
    "Pilih Mode Belajar:",
    ("Visualisasi Segitiga", "Menghitung Sisi Miring", "Latihan Soal", "Aplikasi Dunia Nyata")
)

# Main content based on selected section
if section == "Visualisasi Segitiga":
    st.subheader("Visualisasi Segitiga Siku-Siku")
    st.markdown("""
    **Pahami komponen segitiga siku-siku:**
    - Sisi **a** dan **b** disebut sisi siku-siku
    - Sisi **c** (hypotenusa) adalah sisi miring yang berhadapan dengan sudut siku-siku
    - Sudut antara **a** dan **b** selalu 90°
    """)
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Slider controls
        a = st.slider("Panjang sisi a", 1, 20, 3)
        b = st.slider("Panjang sisi b", 1, 20, 4)
        c = math.sqrt(a**2 + b**2)
        st.markdown(f"**Panjang sisi miring:** `{c:.2f}`")
        
        # Right triangle properties
        st.markdown(f"""
        <div class="formula-box">
            <h4>Sifat Segitiga:</h4>
            <p>• Sudut ∠A + ∠B + ∠C = 180°</p>
            <p>• Sudut siku-siku (90°) di antara sisi <span class="highlight">a</span> dan <span class="highlight">b</span></p>
            <p>• Panjang sisi miring: <span class="highlight">c = √(a² + b²)</span></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Draw triangle visualization
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.set_xlim(0, max(a, b)+1)
        ax.set_ylim(0, max(a, b)+1)
        
        # Draw triangle
        triangle = Polygon([[0, 0], [a, 0], [0, b]], closed=True, 
                          fill=True, color='skyblue', alpha=0.6)
        ax.add_patch(triangle)
        
        # Draw right angle indicator
        rect = Rectangle((0, 0), min(a,b)/4, min(a,b)/4, 
                        fill=True, color='red', alpha=0.5)
        ax.add_patch(rect)
        
        # Label sides and angles
        ax.text(a/2, -0.5, f'a = {a}', ha='center', va='bottom')
        ax.text(-0.5, b/2, f'b = {b}', ha='right', va='center')
        ax.text(a/4, b/4, f'c = {c:.2f}', rotation=math.degrees(math.atan(b/a))-90, 
               ha='center', va='center', bbox=dict(facecolor='white', alpha=0.8))
        
        ax.text(0.1, 0.1, '90°', color='black', fontsize=12)
        ax.text(a+0.1, 0.1, 'A', color='black', fontsize=12)
        ax.text(0.1, b+0.1, 'B', color='black', fontsize=12)
        
        ax.axis('equal')
        ax.axis('off')
        st.pyplot(fig)
        
        # Explanation
        st.markdown("""
        **Penjelasan:**  
        • Kotak merah menunjukkan sudut siku-siku (90°)  
        • Huruf A dan B menunjukkan sudut lancip lainnya  
        • Hitungan otomatis menunjukkan hubungan Pythagoras  
        """)

elif section == "Menghitung Sisi Miring":
    st.subheader("Menghitung Panjang Sisi Miring")
    st.markdown("""
    **Teorema Pythagoras:**  
    Dalam segitiga siku-siku, kuadrat sisi miring (c) sama dengan jumlah kuadrat kedua sisi siku-sikunya.
    """)
    st.latex(r'''c = \sqrt{a^2 + b^2}''')
    
    cols = st.columns(2)
    a = cols[0].number_input("Masukkan panjang sisi a", min_value=1.0, value=3.0, step=0.1)
    b = cols[1].number_input("Masukkan panjang sisi b", min_value=1.0, value=4.0, step=0.1)
    
    if st.button("Hitung Sisi Miring"):
        c = math.sqrt(a**2 + b**2)
        st.markdown(f"<div style='font-size:24px; color:#1565c0;'>Panjang sisi miring c = <span class='highlight'>{c:.3f}</span></div>", 
                   unsafe_allow_html=True)
        
        st.markdown("### Langkah-langkah Perhitungan:")
        steps = [
            ("Menulis rumus Pythagoras", r"c = \sqrt{a^2 + b^2}"),
            ("Masukkan nilai a dan b", fr"c = \sqrt{{{a:.1f}^2 + {b:.1f}^2}}"),
            ("Hitung kuadrat kedua sisi", fr"c = \sqrt{{{a**2:.1f} + {b**2:.1f}}}"),
            ("Jumlahkan kedua kuadrat", fr"c = \sqrt{{{a**2 + b**2:.1f}}}"),
            ("Hitung akar kuadrat", fr"c \approx {c:.3f}")
        ]
        
        for step, eq in steps:
            with st.expander(step):
                st.latex(eq)
        
        # Visual proof with squares
        st.markdown("### Bukti Visual dengan Persegi")
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Draw squares on each side
        s_a = Rectangle((0, 0), a, a, fill=True, color='red', alpha=0.3)
        s_b = Rectangle((0, 0), -b, -b, fill=True, color='blue', alpha=0.3)
        s_c = Rectangle((a, b), -c, -c, angle=math.degrees(math.atan(b/a))-45, 
                       fill=True, color='green', alpha=0.3)
        
        ax.add_patch(s_a)
        ax.add_patch(s_b)
        ax.add_patch(s_c)
        
        # Draw triangle
        triangle = Polygon([[0, 0], [a, 0], [0, b]], closed=True, 
                          fill=False, color='black', linewidth=2)
        ax.add_patch(triangle)
        
        # Labels
        ax.text(a/2, -0.5, f'a = {a}', ha='center')
        ax.text(-0.5, b/2, f'b = {b}', va='center')
        ax.text(a/4, b/4, f'c = {c:.2f}', rotation=math.degrees(math.atan(b/a))-90, 
               ha='center', va='center', bbox=dict(facecolor='white', alpha=0.8))
        
        ax.text(a*0.5, -a*0.7, f'a² = {a**2:.1f}', color='red')
        ax.text(-b*0.7, b*0.5, f'b² = {b**2:.1f}', color='blue')
        ax.text(a*0.8, b*1.2, f'c² = {c**2:.1f}', color='green')
        
        ax.set_xlim(-b-1, a+1)
        ax.set_ylim(-b-1, b+1)
        ax.axis('equal')
        ax.axis('off')
        st.pyplot(fig)

elif section == "Latihan Soal":
    st.subheader("Latihan Soal Teorema Pythagoras")
    st.markdown("""
    Uji pemahamanmu dengan latihan berikut. Pilih jawaban yang benar!
    """)
    
    with st.container():
        with st.expander("Soal 1: Segitiga dasar"):
            st.markdown("""
            Sebuah segitiga siku-siku memiliki sisi:
            - a = 6 cm
            - b = 8 cm
            Berapakah panjang sisi miring (c)?""")
            
            answer = st.radio("Pilih jawaban:", 
                            ("10 cm", "14 cm", "9 cm", "12 cm"),
                            key="q1")
            
            if answer == "10 cm":
                st.success("✅ Benar! 6² + 8² = 36 + 64 = 100 → √100 = 10 cm")
            else:
                st.error("❌ Coba lagi! Gunakan rumus c = √(a² + b²)")

        with st.expander("Soal 2: Aplikasi nyata"):
            st.markdown("""
            Sebuah tangga sepanjang 5 meter bersandar pada tembok. 
            Jika dasar tangga berjarak 3 meter dari tembok, 
            seberapa tinggi tembok yang dicapai tangga?""")
            
            answer = st.radio("Pilih jawaban:", 
                            ("4 meter", "5 meter", "3 meter", "6 meter"),
                            key="q2")
            
            if answer == "4 meter":
                st.success("✅ Benar! √(5² - 3²) = √(25-9) = √16 = 4 meter")
            else:
                st.error("❌ Salah. Tempatkan nilai yang tepat dalam rumus Pythagoras")

        with st.expander("Soal 3: Tantangan"):
            st.markdown("""
            Jika sisi miring segitiga siku-siku adalah 13 cm 
            dan salah satu sisi lainnya 5 cm, berapa panjang sisi ketiga?""")
            
            answer = st.radio("Pilih jawaban:", 
                            ("12 cm", "8 cm", "9 cm", "10 cm"),
                            key="q3")
            
            if answer == "12 cm":
                st.success("✅ Tepat! √(13² - 5²) = √(169-25) = √144 = 12 cm")
            else:
                st.error("❌ Coba hitung lagi. Gunakan rumus b = √(c² - a²)")

else:  # Real-world applications
    st.subheader("Aplikasi Teorema Pythagoras di Dunia Nyata")
    st.markdown("""
    Teorema Pythagoras digunakan dalam berbagai bidang kehidupan:
    """)
    
    applications = [
        {
            "title": "Konstruksi Bangunan",
            "icon": "🏗️",
            "description": "Memastikan sudut siku-siku saat membangun rumah, memeriksa kerataan lantai, dan membuat struktur yang stabil."
        },
        {
            "title": "Navigasi",
            "icon": "🧭",
            "description": "Menghitung jarak terpendek antara dua titik di peta (GPS menggunakan prinsip ini untuk memperkirakan jarak)."
        },
        {
            "title": "Komputer Grafis",
            "icon": "🖥️",
            "description": "Dalam game dan animasi 3D, untuk menghitung jarak antara objek dan efek perspektif."
        },
        {
            "title": "Olahraga",
            "icon": "⚽",
            "description": "Menentukan sudut tendangan optimal atau menghitung jarak lapangan dalam olahraga seperti baseball."
        }
    ]
    
    cols = st.columns(2)
    for i, app in enumerate(applications):
        with cols[i%2]:
            with st.container():
                st.markdown(f"""
                <div style="padding:1rem; background:#e3f2fd; border-radius:10px; margin-bottom:1rem;">
                    <h3>{app['icon']} {app['title']}</h3>
                    <p>{app['description']}</p>
                </div>
                """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#666; font-size:0.9em;">
    Virtual Lab Matematika SMP - Teorema Pythagoras<br>
    Dibuat dengan Streamlit oleh Guru Matematika
</div>
""", unsafe_allow_html=True)
