import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime
import os
from streamlit_calendar import calendar

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
"Somon":{"kalori":208,"protein":20,"karbon":0,"yag":13,"co2":6},
"Ton Balığı":{"kalori":132,"protein":28,"karbon":0,"yag":1,"co2":5},
"Hindi Füme":{"kalori":104,"protein":17,"karbon":1,"yag":2,"co2":4},
"Sucuk":{"kalori":450,"protein":24,"karbon":2,"yag":38,"co2":30},
"Sosis":{"kalori":301,"protein":12,"karbon":2,"yag":27,"co2":28},

# SUT URUNLERI
"Süt":{"kalori":60,"protein":3.2,"karbon":5,"yag":3.3,"co2":3},
"Yoğurt":{"kalori":59,"protein":10,"karbon":3.6,"yag":0.4,"co2":2.2},
"Peynir":{"kalori":402,"protein":25,"karbon":1.3,"yag":33,"co2":13},
"Ayran":{"kalori":37,"protein":2,"karbon":3,"yag":1,"co2":0.2},
"Kaşar Peyniri":{"kalori":404,"protein":25,"karbon":1,"yag":33,"co2":13},
"Lor Peyniri":{"kalori":98,"protein":11,"karbon":3,"yag":4,"co2":2},
"Kefir":{"kalori":41,"protein":3,"karbon":4,"yag":1,"co2":0.3},
"Labne":{"kalori":220,"protein":6,"karbon":4,"yag":21,"co2":3},
    
# BAKLIYAT
"Mercimek":{"kalori":116,"protein":9,"karbon":20,"yag":0.4,"co2":0.9},
"Nohut":{"kalori":164,"protein":9,"karbon":27,"yag":2.6,"co2":1},
"Fasulye":{"kalori":127,"protein":8.7,"karbon":22,"yag":0.5,"co2":1},
"Barbunya":{"kalori":127,"protein":8,"karbon":22,"yag":0.5,"co2":1},
"Börülce":{"kalori":116,"protein":8,"karbon":21,"yag":0.4,"co2":1},
"Bezelye":{"kalori":81,"protein":5,"karbon":14,"yag":0.4,"co2":0.7},

# KARBOHIDRAT
"Ekmek":{"kalori":265,"protein":9,"karbon":49,"yag":3.2,"co2":0.8},
"Bulgur":{"kalori":342,"protein":12,"karbon":76,"yag":1.3,"co2":0.7},
"Makarna":{"kalori":371,"protein":13,"karbon":75,"yag":1.5,"co2":1.1},
"Yulaf":{"kalori":389,"protein":16.9,"karbon":66.3,"yag":6.9,"co2":0.6},
"Patates":{"kalori":77,"protein":2,"karbon":17,"yag":0.1,"co2":0.3},
"Yufka":{"kalori":330,"protein":8,"karbon":60,"yag":2,"co2":0.9},
"Pirinç":{"kalori":365,"protein":7,"karbon":80,"yag":0.6,"co2":2.7},
"Barbunya":{"kalori":127,"protein":8,"karbon":22,"yag":0.5,"co2":1},
"Börülce":{"kalori":116,"protein":8,"karbon":21,"yag":0.4,"co2":1},
"Bezelye":{"kalori":81,"protein":5,"karbon":14,"yag":0.4,"co2":0.7},

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
"Brokoli":{"kalori":34,"protein":2.8,"karbon":7,"yag":0.4,"co2":0.3},
"Ispanak":{"kalori":23,"protein":2.9,"karbon":3.6,"yag":0.4,"co2":0.2},
"Biber":{"kalori":20,"protein":0.9,"karbon":4.6,"yag":0.2,"co2":0.2},
"Soğan":{"kalori":40,"protein":1.1,"karbon":9,"yag":0.1,"co2":0.3},
"Sarımsak":{"kalori":149,"protein":6,"karbon":33,"yag":0.5,"co2":0.4},
    
