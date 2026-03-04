import streamlit as st
import pandas as pd
import datetime
import os

st.set_page_config(page_title="ECO THYROID AI", page_icon="🌿")

# ---------------- USERS ----------------

if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "remember_user" not in st.session_state:
    st.session_state.remember_user = ""

# ---------------- LOGIN ----------------

if not st.session_state.logged_in:

    st.title("🌿 ECO THYROID AI")

    st.success("Yiyiniz, içiniz fakat israf etmeyiniz. (A'raf 31)")

    secim = st.radio("Seçim",["Giriş Yap","Kayıt Ol"])

    username = st.text_input("Kullanıcı Adı",value=st.session_state.remember_user)

    password = st.text_input("Şifre",type="password")

    if secim == "Kayıt Ol":

        if st.button("Kayıt Ol"):

            if username in st.session_state.users:

                st.error("Kullanıcı zaten var")

            else:

                st.session_state.users[username] = password

                st.success("Kayıt başarılı")

    else:

        remember = st.checkbox("Beni hatırla")

        if st.button("Giriş Yap"):

            if username in st.session_state.users and st.session_state.users[username] == password:

                st.session_state.logged_in = True

                if remember:
                    st.session_state.remember_user = username

                st.rerun()

            else:

                st.error("Hatalı giriş")

# ---------------- APP ----------------

else:

    st.title("🌿 ECO THYROID AI")

    st.success("Yiyiniz, içiniz fakat israf etmeyiniz. (A'raf 31)")

    if st.button("Çıkış Yap"):
        st.session_state.logged_in = False
        st.rerun()

# ---------------- USER DATA ----------------

    st.header("Kullanıcı Bilgileri")

    cinsiyet = st.radio("Cinsiyet",["Kadın","Erkek"])

    yas = st.number_input("Yaş",10,100,35)

    boy = st.number_input("Boy (cm)",120,220,165)

    kilo = st.number_input("Kilo (kg)",30,200,60)

# ---------------- THYROID ----------------

    st.header("Tiroid Bilgileri")

    hashimoto = st.checkbox("Hashimoto")

    hipotiroid = st.checkbox("Hipotiroidi")

    hipertiroid = st.checkbox("Hipertiroidi")

    ilac = st.radio("Levotiroksin kullanımı",["Yok","Evet - Düzenli","Evet - Düzensiz"])

    tsh = st.number_input("TSH",0.0,20.0,2.0)

    ft3 = st.number_input("Free T3",0.0,10.0,3.0)

    ft4 = st.number_input("Free T4",0.0,5.0,1.2)

    anti_tpo = st.number_input("Anti TPO",0.0,2000.0,20.0)

# ---------------- FOOD LIST ----------------

    proteinler = ["Yok","Yumurta","Kırmızı Et","Tavuk","Hindi","Balık"]

    karbonhidratlar = ["Yok","Ekmek","Bulgur","Makarna","Patates"]

    yaglar = ["Yok","Zeytinyağı","Ayçiçek Yağı","Mısır Özü Yağı","Avokado","Ceviz"]

    sebzeler = ["Yok","Domates","Salatalık","Havuç","Kabak","Patlıcan","Marul","Maydanoz","Limon"]

# ---------------- CALORIES ----------------

    kalori = {

    "Yumurta":155,"Kırmızı Et":250,"Tavuk":165,"Hindi":135,"Balık":200,

    "Ekmek":265,"Bulgur":83,"Makarna":131,"Patates":77,

    "Zeytinyağı":884,"Ayçiçek Yağı":884,"Mısır Özü Yağı":884,"Avokado":160,"Ceviz":654,

    "Domates":18,"Salatalık":15,"Havuç":41,"Kabak":17,"Patlıcan":25,"Marul":15,"Maydanoz":36,"Limon":29,

    "Yok":0
    }

