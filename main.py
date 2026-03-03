# -------------------
# GİRİŞ / KAYIT EKRANI
# -------------------
if not st.session_state.logged_in:

    st.subheader("Giriş / Kayıt")

    secim = st.radio("Seçim Yapın", ["Giriş Yap", "Kayıt Ol"])

    if secim == "Giriş Yap":
        email = st.text_input("E-mail")
        password = st.text_input("Şifre", type="password")

        if st.button("Giriş"):
            if email and password:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Alanlar boş olamaz")

    elif secim == "Kayıt Ol":
        new_email = st.text_input("E-mail")
        new_password = st.text_input("Şifre", type="password")

        if st.button("Kaydol"):
            if new_email and new_password:
                st.success("Kayıt başarılı 🎉")
            else:
                st.error("Alanlar boş olamaz")

# -------------------
# ANA SİSTEM EKRANI
# -------------------
else:

    # 🌿 Tek Ayet
    st.success(
        "Yiyiniz, içiniz fakat israf etmeyiniz. Çünkü Allah israf edenleri sevmez. (A'raf 31)"
    )

    st.header("Kullanıcı Bilgileri")

    gender = st.radio("Cinsiyet", ["Kadın", "Erkek"])
    age = st.number_input("Yaş", min_value=10, max_value=100)
    height = st.number_input("Boy (cm)", min_value=100, max_value=220)
    weight = st.number_input("Kilo (kg)", min_value=30, max_value=200)

    if st.button("Bilgileri Kaydet"):
        st.success("Bilgiler kaydedildi ✅")

    if st.button("Çıkış Yap"):
        st.session_state.logged_in = False
        st.rerun()
        # -------------------------
# VKI ve BMR Hesaplama
# -------------------------

if st.button("VKI & BMR Hesapla"):

    boy_metre = height / 100
    vki = weight / (boy_metre ** 2)

    if cinsiyet == "Kadın":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
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
    
