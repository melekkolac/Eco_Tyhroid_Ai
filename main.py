import streamlit as st

st.set_page_config(page_title="ECO-THYROID AI", layout="centered")

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------

if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

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
                st.error("Bu kullanıcı zaten mevcut.")
            elif username == "" or password == "":
                st.warning("Boş alan bırakmayın.")
            else:
                st.session_state.users[username] = password
                st.success("Kayıt başarılı. Giriş yapabilirsiniz.")

    else:

        if st.button("Giriş Yap"):
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Hatalı kullanıcı adı veya şifre.")

# -------------------------------------------------
# ANA UYGULAMA
# -------------------------------------------------

else:

    st.title("🌿 ECO-THYROID AI")

    st.success("Yiyiniz, içiniz fakat israf etmeyiniz. (A'raf 31)")

    if st.button("Çıkış Yap"):
        st.session_state.logged_in = False
        st.rerun()

    # -------------------------------------------------
    # KULLANICI BİLGİLERİ
    # -------------------------------------------------

    st.header("👤 Kullanıcı Bilgileri")

    cinsiyet = st.radio("Cinsiyet", ["Kadın", "Erkek"])
    age = st.number_input("Yaş", min_value=10, max_value=100, value=30)
    height = st.number_input("Boy (cm)", min_value=100, max_value=220, value=160)
    weight = st.number_input("Kilo (kg)", min_value=30, max_value=200, value=60)

    # -------------------------------------------------
    # TİROİD BİLGİLERİ
    # -------------------------------------------------

    st.header("🧬 Tiroid Sağlık Bilgileri")

    hashimoto = st.checkbox("Hashimoto var mı?")
    hipotiroid = st.checkbox("Hipotiroidi var mı?")
    hipertiroid = st.checkbox("Hipertiroidi var mı?")
    aile_oykusu = st.checkbox("Ailede tiroid hastalığı var mı?")

    ilac = st.radio(
        "Levotiroksin kullanıyor musunuz?",
        ["Yok", "Evet - Düzenli", "Evet - Düzensiz"]
    )

    tsh = st.number_input("TSH (0.4 - 4.0 mIU/L)", min_value=0.0, max_value=20.0, value=2.5)
    ft3 = st.number_input("Free T3 (2.3 - 4.2 pg/mL)", min_value=0.0, max_value=10.0, value=3.0)
    ft4 = st.number_input("Free T4 (0.8 - 1.8 ng/dL)", min_value=0.0, max_value=5.0, value=1.2)

    # -------------------------------------------------
    # HESAPLAMA
    # -------------------------------------------------

    if st.button("Metabolik Analiz Yap"):

        # VKİ
        boy_m = height / 100
        vki = weight / (boy_m ** 2)

        # BMR (Mifflin)
        if cinsiyet == "Kadın":
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age + 5

        # -------------------------------------------------
        # RİSK PUANI
        # -------------------------------------------------

        risk = 0

        # Demografi
        if cinsiyet == "Kadın":
            risk += 1
        if age >= 40:
            risk += 1
        if vki >= 30:
            risk += 1

        # Klinik
        if hashimoto:
            risk += 2
        if hipotiroid:
            risk += 2
        if hipertiroid:
            risk += 2
        if aile_oykusu:
            risk += 1

        # TSH
        if tsh > 4:
            risk += 2
        elif 2.5 < tsh <= 4:
            risk += 1

        # Free T4
        if ft4 < 0.8:
            risk += 2
        elif ft4 > 1.8:
            risk += 1

        # Free T3
        if ft3 < 2.3:
            risk += 1
        elif ft3 > 4.2:
            risk += 2

        # İlaç
        if ilac == "Evet - Düzensiz":
            risk += 1
        elif ilac == "Evet - Düzenli":
            risk -= 1

        # -------------------------------------------------
        # METABOLİZMA ADAPTASYONU
        # -------------------------------------------------

        katsayi = 1.0

        if hashimoto:
            katsayi -= 0.10

        if hipotiroid:
            katsayi -= 0.07

        if tsh > 4:
            katsayi -= 0.05

        if ft4 < 0.8:
            katsayi -= 0.07

        if ft3 < 2.3:
            katsayi -= 0.05

        if ft3 > 4.2:
            katsayi += 0.05

        if ilac == "Evet - Düzenli":
            katsayi += 0.05

        if ilac == "Evet - Düzensiz":
            katsayi -= 0.05

        duzeltilmis_bmr = bmr * katsayi

        # -------------------------------------------------
        # SONUÇLAR
        # -------------------------------------------------

        st.subheader("📊 Sonuçlar")

        st.write(f"VKİ: {round(vki,2)}")

        if vki < 18.5:
            st.warning("Zayıf")
        elif vki < 25:
            st.success("Normal kilo")
        elif vki < 30:
            st.warning("Fazla kilolu")
        else:
            st.error("Obez")

        st.write(f"BMR: {int(bmr)} kcal/gün")
        st.write(f"Düzeltilmiş Metabolizma: {int(duzeltilmis_bmr)} kcal/gün")

        st.subheader("🧠 Tiroid Risk Analizi")

        if risk <= 2:
            st.success("Düşük Risk")
        elif risk <= 5:
            st.warning("Orta Risk")
        else:
            st.error("Yüksek Risk")
