import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="ECO THYROID AI", layout="wide")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<h1 style='text-align:center;color:#2e7d32;'>🌿 ECO-THYROID AI</h1>
<p style='text-align:center;font-size:18px'>
Yiyiniz, içiniz fakat israf etmeyiniz. (Araf 31)
</p>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIMPLE LOGIN
# --------------------------------------------------

if "users" not in st.session_state:
    st.session_state.users = {}

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:

    secim = st.radio("Hesap",["Giriş Yap","Kayıt Ol"])

    user = st.text_input("Kullanıcı adı")
    pw = st.text_input("Şifre", type="password")

    if secim == "Kayıt Ol":
        if st.button("Kayıt"):
            st.session_state.users[user] = pw
            st.success("Kayıt oluşturuldu")

    if secim == "Giriş Yap":
        if st.button("Giriş"):
            if user in st.session_state.users and st.session_state.users[user] == pw:
                st.session_state.login = True
                st.rerun()
            else:
                st.error("Hatalı giriş")

    st.stop()

# --------------------------------------------------
# USER INFO
# --------------------------------------------------

st.header("👤 Kişisel Bilgiler")

col1,col2,col3,col4 = st.columns(4)

with col1:
    yas = st.number_input("Yaş",10,100,30)

with col2:
    boy = st.number_input("Boy (cm)",120,210,170)

with col3:
    kilo = st.number_input("Kilo (kg)",30,200,70)

with col4:
    cinsiyet = st.radio("Cinsiyet",["Kadın","Erkek"])

# BMI

vki = kilo/((boy/100)**2)

# BMR

if cinsiyet=="Kadın":
    bmr = 10*kilo + 6.25*boy - 5*yas -161
else:
    bmr = 10*kilo + 6.25*boy - 5*yas +5

gunluk_kalori_hedef = bmr*1.2

# --------------------------------------------------
# THYROID
# --------------------------------------------------

st.header("🧬 Tiroid Bilgileri")

tiroid_hastalik = st.radio(
"Tiroid hastalık durumu",
[
"Hastalığım yok",
"Hashimoto",
"Hipotiroid",
"Hipertiroid"
]
)

aile_gecmis = st.checkbox("Ailemde tiroid hastalığı var")

col1,col2,col3,col4 = st.columns(4)

with col1:
    tsh = st.number_input("TSH",0.0,10.0,2.0)

with col2:
    ft3 = st.number_input("Free T3",0.0,10.0,3.0)

with col3:
    ft4 = st.number_input("Free T4",0.0,10.0,1.2)

with col4:
    anti_tpo = st.number_input("Anti TPO",0.0,2000.0,20.0)

# --------------------------------------------------
# FOOD DATABASE
# --------------------------------------------------

proteinler = ["Yumurta","Tavuk","Hindi","Balık","Kırmızı Et"]
karbonhidratlar = ["Ekmek","Bulgur","Makarna","Patates"]
yaglar = ["Zeytinyağı","Ayçiçek Yağı","Avokado","Ceviz"]
sebzeler = ["Domates","Salatalık","Havuç","Kabak","Patlıcan","Marul"]

kalori = {
"Yumurta":155,"Tavuk":165,"Hindi":135,"Balık":200,"Kırmızı Et":250,
"Ekmek":265,"Bulgur":83,"Makarna":131,"Patates":77,
"Zeytinyağı":884,"Ayçiçek Yağı":884,"Avokado":160,"Ceviz":654,
"Domates":18,"Salatalık":15,"Havuç":41,"Kabak":17,"Patlıcan":25,"Marul":15
}

karbon = {
"Yumurta":4.8,"Tavuk":6.9,"Hindi":10,"Balık":5,"Kırmızı Et":27,
"Ekmek":1.1,"Bulgur":1,"Makarna":1.8,"Patates":0.3,
"Zeytinyağı":6,"Ayçiçek Yağı":3,"Avokado":2.5,"Ceviz":0.3,
"Domates":0.3,"Salatalık":0.2,"Havuç":0.2,"Kabak":0.2,"Patlıcan":0.3,"Marul":0.2
}

# --------------------------------------------------
# MEALS
# --------------------------------------------------

st.header("🍽 Öğün Girişi")

col1,col2,col3 = st.columns(3)

