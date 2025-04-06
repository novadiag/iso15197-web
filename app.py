import streamlit as st
import os

# Sayfa başlığı ve yapılandırma
st.set_page_config(page_title="ISO 15197:2013 Standardı", layout="wide")
st.title("📘 ISO 15197:2013 Standardı Web Yayını")

# Dosya listesi (dosya adı, görünen başlık)
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

# Sidebar menü
section_titles = [title for _, title in sections]
selected_title = st.sidebar.selectbox("📂 Bölüm Seçin", section_titles)

# Seçilen başlığa karşılık gelen dosyayı bul
selected_file = next((f for f, t in sections if t == selected_title), None)

# Dosyayı oku ve göster
if selected_file and os.path.exists(selected_file):
    st.markdown(f"## 📄 {selected_title}")
    with open(selected_file, "r", encoding="utf-8") as f:
        content = f.read()
        st.markdown(content, unsafe_allow_html=True)
else:
    st.warning("❗️ Seçilen bölümün dosyası bulunamadı.")
