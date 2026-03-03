import streamlit as st

st.set_page_config(page_title="ECO-THYROID AI", layout="centered")

st.title("ECO-THYROID AI")

st.success("Yiyiniz, içiniz fakat israf etmeyiniz. Çünkü Allah israf edenleri sevmez. (A'raf 31)")

st.header("Kullanıcı Bilgileri")

# -------------------------
# Kullanıcı Giriş Bilgileri
# -------------------------

cinsiyet = st.radio("Cinsiyet", ["Kadın", "Erkek"])

age = st.number_input("Yaş", min_value=10, max_value=100, value=30)

height = st.number_input("Boy (cm)", min_value=100, max_value=220, value=160)

weight = st.number_input("Kilo (kg)", min_value=30, max_value=200, value=60)

# -------------------------
# VKI ve BMR Hesaplama
# -------------------------

if st.button("VKI & BMR Hesapla"):

    boy_metre = height / 100
    vki = weight / (boy_metre ** 2)

    # Mifflin-St Jeor Formülü
    if cinsiyet == "Kadın":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:  # Erkek
        bmr = 10 * weight + 6.25 * height - 5 * age + 5

    st.subheader("Metabolik Analiz")

    st.write(f"📊 VKİ: {round(vki,2)}")

    if vki < 18.5:
        st.warning("Zayıf")
    elif 18.5 <= vki < 25:
        st.success("Normal kilo")
    elif 25 <= vki < 30:
        st.warning("Fazla kilolu")
    else:
        st.error("Obez")

    st.write(f"🔥 BMR: {int(bmr)} kcal/gün")
