import streamlit as st
import os
from io import BytesIO
from markdown2 import markdown

# Sayfa başlığı
# 🔍 Arama kutusu
st.markdown("---")
st.subheader("🔍 İçerik Arama")
search_query = st.text_input("Aramak istediğiniz kelimeyi girin (örn: ISO 13485, glukoz, validasyon):")

if search_query:
    st.markdown(f"#### 🔎 “{search_query}” kelimesiyle eşleşen bölümler:")
    results_found = False

    for file_name, title in sections:
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as f:
                content = f.read()
                if search_query.lower() in content.lower():
                    results_found = True
                    st.markdown(f"---\n### 📄 {title}", unsafe_allow_html=True)
                    # Eşleşen satırları vurgulayarak göster
                    for line in content.splitlines():
                        if search_query.lower() in line.lower():
                            st.markdown(f"🔸 `{line.strip()}`")

    if not results_found:
        st.info("🔍 Aradığınız kelime hiçbir bölümde bulunamadı.")

st.set_page_config(page_title="ISO 15197:2013 Standardı", layout="wide")
st.title("📘 ISO 15197:2013 Standardı Web Yayını")

# Dosya listesi
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

# Menü
titles = [title for _, title in sections]
selected_title = st.sidebar.selectbox("📂 Bölüm Seçin", titles)
selected_file = next((f for f, t in sections if t == selected_title), None)

# İçerik göster
if selected_file and os.path.exists(selected_file):
    st.markdown(f"## 📄 {selected_title}")
    with open(selected_file, "r", encoding="utf-8") as f:
        content = f.read()
        st.markdown(content, unsafe_allow_html=True)
    # İçeriği göster
    st.markdown(content, unsafe_allow_html=True)

    # Not kutusu
    st.markdown("### ✍️ Kendi Notunuzu Yazın")
    user_note = st.text_area(f"📝 {selected_title} için kişisel notlarınız:", key=selected_file)

    if user_note:
        st.info("🧠 Bu not sayfa yenilenince kaybolacaktır. Kalıcı kayıt özelliği yakında!")

    # HTML indir butonu
    if st.button("⬇️ HTML olarak indir"):
        html = markdown(content)
        buffer = BytesIO(html.encode("utf-8"))
        st.download_button(
            label="📥 HTML Dosyasını İndir",
            data=buffer.getvalue(),
            file_name=selected_file.replace(".md", ".html"),
            mime="text/html"
        )
else:
    st.warning("❗️ Seçilen bölümün dosyası bulunamadı.")
