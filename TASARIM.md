# Gnomon Studio — tasarım ve içerik planı

18 Kasım 2026. Referanslar: Impala Studios (`/apps`), Codeway, Bending Spoons,
HubX. Ölçüt: Apple HIG (`~/.claude/skills/apple-design`, 123 sayfa).

---

## 1. Önce kötü haber: o üç sitenin kurgusu bizde çalışmaz

Codeway, Bending Spoons ve HubX aynı retorik üzerine kurulu: **büyüklük kanıtı.**

| Site | Kanıtı |
|---|---|
| Codeway | 594M+ kullanıcı · $0 dış yatırım · 34+ ürün |
| Bending Spoons | 1+ milyar kayıtlı · 500M+ aylık aktif · 9M+ ödeyen |
| HubX | 350M+ kullanıcı · 190 ülke |

Üçünde de ana sayfanın belkemiği bu sayılar. Bizde **yayımlanmış tek uygulama
yok** — Kademe mağazaya bile gönderilmedi. Bu yapıyı kopyalarsak her bölüm boş
bir çerçeve olur: "Uygulamalarımız ___ kişiye ulaştı."

Bu bir tasarım sorunu değil, **güvenilirlik sorunu**. Boş bırakılan sayı,
hiç koyulmamış sayıdan kötüdür.

### Bizim kanıtımız ne

Ölçek yerine **işin kendisi**. "600 milyon kişi" diyemeyiz; ama şunu diyebiliriz:

> İstanbul'da Kasım limiti 136,01 Sm³. Bir nefes aşarsan fatura 2.307 TL'den
> 3.511 TL'ye çıkıyor. Pahalanan aşan kısım değil, ayın tamamı.

Bu somut, doğrulanabilir ve kimsenin kopyalayamayacağı bir cümle. Tek uygulaması
olan ama o uygulamayı **belli ki iyi yapmış** bir stüdyo, büyük görünmeye
çalışan bir stüdyodan daha inandırıcıdır.

**Karar: v1'de indirme sayısı, kullanıcı yorumu, ödül rozeti, ekip fotoğrafı ve
müşteri logosu YOK.** Hiçbiri uydurulmayacak, hiçbiri boş çerçeve olarak
durmayacak. Gerçek sayı geldiğinde bölüm eklenir.

---

## 2. Hikâye

Adı zaten taşıyor. **Gnomon**, güneş saatinin gölgeyi düşüren çubuğu. Bilinen
en eski bilimsel alet. Hesap yapmaz, üretmez — **zaten orada olanı okunur
kılar.** Saati yaratmaz, saatin görülmesini sağlar.

Yaptığımız iş birebir bu:

- Limit zaten var. Tüketimin zaten var. Kademe ikisini **görünür** kılıyor.
- Uçurum zaten orada. Uygulama onu sen düşmeden önce gösteriyor.

Konumlandırma cümlesi:

> **Göremediğin şeyi, iş işten geçmeden gösteririz.**

Bunun "hayatı kolaylaştıran uygulamalar yapıyoruz"dan farkı şu: ikincisini
herkes söylüyor ve hiçbir şey vaat etmiyor. Birincisi bir söz veriyor ve
Kademe o sözü kelimesi kelimesine tutuyor.

### Ses tonu

HIG `writing.md › Getting started`: *"Determine your app's voice."*

Dürüst, ölçülü, abartısız. Kademe'nin kendi içindeki dil zaten bu — bilmediğini
"tahmini" diye işaretliyor, kotayı aşmış kullanıcıya "üşümene gerek yok"
diyor. Site de aynı sesle konuşacak. Ünlem yok, "devrim" yok, "en iyi" yok.

---

## 3. Tasarım sistemi

### 3.1 Işık kuralı — sistemin omurgası

Tek bir kural bütün siteyi yönetiyor: **ışık sol üstten gelir, gölge sağ alta
düşer. Her yüzeyde, her sayfada, istisnasız.**

Kartların aydınlık kenarı sol üstte, gölgesi sağ altta. Bölüm geçişleri sert
bir gölge çizgisiyle ayrılıyor. Hero'daki telefon ışığı soldan alıyor ve sağa
gölge düşürüyor — **telefonun kendisi gnomon oluyor.**

