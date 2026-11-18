---
layout: ../../layouts/Belge.astro
baslik: "Kademe Gizlilik Politikası"
aciklama: "Kademe uygulamasının hangi verileri işlediği. Kısa cevap: sayaç okumalarınız varsayılan olarak cihazınızdan çıkmaz."
ustBaslik: "Kademe"
---
**Son güncelleme:** 19 Kasım 2026

Bu metin Kademe uygulamasının hangi verileri işlediğini anlatır. Kısa cevap:
**sayaç okumalarınız varsayılan olarak cihazınızdan çıkmaz.**

---

## 1. Varsayılan: her şey cihazda

Uygulamayı kurduğunuzda hiçbir hesap açmanız gerekmez ve hiçbir veriniz
sunucuya gitmez. Şunlar yalnızca telefonunuzda saklanır:

- Sayaç bilgileri (verdiğiniz ad, il, sayaç tipi, bağımsız bölüm sayısı,
  düzeltme katsayısı, girdiyseniz birim fiyatlar)
- Girdiğiniz sayaç okumaları ve tarihleri
- Uygulama tercihleri (tema, bildirim ayarları)

Kota hesapları, projeksiyon, aşım tahmini ve fatura tahmini **cihazınızda**
yapılır. Bunun için internet bağlantısı gerekmez.

## 2. Bildirimler

Limit uyarıları cihazınızda hesaplanır ve cihazınızda zamanlanır. Bildirim
göndermek için verileriniz hiçbir yere iletilmez; sunucudan gelen bir bildirim
yoktur. Bildirim izni vermezseniz uygulamanın geri kalanı normal çalışır.

## 3. İsteğe bağlı: yedekleme ve senkronizasyon

Ayarlar → Hesap ve yedekleme bölümünden açarsanız, yalnızca **açarsanız**,
sayaç bilgileriniz ve okumalarınız hesabınıza bağlı olarak sunucumuzda
saklanır. Amaç: telefonunuzu değiştirdiğinizde ya da kaybettiğinizde
verilerinizi geri yükleyebilmek ve ikinci bir cihazla eşitlemek.

Bu özellik **varsayılan olarak kapalıdır**. Açtığınızda uygulama bunu size
açıkça söyler. İstediğiniz zaman kapatabilirsiniz; kapatmak cihazınızdaki
verileri silmez.

**Hesap:** İlk açılışta rastgele üretilen anonim bir kimlik kullanılır; bu
kimlik sizi tanımlayan hiçbir kişisel bilgi içermez. Dilerseniz Apple, Google
veya e-posta ile kalıcı bir kimlik bağlayabilirsiniz; bu, cihazınızı
kaybettiğinizde verilerinize ulaşmanın tek yoludur. E-posta ile bağlarsanız
e-posta adresiniz saklanır ve şifreniz yalnızca geri döndürülemez bir özet
(hash) olarak tutulur; şifrenizin kendisi ne bizde ne sunucuda bulunur.
Apple veya Google ile bağlarsanız yalnızca sağlayıcının verdiği kimlik
saklanır.

**Altyapı:** Yedekleme verisi Supabase üzerinde barındırılır. Satır düzeyi
güvenlik kuralları sayesinde yalnızca kendi kayıtlarınıza erişebilirsiniz.

## 4. İsteğe bağlı: fatura PDF'inden ve fotoğraftan okuma

Kademe Pro'da fatura PDF'inizden, fatura fotoğrafınızdan veya sayaç
fotoğrafınızdan değerleri okutabilirsiniz. Bu, uygulamadaki **tek
istisnadır**: bunun dışındaki her şey cihazınızda kalır.

Özellik **varsayılan olarak kapalıdır**. İlk kullanımdan önce size ne
olduğunu anlatan bir ekran gösterilir ve onayınız alınır. Onay vermezseniz
özellik çalışmaz; uygulamanın geri kalanı etkilenmez.

Özellik yalnızca Kademe Pro'da bulunur ve her sürümde açık olmayabilir.
Uygulamanızda görünmüyorsa bu bölümde anlatılanların hiçbiri gerçekleşmez:
hiçbir dosya cihazınızdan çıkmaz.

