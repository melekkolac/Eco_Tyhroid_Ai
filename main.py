import streamlit as st

# -------------------------------------------------
# SAYFA AYARI
# -------------------------------------------------
st.set_page_config(page_title="ECO-THYROID AI", page_icon="🌿", layout="centered")

st.markdown(
    """
    <style>
    .stApp { background-color:#1e1e1e; color:white; }
    div.stButton > button {
        background-color:#2e7d32; color:white; border-radius:8px; height:3em; width:100%;
    }
    div.stButton > button:hover { background-color:#1b5e20; }
    </style>
    """,
    unsafe_allow_html=True
)

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
# LOGIN / REGISTER
# -------------------------------------------------
if not st.session_state.logged_in:

    st.title("🌿 ECO-THYROID AI")

    st.markdown(
        """
        <div style="background-color:#2e7d32;padding:12px;border-radius:10px;margin-bottom:15px">
        <p style="color:white;text-align:center;margin:0">
        Yiyiniz, içiniz fakat israf etmeyiniz. Çünkü Allah israf edenleri sevmez. (A'raf 31)
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

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
                st.success("Kayıt başarılı.")

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

    st.markdown(
        """
        <div style="background-color:#2e7d32;padding:12px;border-radius:10px;margin-bottom:15px">
        <p style="color:white;text-align:center;margin:0">
        Yiyiniz, içiniz fakat israf etmeyiniz. Çünkü Allah israf edenleri sevmez. (A'raf 31)
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Çıkış Yap"):
        st.session_state.logged_in = False
        st.rerun()

    # -------------------------------------------------
    # KULLANICI BİLGİLERİ
    # -------------------------------------------------
    st.subheader("👤 Kullanıcı Bilgileri")

    cinsiyet = st.radio("Cinsiyet", ["Kadın", "Erkek"])
    yas = st.number_input("Yaş", 10, 100, 30)
    boy = st.number_input("Boy (cm)", 120, 220, 160)
    kilo = st.number_input("Kilo (kg)", 30, 200, 60)

    # -------------------------------------------------
    # TİROİD BİLGİLERİ
    # -------------------------------------------------
    st.subheader("🧬 Tiroid Sağlık Bilgileri")

    hashimoto = st.checkbox("Hashimoto var mı?")
    hipotiroid = st.checkbox("Hipotiroidi var mı?")
    hipertiroid = st.checkbox("Hipertiroidi var mı?")
    aile = st.checkbox("Ailede tiroid hastalığı var mı?")

    ilac = st.radio(
        "Levotiroksin kullanıyor musunuz?",
        ["Yok", "Evet - Düzenli", "Evet - Düzensiz"]
    )

    tsh = st.number_input("TSH", 0.0, 20.0, 2.0)
    ft3 = st.number_input("Free T3", 0.0, 10.0, 3.0)
    ft4 = st.number_input("Free T4", 0.0, 5.0, 1.2)
    anti_tpo = st.number_input("Anti-TPO", 0.0, 2000.0, 20.0)

    # -------------------------------------------------
    # GIDA VERİ TABANI (KALORİ)
    # -------------------------------------------------
    gida_kalori = {

        "Yumurta":155,
        "Kırmızı Et":250,
        "Tavuk":165,
        "Hindi":135,
        "Balık":200,

        "Ekmek":265,
        "Bulgur":83,
        "Makarna":131,
        "Patates":77,

        "Zeytinyağı":884,
        "Ayçiçek Yağı":884,
        "Mısır Özü Yağı":884,
        "Avokado":160,
        "Ceviz":654,

        "Domates":18,
        "Salatalık":15,
        "Havuç":41,
        "Kabak":17,
        "Patlıcan":25,
        "Marul":15,
        "Maydanoz":36,
        "Limon":29,

        "Yok":0
    }

    proteinler = ["Yok","Yumurta","Kırmızı Et","Tavuk","Hindi","Balık"]
    karbonhidratlar = ["Yok","Ekmek","Bulgur","Makarna","Patates"]
    yaglar = ["Yok","Zeytinyağı","Ayçiçek Yağı","Mısır Özü Yağı","Avokado","Ceviz"]
    sebzeler = ["Yok","Domates","Salatalık","Havuç","Kabak","Patlıcan","Marul","Maydanoz","Limon"]

    # -------------------------------------------------
    # ÖĞÜN SEÇİMİ
    # -------------------------------------------------
    st.subheader("🍽 Günlük Öğün Seçimi")

    tab1, tab2, tab3 = st.tabs(["Kahvaltı","Öğle","Akşam"])

    with tab1:
        kahvalti_protein = st.selectbox("Protein", proteinler, key="kp")
        kahvalti_karb = st.selectbox("Karbonhidrat", karbonhidratlar, key="kk")
        kahvalti_yag = st.selectbox("Yağ", yaglar, key="ky")
        kahvalti_sebze = st.selectbox("Sebze", sebzeler, key="ks")

    with tab2:
        ogle_protein = st.selectbox("Protein", proteinler, key="op")
        ogle_karb = st.selectbox("Karbonhidrat", karbonhidratlar, key="ok")
        ogle_yag = st.selectbox("Yağ", yaglar, key="oy")
        ogle_sebze = st.selectbox("Sebze", sebzeler, key="os")

    with tab3:
        aksam_protein = st.selectbox("Protein", proteinler, key="ap")
        aksam_karb = st.selectbox("Karbonhidrat", karbonhidratlar, key="ak")
        aksam_yag = st.selectbox("Yağ", yaglar, key="ay")
        aksam_sebze = st.selectbox("Sebze", sebzeler, key="as")

    # -------------------------------------------------
    # ANALİZ
    # -------------------------------------------------
    if st.button("Metabolik Analiz Yap"):

        vki = kilo / ((boy/100)**2)

        if cinsiyet == "Kadın":
            bmr = 10*kilo + 6.25*boy - 5*yas - 161
        else:
            bmr = 10*kilo + 6.25*boy - 5*yas + 5

        katsayi = 1.0
        risk = 0

        if hashimoto:
            katsayi -= 0.10
            risk += 2

        if hipotiroid:
            katsayi -= 0.05
            risk += 1

        if tsh > 4:
            katsayi -= 0.05
            risk += 1

        if anti_tpo > 35:
            katsayi -= 0.05
            risk += 1

        if ilac == "Evet - Düzenli":
            katsayi += 0.05

        duzeltilmis_bmr = bmr * katsayi

        tdee = duzeltilmis_bmr * 1.2

        toplam_kalori = (
            gida_kalori[kahvalti_protein] +
            gida_kalori[kahvalti_karb] +
            gida_kalori[kahvalti_yag] +
            gida_kalori[kahvalti_sebze] +
            gida_kalori[ogle_protein] +
            gida_kalori[ogle_karb] +
            gida_kalori[ogle_yag] +
            gida_kalori[ogle_sebze] +
            gida_kalori[aksam_protein] +
            gida_kalori[aksam_karb] +
            gida_kalori[aksam_yag] +
            gida_kalori[aksam_sebze]
        )

        # -------------------------------------------------
        # SONUÇLAR
        # -------------------------------------------------
        st.subheader("📊 Sonuçlar")

        if vki < 18.5:
            st.info("Zayıf")
        elif vki < 25:
            st.success("Normal Kilolu")
        elif vki < 30:
            st.warning("Fazla Kilolu")
        else:
            st.error("Obez")

        st.write(f"VKİ: {round(vki,2)}")
        st.write(f"BMR: {int(bmr)} kcal")
        st.write(f"Düzeltilmiş Metabolizma: {int(duzeltilmis_bmr)} kcal")

        # -------------------------------------------------
        # KALORİ TAKİBİ
        # -------------------------------------------------
        st.subheader("🔥 Günlük Kalori Takibi")

        st.write(f"Günlük Kalori Hedefi: {int(tdee)} kcal")
        st.write(f"Seçilen Menü Kalorisi: {toplam_kalori} kcal")

        kalan = tdee - toplam_kalori

        if kalan >= 0:
            st.success(f"Kalan Kalori: {int(kalan)} kcal")
        else:
            st.error(f"Kalori Aşıldı: {int(abs(kalan))} kcal")

        st.progress(min(toplam_kalori/tdee,1.0))

        # -------------------------------------------------
        # ECO SKOR
        # -------------------------------------------------
        if risk <= 2:
            saglik = 90
        elif risk <= 5:
            saglik = 65
        else:
            saglik = 40

        karbon = 70

        eco = (saglik*0.6)+(karbon*0.4)

        st.subheader("🌿 ECO-THYROID SKORU")

        st.progress(eco/100)

        st.write(f"ECO Skor: {int(eco)}/100")