Bu "koyu zemin + bir vurgu rengi" klişesinden çıkış noktamız. O klişe her
yerde var; tutarlı tek bir ışık yönü yok. Ad, motif ve imza öğesi tek bir
görüntüde birleşiyor.

### 3.2 Renk

Rol bazlı, altı değer. Hepsi ölçüldü (WCAG, `kontrast.py`):

| Token | Değer | Rol | Kontrast |
|---|---|---|---|
| `--golge` | `#14130F` | Ana zemin (sıcak kömür, saf siyah değil) | — |
| `--tas` | `#211F18` | Yükseltilmiş yüzey, kart | — |
| `--isik` | `#F5F1E8` | Ana metin (kireçtaşı beyazı) | **16,49:1** / golge · **14,62:1** / tas |
| `--isik-2` | `#B5AF9F` | İkincil metin | **8,49:1** |
| `--isik-3` | `#7E7868` | Yalnız ikon ve ayraç, metin değil | **4,23:1** (eşik 3:1) |
| `--amber` | `#E9A23B` | Vurgu: güneş ışığı | **8,58:1** / golge · **7,61:1** / tas |

Açık zemin varyantı (yasal sayfalar, açık tema):
`--kagit #FAF8F3` · metin `#1A1813` (**16,71:1**) · ikincil `#5C564A`
(**6,86:1**) · amber metin `#8A5A00` (**5,58:1**).

Neden saf siyah değil: üç referansın üçü de siyah. Sıcak kömür hem ayırt
ediyor hem de güneş saati taşına ait. Neden amber: gölgeyi düşüren şey ışık.

`color.md › Best practices`: *"Avoid using the same color to mean different
things."* — Amber yalnız vurgu. Kademe'nin kendi durum renkleri (yeşil/amber/
kırmızı) **sadece** uygulama ekran görüntülerinin ve widget'ın içinde geçerli;
site kabuğunda kullanılmıyor. Aksi halde sitedeki amber "marka", widget'taki
amber "uyarı" olurdu ve aynı renk iki şey derdi.

### 3.3 Tipografi

- **Gövde ve arayüz: Inter** — uygulamada zaten gömülü, `assets/fonts/` içinde
  duruyor, kendi sunucumuzdan servis edilir. Üçüncü taraf istek yok.
- **Sayılar: Inter tabular figür**, her yerde. Uygulamalarımız sayı okutuyor;
  rakam bizde birinci sınıf vatandaş. `font-variant-numeric: tabular-nums`.
- **Başlık: Familjen Grotesk**, yalnızca h1–h3 ve marka kilidinde.
  `branding.md`: *"a custom font for headlines and subheadings while using
  system fonts for body copy"* — gövde yüzleri küçük boyutta okunurluk için
  çizilmiş, marka büyük metinde yaşar.

  Altı aday gerçek başlıklarla yan yana bakıldı (Archivo, Bricolage
  Grotesque, Instrument Sans, Syne, Sometype Mono, Inter). Seçim gerekçesi:
  kesikleri keskin ve hafif açılı — markanın gölge kenarıyla aynı dil;
  ğ ve ş kuyrukları düzgün; ³ ve ₺ dahil, yani eksik glif sessizce yedeğe
  düşmüyor; ve alt kümesi **24 KB**, Archivo'nun beşte biri. Ölçülülüğü
  savunan bir sitenin ağır bir başlık fontu taşıması tutarsız olurdu.

  Elenenler: Sometype Mono *(kavram olarak çekici — sayaç çıktısı gibi — ama
  uzun Türkçe cümlede çok geniş ve yorucu)*, Syne *(fazla moda)*, Archivo ve
  Bricolage *(karakter kazancı dosya boyutunu karşılamadı)*, Instrument Sans
  *(³ ve ₺ yok)*.

  Ağırlık ekseni 400–700; başlıklar bu aralıkta kalmak zorunda.

Taban ölçüler (`accessibility.md › Use recommended defaults`): gövde **17 px**,
mutlak alt sınır 11 px. İnce ağırlık küçük metinde kullanılmayacak.

> ⚠️ Bending Spoons ve Codeway'in ikisi de "sans başlığın içine serif italik"
> numarasını kullanıyor. Biz kullanmayacağız — iki referansta birden olan bir
> hamle bizim imzamız olamaz, taklit olur.

### 3.4 Hareket

