import streamlit as st

st.set_page_config(page_title="ECO-THYROID AI", layout="centered")

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------

if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "remember_user" not in st.session_state:
    st.session_state.remember_user = ""

# -------------------------------------------------
# LOGIN & REGISTER
# -------------------------------------------------

if not st.session_state.logged_in:

    st.title("🌿 ECO-THYROID AI")

    secim = st.radio("Seçim Yap", ["Giriş Yap", "Kayıt Ol"])

    username = st.text_input("Kullanıcı Adı", value=st.session_state.remember_user)
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

        beni_hatirla = st.checkbox("Beni Hatırla")

        if st.button("Giriş Yap"):
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.logged_in = True

                if beni_hatirla:
                    st.session_state.remember_user = username
                else:
                    st.session_state.remember_user = ""

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

    # -----------------------------
    # KULLANICI BİLGİLERİ
    # -----------------------------

    st.header("👤 Kullanıcı Bilgileri")

    cinsiyet = st.radio("Cinsiyet", ["Kadın", "Erkek"])
    age = st.number_input("Yaş", 10, 100, 30)
    height = st.number_input("Boy (cm)", 100, 220, 160)
    weight = st.number_input("Kilo (kg)", 30, 200, 60)

    # -----------------------------
    # TİROİD BİLGİLERİ
    # -----------------------------

    st.header("🧬 Tiroid Sağlık Bilgileri")

    hashimoto = st.checkbox("Hashimoto var mı?")
    hipotiroid = st.checkbox("Hipotiroidi var mı?")
    hipertiroid = st.checkbox("Hipertiroidi var mı?")
    aile = st.checkbox("Ailede tiroid hastalığı var mı?")

    ilac = st.radio(
        "Levotiroksin kullanıyor musunuz?",
        ["Yok", "Evet - Düzenli", "Evet - Düzensiz"]
    )

    tsh = st.number_input("TSH (0.4-4.0)", 0.0, 20.0, 2.5)
    ft3 = st.number_input("Free T3 (2.3-4.2)", 0.0, 10.0, 3.0)
    ft4 = st.number_input("Free T4 (0.8-1.8)", 0.0, 5.0, 1.2)
    anti_tpo = st.number_input("Anti-TPO (0-35 normal)", 0.0, 2000.0, 10.0)

    # -----------------------------
    # HESAPLAMA
    # -----------------------------

    if st.button("Metabolik Analiz Yap"):

        boy_m = height / 100
        vki = weight / (boy_m ** 2)

        # BMR
        if cinsiyet == "Kadın":
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age + 5

        # -------------------------
        # RISK HESABI
        # -------------------------

        risk = 0

        if cinsiyet == "Kadın":
            risk += 1
        if age >= 40:
            risk += 1
        if vki >= 30:
            risk += 1

        if hashimoto:
            risk += 2
        if hipotiroid:
            risk += 2
        if hipertiroid:
            risk += 2
        if aile:
            risk += 1

        if tsh > 4:
            risk += 2
        elif 2.5 < tsh <= 4:
            risk += 1

        if ft4 < 0.8:
            risk += 2
        elif ft4 > 1.8:
            risk += 1

        if ft3 < 2.3:
            risk += 1
        elif ft3 > 4.2:
            risk += 2

        # Anti-TPO
        if anti_tpo > 100:
            risk += 3
        elif anti_tpo > 35:
            risk += 2

        if ilac == "Evet - Düzensiz":
            risk += 1
        elif ilac == "Evet - Düzenli":
            risk -= 1

        # -------------------------
        # METABOLIZMA
        # -------------------------

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
        if anti_tpo > 100:
            katsayi -= 0.08
        elif anti_tpo > 35:
            katsayi -= 0.05

        if ft3 > 4.2:
            katsayi += 0.05

        if ilac == "Evet - Düzenli":
            katsayi += 0.05
        if ilac == "Evet - Düzensiz":
            katsayi -= 0.05

        duzeltilmis_bmr = bmr * katsayi

        # -------------------------
        # SONUCLAR
        # -------------------------

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
        st.write(f"BMR: {int(bmr)} kcal/gün")
        st.write(f"Düzeltilmiş Metabolizma: {int(duzeltilmis_bmr)} kcal/gün")

        st.subheader("🧠 Tiroid Risk Analizi")

        if risk <= 2:
            st.success("Düşük Risk")
        elif risk <= 5:
            st.warning("Orta Risk")
        else:
            st.error("Yüksek Risk")