**Dosyaya ne oluyor.** Seçtiğiniz dosya sunucumuza, oradan da metin okuyan
yapay zekâ modeline (OpenAI) gönderilir. Model fatura veya sayaç üzerindeki
sayıları okur ve yalnızca bu sayıları geri döndürür. Dosya hiçbir yere
kaydedilmez: ne sunucumuzun diskine, ne bir depolama alanına, ne de günlük
kayıtlarına yazılır. İstekle birlikte gelir, yanıtla birlikte silinir.

PDF seçtiğinizde kamera ya da fotoğraf izni istenmez: sistemin dosya
seçicisi yalnızca sizin seçtiğiniz tek dosyayı uygulamaya verir.

**Neyin okunduğu.** Faturadan yalnızca hesapla ilgili satırlar okunur: okuma
tarihi, düzeltme katsayısı, üst ısıl değer, kademe birim fiyatları ve sayaç
endeksi. Faturadaki ad, adres, abone numarası ve tesisat numarası
**istenmez ve saklanmaz**.

**Kaydedilenler.** Dosya saklanmasa da, aylık kullanım hakkınızı takip
edebilmek için şunlar tutulur: 3. bölümde anlatılan anonim kimliğiniz, ay, ve
o ay kaç kez okuma yaptığınız. Bu kayıt dosyanın içeriğiyle ilgili hiçbir
bilgi taşımaz.

**Fotoğraf arşivinize erişmiyoruz.** Yalnızca o an seçtiğiniz tek kareyi
alırız. Galerinizi tarayamaz, listeleyemez ve başka bir fotoğrafa
erişemeyiz.

## 5. Abonelik

Kademe Pro aboneliği App Store veya Google Play üzerinden satılır ve
RevenueCat ile yönetilir. **Ödeme bilgileriniz bize ulaşmaz**; kart
bilgilerinizi yalnızca Apple veya Google görür. Bizim öğrendiğimiz tek şey
aboneliğinizin etkin olup olmadığıdır.

Abonelik için hesap açmanız gerekmez; satın alma mağaza hesabınıza bağlıdır
ve "Satın alımları geri yükle" ile her cihazda geri getirilebilir.

## 6. Yapmadıklarımız

- **Reklam göstermiyoruz** ve hiçbir reklam ağı kullanmıyoruz.
- **Sizi takip etmiyoruz.** Reklam kimliği (IDFA) okumuyoruz, cihaz parmak
  izi çıkarmıyoruz, verilerinizi başka uygulamalardaki davranışınızla
  birleştirmiyoruz.
- **Verilerinizi satmıyoruz** ve pazarlama amacıyla üçüncü taraflarla
  paylaşmıyoruz.
- **Konumunuza erişmiyoruz.** İl bilgisini siz seçersiniz; GPS kullanılmaz.
- **Rehberinize erişmiyoruz.**
- **Çerez kullanmıyoruz.** Bu politikanın yayımlandığı site tamamen
  statiktir: çerez yok, JavaScript yok, analitik yok. Bu yüzden ayrı bir
  çerez politikası da yok.
- **Fotoğraf arşivinizi taramıyoruz.** Kamera ve fotoğraflar yalnızca
  fotoğraftan okuma özelliğini siz kullandığınızda devreye girer ve orada da
  yalnızca o an seçtiğiniz tek kare alınır (4. bölüm).

## 7. Tarife verisi

İl bazlı aylık limitler BOTAŞ'ın yayımladığı kamuya açık tablodan gelir ve
uygulamayla birlikte dağıtılır. Bu veriyi almak için sizden hiçbir bilgi
gönderilmez.

## 8. Veri saklama ve silme

- **Cihazdaki veriler:** Uygulamayı silmeniz tüm yerel verileri siler.
  Ayarlar'dan sayacı ve okumaları tek tek de silebilirsiniz.
- **Yedeklenen veriler:** Yedeklemeyi kapatmak eşitlemeyi durdurur, sunucudaki
  kopyayı silmez.
- **Hesabınızı silmek:** Hesabınızı ve sunucuda tutulan verilerinizin tamamını
  uygulamanın içinden silebilirsiniz: **Ayarlar → Hesap ve yedekleme →
  Hesabı sil**. Silme hemen gerçekleşir, geri alınamaz ve bir talep sırası
  beklemez. Telefonunuzdaki sayaçlar ve okumalar silinmez; uygulama yerel
  olarak çalışmaya devam eder. Dilerseniz aşağıdaki adresten de talep
  edebilirsiniz; bu yolla gelen talepler en geç 30 gün içinde yerine
  getirilir.
