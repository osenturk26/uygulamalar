/* Siteyi Cloudflare'e dağıtır.
 *
 * Kimlik bilgileri `.cloudflare.local.json` içinde ve depoya GİRMİYOR
 * (.gitignore). Komut satırında görünmesinler diye ortam değişkeni olarak
 * veriliyor; wrangler ikisini de buradan okuyor.
 *
 *     npm run dagit
 */
import { readFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

const DOSYA = '.cloudflare.local.json';

let gizli;
try {
  gizli = JSON.parse(readFileSync(DOSYA, 'utf8'));
} catch {
  console.error(`✗ ${DOSYA} bulunamadı.`);
  console.error('  İçine CLOUDFLARE_ACCOUNT_ID ve CLOUDFLARE_API_TOKEN yazın.');
  process.exit(1);
}

const eksik = ['CLOUDFLARE_ACCOUNT_ID', 'CLOUDFLARE_API_TOKEN'].filter((k) => !gizli[k]);
if (eksik.length) {
  console.error(`✗ ${DOSYA} içinde eksik: ${eksik.join(', ')}`);
  process.exit(1);
}

const r = spawnSync('npx', ['wrangler', 'deploy', ...process.argv.slice(2)], {
  stdio: 'inherit',
  env: {
    ...process.env,
    CLOUDFLARE_ACCOUNT_ID: gizli.CLOUDFLARE_ACCOUNT_ID,
    CLOUDFLARE_API_TOKEN: gizli.CLOUDFLARE_API_TOKEN,
  },
});

if (r.status !== 0) {
  console.error('\n✗ Dağıtım başarısız.');
  console.error('  "No access to the specified resource" görüyorsanız token yetkisi eksik:');
  console.error('  Hesap → Workers Scripts → Edit gerekiyor.');
}
process.exit(r.status ?? 1);