# ---------------- CARBON ----------------

    karbon = {

    "Yumurta":4.5,"Kırmızı Et":27,"Tavuk":6.9,"Hindi":10,"Balık":5,

    "Ekmek":1.6,"Bulgur":1.1,"Makarna":1.8,"Patates":0.3,

    "Zeytinyağı":6,"Ayçiçek Yağı":3,"Mısır Özü Yağı":3.5,"Avokado":2,"Ceviz":2.3,

    "Domates":0.3,"Salatalık":0.2,"Havuç":0.2,"Kabak":0.2,"Patlıcan":0.4,"Marul":0.2,"Maydanoz":0.1,"Limon":0.3,

    "Yok":0
    }

# ---------------- MEALS ----------------

    st.header("Öğünler")

    tab1,tab2,tab3 = st.tabs(["Kahvaltı","Öğle","Akşam"])

    with tab1:

        kp = st.selectbox("Protein",proteinler,key="kp")
        gkp = st.number_input("Protein gram",0,500,100,key="gkp")

        kk = st.selectbox("Karbonhidrat",karbonhidratlar,key="kk")
        gkk = st.number_input("Karbonhidrat gram",0,500,100,key="gkk")

        ky = st.selectbox("Yağ",yaglar,key="ky")
        gky = st.number_input("Yağ gram",0,200,20,key="gky")

        ks = st.selectbox("Sebze",sebzeler,key="ks")
        gks = st.number_input("Sebze gram",0,300,50,key="gks")

    with tab2:

        op = st.selectbox("Protein",proteinler,key="op")
        gop = st.number_input("Protein gram",0,500,150,key="gop")

        ok = st.selectbox("Karbonhidrat",karbonhidratlar,key="ok")
        gok = st.number_input("Karbonhidrat gram",0,500,150,key="gok")

        oy = st.selectbox("Yağ",yaglar,key="oy")
        goy = st.number_input("Yağ gram",0,200,30,key="goy")

        osb = st.selectbox("Sebze",sebzeler,key="osb")
        gos = st.number_input("Sebze gram",0,300,100,key="gos")

    with tab3:

        ap = st.selectbox("Protein",proteinler,key="ap")
        gap = st.number_input("Protein gram",0,500,150,key="gap")

        ak = st.selectbox("Karbonhidrat",karbonhidratlar,key="ak")
        gak = st.number_input("Karbonhidrat gram",0,500,100,key="gak")

        ay = st.selectbox("Yağ",yaglar,key="ay")
        gay = st.number_input("Yağ gram",0,200,20,key="gay")

        aseb = st.selectbox("Sebze",sebzeler,key="aseb")
        gas = st.number_input("Sebze gram",0,300,100,key="gas")

# ---------------- ANALYSIS ----------------

    if st.button("Metabolik Analiz Yap"):

        vki = kilo/((boy/100)**2)

        if cinsiyet == "Kadın":
            bmr = 10*kilo + 6.25*boy - 5*yas - 161
        else:
            bmr = 10*kilo + 6.25*boy - 5*yas + 5

        duzeltilmis = bmr*0.9
        hedef = duzeltilmis*1.2

# ---------------- CALORIE ----------------

        toplam_kalori = (

        kalori[kp]*gkp/100 + kalori[kk]*gkk/100 + kalori[ky]*gky/100 + kalori[ks]*gks/100 +
        kalori[op]*gop/100 + kalori[ok]*gok/100 + kalori[oy]*goy/100 + kalori[osb]*gos/100 +
        kalori[ap]*gap/100 + kalori[ak]*gak/100 + kalori[ay]*gay/100 + kalori[aseb]*gas/100
        )

# ---------------- CARBON ----------------

        toplam_karbon = (

        karbon[kp]*gkp/1000 + karbon[kk]*gkk/1000 + karbon[ky]*gky/1000 + karbon[ks]*gks/1000 +
        karbon[op]*gop/1000 + karbon[ok]*gok/1000 + karbon[oy]*goy/1000 + karbon[osb]*gos/1000 +
        karbon[ap]*gap/1000 + karbon[ak]*gak/1000 + karbon[ay]*gay/1000 + karbon[aseb]*gas/1000
        )

