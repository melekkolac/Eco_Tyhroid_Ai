import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="ECO-THYROID AI", layout="wide")

# --------------------------------------------------
# BAŞLIK
# --------------------------------------------------

st.title("🌿 ECO-THYROID AI")

st.caption("“Yiyiniz içiniz fakat israf etmeyiniz.” – Araf 31")

# --------------------------------------------------
# BESİN VERİTABANI (100 g)
# --------------------------------------------------

besinler = {

# PROTEIN
"Yumurta":{"kalori":155,"protein":13,"karbon":1,"yag":11,"co2":4.8},
"Kırmızı Et":{"kalori":250,"protein":26,"karbon":0,"yag":15,"co2":27},
"Tavuk":{"kalori":165,"protein":31,"karbon":0,"yag":3.6,"co2":6},
"Hindi":{"kalori":189,"protein":29,"karbon":0,"yag":7,"co2":10},
"Balık":{"kalori":206,"protein":22,"karbon":0,"yag":12,"co2":5},

# SUT URUNLERI
"Süt":{"kalori":60,"protein":3.2,"karbon":5,"yag":3.3,"co2":3},
"Yoğurt":{"kalori":59,"protein":10,"karbon":3.6,"yag":0.4,"co2":2.2},
"Peynir":{"kalori":402,"protein":25,"karbon":1.3,"yag":33,"co2":13},

# BAKLIYAT
"Mercimek":{"kalori":116,"protein":9,"karbon":20,"yag":0.4,"co2":0.9},
"Nohut":{"kalori":164,"protein":9,"karbon":27,"yag":2.6,"co2":1},
"Fasulye":{"kalori":127,"protein":8.7,"karbon":22,"yag":0.5,"co2":1},

# KARBOHIDRAT
"Ekmek":{"kalori":265,"protein":9,"karbon":49,"yag":3.2,"co2":0.8},
"Bulgur":{"kalori":342,"protein":12,"karbon":76,"yag":1.3,"co2":0.7},
"Makarna":{"kalori":371,"protein":13,"karbon":75,"yag":1.5,"co2":1.1},
"Patates":{"kalori":77,"protein":2,"karbon":17,"yag":0.1,"co2":0.3},
"Pirinç":{"kalori":365,"protein":7,"karbon":80,"yag":0.6,"co2":2.7},

# YAG
"Zeytinyağı":{"kalori":884,"protein":0,"karbon":0,"yag":100,"co2":6},
"Ayçiçek Yağı":{"kalori":884,"protein":0,"karbon":0,"yag":100,"co2":5},
"Mısırözü Yağı":{"kalori":884,"protein":0,"karbon":0,"yag":100,"co2":5},
"Avokado":{"kalori":160,"protein":2,"karbon":9,"yag":15,"co2":2.5},
"Ceviz":{"kalori":654,"protein":15,"karbon":14,"yag":65,"co2":0.3},
"Badem":{"kalori":579,"protein":21,"karbon":22,"yag":50,"co2":0.4},

# SEBZE
"Domates":{"kalori":18,"protein":0.9,"karbon":3.9,"yag":0.2,"co2":0.3},
"Salatalık":{"kalori":16,"protein":0.7,"karbon":3.6,"yag":0.1,"co2":0.2},
"Havuç":{"kalori":41,"protein":0.9,"karbon":10,"yag":0.2,"co2":0.2},
"Marul":{"kalori":15,"protein":1.4,"karbon":2.9,"yag":0.2,"co2":0.2},
"Kabak":{"kalori":17,"protein":1.2,"karbon":3.1,"yag":0.3,"co2":0.2},
"Patlıcan":{"kalori":25,"protein":1,"karbon":6,"yag":0.2,"co2":0.3},
"Maydanoz":{"kalori":36,"protein":3,"karbon":6,"yag":0.8,"co2":0.2},
"Limon":{"kalori":29,"protein":1,"karbon":9,"yag":0.3,"co2":0.2},
}

besin_listesi = list(besinler.keys())