# MEYVE
"Elma":{"kalori":52,"protein":0.3,"karbon":14,"yag":0.2,"co2":0.4},
"Muz":{"kalori":89,"protein":1.1,"karbon":23,"yag":0.3,"co2":0.7},
"Portakal":{"kalori":47,"protein":0.9,"karbon":12,"yag":0.1,"co2":0.3},
"Mandalina":{"kalori":53,"protein":0.8,"karbon":13,"yag":0.3,"co2":0.3},
"Çilek":{"kalori":32,"protein":0.7,"karbon":8,"yag":0.3,"co2":0.2},
"Avokado":{"kalori":160,"protein":2,"karbon":9,"yag":15,"co2":2.5},
    
}

besin_listesi = list(besinler.keys())

# -------------------------
# TIROID DOSTU GIDALAR
# -------------------------

tiroid_dostu = [
"Yumurta","Balık","Tavuk","Yoğurt","Mercimek","Nohut",
"Brokoli","Ispanak","Domates","Salatalık",
"Badem","Ceviz","Avokado","Yulaf","Bulgur"
]

# -------------------------
# DÜŞÜK KARBON AYAK İZİ GIDALAR
# -------------------------

dusuk_karbon = [
"Mercimek","Nohut","Bulgur","Yulaf",
"Domates","Salatalık","Kabak","Patlıcan",
"Brokoli","Ispanak","Marul"
]

# -------------------------
# TIROID + DÜŞÜK KARBON KESİŞİMİ
# -------------------------

uygun_gida = list(set(tiroid_dostu) & set(dusuk_karbon))

# -------------------------
# AI MENU VERITABANI
# -------------------------

menu_onerileri = {

"kahvalti":[
"Yulaf + Yoğurt + Ceviz + Elma",
"Tam buğday ekmeği + Avokado + Yumurta",
"Yoğurt + Chia + Muz",
"Lor peyniri + Domates + Salatalık"
],

"ogle":[
"Mercimek çorbası + Zeytinyağlı sebze",
"Izgara tavuk + Bulgur + Salata",
"Nohut yemeği + Yoğurt",
"Ton balıklı salata + Tam buğday ekmek"
],

"aksam":[
"Izgara balık + Sebze + Salata",
"Sebzeli kinoa + Yoğurt",
"Tavuklu sebze sote",
"Zeytinyağlı kabak + Yoğurt"
]

}

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
# Günlük veri kaydı

veri = {
"Tarih": datetime.date.today(),
"Kalori": toplam_kalori,
"Protein": toplam_protein,
"Karbonhidrat": toplam_karbon,
"Yag": toplam_yag,
"KarbonAyakIzi": toplam_co2,
"ECO": eco
}

df_yeni = pd.DataFrame([veri])
dosya = "eco_kayit.csv"

df = pd.read_csv("eco_kayit.csv")

events = []

for i,row in df.iterrows():

    tarih = row["Tarih"]
    eco = row["ECO"]

    if eco >= 80:
        renk = "green"
    elif eco >= 60:
        renk = "orange"
    else:
        renk = "red"

    events.append({
        "title": f"ECO {round(eco)}",
        "start": tarih,
        "color": renk
    })

if os.path.exists(dosya):

    df_eski = pd.read_csv(dosya)

    df = pd.concat([df_eski, df_yeni])

else:

    df = df_yeni

df.to_csv(dosya, index=False)

# --------------------------------------------------
# GRAFİK
# --------------------------------------------------

fig = go.Figure()

fig.add_bar(x=["Tiroid","Karbon","ECO"],y=[tiroid_skor,karbon_skor,eco])

st.plotly_chart(fig,use_container_width=True)

# -------------------------
# AI GÜNLÜK MENÜ ÖNERİSİ
# -------------------------

st.header("🤖 AI Günlük Menü Önerisi")
import random

# günlük kaloriyi öğünlere böl
kahvalti_kalori = hedef_kalori * 0.30
ogle_kalori = hedef_kalori * 0.40
aksam_kalori = hedef_kalori * 0.30

# uygun gıdalardan menü oluştur
kahvalti_gida = random.sample(uygun_gida, 3)
ogle_gida = random.sample(uygun_gida, 4)
aksam_gida = random.sample(uygun_gida, 3)

