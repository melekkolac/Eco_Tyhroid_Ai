import streamlit as st
import pandas as pd

st.set_page_config(page_title="ECO THYROID AI", layout="wide")

st.title("🌿 ECO-THYROID AI")

st.info("Yiyiniz, içiniz fakat israf etmeyiniz. Çünkü Allah israf edenleri sevmez. (Araf 31)")

# ---------------- LOGIN SYSTEM ----------------

if "users" not in st.session_state:
    st.session_state.users = {}

if "logged" not in st.session_state:
    st.session_state.logged = False

if not st.session_state.logged:

    secim = st.radio("Seçim Yap", ["Giriş Yap", "Kayıt Ol"])

    username = st.text_input("Kullanıcı Adı")
    password = st.text_input("Şifre", type="password")

    if secim == "Kayıt Ol":
        if st.button("Kayıt Ol"):
            st.session_state.users[username] = password
            st.success("Kayıt başarılı")

    if secim == "Giriş Yap":
        if st.button("Giriş Yap"):
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.logged = True
                st.success("Giriş başarılı")
                st.rerun()
            else:
                st.error("Hatalı giriş")

    st.stop()

# ---------------- USER INFO ----------------

st.header("Kullanıcı Bilgileri")

cinsiyet = st.radio("Cinsiyet", ["Kadın", "Erkek"])

yas = st.number_input("Yaş", 10, 100, 30)
boy = st.number_input("Boy (cm)", 120, 210, 170)
kilo = st.number_input("Kilo (kg)", 30, 200, 70)

# ---------------- BMR ----------------

if cinsiyet == "Kadın":
    bmr = 10*kilo + 6.25*boy - 5*yas - 161
else:
    bmr = 10*kilo + 6.25*boy - 5*yas + 5

hedef = bmr * 1.2

# ---------------- BMI ----------------

vki = kilo / ((boy/100)**2)

# ---------------- TIROID HEALTH ----------------

st.header("Tiroid Sağlık Bilgileri")

hashimoto = st.checkbox("Hashimoto var mı?")
hipotiroid = st.checkbox("Hipotiroid var mı?")
hipertiroid = st.checkbox("Hipertiroid var mı?")
aile = st.checkbox("Ailede tiroid hastalığı var mı?")

ilac = st.radio("Levotiroksin kullanıyor musunuz?",["Yok","Evet Düzenli","Evet Düzensiz"])

tsh = st.number_input("TSH (0.4-4)",0.0,10.0,2.0)

ft3 = st.number_input("Free T3 (2.3-4.2)",0.0,10.0,3.0)

ft4 = st.number_input("Free T4 (0.8-1.8)",0.0,10.0,1.2)

anti_tpo = st.number_input("Anti TPO (0-35 normal)",0.0,2000.0,50.0)

# ---------------- FOOD DATABASE ----------------

kalori = {

"Yumurta":155,
"Kırmızı Et":250,
"Tavuk":165,
"Hindi":135,
"Balık":206,

"Ekmek":265,
"Bulgur":342,
"Makarna":371,
"Patates":77,

"Zeytinyağı":884,
"Ayçiçek Yağı":884,
"Mısırözü Yağı":884,
"Avokado":160,
"Ceviz":654,

"Domates":18,
"Salatalık":16,
"Havuç":41,
"Kabak":17,
"Patlıcan":25,
"Marul":15,
"Maydanoz":36,
"Limon":29

}

karbon = {

"Yumurta":4.8,
"Kırmızı Et":27,
"Tavuk":6.9,
"Hindi":10,
"Balık":5,

"Ekmek":1.1,
"Bulgur":1,
"Makarna":1.8,
"Patates":0.3,

"Zeytinyağı":6,
"Ayçiçek Yağı":3,
"Mısırözü Yağı":3,
"Avokado":2.5,
"Ceviz":0.3,

"Domates":0.3,
"Salatalık":0.2,
"Havuç":0.2,
"Kabak":0.2,
"Patlıcan":0.3,
"Marul":0.2,
"Maydanoz":0.1,
"Limon":0.2
}

proteinler=["Yok","Yumurta","Kırmızı Et","Tavuk","Hindi","Balık"]
karbonhidratlar=["Yok","Ekmek","Bulgur","Makarna","Patates"]
yaglar=["Yok","Zeytinyağı","Ayçiçek Yağı","Mısırözü Yağı","Avokado","Ceviz"]
sebzeler=["Yok","Domates","Salatalık","Havuç","Kabak","Patlıcan","Marul","Maydanoz","Limon"]

# ---------------- MEALS ----------------

st.header("Menü Seçimi")

