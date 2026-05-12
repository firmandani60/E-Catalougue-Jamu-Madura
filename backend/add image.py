import pandas as pd

# Load CSV
df = pd.read_csv('data.csv')

# Buat kolom image kosong dulu
df['image'] = ''

# Array link image
links = [
    # 101-150
    "https://share.google/jZHjKj1q4s8v8L4FG",
    "https://share.google/hmL1LmInpCd5AkAcW",
    "https://share.google/AaRyePtqAlA5JMSLc",
    "https://share.google/13vSVzZTW5QN0YNSk",
    "https://share.google/hMsiUbuwGZJghQtIL",
    "https://share.google/zosdtVaOe18UepdPz",
    "https://share.google/VzGV93fmRsuDWER7R",
    "https://share.google/HSbyfJHoG5zzGWbk3",
    "https://share.google/ZqFuz59CeFru3tgND",
    "https://share.google/Vw6UhpPH2eUUamaO2",
    "https://share.google/Pubwt2E5BjIDVvFKb",
    "https://share.google/ot0D4Pi7f2nX2s7wY",
    "https://share.google/1mGp55UAwXl8kSi1v",
    "https://share.google/LEp9dEFALL851s83O",
    "https://share.google/dIJDvXqQsMpyG9wWN",
    "https://share.google/aJjsebwG7Yy2WxTs2",
    "https://share.google/jLHhAZtixdVN7hycx",
    "https://share.google/bwdMTA1GzoBL0xm9s",
    "https://share.google/0e9pv0NavPVbPdsEU",
    "https://share.google/qKGZG8AzuAKuT1xGI",
    "https://share.google/AA2JRW6a4yLEDRFxH",
    "https://share.google/KaawVCV4vWERcIjdo",
    "https://share.google/bIB7TouLAculUTO3B",
    "https://share.google/s0MLVFfWpbs0f3rpK",
    "https://share.google/eOKdhfiEXHxYrs1Wo",
    "https://share.google/2133cKsJmZDttaJlW",
    "https://share.google/Bx3DbPXwvZ96Fhv0F",
    "https://share.google/5pjESpCX79GMBsPTk",
    "https://share.google/6wREA14Qx5uyemjSP",
    "https://share.google/nmQRPs1h0vnMzwR1T",
    "https://share.google/hNc16Dzea15UtfBqG",
    "https://share.google/8GKdQviMobBQ85joB",
    "https://share.google/kMrjRdPErs4XbK1ml",
    "https://share.google/mIOjuup6ktk1eVCVU",
    "https://share.google/LqOkd5y3c1XOLTw8a",
    "https://share.google/HLJXN6FcIAKVx5rm5",
    "https://share.google/FVV2amcExepUSp3o3",
    "https://share.google/iXKT5do6Kxq2FbdpF",
    "https://share.google/WDQ94fUQQkmJ4NMQN",
    "https://share.google/hqQqrtWc39g2KmwN2",
    "https://share.google/eKd8ZCxnREQeXr2yT",
    "https://share.google/qT72kWTjFmiC5mqlQ",
    "https://share.google/EZ1lcH8MK02krRjmR",
    "https://share.google/x6Pu4y2y7oyweri1l",
    "https://share.google/HOX3HoEJXTh7djG4Q",
    "https://share.google/PGkthLHF61u3lTwtu",
    "https://share.google/9vDZKyPI9RadfM4bV",
    "https://share.google/rmOtTxZltzyHCRs4e",
    "https://share.google/v8euHURMvLIuO6OLb",
    "https://share.google/8pa2wg3jvFkeTDjun",
    # 150-205
    "https://img.lazcdn.com/live/id/p/77836916b469b572451c7ea7f105135c.jpg_720x720q80.jpg",
    "https://down-id.img.susercontent.com/file/id-11134207-7r992-ls18zojkpaa12d",
    "https://www.sidomuncul.co.id/assets/images/product/produk-jamu-bersalin.png",
    "https://down-id.img.susercontent.com/file/id-11134207-7r98p-lsawzvhh2fst4a",
    "https://down-id.img.susercontent.com/file/id-11134207-7ra0m-mbn97rf0dztf0a",
    "https://img.lazcdn.com/g/ff/kf/S9cff1ee1a379477dac96786ebef046dc5.jpg_360x360q80.jpg",
    "https://down-id.img.susercontent.com/file/id-11134207-7rbk2-ma7udfywusec01",
    "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/7880363ed85d4b94a279dc978b55390a~tplv-aphluv4xwc-resize-jpeg:700:0.jpeg",
    "https://www.sidomuncul.co.id/assets/images/product/produk-jamu-galian-singset.png",
    "https://cf.shopee.co.id/file/cbfa030de541d947fbba2f318095a0ba",
    "https://img.lazcdn.com/g/p/0e1d6c47c23a50db7a9767b1c52af791.jpg_960x960q80.jpg_.webp",
    "https://www.sidomuncul.co.id/assets/images/product/produk-jamu-pegal-linu-ginseng.png",
    "https://down-id.img.susercontent.com/file/sg-11134201-22100-h2xt2hv4wniv69",
    "https://img.lazcdn.com/g/p/aa57964f8946e725af532845786e4dbd.jpg_720x720q80.jpg",
    "https://down-id.img.susercontent.com/file/66b014e0cf7d9f624698de1e49c4432a",
    "https://id-test-11.slatic.net/p/e12ee076d7e780aa7b77d9630f8455d4.jpg",
    "https://id-test-11.slatic.net/p/218fe42d9fd7a7991db5b5e6c1ecdf1a.jpg",
    "https://img.lazcdn.com/g/ff/kf/S3ca99ff8eade4f149b0f5f696f672887L.jpg_720x720q80.jpg",
    "https://down-id.img.susercontent.com/file/1b05d84a36abab6d107538874c67e15e",
    "https://down-id.img.susercontent.com/file/id-11134207-7r98p-m0cb9hg8vhau96",
    "https://images-cdn.ubuy.ae/634d07242792fc7238667ec1-kopi-jantan-is-a-herbal-coffee-that-is.jpg",
    "https://down-id.img.susercontent.com/file/id-11134207-7qul1-lf6aw3i5fntwc0",
    "https://images.tokopedia.net/img/cache/700/VqbcmM/2024/1/19/b7ff7515-43c9-4747-be93-d14fcfb9189f.jpg.webp",
    "https://down-id.img.susercontent.com/file/sg-11134201-22120-haexojmnd5kv65",
    "https://favo.id/cdn/shop/products/23c4f3f0-714c-4c7f-b24d-9f3b7ed017b5.jpg?v=1757321814",
    "https://down-id.img.susercontent.com/file/2b6f4f359d3c5c375e423e32a1bc0900",
    "https://down-id.img.susercontent.com/file/d5e5db53cf39f81fd0fcd7ecea7a155e",
    "https://id-live-01.slatic.net/p/a2c833aec9282ab51a65d9fb6709afc4.jpg",
    "https://down-id.img.susercontent.com/file/sg-11134201-23030-its2ehxuylov75",
    "https://id-live-01.slatic.net/shop/9f055862526507b8b4aec6e523c2ef97.jpeg",
    "https://down-id.img.susercontent.com/file/e35d049e07c05e7223675ed77b1b128c",
    "https://down-id.img.susercontent.com/file/671e5b789b24e6c86d32310d020765a2",
    "https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full//99/MTA-7094086/gemuk_sehat_gemuk_sehat_penambah_berat_badan_herbal_-12_kapsul-_full02_td341gyj.jpg",
    "https://down-id.img.susercontent.com/file/8c48eeaf22e49fc6e434f2ee1e487d44",
    "https://id-live-01.slatic.net/p/1fffb5c7eeeb4b418f06ef4f7c77347b.jpg",
    "https://sg-test-11.slatic.net/other/common/9d9a6f7dfb15415589a52b46ee5d3350.jpeg",
    "https://cf.shopee.co.id/file/e1a826b623dc3d52b863e3c1e9307558",
    "https://cf.shopee.co.id/file/2350139c9693d7c4bf0908ce23ffbfde",
    "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/img/hDjmkQ/2024/11/2/02284231-f9eb-4fbf-852d-7602dc5b2fa1.jpg~tplv-aphluv4xwc-resize-jpeg:700:0.jpg",
    "https://down-id.img.susercontent.com/file/78f07ddf3a60b00e1c2016286568bf25",
    "https://id-test-11.slatic.net/p/51a6e2b46ac3d7551615af4e94f95dda.jpg",
    "https://down-id.img.susercontent.com/file/4fc936d13e8db6bee4b9dad49f7ff31d",
    "https://favo.id/cdn/shop/files/FMISUP1002_Feminax-Lancar-Haid---12-Pcs.jpg?v=1757320656",
    "https://down-id.img.susercontent.com/file/id-11134207-7qul6-lhxdxbn9x8v21d",
    "https://cf.shopee.co.id/file/ac32b9aad30b1e55faba28200f2eec18",
    "https://filebroker-cdn.lazada.co.id/kf/Sceb1fbcd3150407da6c6721fc7e1b177C.jpg",
    "https://down-id.img.susercontent.com/file/311bb656142b84b11cd2e207be7589d5v",
    "https://id-test-11.slatic.net/p/b4c24938a040fba2260822ce1122b438.jpg",
    "https://down-id.img.susercontent.com/file/e46baa50780520bef890a2191349b607",
    "https://down-id.img.susercontent.com/file/720a45ec5a118c1cf5b837e637f1afff",
    "https://id-live-01.slatic.net/p/a62c5a49cc5f2913d95f722f28cef374.jpg",
    "https://down-id.img.susercontent.com/file/id-11134207-7r98y-lmn8ylydzgjy70",
    "https://img.lazcdn.com/g/ff/kf/Sf47f80cd1701460f8b311ea993cbfb47l.jpg_720x720q80.jpg",
    "https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full//97/MTA-5177851/firdaus_galian_montok_firdaus_jamu_madura_perawatan_payudara_herbal_full02_hlqdovw8.jpg",
    "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/img/VqbcmM/2023/11/12/eabe0d9f-b07c-4988-ba58-df094a94cb48.jpg~tplv-aphluv4xwc-resize-jpeg:700:0.jpg",
    "https://down-id.img.susercontent.com/file/id-11134207-7r990-lla3tu3sy7g10b"
]

# Isi mulai index ke-10
start_index = 10

# Masukkan link ke dataframe
for i, link in enumerate(links):
    df.loc[start_index + i, 'image'] = link

# Save
df.to_csv('hasil.csv', index=False)

print(df[['image']].head(15))