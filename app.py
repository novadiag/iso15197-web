import streamlit as st
import os

# Sayfa başlığı ve yapı
st.set_page_config(page_title="ISO 15197:2013 Standardı", layout="wide")
st.title("📘 ISO 15197:2013 Standardı Web Yayını")

# Manuel tanımlı .md dosya listesi (sıralı)
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

# Her dosyayı sırayla yükle ve göster
for file_name in section_files:
    st.markdown(f"---\n### 📄 {file_name.replace('_', ' ').replace('.md', '').title()}", unsafe_allow_html=True)
    
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
            st.markdown(content, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"❌ Dosya bulunamadı: `{file_name}`")
    except Exception as e:
        st.error(f"🚫 {file_name} yüklenirken hata oluştu: {e}")
