import streamlit as st
import math

st.set_page_config(
    page_title="Virtual Lab Kesebangunan - Segitiga",
    page_icon="🔺",
    layout="centered",
)

# Styling and animation CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');
    body, .main {
        font-family: 'Poppins', sans-serif;
        color: #1f2937;
        background-color: #f3f4f6;
        margin: 0; padding: 0;
    }
    h1 {
        font-weight: 700;
        font-size: 2.8rem;
        margin-bottom: 0.2rem;
        color: #2563eb;
        text-align: center;
    }
    h2 {
        color: #374151;
        margin-top: 2rem;
        margin-bottom: 0.8rem;
        font-weight: 600;
    }
    .container {
        max-width: 900px;
        margin: 0 auto 3rem auto;
        background: white;
        padding: 2rem 2.5rem;
        border-radius: 1rem;
        box-shadow: 0 8px 20px rgb(59 130 246 / 0.2);
    }
    .description {
        font-size: 1rem;
        line-height: 1.6;
        color: #4b5563;
        margin-bottom: 1.5rem;
    }
    .triangle-svg {
        width: 100%;
        max-width: 400px;
        margin: 1.5rem auto;
        display: block;
    }
    .angle-label {
        font-weight: 700;
        font-size: 1.1rem;
        fill: #2563eb;
        font-family: 'Poppins', sans-serif;
        user-select: none;
    }
    .side-label {
        font-weight: 600;
        fill: #374151;
        font-family: 'Poppins', sans-serif;
        user-select: none;
    }
    .angle-arc {
        fill: none;
        stroke: #2563eb;
        stroke-width: 3;
    }
    /* Animations for angle arcs to highlight */
    @keyframes pulseBlue {
        0%, 100% { stroke-width: 3; opacity: 1; }
        50% { stroke-width: 8; opacity: 0.5; }
    }
    .animate-arc {
        animation: pulseBlue 2.5s ease-in-out infinite;
    }

    /* Section for angle relations */
    .relation-svg {
        width: 100%;
        max-width: 380px;
        margin: 1rem auto 2rem auto;
        display: block;
    }
    .relation-description {
        font-size: 1rem;
        color: #374151;
        line-height: 1.5;
    }

    /* Highlighted angles style */
    .highlight-angle {
        stroke: #ef4444;
        stroke-width: 6 !important;
    }
    .highlight-text {
        fill: #b91c1c !important;
        font-weight: 800 !important;
    }

    /* Input area */
    .quiz-input label {
        font-weight: 600;
        margin-bottom: 0.3rem;
        display: block;
        color: #1f2937;
    }
    .quiz-input input, .quiz-input select {
        width: 100%;
        padding: 0.4rem 0.6rem;
        font-size: 1rem;
        border: 1.5px solid #9ca3af;
        border-radius: 0.375rem;
        margin-bottom: 1rem;
    }
    .quiz-feedback {
        font-weight: 700;
        margin-top: 1rem;
    }
    .correct {
        color: #22c55e;
    }
    .incorrect {
        color: #ef4444;
    }

    /* Responsive tweaks */
    @media (max-width: 480px) {
        .container {
            padding: 1.5rem 1.5rem;
        }
        h1 {
            font-size: 2rem;
        }
        h2 {
            font-size: 1.25rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page Header
st.markdown("<h1>Virtual Lab Kesebangunan - Segitiga</h1>", unsafe_allow_html=True)
st.markdown("""
<p class="description">
Selamat datang di virtual lab kesebangunan! Kamu dapat mengubah sudut segitiga dan
belajar tentang konsep sudut berhadapan, sudut sehadap, dan sudut berotlak belakang
dengan animasi menarik.
</p>
""", unsafe_allow_html=True)

# Triangle angle inputs
st.markdown("<h2>Atur Sudut Segitiga</h2>", unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns(2)
    angle1 = col1.slider("Sudut A (derajat)", min_value=1, max_value=178, value=60, step=1)
    angle2 = col2.slider("Sudut B (derajat)", min_value=1, max_value=178, value=60, step=1)
    # Ensure sum less than 180, else fix
    if angle1 + angle2 >= 179:
        angle2 = 179 - angle1
        st.warning("Penyesuaian otomatis: Sudut B disesuaikan agar jumlah sudut kurang dari 180 derajat.")
    angle3 = 180 - angle1 - angle2

# Calculate triangle vertex coordinates (2D coordinates for SVG)
# We'll fix base side horizontal length and compute coordinates with law of cosines
base_length = 300  # fixed base in pixels

# Calculate points:
# A at (0,0)
# B at (base_length, 0)
# C coordinates by 2 angles

# Using angles, find point C using law of sines:
# angle C = angle3
# side a = BC, side b = AC, base c = AB = base_length

# From Law of Sines:
# a / sin A = b / sin B = c / sin C

# Calculate length sides:
# side a opposite to angle A, side b opposite to angle B
sinA = math.sin(math.radians(angle1))
sinB = math.sin(math.radians(angle2))
sinC = math.sin(math.radians(angle3))

# Side a = length of BC = c * (sin A / sin C)
side_a = base_length * sinA / sinC
# Side b = length of AC = c * (sin B / sin C)
side_b = base_length * sinB / sinC

# Coordinates:
# A = (0, 0)
# B = (base_length, 0)
# C = (xC, yC)
# Using side lengths and base, we calculate C
# Base AB along x-axis from 0 to base_length
# Using coordinate formula:
# x_C = side_b * cos(angle at B)
# y_C = side_b * sin(angle at B)

angleB_rad = math.radians(angle2)
xC = side_b * math.cos(angleB_rad)
yC = side_b * math.sin(angleB_rad)

# Offset all coords to fit inside viewBox with margin
margin = 40
min_x = min(0, base_length, xC)
min_y = min(0, 0, yC)
offset_x = -min_x + margin
offset_y = -min_y + margin

Ax = 0 + offset_x
Ay = 0 + offset_y
Bx = base_length + offset_x
By = 0 + offset_y
Cx = xC + offset_x
Cy = yC + offset_y

svg_width = base_length + offset_x * 2 + 40
svg_height = yC + offset_y * 2 + 40

# Triangle SVG with arcs for angles
triangle_svg = f"""
<svg width="{svg_width}px" height="{svg_height}px" viewBox="0 0 {svg_width} {svg_height}" role="img" aria-label="Segitiga dengan sudut yang bisa diubah">
  <!-- Triangle sides -->
  <line x1="{Ax}" y1="{Ay}" x2="{Bx}" y2="{By}" stroke="#2563eb" stroke-width="4"/>
  <line x1="{Bx}" y1="{By}" x2="{Cx}" y2="{Cy}" stroke="#2563eb" stroke-width="4"/>
  <line x1="{Cx}" y1="{Cy}" x2="{Ax}" y2="{Ay}" stroke="#2563eb" stroke-width="4"/>

  <!-- Angle arcs (small arcs at each vertex) -->
  <!-- Angle A arc -->
  <path d="
    M {Ax + 30} {Ay}
    A 30 30 0 0 1 {Ax + 11} {Ay + 28}
  " class="angle-arc animate-arc"/>
  <text x="{Ax + 10}" y="{Ay + 50}" class="angle-label">A: {angle1}°</text>

  <!-- Angle B arc -->
  <path d="
    M {Bx - 30} {By}
    A 30 30 0 0 1 {Bx - 11} {By + 28}
  " class="angle-arc animate-arc"/>
  <text x="{Bx - 50}" y="{By + 50}" class="angle-label">B: {angle2}°</text>

  <!-- Angle C arc -->
  <path d="
    M {Cx} {Cy}
    m -28 0
    A 28 28 0 0 1 {Cx + (28 * math.cos(math.radians(angle3))):.2f} {Cy - (28 * math.sin(math.radians(angle3))):.2f}
  " class="angle-arc animate-arc"/>
  <text x="{Cx - 65}" y="{Cy + 10}" class="angle-label">C: {angle3}°</text>

  <!-- Vertices labels -->
  <text x="{Ax - 20}" y="{Ay + 20}" class="side-label">A</text>
  <text x="{Bx + 10}" y="{By + 20}" class="side-label">B</text>
  <text x="{Cx - 10}" y="{Cy - 10}" class="side-label">C</text>
</svg>
"""

st.markdown("<h2>Segitiga Dinamis</h2>", unsafe_allow_html=True)
st.markdown(triangle_svg, unsafe_allow_html=True)

# Explanation text about sum of angles
st.markdown("""
<p class="description">
Segitiga memiliki <strong>jumlah sudut 180°</strong>. Kamu dapat mengubah Sudut A dan Sudut B, 
dan Sudut C akan dihitung secara otomatis.
</p>
""", unsafe_allow_html=True)


# Section for angle relations with animations and explanations

st.markdown("<h2>Sudut Berhadapan (Vertically Opposite Angles)</h2>", unsafe_allow_html=True)
st.markdown("""
<p class="relation-description">
Sudut berhadapan adalah sudut yang berada berhadapan secara langsung pada dua garis yang saling berpotongan. Sudut-sudut ini selalu sama besar.
</p>
""", unsafe_allow_html=True)
# SVG for vertically opposite angles showing intersecting lines
vert_angle_svg = """
<svg class="relation-svg" viewBox="0 0 300 200" aria-label="Sudut Berhadapan">
  <!-- intersecting lines -->
  <line x1="20" y1="180" x2="280" y2="20" stroke="#2563eb" stroke-width="4"/>
  <line x1="20" y1="20" x2="280" y2="180" stroke="#2563eb" stroke-width="4"/>
  <!-- angles -->
  <circle cx="75" cy="75" r="30" fill="none" stroke="#ef4444" stroke-width="6" class="animate-arc"/>
  <circle cx="225" cy="125" r="30" fill="none" stroke="#ef4444" stroke-width="6" class="animate-arc"/>
  <!-- angle text -->
  <text x="55" y="85" fill="#b91c1c" font-weight="700" font-size="20">α</text>
  <text x="205" y="135" fill="#b91c1c" font-weight="700" font-size="20">α</text>
</svg>
"""
st.markdown(vert_angle_svg, unsafe_allow_html=True)

st.markdown("<h2>Sudut Sehadap (Corresponding Angles)</h2>", unsafe_allow_html=True)
st.markdown("""
<p class="relation-description">
Sudut sehadap adalah sudut-sudut yang terletak pada posisi yang sama di dua garis sejajar dan sebuah garis transversal. Sudut ini memiliki besar yang sama.
</p>
""", unsafe_allow_html=True)
# SVG for corresponding angles with parallel lines and transversal
corresponding_svg = """
<svg class="relation-svg" viewBox="0 0 300 200" aria-label="Sudut Sehadap">
  <!-- parallel lines -->
  <line x1="30" y1="50" x2="270" y2="50" stroke="#2563eb" stroke-width="4" />
  <line x1="30" y1="150" x2="270" y2="150" stroke="#2563eb" stroke-width="4" />
  <!-- transversal -->
  <line x1="180" y1="10" x2="120" y2="190" stroke="#2563eb" stroke-width="4" />
  <!-- angles -->
  <circle cx="160" cy="50" r="25" fill="none" stroke="#ef4444" stroke-width="6" class="animate-arc"/>
  <circle cx="140" cy="150" r="25" fill="none" stroke="#ef4444" stroke-width="6" class="animate-arc"/>
  <!-- angle text -->
  <text x="150" y="60" fill="#b91c1c" font-weight="700" font-size="20">β</text>
  <text x="130" y="140" fill="#b91c1c" font-weight="700" font-size="20">β</text>
</svg>
"""
st.markdown(corresponding_svg, unsafe_allow_html=True)

st.markdown("<h2>Sudut Berotlak Belakang (Alternate Interior Angles)</h2>", unsafe_allow_html=True)
st.markdown("""
<p class="relation-description">
Sudut berotlak belakang adalah sudut-sudut yang terletak di sisi berlawanan garis transversal dan di antara dua garis sejajar. Sudut ini memiliki besar yang sama.
</p>
""", unsafe_allow_html=True)
# SVG for alternate interior angles animation
alt_interior_svg = """
<svg class="relation-svg" viewBox="0 0 300 200" aria-label="Sudut Berotlak Belakang">
  <!-- parallel lines -->
  <line x1="30" y1="50" x2="270" y2="50" stroke="#2563eb" stroke-width="4" />
  <line x1="30" y1="150" x2="270" y2="150" stroke="#2563eb" stroke-width="4" />
  <!-- transversal -->
  <line x1="120" y1="10" x2="180" y2="190" stroke="#2563eb" stroke-width="4" />
  <!-- angles -->
  <circle cx="160" cy="50" r="25" fill="none" stroke="#ef4444" stroke-width="6" class="animate-arc"/>
  <circle cx="140" cy="150" r="25" fill="none" stroke="#ef4444" stroke-width="6" class="animate-arc"/>
  <!-- angle text -->
  <text x="150" y="60" fill="#b91c1c" font-weight="700" font-size="20">γ</text>
  <text x="130" y="140" fill="#b91c1c" font-weight="700" font-size="20">γ</text>
</svg>
"""
st.markdown(alt_interior_svg, unsafe_allow_html=True)

# Quiz like interactive section
st.markdown("<h2>Kuis Interaktif Sudut</h2>", unsafe_allow_html=True)
st.markdown("""
<p>Untuk membantu pemahaman, coba pilih pernyataan yang benar tentang sudut-sudut berwarna merah pada ilustrasi di atas. Sudut berhadapan, sudut sehadap, atau sudut berotlak belakang?</p>
""", unsafe_allow_html=True)

quiz_option = st.selectbox(
    "Pilih jenis sudut yang diilustrasikan (pilih satu):",
    options=["-- Pilih jenis sudut --", "Sudut Berhadapan (Vertically Opposite Angles)",
             "Sudut Sehadap (Corresponding Angles)",
             "Sudut Berotlak Belakang (Alternate Interior Angles)"]
)

feedback = ""
correct_answer = ""

if st.button("Periksa Jawaban"):
    if quiz_option == "-- Pilih jenis sudut --":
        feedback = ("<span class='incorrect'>Mohon pilih salah satu jenis sudut untuk diperiksa.</span>")
    elif quiz_option == "Sudut Berhadapan (Vertically Opposite Angles)":
        correct_answer = "Sudut Berhadapan (Vertically Opposite Angles)"
        feedback = ("<span class='correct'>Benar! Sudut berhadapan memiliki besar yang sama dan terletak berhadapan di titik perpotongan dua garis.</span>")
    elif quiz_option == "Sudut Sehadap (Corresponding Angles)":
        correct_answer = "Sudut Sehadap (Corresponding Angles)"
        feedback = ("<span class='correct'>Benar! Sudut sehadap sama besar dan berada pada posisi yang sama relatif terhadap dua garis sejajar dan transversal.</span>")
    elif quiz_option == "Sudut Berotlak Belakang (Alternate Interior Angles)":
        correct_answer = "Sudut Berotlak Belakang (Alternate Interior Angles)"
        feedback = ("<span class='correct'>Benar! Sudut berotlak belakang muncul di sisi berlawanan transversal dan sama besarnya.</span>")
    else:
        feedback = ("<span class='incorrect'>Jawaban salah, coba lagi.</span>")

    st.markdown(f"<div class='quiz-feedback'>{feedback}</div>", unsafe_allow_html=True)


# Footer note and credits
st.markdown("""
<div style="margin-top: 3rem; font-size: 0.9rem; color: #6b7280; text-align: center;">
    &copy; 2024 Virtual Lab Kesebangunan - Dibuat dengan penuh semangat menggunakan Streamlit.
</div>
""", unsafe_allow_html=True)