# --------------------------------------------------
# KİŞİSEL BİLGİLER
# --------------------------------------------------

st.header("👤 Kişisel Bilgiler")

# Cinsiyet
cinsiyet = st.radio(
"Cinsiyet",
["Kadın","Erkek"],
horizontal=True
)

# Yaş Boy Kilo yan yana
col1,col2,col3 = st.columns(3)

with col1:
    yas = st.number_input("Yaş",15,90,30)

with col2:
    boy = st.number_input("Boy (cm)",140,210,170)

with col3:
    kilo = st.number_input("Kilo (kg)",40,200,70)

# --------------------------------------------------
# VKI
# --------------------------------------------------

vki = kilo / ((boy/100)**2)

# --------------------------------------------------
# BMR
# --------------------------------------------------

if cinsiyet == "Kadın":
    bmr = 10*kilo + 6.25*boy - 5*yas - 161
else:
    bmr = 10*kilo + 6.25*boy - 5*yas + 5

hedef_kalori = bmr * 1.2

# --------------------------------------------------
# TİROİD
# --------------------------------------------------
st.header("🧬 Tiroid Bilgileri")

tiroid_hastalik = st.radio(
"Durumunuz",
[
"Hastalığım yok",
"Hashimoto",
"Hipotiroid",
"Hipertiroid"
]
)

aile_tiroid = st.checkbox("Ailede tiroid hastalığı var")

col1,col2,col3,col4 = st.columns(4)

with col1:
    tsh = st.number_input("TSH (0.4 - 4.0)",0.0,20.0,2.0)

with col2:
    ft3 = st.number_input("Free T3 (2.3 - 4.2)",0.0,10.0,3.2)

with col3:
    ft4 = st.number_input("Free T4 (0.8 - 1.8)",0.0,5.0,1.1)

with col4:
    anti_tpo = st.number_input("Anti-TPO (0 - 35)",0.0,2000.0,0.0)
    
    st.subheader("🧠 Tiroid Eğilim Analizi")

egilim = "Normal"

if anti_tpo > 35:
    egilim = "Otoimmün tiroid eğilimi (Hashimoto olasılığı)"

if tsh > 4 and ft4 < 0.8:
    egilim = "Hipotiroid eğilimi"

elif tsh > 4 and ft4 >= 0.8:
    egilim = "Subklinik hipotiroid eğilimi"

elif tsh < 0.4 and ft4 > 1.8:
    egilim = "Hipertiroid eğilimi"

elif tsh < 0.4 and ft4 <= 1.8:
    egilim = "Subklinik hipertiroid eğilimi"

elif ft3 < 2.3:
    egilim = "Düşük T3 eğilimi"

if egilim == "Normal":
    st.success("Tiroid hormon dengesi referans aralıkta görünüyor.")
else:
    st.warning("Tespit edilen eğilim: " + egilim)

# --------------------------------------------------
# ÖĞÜN GİRİŞİ
# --------------------------------------------------

st.header("🍽 Öğünler")

def ogun(baslik):

    st.subheader(baslik)

    secilen = st.multiselect("Besin seç",besin_listesi,key=baslik)

    ogun_dict = {}

    for g in secilen:

        gram = st.number_input(f"{g} gram",0,500,0,key=baslik+g)

        ogun_dict[g] = gram

    return ogun_dict

col1,col2,col3 = st.columns(3)

with col1:
    kahvalti = ogun("Kahvaltı")

with col2:
    ogle = ogun("Öğle")

with col3:
    aksam = ogun("Akşam")

# --------------------------------------------------
# MAKRO HESAPLAMA
# --------------------------------------------------

toplam_kalori = 0
toplam_protein = 0
toplam_karbon = 0
toplam_yag = 0
toplam_co2 = 0

for ogun in [kahvalti,ogle,aksam]:

    for g,gram in ogun.items():

        veri = besinler[g]

        toplam_kalori += veri["kalori"] * gram / 100
        toplam_protein += veri["protein"] * gram / 100
        toplam_karbon += veri["karbon"] * gram / 100
        toplam_yag += veri["yag"] * gram / 100
        toplam_co2 += veri["co2"] * gram / 1000