# ---------------- TIROID SCORE ----------------

        tiroid = 100

        if hashimoto: tiroid -= 20
        if hipotiroid: tiroid -= 15
        if hipertiroid: tiroid -= 15
        if tsh > 4: tiroid -= 15
        if tsh < 0.4: tiroid -= 10
        if ft3 < 2.3: tiroid -= 10
        if ft4 < 0.8: tiroid -= 10
        if anti_tpo > 100: tiroid -= 20

        if ilac == "Evet - Düzenli":
            tiroid += 5

        if ilac == "Evet - Düzensiz":
            tiroid -= 5

        tiroid = max(0,min(100,tiroid))

# ---------------- CARBON SCORE ----------------

        if toplam_karbon < 2:
            karbon_skor = 100
        elif toplam_karbon < 4:
            karbon_skor = 80
        elif toplam_karbon < 6:
            karbon_skor = 60
        else:
            karbon_skor = 40

# ---------------- ECO SCORE ----------------

        eco = (tiroid*0.6)+(karbon_skor*0.4)

# ---------------- RESULTS ----------------

        st.header("Sonuçlar")

        st.subheader("Tiroid Skoru")
        st.progress(tiroid/100)
        st.write(int(tiroid))

        st.subheader("Karbon Ayak İzi")
        st.write(round(toplam_karbon,2),"kg CO₂")

        st.subheader("Karbon Skoru")
        st.progress(karbon_skor/100)
        st.write(karbon_skor)

# Türkiye ortalaması

        turkiye_ortalama = 5.3

        oran = min(toplam_karbon/turkiye_ortalama,1.0)

        st.subheader("Türkiye Karbon Ortalaması Karşılaştırma")

        st.progress(oran)

        if toplam_karbon < turkiye_ortalama:
            st.success("Türkiye ortalamasından düşük karbon ayak izi")
        else:
            st.error("Türkiye ortalamasından yüksek karbon ayak izi")

        st.subheader("ECO Skor")
        st.progress(eco/100)
        st.write(int(eco))

# ---------------- GRAPH ----------------

        data = pd.DataFrame({

        "Kategori":["Tiroid","Karbon","ECO"],

        "Skor":[tiroid,karbon_skor,eco]

        })

        st.bar_chart(data.set_index("Kategori"))
        # ---------------- AI MENU SUGGESTION ----------------

        st.header("🤖 AI Menü Tavsiyesi")

        oneriler = []

        def ai(gida,gram):

            # sağlıksız seçim → değiştir

            if gida == "Kırmızı Et":

                oneriler.append("Kırmızı et yerine tavuk veya balık seçersen karbon ayak izi azalır")

            elif gida == "Ayçiçek Yağı":

                oneriler.append("Ayçiçek yağı yerine zeytinyağı tercih edebilirsin")

            elif gida == "Mısır Özü Yağı":

                oneriler.append("Mısır özü yağı yerine zeytinyağı kullanmak daha sağlıklı")

            elif gida == "Makarna":

                oneriler.append("Makarna yerine bulgur tercih edebilirsin")

            # sağlıklı ama fazla gram

            elif gida in ["Tavuk","Balık","Yumurta","Bulgur"]:

                if gram > 150:

                    oneriler.append(f"{gida} sağlıklı bir seçim ancak {gram}g yerine 120g yeterli olabilir")

        # kahvaltı

        ai(kp,gkp)
        ai(kk,gkk)
        ai(ky,gky)
        ai(ks,gks)

        # öğle

        ai(op,gop)
        ai(ok,gok)
        ai(oy,goy)
        ai(osb,gos)

        # akşam

        ai(ap,gap)
        ai(ak,gak)
        ai(ay,gay)
        ai(aseb,gas)

        if len(oneriler) == 0:

            st.success("Menü dengeli görünüyor 👍")

        else:

            for o in oneriler:

                st.info(o)
