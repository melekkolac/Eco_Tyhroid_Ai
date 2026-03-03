import streamlit as st

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------

if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "remember_me" not in st.session_state:
    st.session_state.remember_me = False

if "username" not in st.session_state:
    st.session_state.username = ""

# -------------------------------------------------
# LOGIN & REGISTER
# -------------------------------------------------

if not st.session_state.logged_in:

    st.title("🌿 ECO-THYROID AI")

    secim = st.radio("Seçim Yap", ["Giriş Yap", "Kayıt Ol"])

    username = st.text_input("Kullanıcı Adı")
    password = st.text_input("Şifre", type="password")

    if secim == "Kayıt Ol":
        if st.button("Kayıt Ol"):
            if username in st.session_state.users:
                st.error("Bu kullanıcı zaten var")
            else:
                st.session_state.users[username] = password
                st.success("Kayıt başarılı")

    if secim == "Giriş Yap":
        remember = st.checkbox("Beni Hatırla")

        if st.button("Giriş Yap"):
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.remember_me = remember
                st.success("Giriş başarılı")
                st.rerun()
            else:
                st.error("Hatalı giriş")

else:

    # -------------------------------------------------
    # KULLANICI PANELİ
    # -------------------------------------------------

    st.title("🌿 ECO-THYROID AI")

    st.write(“Yiyinin içiniz, fakat israf etmeyiniz. (A’raf 31)”)

    if st.button("Çıkış Yap"):
        st.session_state.logged_in = False
        st.rerun()

    st.subheader("👤 Kullanıcı Bilgileri")

    cinsiyet = st.radio("Cinsiyet", ["Kadın", "Erkek"])
    yas = st.number_input("Yaş", min_value=10, max_value=100, value=30)
    boy = st.number_input("Boy (cm)", min_value=120, max_value=220, value=160)
    kilo = st.number_input("Kilo (kg)", min_value=30, max_value=200, value=60)

    st.subheader("🧬 Tiroid Sağlık Bilgileri")

    hashimoto = st.checkbox("Hashimoto var mı?")
    hipotiroidi = st.checkbox("Hipotiroidi var mı?")
    hipertiroidi = st.checkbox("Hipertiroidi var mı?")
    aile = st.checkbox("Ailede tiroid hastalığı var mı?")

    ilac = st.radio(
        "Levotiroksin kullanıyor musunuz?",
        ["Yok", "Evet - Düzenli", "Evet - Düzensiz"]
    )

    tsh = st.number_input("TSH (0.4-4.0)", value=2.0)
    ft3 = st.number_input("Free T3 (2.3-4.2)", value=3.0)
    ft4 = st.number_input("Free T4 (0.8-1.8)", value=1.0)
    anti_tpo = st.number_input("Anti-TPO (0-35 normal)", value=20.0)

    if st.button("Metabolik Analiz Yap"):

        # -------------------------------------------------
        # VKİ
        # -------------------------------------------------

        vki = kilo / ((boy / 100) ** 2)

        # -------------------------------------------------
        # BMR (Mifflin-St Jeor)
        # -------------------------------------------------

        if cinsiyet == "Kadın":
            bmr = 10 * kilo + 6.25 * boy - 5 * yas - 161
        else:
            bmr = 10 * kilo + 6.25 * boy - 5 * yas + 5

        # -------------------------------------------------
        # METABOLİK DÜZELTME KATSAYISI
        # -------------------------------------------------

        katsayi = 1.0
        risk = 0

        if hashimoto:
            katsayi -= 0.10
            risk += 2

        if hipotiroidi:
            katsayi -= 0.10
            risk += 2

        if hipertiroidi:
            katsayi += 0.05
            risk += 1

        if aile:
            risk += 1

        if tsh > 4:
            katsayi -= 0.05
            risk += 1

        if ft4 < 0.8:
            katsayi -= 0.05
            risk += 1

        if ft3 < 2.3:
            katsayi -= 0.05
            risk += 1

        if anti_tpo > 100:
            katsayi -= 0.08
            risk += 2
        elif anti_tpo > 35:
            katsayi -= 0.05
            risk += 1

        if ilac == "Evet - Düzenli":
            katsayi += 0.05

        if ilac == "Evet - Düzensiz":
            katsayi -= 0.05
            risk += 1

        duzeltilmis_bmr = bmr * katsayi

        # -------------------------------------------------
        # SONUÇLAR
        # -------------------------------------------------

        st.subheader("📊 Sonuçlar")

        st.progress(min(vki / 40, 1.0))

        if vki < 18.5:
            st.info("Zayıf")
        elif vki < 25:
            st.success("Normal Kilolu")
        elif vki < 30:
            st.warning("Fazla Kilolu")
        else:
            st.error("Obez")

        st.write(f"VKİ: {round(vki,2)}")
        st.write(f"BMR: {int(bmr)} kcal/gün")
        st.write(f"Düzeltilmiş Metabolizma: {int(duzeltilmis_bmr)} kcal/gün")

        st.subheader("🧠 Tiroid Risk Analizi")

        if risk <= 2:
            st.success("Düşük Risk")
        elif risk <= 5:
            st.warning("Orta Risk")
        else:
            st.error("Yüksek Risk")
