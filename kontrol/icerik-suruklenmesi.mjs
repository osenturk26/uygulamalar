/* Yasal metnin tek kaynağı `src/pages/`. `icerik/` eski pandoc kurulumundan
 * kalma ve artık yayımlanmıyor.
 *
 * Bu betiğin işi tek bir soruyu sormak: YAYIMLANAN metin, elimizdeki en
 * yeni metin mi? Çünkü yayımlanan gizlilik politikası uygulamanın gerçekte
 * yaptığını anlatmıyorsa bu sadece tutarsızlık değil, App Store 5.1.1 ve
 * KVKK açısından yanlış beyan (docs/legal/README.md).
 *
 * İki kez gerçekten oldu:
 *   19:40 taşıdım → 19:41 kaynağa "fotoğraftan okuma" eklendi (eksik kaldım)
 *   19:46 eşitledim → 20:11 yeni konuma "PDF'ten okuma" eklendi (bu sefer doğru yere)
 *
 * Kural: `icerik/` daha yeniyse DURDUR — biri eski kaynağı düzenlemiş ve
 * değişiklik yayımlanmayacak. `src/pages/` daha yeniyse sadece uyar:
 * `icerik/` ölü bir kopya, silinmeyi bekliyor.
 */
import { readFileSync, existsSync, statSync } from 'node:fs';

const CIFTLER = [
  ['icerik/kademe/gizlilik.md', 'src/pages/kademe/gizlilik.md'],
  ['icerik/kademe/kullanim-kosullari.md', 'src/pages/kademe/kullanim-kosullari.md'],
  ['icerik/kademe/index.md', 'src/pages/kademe/destek.md'],
];

const govde = (y) => readFileSync(y, 'utf8').replace(/^---\n[\s\S]*?\n---\n/, '').trim();

let dur = 0, olu = 0;
for (const [eski, yeni] of CIFTLER) {
  if (!existsSync(eski)) continue;
  if (!existsSync(yeni)) { console.error(`✗ ${yeni} yok ama ${eski} duruyor`); dur++; continue; }
  if (govde(eski).replace(/\{\{EPOSTA\}\}/g, 'kademe@gnomonstudio.com') === govde(yeni)) continue;

  if (statSync(eski).mtimeMs > statSync(yeni).mtimeMs) {
    console.error(`✗ ESKİ KAYNAK DAHA YENİ: ${eski}`);
    console.error(`  Biri ${eski} dosyasını düzenlemiş ama site ${yeni} dosyasından`);
    console.error(`  derleniyor. Değişiklik yayımlanmayacak. Önce ${yeni} dosyasına taşı.`);
    dur++;
  } else {
    console.warn(`⚠ ölü kopya: ${eski} (yayımlanan ${yeni} daha yeni)`);
    olu++;
  }
}

if (dur) {
  console.error('\nDerleme durduruldu: yayımlanacak metin en yeni metin değil.');
  process.exit(1);
}
if (olu) {
  console.log(`\n${olu} ölü kopya var. icerik/ klasörü silinebilir — tek kaynak src/pages/.`);
} else {
  console.log('✓ içerik tek kaynakla uyumlu');
}