kahvalti_oneri = " + ".join(kahvalti_gida)
ogle_oneri = " + ".join(ogle_gida)
aksam_oneri = " + ".join(aksam_gida)
st.subheader("🍽 Önerilen Menü")

st.markdown(f"🥣 **Kahvaltı:** {kahvalti_oneri}")
st.markdown(f"🍲 **Öğle:** {ogle_oneri}")
st.markdown(f"🍽 **Akşam:** {aksam_oneri}")

# -------------------------
# MENU ANALIZI
# -------------------------

menu_gida = kahvalti_gida + ogle_gida + aksam_gida

toplam_kalori = 0
toplam_protein = 0
toplam_karbon = 0

for gida in menu_gida:

    if gida not in besinler:
        st.error(f"Veritabanında olmayan gıda: {gida}")

    if gida in besinler:
        toplam_kalori += besinler[gida]["kalori"]
        toplam_protein += besinler[gida]["protein"]
        toplam_karbon += besinler[gida]["co2"]

protein_ihtiyac = kilo * 1.0

protein_yuzde = (toplam_protein / protein_ihtiyac) * 100
kalori_yuzde = (toplam_kalori / hedef_kalori) * 100
st.subheader("🧠 AI Öğün Dengesi Analizi")
if kalori_yuzde > 120:

    st.warning("Menünüz günlük kalori ihtiyacınızın %120'sini aşıyor.")

elif kalori_yuzde < 80:

    st.info("Menünüz günlük kalori ihtiyacınızın altında.")

else:

    st.success("Kalori dengesi uygun.")
if protein_yuzde < 80:

    st.warning("Protein alımınız düşük.")

elif protein_yuzde > 150:

    st.info("Protein alımınız oldukça yüksek.")

else:

    st.success("Protein dengesi iyi.")
if toplam_karbon > 15:

    st.warning("Menünüzün karbon ayak izi yüksek.")

elif toplam_karbon < 8:

    st.success("Menünüz çevre dostu.")

else:

    st.info("Karbon ayak izi orta seviyede.")
    
st.header("📅 ECO Takvimi")

secili_tarih = st.date_input(
"Gün seç",
datetime.date.today()
)
if os.path.exists("eco_kayit.csv"):

    df = pd.read_csv("eco_kayit.csv")

    df["Tarih"] = pd.to_datetime(df["Tarih"]).dt.date
    gun_veri = df[df["Tarih"] == secili_tarih]
    if not gun_veri.empty:

        st.subheader("📊 Günlük Analiz")

        st.write("ECO Skor:", round(gun_veri["ECO"].values[0],1))

        st.write("Kalori:", round(gun_veri["Kalori"].values[0],1))

        st.write("Karbon Ayak İzi:", round(gun_veri["KarbonAyakIzi"].values[0],2))

else:

    st.info("Bu gün için kayıt bulunamadı.")

st.subheader("📊 ECO Skor Takibi")

st.line_chart(df.set_index("Tarih")["ECO"])

st.subheader("🧠 AI Haftalık Analiz")

son7 = df.tail(7)

eco_ort = son7["ECO"].mean()

st.write("Son 7 gün ortalama ECO skorunuz:", round(eco_ort,1))

if eco_ort > 80:
    st.success("Beslenme düzeniniz sürdürülebilir.")

elif eco_ort > 60:
    st.warning("Beslenme düzeniniz orta seviyede.")

else:
    st.error("Beslenme düzeniniz iyileştirilmeli.")

# --------------------------------------------------
# AI MENU DANISMANI
# ---------------------------------------

st.header("🤖 AI Menü Danışmanı")

