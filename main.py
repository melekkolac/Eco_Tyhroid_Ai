import streamlit as st

st.set_page_config(page_title="ECO-THYROID AI", page_icon="🌿")

# ---------------- LOGIN SESSION ----------------

if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "remember_user" not in st.session_state:
    st.session_state.remember_user = ""

# ---------------- LOGIN / REGISTER ----------------

if not st.session_state.logged_in:

    st.title("🌿 ECO-THYROID AI")
    st.success("Yiyiniz, içiniz fakat israf etmeyiniz. (A'raf 31)")

    secim = st.radio("Seçim", ["Giriş Yap", "Kayıt Ol"])

    username = st.text_input("Kullanıcı Adı", value=st.session_state.remember_user)
    password = st.text_input("Şifre", type="password")

    if secim == "Kayıt Ol":

        if st.button("Kayıt Ol"):

            if username in st.session_state.users:
                st.error("Kullanıcı zaten mevcut")

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

# ---------------- MAIN APP ----------------

else:

    st.title("🌿 ECO-THYROID AI")
    st.success("Yiyiniz, içiniz fakat israf etmeyiniz. (A'raf 31)")

    if st.button("Çıkış Yap"):
        st.session_state.logged_in = False
        st.rerun()

    # ---------------- USER DATA ----------------

    st.header("Kullanıcı Bilgileri")

    cinsiyet = st.radio("Cinsiyet", ["Kadın", "Erkek"])
    yas = st.number_input("Yaş", 10, 100, 35)
    boy = st.number_input("Boy (cm)", 120, 220, 165)
    kilo = st.number_input("Kilo (kg)", 30, 200, 60)

    # ---------------- THYROID ----------------

    st.header("Tiroid Bilgileri")

    hashimoto = st.checkbox("Hashimoto")
    hipotiroid = st.checkbox("Hipotiroidi")
    hipertiroid = st.checkbox("Hipertiroidi")

    ilac = st.radio("Levotiroksin", ["Yok", "Evet - Düzenli", "Evet - Düzensiz"])

    tsh = st.number_input("TSH", 0.0, 20.0, 2.0)
    ft3 = st.number_input("Free T3", 0.0, 10.0, 3.0)
    ft4 = st.number_input("Free T4", 0.0, 5.0, 1.2)
    anti_tpo = st.number_input("Anti TPO", 0.0, 2000.0, 20.0)

    # ---------------- FOOD DATA ----------------

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

    # ---------------- MEALS ----------------

    st.header("Günlük Öğünler")

    tab1, tab2, tab3 = st.tabs(["Kahvaltı","Öğle","Akşam"])

    with tab1:

        kp = st.selectbox("Protein", proteinler, key="kp")
        gkp = st.number_input("Protein gram",0,500,100,key="gkp")

        kk = st.selectbox("Karbonhidrat", karbonhidratlar, key="kk")
        gkk = st.number_input("Karbonhidrat gram",0,500,100,key="gkk")

        ky = st.selectbox("Yağ", yaglar, key="ky")
        gky = st.number_input("Yağ gram",0,200,20,key="gky")

        ks = st.selectbox("Sebze", sebzeler, key="ks")
        gks = st.number_input("Sebze gram",0,300,50,key="gks")

    with tab2:

        op = st.selectbox("Protein", proteinler, key="op")
        gop = st.number_input("Protein gram",0,500,150,key="gop")

        ok = st.selectbox("Karbonhidrat", karbonhidratlar, key="ok")
        gok = st.number_input("Karbonhidrat gram",0,500,150,key="gok")

        oy = st.selectbox("Yağ", yaglar, key="oy")
        goy = st.number_input("Yağ gram",0,200,30,key="goy")

        os = st.selectbox("Sebze", sebzeler, key="os")
        gos = st.number_input("Sebze gram",0,300,100,key="gos")

    with tab3:

        ap = st.selectbox("Protein", proteinler, key="ap")
        gap = st.number_input("Protein gram",0,500,150,key="gap")

        ak = st.selectbox("Karbonhidrat", karbonhidratlar, key="ak")
        gak = st.number_input("Karbonhidrat gram",0,500,100,key="gak")

        ay = st.selectbox("Yağ", yaglar, key="ay")
        gay = st.number_input("Yağ gram",0,200,20,key="gay")

        aseb = st.selectbox("Sebze", sebzeler, key="aseb")
        gas = st.number_input("Sebze gram",0,300,100,key="gas")

    # ---------------- ANALYSIS ----------------

    if st.button("Metabolik Analiz Yap"):

        vki = kilo / ((boy/100)**2)

        if cinsiyet == "Kadın":
            bmr = 10*kilo + 6.25*boy - 5*yas - 161
        else:
            bmr = 10*kilo + 6.25*boy - 5*yas + 5

        katsayi = 1

        if hashimoto:
            katsayi -= 0.1

        if tsh > 4:
            katsayi -= 0.05

        if anti_tpo > 35:
            katsayi -= 0.05

        duzeltilmis_bmr = bmr * katsayi
        tdee = duzeltilmis_bmr * 1.2

        # -------- KALORI --------

        toplam_kalori = (

        gida_kalori[kp]*gkp/100 +
        gida_kalori[kk]*gkk/100 +
        gida_kalori[ky]*gky/100 +
        gida_kalori[ks]*gks/100 +

        gida_kalori[op]*gop/100 +
        gida_kalori[ok]*gok/100 +
        gida_kalori[oy]*goy/100 +
        gida_kalori[os]*gos/100 +

        gida_kalori[ap]*gap/100 +
        gida_kalori[ak]*gak/100 +
        gida_kalori[ay]*gay/100 +
        gida_kalori[aseb]*gas/100
        )

        # -------- KARBON --------

        toplam_karbon = (

        gida_karbon[kp]*gkp/1000 +
        gida_karbon[kk]*gkk/1000 +
        gida_karbon[ky]*gky/1000 +
        gida_karbon[ks]*gks/1000 +

        gida_karbon[op]*gop/1000 +
        gida_karbon[ok]*gok/1000 +
        gida_karbon[oy]*goy/1000 +
        gida_karbon[os]*gos/1000 +

        gida_karbon[ap]*gap/1000 +
        gida_karbon[ak]*gak/1000 +
        gida_karbon[ay]*gay/1000 +
        gida_karbon[aseb]*gas/1000
        )

        # -------- RESULTS --------

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

        st.write("Toplam karbon:", round(toplam_karbon,2),"kg CO₂")
