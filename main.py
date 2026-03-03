import streamlit as st

st.set_page_config(page_title="ECO-THYROID AI", layout="centered")

# -------------------------------------------------
# SESSION STATE TANIMLARI
# -------------------------------------------------

if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "remembered_user" not in st.session_state:
    st.session_state.remembered_user = ""

# -------------------------------------------------
# LOGIN & REGISTER EKRANI
# -------------------------------------------------

if not st.session_state.logged_in:

    st.title("🌿 ECO-THYROID AI")

    secim = st.radio("Seçim Yap", ["Giriş Yap", "Kayıt Ol"])

    username = st.text_input("Kullanıcı Adı")
    password = st.text_input("Şifre", type="password")

    if secim == "Kayıt Ol":

        if st.button("Kayıt Ol"):
            if username in st.session_state.users:
                st.error("Bu kullanıcı zaten var.")
            elif username == "" or password == "":
                st.warning("Boş alan bırakmayın.")
            else:
                st.session_state.users[username] = password
                st.success("Kayıt başarılı. Giriş yapabilirsiniz.")

    else:

        beni_hatirla = st.checkbox("Beni Hatırla")

        if st.button("Giriş Yap"):
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.logged_in = True

                if beni_hatirla:
                    st.session_state.remembered_user = username

                st.success("Giriş başarılı.")
                st.rerun()
            else:
                st.error("Hatalı kullanıcı adı veya şifre.")

# -------------------------------------------------
# ANA UYGULAMA
# -------------------------------------------------

else:

    st.title("🌿 ECO-THYROID AI")

    st.success("Yiyiniz, içiniz fakat israf etmeyiniz. Çünkü Allah israf edenleri sevmez. (A'raf 31)")

    if st.button("Çıkış Yap"):
        st.session_state.logged_in = False
        st.rerun()

    st.header("👤 Kullanıcı Bilgileri")

    cinsiyet = st.radio("Cinsiyet", ["Kadın", "Erkek"])

    age = st.number_input("Yaş", min_value=10, max_value=100, value=30)

    height = st.number_input("Boy (cm)", min_value=100, max_value=220, value=160)

    weight = st.number_input("Kilo (kg)", min_value=30, max_value=200, value=60)

    st.header("🧬 Tiroid Sağlık Bilgileri")

    hashimoto = st.checkbox("Hashimoto var mı?")
    hipotiroid = st.checkbox("Hipotiroidi var mı?")
    hipertiroid = st.checkbox("Hipertiroidi var mı?")
    aile_oykusu = st.checkbox("Ailede tiroid hastalığı var mı?")

    ilac = st.radio(
        "Levotiroksin kullanıyor musunuz?",
        ["Yok", "Evet - Düzenli", "Evet - Düzensiz"]
    )

    tsh = st.number_input("TSH değeri", min_value=0.0, max_value=20.0, value=2.5)

    # -------------------------------------------------
    # HESAPLAMA
    # -------------------------------------------------

    if st.button("Metabolik Analiz Yap"):

        # VKI
        boy_metre = height / 100
        vki = weight / (boy_metre ** 2)

        # BMR (Mifflin-St Jeor)
        if cinsiyet == "Kadın":
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age + 5

        # -------------------------------------------------
        # RİSK HESABI
        # -------------------------------------------------

        risk_puan = 0

        # Demografik
        if cinsiyet == "Kadın":
            risk_puan += 1

        if age >= 40:
            risk_puan += 1

        if vki >= 30:
            risk_puan += 1

        # Klinik
        if hashimoto:
            risk_puan += 2

        if hipotiroid:
            risk_puan += 2

        if aile_oykusu:
            risk_puan += 1

        if tsh > 4:
            risk_puan += 2
        elif 2.5 < tsh <= 4:
            risk_puan += 1

        if ilac == "Evet - Düzensiz":
            risk_puan += 1
        elif ilac == "Evet - Düzenli":
            risk_puan -= 1

        # -------------------------------------------------
        # METABOLİZMA ADAPTASYONU
        # -------------------------------------------------

        metabolizma_katsayi = 1.0

        if hashimoto:
            metabolizma_katsayi -= 0.10

        if hipotiroid and age >= 40:
            metabolizma_katsayi -= 0.05

        if vki >= 30:
            metabolizma_katsayi -= 0.05

        if tsh > 4:
            metabolizma_katsayi -= 0.05

        if ilac == "Evet - Düzenli":
            metabolizma_katsayi += 0.05

        if ilac == "Evet - Düzensiz":
            metabolizma_katsayi -= 0.05

        duzeltilmis_bmr = bmr * metabolizma_katsayi

        # -------------------------------------------------
        # SONUÇLAR
        # -------------------------------------------------

        st.subheader("📊 Sonuçlar")

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
        st.write(f"🔥 Düzeltilmiş Metabolizma: {int(duzeltilmis_bmr)} kcal/gün")

        st.subheader("🧠 Tiroid Risk Analizi")

        if risk_puan <= 2:
            st.success("Düşük Risk")
        elif 3 <= risk_puan <= 5:
            st.warning("Orta Risk")
        else:
            st.error("Yüksek Risk")
