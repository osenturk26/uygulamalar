// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Çıktı `docs/` altına yazılıyor ve depoya commit ediliyor.
//
// GitHub Pages derleme çalıştırmıyor; yayımladığı şey depodaki klasörün
// kendisi. Bu yüzden üretilmiş HTML commit ediliyor.
//
// Bir ara Cloudflare Workers'a geçilecekti ve çıktı `dist/`e alınmıştı.
// Geri alındı: hesabın API token'ı Workers'a da Pages'e de YAZAMIYOR
// (ölçüldü — DNS yazma açık, Workers yazma kapalı, token yönetimi kapalı),
// yani Cloudflare'e dağıtmanın panele girmeden bir yolu yok. GitHub Pages
// özel alan adıyla siteyi kökten sunuyor, mutlak yollar doğru çalışıyor
// ve kurulum uçtan uca buradan yapılabiliyor.
//
// `wrangler.jsonc` duruyor: Workers yetkili bir token gelirse `npm run
// dagit` aynı klasörü gönderir, tek değişiklik DNS olur.
//
// Astro varsayılan olarak **sıfır JavaScript** üretir: bir bileşene
// `client:*` direktifi verilmedikçe tarayıcıya hiç script inmez. Yasal
// sayfaların JS'siz kalması bu projede tercih değil zorunluluk — App Store
// incelemesi gizlilik adresini bazen otomatik bir denetleyiciyle açıyor ve
// boş ekran 3.1.2'den red demek.
export default defineConfig({
  site: 'https://gnomonstudio.com',
  // Sitemap `site` değerine ihtiyaç duyuyor; adresler mutlak üretiliyor.
  //
  // serialize şart: eklenti `build.format` ayarını bilmiyor ve adresleri
  // uzantısız üretiyor (/hakkimizda). Bizde her sayfa .html olarak
  // yayımlandığı için o adresler 404 verirdi — kırık adreslerle dolu bir
  // site haritası, hiç site haritası olmamasından kötüdür.
  integrations: [
    sitemap({
      serialize(oge) {
        const u = new URL(oge.url);
        if (u.pathname !== '/' && !u.pathname.endsWith('.html')) {
          u.pathname = u.pathname.replace(/\/$/, '') + '.html';
          oge.url = u.toString();
        }
        return oge;
      },
    }),
  ],
  outDir: './docs',
  build: {
    // 'file' = /kademe/gizlilik.html. Uzantısız "temiz adres" DEĞİL, çünkü
    // Kademe'nin app_config.dart varsayılanları bu adresleri .html uzantılı
    // olarak içinde taşıyor; uzantıyı atmak uygulamadaki üç bağlantıyı
    // birden kırardı.
    format: 'file',
  },
});