`motion.md`: amaçlı, kısa, iptal edilebilir.

- Kaydırırken bölüm belirme: `animation-timeline: view()`, JS yok.
- **Tek koreografi anı:** hero'daki gölgenin sayfa açılırken bir kez uzaması.
  Günün ilerlemesi gibi. Başka hiçbir yerde dikkat çeken hareket yok.
- `prefers-reduced-motion` açıkken her şey son karesinde çizilir.

---

## 4. İmza öğesi

**iPhone ana ekranı, üzerinde Kademe widget'ı.** (Impala'nın yaptığı iş, ama
tek uygulamayla dürüst çalışan hâli.)

İçerik: durum çubuğu · büyük Kademe widget'ı (kota halkası %35 amber, "48,00
Sm³", "136,01 Sm³ limitte", "Aşım riski" çipi) · altında Kademe ikonu · sayfa
noktaları · iOS arama hapı. Dock yok — tek ikonu dock'ta tekrarlamak sahte
durur.

Boş görünmüyor çünkü **gerçek bir telefon da böyle görünür**: bir widget, bir
ikon. Uygulama çıktıkça ızgara doluyor, widget kalıyor.

Bütün cesaret burada harcanıyor. Geri kalan her şey sakin.
(`branding.md`: *"Ensure branding always defers to content."*)

### Marka işareti

Güneş saati kadranı, üzerinde merkezden kenara uzanan gölge yarığı.
**Tek yol, tek renk:** gölge boyalı değil, kadrandan çıkarılmış bir oyuk —
böylece koyu zeminde, açık zeminde, monokromda ve 16 pikselde aynı şekil.
Yarığın açısı **38°**, yani yukarıdaki ışık kuralıyla aynı.

Elenen yönler ve sebepleri: ince üçgen + taban çizgisi *(yelkenli
okunuyordu)*, köşeden bölünmüş yuvarlak kare *(app ikonu sanılıyordu)*,
merkeze doğru sivrilen gölge dilimi *(pasta grafiği okunuyordu)*, G harfi
*(kelime markasının yanında kendini tekrar ediyordu)*.

İşaret amber, kelime nötr: vurgu rengi tek yerde kalıyor.
Üretim: `python3 kontrol/marka-gorselleri.py` — favicon, Apple dokunma
ikonu ve OG görseli `Logo.astro` ile aynı geometriden türüyor.

---

## 5. Sayfa yapısı

```
/                               Ana sayfa
/uygulamalar.html               Ana ekran, tam boy
/kademe.html                    Kademe tanıtım sayfası
/kademe/destek.html             Destek + SSS        ← mağaza bu adresi istiyor
/kademe/gizlilik.html           Gizlilik            ← uygulamaya gömülü
/kademe/kullanim-kosullari.html Koşullar            ← uygulamaya gömülü
/hakkimizda.html                Hikâye
/iletisim.html
```

`build.format: 'file'` alt klasörün index'ini `/kademe.html` olarak üretiyor,
`/kademe/` olarak değil. Yani her uygulama bir `/<slug>.html` sayfası + bir
`/<slug>/` belge klasörü oluyor. Çıplak `/<slug>/` adresi 404 olmasın diye
`public/<slug>/index.html` içinde meta-refresh durağı var — JS değil, her
barındırmada çalışıyor.

**`.html` uzantısı korunuyor.** Sebebi: Kademe'nin `app_config.dart`
varsayılanları bu adresleri içinde taşıyor. Uzantısız temiz adrese geçmek
uygulamadaki üç bağlantıyı kırardı.

### Değişmesi gereken tek şey

Uygulamadaki `SUPPORT_URL` şu an `https://gnomonstudio.com/kademe/` — yani
`/kademe/` destek sayfası sanılıyor. Ama orası tanıtım sayfası olacak. İki
yerde tek satır değişiyor:

- `kademe_app/lib/core/config/app_config.dart` → `supportUrl` varsayılanı
- `kademe_app/supabase.local.json` → `SUPPORT_URL`

İkisi de `/kademe/destek.html` olacak. Mağazaya gönderilmediği için şu an
bedava; gönderimden sonra bu değişiklik eski sürümlerde ölü bağlantı demek.

### 5.1 Ana sayfa

