import streamlit as st
import os
from io import BytesIO
from markdown2 import markdown

# ✅ Sayfa yapılandırması (İLK SATIR OLMALI)
st.set_page_config(page_title="ISO 15197:2013 Standardı", layout="wide")

# 📘 Başlık
st.title("📘 ISO 15197:2013 Standardı Web Yayını")

# 📁 Bölüm listesi (dosya adı, görünen başlık)
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
                    for line in content.splitlines():
                        if search_query.lower() in line.lower():
                            st.markdown(f"🔸 `{line.strip()}`")
    if not results_found:
        st.info("🔍 Aradığınız kelime hiçbir bölümde bulunamadı.")
else:
    # 📂 Menüden bölüm seç
    titles = [title for _, title in sections]
    selected_title = st.sidebar.selectbox("📂 Bölüm Seçin", titles)
    selected_file = next((f for f, t in sections if t == selected_title), None)

    if selected_file and os.path.exists(selected_file):
        st.markdown(f"## 📄 {selected_title}")
        with open(selected_file, "r", encoding="utf-8") as f:
            content = f.read()
            st.markdown(content, unsafe_allow_html=True)

        # 📝 Not yazma alanı
        st.markdown("### ✍️ Kendi Notunuzu Yazın")
        user_note = st.text_area(f"📝 {selected_title} için kişisel notlarınız:", key=selected_file)
        if user_note:
            st.info("🧠 Bu not sayfa yenilenince kaybolacaktır. Kalıcı kayıt özelliği yakında!")

        # 💾 HTML olarak indir
        if st.button("⬇️ HTML olarak indir"):
            html = markdown(content)
            buffer = BytesIO(html.encode("utf-8"))
            st.download_button(
                label="📥 HTML Dosyasını İndir",
                data=buffer.getvalue(),
                file_name=selected_file.replace(".md", ".html"),
                mime="text/html"
            )

        # 📎 Ek dosyaları göster
        download_path = os.path.join("downloads", selected_file.replace(".md", ""))
        if os.path.isdir(download_path):
            st.markdown("### 📎 Bu bölüme ait ek dosyalar")
            for filename in os.listdir(download_path):
                filepath = os.path.join(download_path, filename)
                with open(filepath, "rb") as f:
                    st.download_button(
                        label=f"📥 {filename}",
                        data=f,
                        file_name=filename,
                        mime="application/octet-stream"
                    )
    else:
        st.warning("❗️ Seçilen bölümün dosyası bulunamadı.")
