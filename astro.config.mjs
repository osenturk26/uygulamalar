// @ts-check
import { defineConfig } from 'astro/config';

// Çıktı `dist/` altına yazılıyor ve DEPOYA GİRMİYOR.
//
// Eskiden `docs/` idi ve commit ediliyordu, çünkü GitHub Pages o klasörü
// derleme işi kurmadan yayımlayabiliyordu. Barındırma Cloudflare'e geçince
// o gerekçe kalmadı: `npm run dagit` yerelde derleyip gönderiyor. Üretilmiş
// HTML'i depoda tutmak her commit'i şişiriyordu ve kaynakla çıktının
// ayrışması için ayrı bir yol açıyordu.
//
// Astro varsayılan olarak **sıfır JavaScript** üretir: bir bileşene
// `client:*` direktifi verilmedikçe tarayıcıya hiç script inmez. Yasal
// sayfaların JS'siz kalması bu projede tercih değil zorunluluk — App Store
// incelemesi gizlilik adresini bazen otomatik bir denetleyiciyle açıyor ve
// boş ekran 3.1.2'den red demek.
export default defineConfig({
  site: 'https://gnomonstudio.com',
  outDir: './dist',
  build: {
    // 'file' = /kademe/gizlilik.html. Uzantısız "temiz adres" DEĞİL, çünkü
    // Kademe'nin app_config.dart varsayılanları bu adresleri .html uzantılı
    // olarak içinde taşıyor; uzantıyı atmak uygulamadaki üç bağlantıyı
    // birden kırardı.
    format: 'file',
  },
});
