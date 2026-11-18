// @ts-check
import { defineConfig } from 'astro/config';

// Çıktı `docs/` altına yazılıyor: hem GitHub Pages hem Cloudflare Pages bu
// klasörü derleme işi kurmadan doğrudan yayımlayabiliyor. Eski pandoc
// kurulumu da aynı sebeple buraya yazıyordu, desen korunuyor.
//
// Astro varsayılan olarak **sıfır JavaScript** üretir: bir bileşene
// `client:*` direktifi verilmedikçe tarayıcıya hiç script inmez. Yasal
// sayfaların JS'siz kalması bu projede tercih değil zorunluluk — App Store
// incelemesi gizlilik adresini bazen otomatik bir denetleyiciyle açıyor ve
// boş ekran 3.1.2'den red demek.
export default defineConfig({
  site: 'https://gnomonstudio.com',
  outDir: './docs',
  build: {
    // 'file' = /kademe/gizlilik.html. Uzantısız "temiz adres" DEĞİL, çünkü
    // Kademe'nin app_config.dart varsayılanları bu adresleri .html uzantılı
    // olarak içinde taşıyor; uzantıyı atmak uygulamadaki üç bağlantıyı
    // birden kırardı.
    format: 'file',
  },
});
