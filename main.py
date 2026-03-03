import streamlit as st

st.set_page_config(page_title="ECO-THYROID AI", layout="centered")

# -------------------------
# SESSION STATE TANIMLARI
# -------------------------

if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "remember_me" not in st.session_state:
    st.session_state.remember_me = False

# -------------------------
# LOGIN / REGISTER EKRANI
# -------------------------

if not st.session_state.logged_in:

    st.title("ECO-THYROID AI")

    secim = st.radio("Seçim Yap", ["Giriş Yap", "Kayıt Ol"])

    username = st.text_input("Kullanıcı Adı")
    password = st.text_input("Şifre", type="password")

    if secim == "Kayıt Ol":

        if st.button("Kayıt Ol"):
            if username in st.session_state.users:
                st.error("Bu kullanıcı zaten var!")
            elif username == "" or password == "":
                st.warning("Boş alan bırakmayın.")
            else:
                st.session_state.users[username] = password
                st.success("Kayıt başarılı! Giriş yapabilirsiniz.")

    else:  # Giriş Yap

        beni_hatirla = st.checkbox("Beni Hatırla")

        if st.button("Giriş Yap"):
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.logged_in = True
                st.session_state.remember_me = beni_hatirla
                st.success("Giriş başarılı!")
                st.rerun()
            else:
                st.error("Hatalı kullanıcı adı veya şifre.")

# -------------------------
# ANA UYGULAMA
# -------------------------

else:

    st.title("ECO-THYROID AI")

    st.success("Yiyiniz, içiniz fakat israf etmeyiniz. Çünkü Allah israf edenleri sevmez. (A'raf 31)")

    if st.button("Çıkış Yap"):
        st.session_state.logged_in = False
        st.rerun()

    st.header("Kullanıcı Bilgileri")

    cinsiyet = st.radio("Cinsiyet", ["Kadın", "Erkek"])

    age = st.number_input("Yaş", min_value=10, max_value=100, value=30)

    height = st.number_input("Boy (cm)", min_value=100, max_value=220, value=160)

    weight = st.number_input("Kilo (kg)", min_value=30, max_value=200, value=60)

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