- Silinen kayıtlar, cihazlar arası tutarlılık için en fazla 180 gün boyunca
  yalnızca "silindi" işareti olarak tutulur; içerikleri saklanmaz.

## 9. Hukuki sebep ve toplama yöntemi

Kişisel verileriniz **yalnızca uygulamayı kullanmanız sırasında, sizin
girdiğiniz veya seçtiğiniz bilgilerden** toplanır. Arka planda çalışan bir
toplama yoktur; veri satın alınmaz, başka kaynaklardan derlenmez.

| Ne | Nasıl toplanıyor | Neden işleniyor |
|---|---|---|
| Sayaç bilgisi ve okumalar | Siz girersiniz | Kota hesabı — sözleşmenin ifası |
| Yedeklenen kopya | Siz açarsanız | Verinizi geri yükleyebilmeniz — açık rızanız |
| Fatura PDF'i / fotoğraf | Siz seçip yüklersiniz | Sayıları okuyup size döndürmek — açık rızanız |
| Abonelik durumu | Mağazadan gelir | Pro erişimi — sözleşmenin ifası |

Yedekleme ve fotoğraftan okuma **varsayılan olarak kapalıdır**; siz
açmadıkça bu veriler hiç işlenmez. İstediğiniz zaman kapatabilirsiniz.

## 10. Yurt dışına aktarım

Varsayılan kullanımda hiçbir veriniz yurt dışına çıkmaz, çünkü cihazdan
hiç çıkmaz. Yalnızca aşağıdaki iki özelliği **siz açarsanız** aktarım olur:

| Özellik | Nereye | Ülke |
|---|---|---|
| Yedekleme ve senkron | Supabase | Almanya (Frankfurt) |
| Fatura PDF'i / fotoğraftan okuma | Sunucumuz → OpenAI | ABD |

Fotoğraf ve PDF hiçbir yere kaydedilmez: istekle birlikte gider, yanıtla
birlikte silinir (4. bölüm). Her iki özellik de ilk kullanımdan önce size
ne olduğunu anlatır ve onayınızı ister; onay vermezseniz özellik çalışmaz
ve uygulamanın geri kalanı etkilenmez.

## 11. Haklarınız (KVKK madde 11)

6698 sayılı Kişisel Verilerin Korunması Kanunu'nun 11. maddesi uyarınca
şu haklara sahipsiniz:

- Kişisel verinizin işlenip işlenmediğini **öğrenme**
- İşlenmişse buna ilişkin **bilgi talep etme**
- İşlenme amacını ve amacına uygun kullanılıp kullanılmadığını öğrenme
- Yurt içinde veya yurt dışında **aktarıldığı üçüncü kişileri bilme**
- Eksik veya yanlış işlenmişse **düzeltilmesini** isteme
- Kanundaki şartlar çerçevesinde **silinmesini veya yok edilmesini** isteme
- Düzeltme ve silme işlemlerinin aktarıldığı üçüncü kişilere **bildirilmesini**
  isteme
- İşlenen verilerin münhasıran otomatik sistemlerle analiz edilmesi
  suretiyle aleyhinize bir sonuç çıkmasına **itiraz etme**
- Kanuna aykırı işleme sebebiyle zarara uğramanız hâlinde **zararın
  giderilmesini** talep etme

Taleplerinizi aşağıdaki iletişim adresine yazabilirsiniz; en geç **30 gün**
içinde sonuçlandırılır. Hesabınızı ve sunucudaki verilerinizi beklemeden,
doğrudan uygulamanın içinden de silebilirsiniz (8. bölüm).

## 12. Çocuklar

Uygulama 13 yaş altı kullanıcılara yönelik değildir ve bilerek bu yaş
grubundan veri toplamaz.

## 13. Değişiklikler

Bu metinde önemli bir değişiklik olursa uygulama içinde bildirilir ve
yukarıdaki tarih güncellenir.

## 14. İletişim

Gizlilikle ilgili her konu için: **kademe@gnomonstudio.com**