| # | Bölüm | İçerik |
|---|---|---|
| 1 | Hero | Konumlandırma cümlesi + tek paragraf. Gölge koreografisi burada. |
| 2 | **Ana ekran** | İmza öğesi. Diğerlerinin sayı koyduğu yere biz işi koyuyoruz. |
| 3 | Nasıl çalışıyoruz | Üç ilke, her birinin altında Kademe'den **gerçek** kanıt: bilmediğinde "tahmini" der · okumalar cihazdan çıkmaz · her uygulama tek soruya cevap verir |
| 4 | Kademe şeridi | Uçurum rakamı (136,01 → 1.204 TL), app sayfasına bağlantı |
| 5 | Footer | İletişim, yasal, sosyal |

Ana sayfada gnomon hikâyesi **anlatılmıyor**. Hero görseli zaten onu söylüyor;
altına bir de yazmak aynı şeyi iki kez söylemek olur. Hikâye `/hakkimizda/`'da.

### 5.2 `/uygulamalar/`

Impala kalıbı: kısa giriş + tam boy ana ekran. İkonlar tıklanabilir. Bir
uygulamanın sayfası varsa oraya, yoksa doğrudan mağazaya gider — Impala da
böyle yapıyor, hepsine sayfa açmak zorunda değiliz.

### 5.3 `/kademe/`

Ora Weather kalıbı, kanıtlanmış ve tekrarlanabilir:

ikon → ad → iki satır vaat → App Store rozeti → sola-sağa dönüşümlü
telefon/metin blokları (her blok bir özellik: üst başlık + kalın başlık + iki
cümle) → kapanış CTA'sı.

Özellik blokları: uçurum eğrisi · kota halkası ve ay sonu tahmini · dürüst
hesap ("tahmini" etiketi) · merkezi sistem · Pro.

### 5.4 Yasal ve destek sayfaları

İçerik aynen taşınıyor (`icerik/kademe/*.md`). **Sıfır JavaScript**, pazarlık
yok: App Store incelemesi gizlilik adresini bazen otomatik denetleyiciyle
açıyor, boş ekran 3.1.2'den red. Astro varsayılanı zaten sıfır JS.

---

## 6. Erişilebilirlik tabanı

`accessibility.md` sayıları, istisnasız:

- Metin ≤17 px → **4,5:1** · ≥18 px veya kalın → **3:1**. Palet tablosu yukarıda.
- Dokunma hedefi **44×44 px**, mutlak alt sınır 28×28. Aralarında ~12 px boşluk.
- Renk tek başına hiçbir anlamı taşımaz.
- `prefers-reduced-motion`, `prefers-contrast`, açık/koyu tema: üçünün de karşılığı var.
- Telefon genişliğinde yatay kaydırma yok, 16 px kenar boşluğu.

---

## 7. Sıra

1. **Altyapı** — Cloudflare Pages projesi, depo bağlantısı, Email Routing
2. **İskelet** — Astro düzeni, token'lar, yasal + destek sayfalarının taşınması
   (bu noktada site eskisiyle aynı işi görüyor, mağaza bağlantıları çalışıyor)
3. **İmza** — ana ekran + widget bileşeni
4. **Ana sayfa**
5. **`/kademe/` sayfası**
6. **Yayın öncesi** — gerçek ekran görüntüleri, App Store rozeti, OG görselleri, sitemap

---

## 8. Açık kararlar

| Konu | Durum |
|---|---|
| ~~**Başlık yazı tipi**~~ | ✅ Familjen Grotesk, 24 KB alt küme (§3.3). |
| ~~**Gnomon logosu**~~ | ✅ Çizildi — güneş saati kadranı + gölge yarığı (§4). |
| ~~**Ekran görüntüleri**~~ | ✅ Simülatörden çekildi (iPhone 16 Pro Max, 1320×2868, koyu tema). |
| **Dil** | v1 Türkçe. `/en/` henüz kurulmadı; ajans/yatırım tarafı gündeme gelince açılacak. |
| **HTTPS** | GitHub sertifikayı henüz vermedi. DNS doğru (CAA engeli yok, dört A kaydı, www CNAME). Normal penceresi 24 saat; geçerse alan adını panelden kaldırıp yeniden eklemek gerekiyor. |
| **Mağaza rozetleri** | Uygulama yayımlanınca App Store / Google Play rozetleri eklenecek. |
