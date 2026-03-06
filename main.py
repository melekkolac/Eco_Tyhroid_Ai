import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="ECO THYROID AI", layout="wide")

# ------------------------------------------------
# HEADER
# ------------------------------------------------

st.markdown("""
<h1 style='text-align:center;color:#2e7d32;'>🌿 ECO-THYROID AI</h1>
<p style='text-align:center;font-size:18px'>
Yiyiniz, içiniz fakat israf etmeyiniz. (Araf 31)
</p>
""", unsafe_allow_html=True)

# ------------------------------------------------
# LOGIN
# ------------------------------------------------

if "users" not in st.session_state:
    st.session_state.users = {}

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:

    secim = st.radio("Hesap",["Giriş Yap","Kayıt Ol"])

    user = st.text_input("Kullanıcı adı")
    pw = st.text_input("Şifre",type="password")

    if secim=="Kayıt Ol":
        if st.button("Kayıt"):
            st.session_state.users[user]=pw
            st.success("Kayıt oluşturuldu")

    if secim=="Giriş Yap":
        if st.button("Giriş"):
            if user in st.session_state.users and st.session_state.users[user]==pw:
                st.session_state.login=True
                st.rerun()
            else:
                st.error("Hatalı giriş")

    st.stop()

# ------------------------------------------------
# USER INFO
# ------------------------------------------------

st.header("👤 Kişisel Bilgiler")

c1,c2,c3,c4 = st.columns(4)

with c1:
    yas = st.number_input("Yaş",10,100,30)

with c2:
    boy = st.number_input("Boy (cm)",120,210,170)

with c3:
    kilo = st.number_input("Kilo (kg)",30,200,70)

with c4:
    cinsiyet = st.radio("Cinsiyet",["Kadın","Erkek"])

vki = kilo / ((boy/100)**2)

if cinsiyet=="Kadın":
    bmr = 10*kilo + 6.25*boy -5*yas -161
else:
    bmr = 10*kilo + 6.25*boy -5*yas +5

gunluk_kalori = bmr * 1.3

# ------------------------------------------------
# TIROID
# ------------------------------------------------

st.header("🧬 Tiroid Bilgileri")

tiroid_hastalik = st.radio(
"Tiroid hastalık durumu",
["Hastalığım yok","Hashimoto","Hipotiroid","Hipertiroid"]
)

aile_gecmis = st.checkbox("Ailemde tiroid hastalığı var")

c1,c2,c3,c4 = st.columns(4)

with c1:
    tsh = st.number_input("TSH",0.0,10.0,2.0)

with c2:
    ft3 = st.number_input("Free T3",0.0,10.0,3.0)

with c3:
    ft4 = st.number_input("Free T4",0.0,10.0,1.2)

with c4:
    anti_tpo = st.number_input("Anti TPO",0.0,2000.0,20.0)

# ------------------------------------------------
# FOOD DATABASE
# ------------------------------------------------

besinler = {
"Yumurta":{"kalori":155,"protein":13,"karbon":1.1,"yag":11,"co2":4.8},
"Tavuk":{"kalori":165,"protein":31,"karbon":0,"yag":3.6,"co2":6.9},
"Hindi":{"kalori":135,"protein":29,"karbon":0,"yag":1,"co2":10},
"Kırmızı Et":{"kalori":250,"protein":26,"karbon":0,"yag":15,"co2":27},
"Balık":{"kalori":200,"protein":22,"karbon":0,"yag":12,"co2":5},
"Mercimek":{"kalori":116,"protein":9,"karbon":20,"yag":0.4,"co2":0.9},
"Nohut":{"kalori":164,"protein":9,"karbon":27,"yag":2.6,"co2":1},

"Ekmek":{"kalori":265,"protein":9,"karbon":49,"yag":3,"co2":1.1},
"Bulgur":{"kalori":83,"protein":3,"karbon":18,"yag":0.2,"co2":1},
"Makarna":{"kalori":131,"protein":5,"karbon":25,"yag":1.1,"co2":1.8},
"Pirinç":{"kalori":130,"protein":2.7,"karbon":28,"yag":0.3,"co2":2.7},
"Patates":{"kalori":77,"protein":2,"karbon":17,"yag":0.1,"co2":0.3},

"Zeytinyağı":{"kalori":884,"protein":0,"karbon":0,"yag":100,"co2":6},
"Ceviz":{"kalori":654,"protein":15,"karbon":14,"yag":65,"co2":0.3},
"Badem":{"kalori":579,"protein":21,"karbon":22,"yag":50,"co2":0.4},

"Domates":{"kalori":18,"protein":0.9,"karbon":3.9,"yag":0.2,"co2":0.3},
"Salatalık":{"kalori":16,"protein":0.7,"karbon":3.6,"yag":0.1,"co2":0.2},
"Havuç":{"kalori":41,"protein":0.9,"karbon":10,"yag":0.2,"co2":0.2},
"Marul":{"kalori":15,"protein":1.4,"karbon":2.9,"yag":0.2,"co2":0.2},
"Kabak":{"kalori":17,"protein":1.2,"karbon":3.1,"yag":0.3,"co2":0.2},

"Elma":{"kalori":52,"protein":0.3,"karbon":14,"yag":0.2,"co2":0.4},
"Muz":{"kalori":89,"protein":1.1,"karbon":23,"yag":0.3,"co2":0.7},
"Portakal":{"kalori":47,"protein":0.9,"karbon":12,"yag":0.1,"co2":0.3}
}

