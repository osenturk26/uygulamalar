# Gnomon Studio

Stüdyonun sitesi: uygulamaların tanıtımı, destek ve yasal sayfaları.
Tek site, uygulama başına bir klasör.

> **Göremediğin şeyi, iş işten geçmeden gösteririz.**

Her uygulama için App Store ve Google Play üç adres istiyor: destek, gizlilik
politikası, kullanım koşulları. Uygulama başına ayrı alan adı almak yerine
hepsi burada duruyor; yeni uygulama bir klasör demek.

Astro · sıfır JavaScript çıktısı · `gnomonstudio.com`

## Yapı

```
src/
  pages/           sayfalar (dosya adı = adres)
    index.astro          /
    uygulamalar.astro    /uygulamalar.html
    hakkimizda.astro     /hakkimizda.html
    iletisim.astro       /iletisim.html
    kademe/
      index.astro        /kademe.html          tanıtım
      destek.md          /kademe/destek.html   destek + SSS
      gizlilik.md        /kademe/gizlilik.html
      kullanim-kosullari.md
  layouts/
    Temel.astro      site kabuğu (gezinme, footer)
    Belge.astro      yasal ve destek metinleri — SIFIR JS
  components/        paylaşılan parçalar
  data/site.js       site değişkenleri + uygulama kaydı
  styles/global.css  tasarım tokenları
public/            olduğu gibi kopyalanan dosyalar (font, ikon, ekran görüntüsü)
dist/              ÜRETİLEN site; depoya girmiyor
TASARIM.md         tasarım ve içerik planı
```

Tasarım kararlarının tamamı **`TASARIM.md`** içinde: hikâye, renk paleti
(ölçülmüş kontrast oranlarıyla), ışık kuralı, imza öğesi ve sayfa planı.

## Derleme

```bash
npm install     # ilk kurulumda bir kez
npm run build   # src/ → docs/
npm run dev     # yerel sunucu, canlı yenileme
```

Çıktı `dist/` altına yazılıyor ve **depoya girmiyor**. GitHub yalnız kaynak
kodu tutuyor; barındırma Cloudflare'de ve `npm run dagit` yerelde derleyip
gönderiyor.

> **Eski pandoc kurulumu (`build.py`, `sablon.html`, `icerik/`, `assets/`)
> artık kullanılmıyor.** İçerik `src/pages/` altına taşındı. `build.py`
> çalıştırılırsa `docs/` klasörünü silip eski dört sayfayı geri yazar, yani
> yeni siteyi ezer. Rahat olduğunda bu dört yol silinebilir; git'te duruyorlar.

## Yayın

Site Cloudflare Workers'ın statik varlık sunumuyla yayımlanıyor
(`wrangler.jsonc`). Pages değil, çünkü hesabın API token'ı Pages'e kapalı,
Workers'a açık; sonuç aynı.

```bash
npm run dagit     # derler ve Cloudflare'e gönderir
```

Kimlik bilgileri `.cloudflare.local.json` içinde ve **depoya girmiyor**.
Şablonu:

```json
{
  "CLOUDFLARE_ACCOUNT_ID": "...",
  "CLOUDFLARE_API_TOKEN": "..."
}
```

Token'ın ihtiyacı olan yetki: **Hesap → Workers Scripts → Edit**.
Alan adını bağlamak için ayrıca **Bölge → DNS → Edit** gerekiyor.

> **GitHub Pages bırakıldı.** Depo artık yalnız kaynak kodu tutuyor.
> Üretilmiş HTML commit edilmiyor, CNAME dosyası yok, adresler alan adının
> kökünü varsayıyor (mutlak yol). Bu üçü de GitHub Pages'in gereksinimiydi:
> Pages derleme çalıştırmadığı için çıktının commit'lenmesini, özel alan adı
> için CNAME dosyasını, ve `/uygulamalar/` alt yolunda çalışmak için göreli
> yolları istiyordu. Hiçbiri artık geçerli değil.

## Adresler neden `.html` uzantılı

Kademe'nin `app_config.dart` varsayılanları gizlilik ve kullanım koşulları
adreslerini **uygulamanın içinde** taşıyor ve `.html` uzantılılar. Uzantısız
"temiz adres"e geçmek o bağlantıları kırardı. Bu yüzden `build.format` ayarı
`'file'`.

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
