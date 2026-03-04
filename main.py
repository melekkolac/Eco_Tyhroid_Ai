import streamlit as st
import pandas as pd
import datetime
import os

st.set_page_config(page_title="ECO THYROID AI", page_icon="🌿")

st.title("🌿 ECO THYROID AI")

st.success("Yiyiniz, içiniz fakat israf etmeyiniz. (Araf 31)")

# -------------------------------
# KULLANICI BİLGİLERİ
# -------------------------------

st.header("Kullanıcı Bilgileri")

cinsiyet = st.radio("Cinsiyet",["Kadın","Erkek"])

yas = st.number_input("Yaş",10,100,35)

boy = st.number_input("Boy (cm)",120,220,165)

kilo = st.number_input("Kilo (kg)",30,200,60)

# -------------------------------
# TİROİD BİLGİLERİ
# -------------------------------

st.header("Tiroid Bilgileri")

hashimoto = st.checkbox("Hashimoto")

tsh = st.number_input("TSH",0.0,20.0,2.0)

ft3 = st.number_input("Free T3",0.0,10.0,3.0)

ft4 = st.number_input("Free T4",0.0,5.0,1.2)

anti_tpo = st.number_input("Anti TPO",0.0,2000.0,20.0)

# -------------------------------
# BESİN VERİ TABANI
# -------------------------------

proteinler = ["Yok","Yumurta","Kırmızı Et","Tavuk","Hindi","Balık"]

karbonhidratlar = ["Yok","Ekmek","Bulgur","Makarna","Patates"]

yaglar = ["Yok","Zeytinyağı","Ayçiçek Yağı","Mısır Özü Yağı","Avokado","Ceviz"]

sebzeler = ["Yok","Domates","Salatalık","Havuç","Kabak","Patlıcan","Marul","Maydanoz","Limon"]

# kalori /100g

kalori = {

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

# karbon kgCO2/kg

karbon = {

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

# -------------------------------
# ÖĞÜNLER
# -------------------------------

st.header("Öğün Seçimi")

tab1,tab2,tab3 = st.tabs(["Kahvaltı","Öğle","Akşam"])

with tab1:

    kp = st.selectbox("Protein",proteinler,key="kp")
    gkp = st.number_input("Gram",0,500,100,key="gkp")

    kk = st.selectbox("Karbonhidrat",karbonhidratlar,key="kk")
    gkk = st.number_input("Gram",0,500,100,key="gkk")

    ky = st.selectbox("Yağ",yaglar,key="ky")
    gky = st.number_input("Gram",0,200,20,key="gky")

    ks = st.selectbox("Sebze",sebzeler,key="ks")
    gks = st.number_input("Gram",0,300,50,key="gks")

with tab2:

    op = st.selectbox("Protein",proteinler,key="op")
    gop = st.number_input("Gram",0,500,150,key="gop")

    ok = st.selectbox("Karbonhidrat",karbonhidratlar,key="ok")
    gok = st.number_input("Gram",0,500,150,key="gok")

    oy = st.selectbox("Yağ",yaglar,key="oy")
    goy = st.number_input("Gram",0,200,30,key="goy")

    os = st.selectbox("Sebze",sebzeler,key="os")
    gos = st.number_input("Gram",0,300,100,key="gos")

with tab3:

    ap = st.selectbox("Protein",proteinler,key="ap")
    gap = st.number_input("Gram",0,500,150,key="gap")

    ak = st.selectbox("Karbonhidrat",karbonhidratlar,key="ak")
    gak = st.number_input("Gram",0,500,100,key="gak")

    ay = st.selectbox("Yağ",yaglar,key="ay")
    gay = st.number_input("Gram",0,200,20,key="gay")

    aseb = st.selectbox("Sebze",sebzeler,key="aseb")
    gas = st.number_input("Gram",0,300,100,key="gas")

# -------------------------------
# ANALİZ
# -------------------------------

if st.button("Analiz Yap"):

    # VKI

    vki = kilo/((boy/100)**2)

    # BMR

    if cinsiyet == "Kadın":
        bmr = 10*kilo + 6.25*boy - 5*yas - 161
    else:
        bmr = 10*kilo + 6.25*boy - 5*yas + 5

    duzeltilmis = bmr*0.9

    hedef = duzeltilmis*1.2

    # kalori

    toplam_kalori = (
    kalori[kp]*gkp/100 +
    kalori[kk]*gkk/100 +
    kalori[ky]*gky/100 +
    kalori[ks]*gks/100 +

    kalori[op]*gop/100 +
    kalori[ok]*gok/100 +
    kalori[oy]*goy/100 +
    kalori[os]*gos/100 +

    kalori[ap]*gap/100 +
    kalori[ak]*gak/100 +
    kalori[ay]*gay/100 +
    kalori[aseb]*gas/100
    )

    # karbon

    toplam_karbon = (
    karbon[kp]*gkp/1000 +
    karbon[kk]*gkk/1000 +
    karbon[ky]*gky/1000 +
    karbon[ks]*gks/1000 +

    karbon[op]*gop/1000 +
    karbon[ok]*gok/1000 +
    karbon[oy]*goy/1000 +
    karbon[os]*gos/1000 +

    karbon[ap]*gap/1000 +
    karbon[ak]*gak/1000 +
    karbon[ay]*gay/1000 +
    karbon[aseb]*gas/1000
    )

    # -------------------------------
    # KALORİ DURUMU
    # -------------------------------

    st.header("Kalori Analizi")

    st.write("Günlük hedef:",int(hedef))

    st.write("Seçilen menü:",int(toplam_kalori))

    kalan = hedef - toplam_kalori

    if kalan > 0:
        st.success(f"Kalan kalori {int(kalan)} kcal")
    else:
        st.error(f"Kalori aşımı {int(abs(kalan))} kcal")

    st.progress(min(toplam_kalori/hedef,1.0))

    # -------------------------------
    # TİROİD SKOR
    # -------------------------------

    tiroid = 100

    if hashimoto:
        tiroid -= 20

    if tsh > 4:
        tiroid -= 15

    if ft3 < 2.3:
        tiroid -= 10

    if ft4 < 0.8:
        tiroid -= 10

    if anti_tpo > 100:
        tiroid -= 20

    tiroid = max(0,min(100,tiroid))

    # -------------------------------
    # KARBON SKOR
    # -------------------------------

    if toplam_karbon < 2:
        karbon_skor = 100
    elif toplam_karbon < 4:
        karbon_skor = 80
    elif toplam_karbon < 6:
        karbon_skor = 60
    else:
        karbon_skor = 40

    # -------------------------------
    # ECO SKOR
    # -------------------------------

    eco = (tiroid*0.6)+(karbon_skor*0.4)

    st.header("ECO Skor")

    st.progress(eco/100)

    st.write(int(eco))

    # -------------------------------
    # ECO TAKİP PANELİ
    # -------------------------------

    kayit = {

    "Tarih":datetime.date.today(),

    "ECO":eco,

    "Tiroid":tiroid,

    "Karbon":karbon_skor

    }

    df_yeni = pd.DataFrame([kayit])

    if os.path.exists("eco_kayit.csv"):

        df_eski = pd.read_csv("eco_kayit.csv")

        df = pd.concat([df_eski,df_yeni])

    else:

        df = df_yeni

    df.to_csv("eco_kayit.csv",index=False)

    st.header("ECO Takip Paneli")

    st.line_chart(df[["ECO","Tiroid","Karbon"]])