def ogun(secim):

    st.subheader(secim)

    p=st.selectbox("Protein",proteinler,key=secim+"p")
    gp=st.number_input("Protein gram",0,500,0,key=secim+"pg")

    k=st.selectbox("Karbonhidrat",karbonhidratlar,key=secim+"k")
    gk=st.number_input("Karbonhidrat gram",0,500,0,key=secim+"kg")

    y=st.selectbox("Yağ",yaglar,key=secim+"y")
    gy=st.number_input("Yağ gram",0,200,0,key=secim+"yg")

    s=st.selectbox("Sebze",sebzeler,key=secim+"s")
    gs=st.number_input("Sebze gram",0,500,0,key=secim+"sg")

    return p,gp,k,gk,y,gy,s,gs

kp,gkp,kk,gkk,ky,gky,ks,gks = ogun("Kahvaltı")
op,gop,ok,gok,oy,goy,os,gos = ogun("Öğle")
ap,gap,ak,gak,ay,gay,asb,gas = ogun("Akşam")

# ---------------- CALORIE ----------------

def hesap(food,gram,dicti):
    if food=="Yok":
        return 0
    return dicti[food]*gram/100

toplam_kalori = (
hesap(kp,gkp,kalori)+hesap(kk,gkk,kalori)+hesap(ky,gky,kalori)+hesap(ks,gks,kalori)+
hesap(op,gop,kalori)+hesap(ok,gok,kalori)+hesap(oy,goy,kalori)+hesap(os,gos,kalori)+
hesap(ap,gap,kalori)+hesap(ak,gak,kalori)+hesap(ay,gay,kalori)+hesap(asb,gas,kalori)
)

# ---------------- CARBON ----------------

toplam_karbon = (
hesap(kp,gkp,karbon)/10 + hesap(kk,gkk,karbon)/10 + hesap(ky,gky,karbon)/10 + hesap(ks,gks,karbon)/10 +
hesap(op,gop,karbon)/10 + hesap(ok,gok,karbon)/10 + hesap(oy,goy,karbon)/10 + hesap(os,gos,karbon)/10 +
hesap(ap,gap,karbon)/10 + hesap(ak,gak,karbon)/10 + hesap(ay,gay,karbon)/10 + hesap(asb,gas,karbon)/10
)

# ---------------- CALORIE ANALYSIS ----------------

st.subheader("Günlük Kalori Analizi")

st.write("Günlük hedef:",int(hedef),"kcal")

st.write("Menü:",int(toplam_kalori),"kcal")

kalan=hedef-toplam_kalori

if kalan>0:
    st.success(f"Kalan kalori: {int(kalan)} kcal")
else:
    st.error(f"Kalori aşımı: {int(abs(kalan))} kcal")

st.progress(min(toplam_kalori/hedef,1.0))

# ---------------- TIROID SCORE ----------------

tiroid=100

if hashimoto:
    tiroid-=20

if hipotiroid:
    tiroid-=15

if hipertiroid:
    tiroid-=15

if tsh>4:
    tiroid-=15

if tsh<0.4:
    tiroid-=10

if ft3<2.3:
    tiroid-=10

if ft4<0.8:
    tiroid-=10

if anti_tpo>35:
    tiroid-=15

tiroid=max(0,tiroid)

# ---------------- CARBON SCORE ----------------

karbon_skor=max(0,100-toplam_karbon*5)

# ---------------- ECO SCORE ----------------

eco=int((tiroid+karbon_skor)/2)

# ---------------- RESULTS ----------------

st.header("Sonuçlar")

st.subheader("VKİ")

st.write(round(vki,2))

st.progress(min(vki/40,1.0))

if vki<18.5:
    st.info("Zayıf")

elif vki<25:
    st.success("Normal")

elif vki<30:
    st.warning("Fazla Kilolu")

else:
    st.error("Obez")

st.subheader("BMR")

st.write(int(bmr),"kcal")

st.subheader("Tiroid Skoru")

st.progress(tiroid/100)

st.write(tiroid)

st.subheader("Karbon Ayak İzi")

st.write(round(toplam_karbon,2),"kg CO2")

st.subheader("Karbon Skoru")

st.progress(karbon_skor/100)

st.write(int(karbon_skor))

st.subheader("ECO Skor")

st.progress(eco/100)

st.write(int(eco))

# ---------------- AI ADVICE ----------------

st.header("AI Menü Tavsiyesi")

if toplam_kalori>hedef:
    st.warning("Kalori yüksek. Gram azaltabilirsiniz.")

elif toplam_kalori<hedef*0.7:
    st.info("Kalori düşük. Protein artırabilirsiniz.")

if toplam_karbon>8:
    st.warning("Karbon ayak izi yüksek. Kırmızı et azaltılabilir.")

if tiroid<60:
    st.warning("Tiroid riskiniz var. Dengeli beslenme önerilir.")
