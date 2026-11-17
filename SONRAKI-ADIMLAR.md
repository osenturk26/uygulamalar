# Sonraki adımlar: alan adı, bağlantılar, yönetim paneli

Yayına almadan önce bakılacak. 9 Kasım 2026'da konuşuldu, karar ertelendi.

---

## 1. Alan adı: `appdestek.com`

Alınacak ve bu sitenin önüne konacak. Yapı **yollarla** kalıyor, alt alan
adıyla değil:

```
appdestek.com/kademe/gizlilik.html
appdestek.com/dubai/gizlilik.html
```

Alt alan adı (`kademe.appdestek.com`) değerlendirildi ve bırakıldı: GitHub
Pages'te bir depo bir özel alan adı tutuyor, yani uygulama başına alt alan
adı uygulama başına ayrı depo demek. Şablon, CSS ve derleme betiği her
depoda kopyalanır; bir stil düzeltmesi N commit olur. Karşılığında mağaza
tarafında hiçbir kazanç yok, Apple da Google da yol mu alt alan adı mı
diye bakmıyor.

Bir uygulama kendi kimliğini hak ettiğinde ona **gerçek bir alan adı**
verilecek (`kademe.app` gibi), alt alan adı değil.

### Geçiş adımları

1. `docs/CNAME` dosyasına `appdestek.com` yaz
2. DNS: apex için GitHub Pages A kayıtları, `www` için CNAME
3. `site.json` → `eposta` (`destek@appdestek.com`) ve `yayinci` doldur,
   `python3 build.py`
4. Uygulamalardaki üç adres: `TERMS_URL`, `PRIVACY_URL`, `SUPPORT_URL`
   (`--dart-define-from-file` dosyasından, kod değişmiyor)
5. App Store Connect ve Google Play Console'daki gizlilik ve destek
   adreslerini güncelle

> ⚠️ **Mağazaya göndermeden ÖNCE yapılmalı.** Bu adresler uygulamanın
> içine derleniyor: bir sürüm yayımlandıktan sonra alan adı değişirse o
> sürümü kullananlar ölü bağlantıya çarpar, ve kırık bir gizlilik
> bağlantısı App Store 3.1.2'nin konusu. Yani ya alan adı baştan doğru
> olacak ya da eskisi süresiz ayakta tutulacak.

### 15 uygulamada ne oluyor

17 Kas 2026'da hesaplandı. Zaman içinde 10-15 uygulama hedefleniyor ve
sorulan soru "uygulama başına ne ödeyeceğim" idi. Cevap: **hiçbir şey.**

| Kalem | 1 uygulama | 15 uygulama | Neden |
|---|---|---|---|
| Alan adı | ~$12/yıl | ~$12/yıl | Tek alan adı, yollarla bölünüyor |
| Barındırma | 0 | 0 | GitHub Pages, tek depo |
| E-posta | 0 | 0 | Yönlendirme, uygulama başına takma ad |
| Apple Developer | $99/yıl | $99/yıl | Üyelik hesaba ait, uygulamaya değil |

Yollarla gitmenin asıl kazancı burada görünüyor ve barındırma kısıtından
daha güçlü: **yeni uygulama hiçbir yapılandırma istemiyor.** Alt alan adı
seçilseydi her uygulama için bir DNS kaydı, bir sertifika beklemesi ve bir
panel adımı olurdu. Yolla ise yeni uygulama bir klasör demek:

1. `icerik/<uygulama>/` altına üç sayfa
2. `python3 build.py`
3. Uygulamanın `--dart-define-from-file` dosyasına üç adres
4. E-posta takma adı

### E-posta: uygulama başına adres, ücretsiz

Tek bir `destek@` yerine **uygulama başına takma ad** daha iyi:
`kademe@`, `<uygulama>@`. Gelen kutusunda hangi uygulamadan geldiği
belli oluyor, ve bir uygulama devredilirse adresi de onunla gidiyor.

Yol: alan adının DNS'i **Cloudflare**'e alınır (alan adı nereden alınmış
olursa olsun) ve **Email Routing** açılır. Gelen posta yönlendirmesi
ücretsiz ve alan adı başına 200 kurala kadar çıkıyor; 15 uygulama için
fazlasıyla yeterli. Hepsi aynı Gmail kutusuna düşer.

> **Tek eksiği yanıt verirken görünen adres.** Yönlendirme gelen postayı
> taşıyor; `kademe@` adresinden **yanıt** göndermek ayrı bir SMTP
> istiyor (Gmail'deki "Send mail as"). Mağaza incelemesi için önemli olan
> postanın ulaşması, o yüzden bu bir engel değil; ama destek yazışması
> başlayınca halledilmeli.

---

## 2. Yönetim paneli

Hedef: uygulamaların istatistiklerini, bildirimlerini ve içeriğini tek
yerden yönetmek. `appdestek.com` altında.

Kademe'nin planında Faz 5 olarak zaten var ve şeması uygulandı; tablolar
Supabase'de duruyor:

| Tablo | Ne için |
|---|---|
| `devices` | cihaz listesi, il/platform/sürüm/Pro dağılımı |
| `tariff_versions` + `gas_limits` / `gas_prices` | **asıl iş**: BOTAŞ revizyonlarını yayınlamak |
| `notification_campaigns` | hedefli bildirim (il, Pro durumu, sürüm) |
| `app_content` | duyuru, ipucu, SSS |
| `analytics_events` | olay grafikleri |

`admins` tablosu ve `is_admin()` fonksiyonu da şemada; yazma yetkisi ona
bağlı.

**En kritik ekran `tariffs`.** BOTAŞ limitleri habersiz revize ediyor (30
Ekim 2026'da İstanbul'un Kasım limiti 101,71'den 136,01'e çıktı). Akış:
`tools/botas_import.dart` ile PDF'i ayrıştır → panelde diff önizle → onayla
→ sürüm yayınla → uygulamalar bir sonraki açılışta çeker.

**Karar verilmedi:** panel ayrı bir Flutter Web uygulaması mı olacak
(Dubai Guide'ın `admin_panel` şablonu var), yoksa bu statik sitenin yanına
mı konacak. Statik site + JavaScript panel aynı depoda durabilir ama
şu anki sitenin "hiç script yok" özelliğini korumak gerekiyor — yasal
sayfaların JavaScript'e bağlı olmaması bilinçli bir karar.

---

## 3. Uygulama içi bağlantılar

Her uygulamanın mağazada **üç** adrese ihtiyacı var:

| Adres | Nerede isteniyor | Kademe'de |
|---|---|---|
| Gizlilik politikası | App Store Connect + Play Console | `AppConfig.privacyUrl` |
| Kullanım koşulları | Abonelik meta verisi (3.1.2) | `AppConfig.termsUrl` |
| Destek | App Store Connect | `AppConfig.supportUrl` |

Üçü de şu an GitHub Pages adresini gösteriyor ve çalışıyor. Alan adı
gelince değişecek.
