import streamlit as st

# -------------------------------------------------
# SAYFA AYARI
# -------------------------------------------------
st.set_page_config(page_title="ECO-THYROID AI", page_icon="🌿", layout="centered")

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

    st.success("Yiyiniz, içiniz fakat israf etmeyiniz. (A'raf 31)")

    secim = st.radio("Seçim", ["Giriş Yap", "Kayıt Ol"])

    username = st.text_input("Kullanıcı Adı", value=st.session_state.remember_user)
    password = st.text_input("Şifre", type="password")

    if secim == "Kayıt Ol":

        if st.button("Kayıt Ol"):
            if username in st.session_state.users:
                st.error("Kullanıcı zaten var")
            else:
                st.session_state.users[username] = password
                st.success("Kayıt başarılı")

    else:

        remember = st.checkbox("Beni Hatırla")

        if st.button("Giriş Yap"):

            if username in st.session_state.users and st.session_state.users[username] == password:

                st.session_state.logged_in = True

                if remember:
                    st.session_state.remember_user = username

                st.rerun()

            else:
                st.error("Hatalı giriş")

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
    st.header("Kullanıcı Bilgileri")

    cinsiyet = st.radio("Cinsiyet", ["Kadın", "Erkek"])
    yas = st.number_input("Yaş", 10, 100, 30)
    boy = st.number_input("Boy (cm)", 120, 220, 165)
    kilo = st.number_input("Kilo (kg)", 30, 200, 65)

    # -------------------------------------------------
    # TİROİD BİLGİLERİ
    # -------------------------------------------------
    st.header("Tiroid Bilgileri")

    hashimoto = st.checkbox("Hashimoto")
    hipotiroid = st.checkbox("Hipotiroidi")
    hipertiroid = st.checkbox("Hipertiroidi")

    ilac = st.radio(
        "Levotiroksin kullanımı",
        ["Yok", "Evet - Düzenli", "Evet - Düzensiz"]
    )

    tsh = st.number_input("TSH", 0.0, 20.0, 2.0)
    ft3 = st.number_input("Free T3", 0.0, 10.0, 3.0)
    ft4 = st.number_input("Free T4", 0.0, 5.0, 1.2)
    anti_tpo = st.number_input("Anti TPO", 0.0, 2000.0, 20.0)

    # -------------------------------------------------
    # GIDA KALORİ (100g)
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

    # -------------------------------------------------
    # GIDA KARBON (kg CO2 / kg)
    # -------------------------------------------------
    gida_karbon = {

        "Yumurta":4.5,
        "Kırmızı Et":27,
        "Tavuk":6.9,
        "Hindi":10,
        "Balık":5,

        "Ekmek":1.6,
        "Bulgur":1.1,
        "Makarna":1.8,
        "Patates":0.3,

        "Zeytinyağı":6,
        "Ayçiçek Yağı":3,
        "Mısır Özü Yağı":3.5,
        "Avokado":2,
        "Ceviz":2.3,

        "Domates":0.3,
        "Salatalık":0.2,
        "Havuç":0.2,
        "Kabak":0.2,
        "Patlıcan":0.4,
        "Marul":0.2,
        "Maydanoz":0.1,
        "Limon":0.3,

        "Yok":0
    }

    proteinler = ["Yok","Yumurta","Kırmızı Et","Tavuk","Hindi","Balık"]
    karbonhidratlar = ["Yok","Ekmek","Bulgur","Makarna","Patates"]
    yaglar = ["Yok","Zeytinyağı","Ayçiçek Yağı","Mısır Özü Yağı","Avokado","Ceviz"]
    sebzeler = ["Yok","Domates","Salatalık","Havuç","Kabak","Patlıcan","Marul","Maydanoz","Limon"]

    # -------------------------------------------------
    # ÖĞÜN SEÇİMİ
    # -------------------------------------------------
    st.header("Günlük Öğünler")

    tab1, tab2, tab3 = st.tabs(["Kahvaltı","Öğle","Akşam"])

    with tab1:

        kahvalti_protein = st.selectbox("Protein", proteinler)
        gram_kp = st.number_input("Protein gram",0,500,100)

        kahvalti_karb = st.selectbox("Karbonhidrat", karbonhidratlar)
        gram_kk = st.number_input("Karbonhidrat gram",0,500,100)

        kahvalti_yag = st.selectbox("Yağ", yaglar)
        gram_ky = st.number_input("Yağ gram",0,200,20)

        kahvalti_sebze = st.selectbox("Sebze", sebzeler)
        gram_ks = st.number_input("Sebze gram",0,300,50)

    with tab2:

        ogle_protein = st.selectbox("Protein", proteinler)
        gram_op = st.number_input("Protein gram",0,500,150)

        ogle_karb = st.selectbox("Karbonhidrat", karbonhidratlar)
        gram_ok = st.number_input("Karbonhidrat gram",0,500,150)

        ogle_yag = st.selectbox("Yağ", yaglar)
        gram_oy = st.number_input("Yağ gram",0,200,30)

        ogle_sebze = st.selectbox("Sebze", sebzeler)
        gram_os = st.number_input("Sebze gram",0,300,100)

    with tab3:

        aksam_protein = st.selectbox("Protein", proteinler)
        gram_ap = st.number_input("Protein gram",0,500,150)

        aksam_karb = st.selectbox("Karbonhidrat", karbonhidratlar)
        gram_ak = st.number_input("Karbonhidrat gram",0,500,100)

        aksam_yag = st.selectbox("Yağ", yaglar)
        gram_ay = st.number_input("Yağ gram",0,200,20)

        aksam_sebze = st.selectbox("Sebze", sebzeler)
        gram_as = st.number_input("Sebze gram",0,300,100)

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
            katsayi -= 0.1
            risk += 2

        if tsh > 4:
            katsayi -= 0.05
            risk += 1

        if anti_tpo > 35:
            katsayi -= 0.05
            risk += 1

        duzeltilmis_bmr = bmr * katsayi

        tdee = duzeltilmis_bmr * 1.2

        # -------------------------------------------------
        # KALORİ HESABI
        # -------------------------------------------------
        toplam_kalori = (

        gida_kalori[kahvalti_protein] * gram_kp / 100 +
        gida_kalori[kahvalti_karb] * gram_kk / 100 +
        gida_kalori[kahvalti_yag] * gram_ky / 100 +
        gida_kalori[kahvalti_sebze] * gram_ks / 100 +

        gida_kalori[ogle_protein] * gram_op / 100 +
        gida_kalori[ogle_karb] * gram_ok / 100 +
        gida_kalori[ogle_yag] * gram_oy / 100 +
        gida_kalori[ogle_sebze] * gram_os / 100 +

        gida_kalori[aksam_protein] * gram_ap / 100 +
        gida_kalori[aksam_karb] * gram_ak / 100 +
        gida_kalori[aksam_yag] * gram_ay / 100 +
        gida_kalori[aksam_sebze] * gram_as / 100

        )

        # -------------------------------------------------
        # KARBON HESABI
        # -------------------------------------------------
        toplam_karbon = (

        gida_karbon[kahvalti_protein] * gram_kp / 1000 +
        gida_karbon[kahvalti_karb] * gram_kk / 1000 +
        gida_karbon[kahvalti_yag] * gram_ky / 1000 +
        gida_karbon[kahvalti_sebze] * gram_ks / 1000 +

        gida_karbon[ogle_protein] * gram_op / 1000 +
        gida_karbon[ogle_karb] * gram_ok / 1000 +
        gida_karbon[ogle_yag] * gram_oy / 1000 +
        gida_karbon[ogle_sebze] * gram_os / 1000 +

        gida_karbon[aksam_protein] * gram_ap / 1000 +
        gida_karbon[aksam_karb] * gram_ak / 1000 +
        gida_karbon[aksam_yag] * gram_ay / 1000 +
        gida_karbon[aksam_sebze] * gram_as / 1000

        )

        # -------------------------------------------------
        # SONUÇLAR
        # -------------------------------------------------
        st.header("Sonuçlar")

        st.write("VKİ:", round(vki,2))
        st.write("BMR:", int(bmr))
        st.write("Düzeltilmiş Metabolizma:", int(duzeltilmis_bmr))

        st.subheader("Kalori Takibi")

        st.write("Günlük hedef:", int(tdee))
        st.write("Seçilen menü:", int(toplam_kalori))

        kalan = tdee - toplam_kalori

        if kalan >= 0:
            st.success(f"Kalan kalori {int(kalan)}")
        else:
            st.error(f"Aşılan kalori {int(abs(kalan))}")

        st.progress(min(toplam_kalori/tdee,1.0))

        st.subheader("Karbon Ayak İzi")

        st.write("Toplam karbon:", round(toplam_karbon,2),"kg CO2")

        if toplam_karbon < 2:
            karbon_skor = 90
        elif toplam_karbon < 5:
            karbon_skor = 65
        else:
            karbon_skor = 40

        if risk <= 2:
            saglik = 90
        elif risk <= 5:
            saglik = 65
        else:
            saglik = 40

        eco = (saglik*0.6)+(karbon_skor*0.4)

        st.subheader("ECO THYROID SKOR")

        st.progress(eco/100)

        st.write(int(eco))
