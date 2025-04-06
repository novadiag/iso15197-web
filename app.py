import streamlit as st
import os

# Sayfa başlığı
st.set_page_config(page_title="ISO 15197:2013 Standardı", layout="wide")
st.title("📘 ISO 15197:2013 Standardı Web Yayını")

# Dosya listesi (manuel, sıralı ve güvenli)
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

# Her bölümü sırayla yükle ve göster
for file_name in section_files:
    if os.path.exists(file_name):
        st.markdown(f"---\n## 📄 {file_name.replace('_', ' ').replace('.md', '').title()}", unsafe_allow_html=True)
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
            st.markdown(content, unsafe_allow_html=True)
    else:
        st.error(f"❌ Dosya bulunamadı: `{file_name}`")
