export const site = {
  ad: 'Gnomon Studio',
  alanAdi: 'gnomonstudio.com',
  eposta: 'merhaba@gnomonstudio.com',
  slogan: 'Göremediğin şeyi, iş işten geçmeden gösteririz.',
};

/* Uygulama kaydı. Yeni uygulama = buraya bir girdi + `src/pages/<slug>/`
 * altına sayfalar. SONRAKI-ADIMLAR.md'deki "yeni uygulama bir klasör
 * demek" kuralı korunuyor. */
export const uygulamalar = [
  {
    slug: 'kademe',
    ad: 'Kademe',
    altBaslik: 'Tüketim Hesaplama',
    ozet:
      'Doğal gazda kademeli tarifeyi takip eder: ilinin aylık limiti, ne ' +
      'kadar kaldığın ve limiti aşmanın faturaya kaç lira ekleyeceği.',
    ikon: '/uygulamalar/kademe/ikon.png',
    durum: 'yakinda', // 'yayinda' olunca mağaza bağlantıları açılır
    appStore: null,
    playStore: null,
  },
];

/* Adres uygulamanın klasör adından türüyor: kademe@gnomonstudio.com.
 * Gelen kutusunda hangi uygulamadan geldiği belli oluyor ve bir uygulama
 * devredilirse adresi de onunla gidiyor. (Eski build.py de böyle yapıyordu.) */
export const epostaIcin = (slug) => `${slug}@${site.alanAdi}`;

/* Uygulama sayfasinin adresi. `format: 'file'` yuzunden /kademe.html;
 * tek yerden turuyor ki bicim degisirse tum baglantilar birden donsun. */
export const sayfaIcin = (slug) => `/${slug}.html`;

export const uygulamaBul = (slug) => uygulamalar.find((u) => u.slug === slug);