with st.chat_message("assistant"):

    st.write("Merhaba! Günlük menünüzü sağlık ve çevresel sürdürülebilirlik açısından analiz ettim.")

    # Makro toplamı
    toplam_macro = toplam_protein + toplam_karbonhidrat + toplam_yag

    if toplam_macro > 0:

        # Makro yüzdeleri
        p_oran = (toplam_protein / toplam_macro) * 100
        k_oran = (toplam_karbonhidrat / toplam_macro) * 100
        y_oran = (toplam_yag / toplam_macro) * 100

        st.write(
            f"Makro dağılımınız: Protein %{p_oran:.1f}, Karbonhidrat %{k_oran:.1f}, Yağ %{y_oran:.1f}"
        )

        # -----------------------------
        # PROTEIN ANALIZI
        # -----------------------------

        protein_ihtiyac = kilo * 1.0
        protein_karsilama = (toplam_protein / protein_ihtiyac) * 100

        if protein_karsilama < 80:
            st.write(
                f"⚠️ Protein ihtiyacınızın %{protein_karsilama:.1f}'i karşılandı. "
                "Mercimek, balık veya yoğurt eklenmesi önerilir."
            )

        elif protein_karsilama > 130:
            st.write(
                "Protein tüketiminiz yüksek seviyede. Dengeli dağılım önerilir."
            )

        else:
            st.write("✅ Protein alımınız dengeli.")

        # -----------------------------
        # KALORI ANALIZI
        # -----------------------------

        kalori_oran = (toplam_kalori / hedef_kalori) * 100

        if kalori_oran > 120:
            st.warning(
                f"Günlük kalori ihtiyacınızın %{kalori_oran:.1f}'ini tüketmişsiniz. "
                "Kalori alımını azaltmanız önerilir."
            )

        elif kalori_oran < 80:
            st.info(
                f"Kalori alımınız hedefinizin altında (%{kalori_oran:.1f}). "
                "Enerji ihtiyacınız için öğün artırılabilir."
            )

        else:
            st.success("Kalori alımınız hedef aralıkta.")

        # -----------------------------
        # KARBOHIDRAT ANALIZI
        # -----------------------------

        if k_oran > 55:
            azalt = k_oran - 55
            st.write(
                f"⚠️ Karbonhidrat oranı %{k_oran:.1f}. Yaklaşık %{azalt:.1f} azaltılması önerilir."
            )

        # -----------------------------
        # YAG ANALIZI
        # -----------------------------

        if y_oran > 35:
            azalt = y_oran - 35
            st.write(
                f"⚠️ Yağ oranı %{y_oran:.1f}. Yaklaşık %{azalt:.1f} azaltılması önerilir."
            )

        # -----------------------------
        # TIROID ANALIZI
        # -----------------------------

        if tiroid_hastalik == "Hashimoto":

            if p_oran < 15:
                st.write("Hashimoto için protein oranının artırılması önerilir.")

            if k_oran > 60:
                st.write("Hashimoto için yüksek karbonhidrat inflamasyonu artırabilir.")

        if tiroid_hastalik == "Hipotiroid":

            if y_oran > 35:
                st.write("Hipotiroid için yüksek yağ metabolizmayı zorlayabilir.")

            if p_oran < 15:
                st.write("Hipotiroid metabolizması için protein artırılması faydalı olabilir.")

        # -----------------------------
        # KARBON AYAK IZI ANALIZI
        # -----------------------------

        st.write(f"🌍 Karbon ayak iziniz {toplam_co2:.2f} kg CO₂")

        turkiye_ortalama = 4

        if toplam_co2 > turkiye_ortalama:

            fark = toplam_co2 - turkiye_ortalama
            yuzde = (fark / turkiye_ortalama) * 100

            st.write(
                f"Bu değer Türkiye ortalamasından %{yuzde:.1f} daha yüksek."
            )

            st.write(
                "Karbon ayak izinizi azaltmak için baklagil ve sebze ağırlıklı öğünler tercih edilebilir."
            )

        else:

            fark = turkiye_ortalama - toplam_co2
            yuzde = (fark / turkiye_ortalama) * 100

            st.write(
                f"Karbon ayak iziniz Türkiye ortalamasından %{yuzde:.1f} daha düşük."
            )

        # -----------------------------
        # ECO SKOR ANALIZI
        # -----------------------------

        if eco > 80:
            st.success("🌱 ECO skorunuz çok iyi. Hem sağlık hem çevre açısından dengeli bir menü.")

        elif eco > 60:
            st.info("ECO skorunuz orta seviyede. Küçük değişikliklerle geliştirilebilir.")

        else:
            st.warning("ECO skorunuz düşük. Daha sürdürülebilir besin seçimleri önerilir.")