# --------------------------------------------------
# SONUÇLAR
# --------------------------------------------------

st.header("📊 Sonuçlar")

st.write(f"VKI: {vki:.2f}")
st.write(f"BMR: {int(bmr)} kcal")
st.write(f"Günlük hedef kalori: {int(hedef_kalori)} kcal")
st.write(f"Menü kalorisi: {int(toplam_kalori)} kcal")

# --------------------------------------------------
# KARŞILAŞTIRMA
# --------------------------------------------------

kalan = hedef_kalori - toplam_kalori

if kalan > 0:
    st.success(f"Kalan kalori: {int(kalan)} kcal")
else:
    st.error(f"Kalori aşımı: {int(abs(kalan))} kcal")

st.progress(min(toplam_kalori/hedef_kalori,1.0))

# --------------------------------------------------
# MAKRO YÜZDELER
# --------------------------------------------------

protein_kal = toplam_protein * 4
karbon_kal = toplam_karbon * 4
yag_kal = toplam_yag * 9

toplam_macro = protein_kal + karbon_kal + yag_kal

if toplam_macro > 0:

    p_oran = protein_kal/toplam_macro*100
    k_oran = karbon_kal/toplam_macro*100
    y_oran = yag_kal/toplam_macro*100

# --------------------------------------------------
# SKORLAR
# --------------------------------------------------

tiroid_skor = 100

if tiroid_hastalik != "Hastalığım yok":
    tiroid_skor -= 20

if anti_tpo > 35:
    tiroid_skor -= 10

karbon_skor = max(0,100 - toplam_co2*10)

eco = (tiroid_skor + karbon_skor)/2

# --------------------------------------------------
# GRAFİK
# --------------------------------------------------

fig = go.Figure()

fig.add_bar(x=["Tiroid","Karbon","ECO"],y=[tiroid_skor,karbon_skor,eco])

st.plotly_chart(fig,use_container_width=True)

# --------------------------------------------------
# AI MENÜ DANIŞMANI
# --------------------------------------------------

st.header("🤖 AI Menü Danışmanı")

with st.chat_message("assistant"):

    st.write("Merhaba! Günlük menünüzü detaylı analiz ettim.")

    if toplam_macro > 0:

        st.write(
        f"Makro dağılımınız: Protein %{p_oran:.1f}, Karbonhidrat %{k_oran:.1f}, Yağ %{y_oran:.1f}"
        )

        if k_oran > 55:
            st.write(f"Karbonhidrat oranı %{k_oran:.1f}. Yaklaşık %{k_oran-55:.1f} azaltmanız önerilir.")

        if p_oran < 10:
            st.write(f"Protein oranı %{p_oran:.1f}. Yaklaşık %{10-p_oran:.1f} artırmanız önerilir.")

        if y_oran > 35:
            st.write(f"Yağ oranı %{y_oran:.1f}. Yaklaşık %{y_oran-35:.1f} azaltmanız önerilir.")

    st.write(f"Karbon ayak iziniz {toplam_co2:.2f} kg CO₂.")

    turkiye_ortalama = 4

    if toplam_co2 > turkiye_ortalama:

        fark = toplam_co2 - turkiye_ortalama
        yuzde = fark/turkiye_ortalama*100

        st.write(f"Bu değer Türkiye ortalamasından %{yuzde:.1f} daha yüksek.")

    else:

        fark = turkiye_ortalama - toplam_co2
        yuzde = fark/turkiye_ortalama*100

        st.write(f"Karbon ayak iziniz Türkiye ortalamasından %{yuzde:.1f} daha düşük.")

    if eco > 80:
        st.write("ECO skorunuz çok iyi.")

    elif eco > 60:
        st.write("ECO skorunuz orta seviyede.")

    else:
        st.write("ECO skorunuz düşük, menü iyileştirilebilir.")