def ogun_panel(baslik):

    st.subheader(baslik)

    p = st.multiselect("Protein", proteinler, key=baslik+"p")
    k = st.multiselect("Karbonhidrat", karbonhidratlar, key=baslik+"k")
    y = st.multiselect("Yağ", yaglar, key=baslik+"y")
    s = st.multiselect("Sebze", sebzeler, key=baslik+"s")

    grams = {}

    for g in p+k+y+s:
        grams[g] = st.number_input(f"{g} gram",0,500,0,key=baslik+g)

    return grams

with col1:
    kahvalti = ogun_panel("Kahvaltı")

with col2:
    ogle = ogun_panel("Öğle")

with col3:
    aksam = ogun_panel("Akşam")

# --------------------------------------------------
# CALORIE + CARBON
# --------------------------------------------------

def hesap(veri, tablo):

    toplam = 0

    for g,gram in veri.items():
        toplam += tablo[g]*gram/100

    return toplam

kalori_k = hesap(kahvalti,kalori)
kalori_o = hesap(ogle,kalori)
kalori_a = hesap(aksam,kalori)

toplam_kalori = kalori_k + kalori_o + kalori_a

karbon_k = hesap(kahvalti,karbon)
karbon_o = hesap(ogle,karbon)
karbon_a = hesap(aksam,karbon)

toplam_karbon = karbon_k + karbon_o + karbon_a

# --------------------------------------------------
# PROTEIN ANALYSIS
# --------------------------------------------------

protein_k = sum(v for k,v in kahvalti.items() if k in proteinler)
protein_o = sum(v for k,v in ogle.items() if k in proteinler)
protein_a = sum(v for k,v in aksam.items() if k in proteinler)

gunluk_protein = protein_k + protein_o + protein_a

protein_ihtiyac = kilo*1

# --------------------------------------------------
# SCORES
# --------------------------------------------------

tiroid_skor = 100

if tiroid_hastalik!="Hastalığım yok":
    tiroid_skor -=20

if aile_gecmis:
    tiroid_skor -=5

if tsh>4:
    tiroid_skor -=10

if anti_tpo>35:
    tiroid_skor -=10

tiroid_skor = max(0,tiroid_skor)

karbon_skor = max(0,100-toplam_karbon*5)

eco = int((tiroid_skor+karbon_skor)/2)

# --------------------------------------------------
# METRICS
# --------------------------------------------------

st.header("📊 Sağlık Özeti")

c1,c2,c3 = st.columns(3)

c1.metric("VKİ",round(vki,1))
c2.metric("BMR",int(bmr))
c3.metric("ECO",eco)

# --------------------------------------------------
# CALORIE
# --------------------------------------------------

st.subheader("🍽 Günlük Kalori")

st.progress(min(toplam_kalori/gunluk_kalori_hedef,1.0))

st.write("Hedef:",int(gunluk_kalori_hedef),"kcal")
st.write("Menü:",int(toplam_kalori),"kcal")

# --------------------------------------------------
# SCORES SIDE BY SIDE
# --------------------------------------------------

col1,col2 = st.columns(2)

with col1:

    st.subheader("🧬 Tiroid Skoru")

    st.progress(tiroid_skor/100)

    st.write(tiroid_skor)

with col2:

    st.subheader("🌍 Karbon Skoru")

    st.progress(karbon_skor/100)

    st.write(round(toplam_karbon,2),"kg CO₂")

# --------------------------------------------------
# ECO GRAPH
# --------------------------------------------------

fig = go.Figure()

fig.add_trace(go.Bar(
x=["Tiroid","Karbon","ECO"],
y=[tiroid_skor,karbon_skor,eco],
marker_color=["green","orange","blue"]
))

fig.update_layout(title="ECO Performans Grafiği")

st.plotly_chart(fig)

# --------------------------------------------------
# AI ANALYSIS
# --------------------------------------------------

st.header("🤖 AI Menü Analizi")

if gunluk_protein < protein_ihtiyac*0.8:
    st.warning("Protein alımı düşük")

elif gunluk_protein > protein_ihtiyac*1.5:
    st.warning("Protein fazla")

else:
    st.success("Protein dengeli")

if toplam_karbon > 8:
    st.warning("Karbon ayak izi yüksek")

if eco > 75:
    st.success("Harika gidiyorsunuz 🌿")

elif eco > 60:
    st.info("Dengeli bir beslenme")

else:
    st.error("Beslenme düzeni iyileştirilebilir")