besin_listesi = list(besinler.keys())

# ------------------------------------------------
# MEALS
# ------------------------------------------------

st.header("🍽 Öğün Girişi")

col1,col2,col3 = st.columns(3)

def ogun(baslik):

    st.subheader(baslik)

    secilen = st.multiselect("Besin seç",besin_listesi,key=baslik)

    veri = {}

    for g in secilen:
        gram = st.number_input(f"{g} gram",0,500,0,key=baslik+g)
        veri[g] = gram

    return veri

with col1:
    kahvalti = ogun("Kahvaltı")

with col2:
    ogle = ogun("Öğle")

with col3:
    aksam = ogun("Akşam")

# ------------------------------------------------
# HESAP MOTORU
# ------------------------------------------------

def hesap(ogun):

    kalori=protein=karbon=yag=co2=0

    for besin,gram in ogun.items():

        veri = besinler[besin]

        kalori += veri["kalori"] * gram /100
        protein += veri["protein"] * gram /100
        karbon += veri["karbon"] * gram /100
        yag += veri["yag"] * gram /100
        co2 += veri["co2"] * gram /1000

    return kalori,protein,karbon,yag,co2

k1,p1,c1,y1,co1 = hesap(kahvalti)
k2,p2,c2,y2,co2 = hesap(ogle)
k3,p3,c3,y3,co3 = hesap(aksam)

toplam_kalori = k1+k2+k3
toplam_protein = p1+p2+p3
toplam_karbon = c1+c2+c3
toplam_yag = y1+y2+y3
toplam_co2 = co1+co2+co3

# ------------------------------------------------
# SCORES
# ------------------------------------------------

protein_ihtiyac = kilo*0.8

tiroid = 100

if tiroid_hastalik=="Hashimoto":
    tiroid-=20

if aile_gecmis:
    tiroid-=5

if tsh>4:
    tiroid-=10

if anti_tpo>35:
    tiroid-=10

referans=5

karbon_skor = 100*(1-(toplam_co2/referans))
karbon_skor = max(0,min(100,karbon_skor))

eco = (tiroid*0.6)+(karbon_skor*0.4)

# ------------------------------------------------
# DASHBOARD
# ------------------------------------------------

st.header("📊 Sağlık Özeti")

c1,c2,c3 = st.columns(3)

c1.metric("VKİ",round(vki,1))
c2.metric("BMR",int(bmr))
c3.metric("ECO",int(eco))

# ------------------------------------------------
# GRAPH
# ------------------------------------------------

fig = go.Figure()

fig.add_trace(go.Bar(
x=["Tiroid","Karbon","ECO"],
y=[tiroid,karbon_skor,eco]
))

st.plotly_chart(fig)

# ------------------------------------------------
# AI ANALYSIS
# ------------------------------------------------

st.header("🤖 AI Menü Analizi")

if toplam_protein < protein_ihtiyac:
    st.warning("Protein tüketimi düşük (WHO önerisi 0.8 g/kg)")

if toplam_co2 > 5:
    st.warning("Karbon ayak izi yüksek")

sebzeler=["Domates","Salatalık","Havuç","Marul","Kabak"]
meyveler=["Elma","Muz","Portakal"]

sebze_miktar = sum(v for k,v in kahvalti.items() if k in sebzeler) + \
               sum(v for k,v in ogle.items() if k in sebzeler) + \
               sum(v for k,v in aksam.items() if k in sebzeler)

meyve_miktar = sum(v for k,v in kahvalti.items() if k in meyveler) + \
               sum(v for k,v in ogle.items() if k in meyveler) + \
               sum(v for k,v in aksam.items() if k in meyveler)

if sebze_miktar + meyve_miktar < 400:
    st.warning("WHO önerisine göre sebze meyve tüketimi düşük (400g/gün)")

if eco > 80:
    st.success("Beslenme düzeni sürdürülebilir ve sağlıklı")
