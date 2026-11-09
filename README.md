# Uygulamalar

Yayımlanan mobil uygulamaların **destek ve yasal sayfaları**. Tek site,
uygulama başına bir klasör.

Her uygulama için App Store ve Google Play üç adres istiyor: destek, gizlilik
politikası, kullanım koşulları. Uygulama başına ayrı alan adı almak yerine
hepsi burada duruyor; yeni uygulama bir klasör demek.

## Yapı

```
icerik/            kaynak (Markdown)
  index.md         yayıncı sayfası
  kademe/
    index.md       destek + sık sorulanlar
    gizlilik.md
    kullanim-kosullari.md
sablon.html        ortak HTML iskeleti (pandoc şablonu)
assets/style.css   tek CSS, JavaScript yok
site.json          site geneli değişkenler (iletişim adresi, yayıncı adı)
docs/              ÜRETİLEN site; GitHub Pages buradan yayımlıyor
```

## Derleme

```bash
python3 build.py
```

`pandoc` gerekiyor (`brew install pandoc`). Çıktı `docs/` altına yazılıyor ve
depoya commit ediliyor: Pages ayrı bir derleme işi çalıştırmadan doğrudan
yayımlasın diye.

## Neden düz HTML

Mağaza incelemesi gizlilik adresini bazen otomatik bir denetleyiciyle
açıyor. Sayfanın görünmesi JavaScript'in çalışmasına bağlıysa boş ekran
görme ihtimali var ve bu App Store 3.1.2'den red demek. Üretilen dosyalarda
hiç script yok.

## Alan adı

Şu an GitHub Pages'in varsayılan adresinde. Özel alan adı alınınca:

1. `docs/CNAME` dosyasına alan adını yaz
2. DNS'te A kayıtlarını GitHub Pages'e yönlendir
3. `site.json` içindeki `eposta` ve `yayinci` alanlarını doldur, yeniden derle
4. Uygulamalardaki `TERMS_URL` / `PRIVACY_URL` değerlerini güncelle

Yollar göreli yazıldığı için site hem alt yolda hem alan adının kökünde
çalışıyor; taşımak DNS dışında bir şey gerektirmiyor.
