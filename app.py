import streamlit as st
import os

st.set_page_config(page_title="ISO 15197:2013 Standardı", layout="wide")

st.title("📘 ISO 15197:2013 Standardı Web Yayını")

# Bulunduğunuz dizindeki tüm .md dosyaları al
section_files = sorted([f for f in os.listdir(".") if f.endswith(".md")])

# Menü - bölüm seçimi
selected_section = st.sidebar.selectbox("📂 Bölüm Seçin", section_files)

# Seçilen dosyayı aç ve göster
with open(selected_section, "r", encoding="utf-8") as file:
    content = file.read()
    st.markdown(content, unsafe_allow_html=True)
import streamlit as st
import os

st.set_page_config(page_title="ISO 15197:2013 Standardı", layout="wide")

st.title("📘 ISO 15197:2013 Standardı Web Yayını")

# Bulunduğunuz dizindeki tüm .md dosyalarını al
section_files = sorted([
    f for f in os.listdir(".")
    if f.endswith(".md")
])

# Menüden bölüm seçimi
selected_section = st.sidebar.selectbox("📂 Bölüm Seçin", section_files)

# Seçilen dosyayı oku ve göster
with open(selected_section, "r", encoding="utf-8") as file:
    content = file.read()
    st.markdown(content, unsafe_allow_html=True)
import streamlit as st

st.set_page_config(page_title="ISO 15197:2013 Standardı", layout="wide")
st.title("📘 ISO 15197:2013 Standardı Web Yayını")

# Tüm bölümleri manuel listele
section_files = [
    "01_amac_ve_kapsam.md",
    "02_normatif_referanslar.md",
    "03_tanimlar.md",
    "04_tasarim_ve_gelistirme.md",
    "05_guvenlik_testleri.md",
    "06_analitik_performans.md",
    "07_ureticiden_bilgiler.md",
    "08_kullanici_performansi.md",
    "ek_a_girisim_maddeleri.md",
    "ek_b_izlenebilirlik.md",
    "ek_c_gerekce.md"
]

]

selected_section = st.sidebar.selectbox("📂 Bölüm Seçin", section_files)

# Markdown dosyasını oku ve göster
with open(selected_section, "r", encoding="utf-8") as file:
    content = file.read()
    st.markdown(content, unsafe_allow_html=True)
