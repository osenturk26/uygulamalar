---
title: "Kademe Gizlilik Politikası"
aciklama: "Kademe uygulamasının hangi verileri işlediği. Kısa cevap: sayaç okumalarınız varsayılan olarak cihazınızdan çıkmaz."
---

**Son güncelleme:** 8 Kasım 2026

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

## 4. Abonelik

Kademe Pro aboneliği App Store veya Google Play üzerinden satılır ve
RevenueCat ile yönetilir. **Ödeme bilgileriniz bize ulaşmaz**; kart
bilgilerinizi yalnızca Apple veya Google görür. Bizim öğrendiğimiz tek şey
aboneliğinizin etkin olup olmadığıdır.

Abonelik için hesap açmanız gerekmez; satın alma mağaza hesabınıza bağlıdır
ve "Satın alımları geri yükle" ile her cihazda geri getirilebilir.

## 5. Yapmadıklarımız

- **Reklam göstermiyoruz** ve hiçbir reklam ağı kullanmıyoruz.
- **Sizi takip etmiyoruz.** Reklam kimliği (IDFA) okumuyoruz, cihaz parmak
  izi çıkarmıyoruz, verilerinizi başka uygulamalardaki davranışınızla
  birleştirmiyoruz.
- **Verilerinizi satmıyoruz** ve pazarlama amacıyla üçüncü taraflarla
  paylaşmıyoruz.
- **Konumunuza erişmiyoruz.** İl bilgisini siz seçersiniz; GPS kullanılmaz.
- **Rehberinize, fotoğraflarınıza veya kameranıza erişmiyoruz.**

## 6. Tarife verisi

İl bazlı aylık limitler BOTAŞ'ın yayımladığı kamuya açık tablodan gelir ve
uygulamayla birlikte dağıtılır. Bu veriyi almak için sizden hiçbir bilgi
gönderilmez.

## 7. Veri saklama ve silme

- **Cihazdaki veriler:** Uygulamayı silmeniz tüm yerel verileri siler.
  Ayarlar'dan sayacı ve okumaları tek tek de silebilirsiniz.
- **Yedeklenen veriler:** Yedeklemeyi kapatmak eşitlemeyi durdurur.
  Hesabınızdaki kopyanın tamamen silinmesini isterseniz aşağıdaki adresten
  talep edebilirsiniz; talebiniz en geç 30 gün içinde yerine getirilir.
- Silinen kayıtlar, cihazlar arası tutarlılık için en fazla 180 gün boyunca
  yalnızca "silindi" işareti olarak tutulur; içerikleri saklanmaz.

## 8. Haklarınız (KVKK)

6698 sayılı Kişisel Verilerin Korunması Kanunu kapsamında; işlenen
verileriniz hakkında bilgi talep etme, düzeltilmesini veya silinmesini
isteme ve işlemeye itiraz etme haklarına sahipsiniz. Talepleriniz için
aşağıdaki adrese yazabilirsiniz.

## 9. Çocuklar

Uygulama 13 yaş altı kullanıcılara yönelik değildir ve bilerek bu yaş
grubundan veri toplamaz.

## 10. Değişiklikler

Bu metinde önemli bir değişiklik olursa uygulama içinde bildirilir ve
yukarıdaki tarih güncellenir.

## 11. İletişim

Gizlilikle ilgili her konu için: **{{EPOSTA}}**

