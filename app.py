import streamlit as st
import os

st.set_page_config(page_title="ISO 15197:2013 Standardı", layout="wide")
st.title("📘 ISO 15197:2013 Standardı Web Yayını")

# Dosya ve başlık listesi
sections = [
    ("01_amac_ve_kapsam.md", "1. Amaç ve Kapsam"),
    ("02_normatif_referanslar.md", "2. Normatif Referanslar"),
    ("03_tanimlar.md", "3. Tanımlar"),
    ("04_tasarim_ve_gelistirme.md", "4. Tasarım ve Geliştirme"),
    ("05_guvenlik_testleri.md", "5. Güvenlik Testleri"),
    ("06_analitik_performans.md", "6. Analitik Performans"),
    ("07_ureticiden_bilgiler.md", "7. Üreticiden Bilgiler"),
    ("08_kullanici_performansi.md", "8. Kullanıcı Performansı"),
    ("ek_a_girisim_maddeleri.md", "Ek A - Girişim Maddeleri"),
    ("ek_b_izlenebilirlik.md", "Ek B - İzlenebilirlik Zinciri"),
    ("ek_c_gerekce.md", "Ek C - Performans Gerekçeleri")
]

# İçindekiler bölümü
st.markdown("## 📑 Bölümler")
for _, title in sections:
    anchor = title.lower().replace(" ", "-").replace(".", "").replace("ç", "c").replace("ı", "i").replace("ğ", "g").replace("ü", "u").replace("ö", "o").replace("ş", "s")
    st.markdown(f"- [{title}](#{anchor})")

# İçerikleri sırayla göster
for file_name, title in sections:
    anchor = title.lower().replace(" ", "-").replace(".", "").replace("ç", "c").replace("ı", "i").replace("ğ", "g").replace("ü", "u").replace("ö", "o").replace("ş", "s")
    st.markdown(f"<hr><h2 id='{anchor}'>📄 {title}</h2>", unsafe_allow_html=True)
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
            st.markdown(content, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"❗️ {file_name} bulunamadı.")
    except Exception as e:
        st.error(f"🚫 {file_name} yüklenirken hata oluştu: {e}")
