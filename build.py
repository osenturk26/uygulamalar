#!/usr/bin/env python3
"""icerik/*.md → docs/*.html

Neden bir derleme adımı var: yasal metin Markdown olarak yazılıp okunuyor
ama **düz HTML olarak yayımlanması** gerekiyor. Mağaza incelemesi gizlilik
adresini bazen otomatik bir denetleyiciyle açıyor; sayfanın görünmesi
JavaScript'e bağlıysa boş ekran görme ihtimali var ve bu 3.1.2'den red
demek. Üretilen dosyalar olduğu gibi servis ediliyor.

Çıktı `docs/` altına yazılıyor çünkü GitHub Pages bu klasörü doğrudan
yayımlayabiliyor; ayrı bir derleme işi kurmaya gerek kalmıyor.

    python3 build.py
"""

import json
import os
import pathlib
import shutil
import subprocess
import sys

os.chdir(pathlib.Path(__file__).resolve().parent)

KAYNAK = pathlib.Path("icerik")
CIKTI = pathlib.Path("docs")
SABLON = pathlib.Path("sablon.html")
AYAR = pathlib.Path("site.json")


def ayarlar() -> dict:
    if AYAR.exists():
        return json.loads(AYAR.read_text())
    return {}


def main() -> int:
    if shutil.which("pandoc") is None:
        print("pandoc bulunamadı: brew install pandoc", file=sys.stderr)
        return 1

    ayar = ayarlar()
    alan = ayar.get("alan_adi", "")
    eposta = ayar.get("eposta", "")
    yayinci = ayar.get("yayinci", "")

    if not eposta and not alan:
        # Yayımlanmış bir gizlilik politikasında iletişim adresi zorunlu.
        # Derlemeyi durdurmuyoruz ki site kurulurken test edilebilsin, ama
        # sessizce geçmek de doğru değil.
        print("⚠️  site.json içinde 'alan_adi' ve 'eposta' boş — sayfalarda yer tutucu kalacak.")

    if CIKTI.exists():
        shutil.rmtree(CIKTI)
    CIKTI.mkdir()

    shutil.copytree("assets", CIKTI / "assets")
    # GitHub Pages varsayılan olarak Jekyll çalıştırıyor ve alt çizgiyle
    # başlayan dosyaları atlıyor. Bizim üretimimiz zaten bitmiş HTML.
    (CIKTI / ".nojekyll").write_text("")

    # CNAME **üretiliyor**, elle tutulmuyor. Sebebi hemen yukarıdaki
    # `rmtree`: docs/ her derlemede sıfırlanıyor, yani elle konan bir
    # CNAME ilk `python3 build.py` çağrısında uçar. GitHub Pages o dosyayı
    # kaybedince özel alan adını da bırakıyor ve site github.io adresine
    # düşüyor; uygulamaların içine derlenmiş gizlilik bağlantısı da
    # kırılıyor (App Store 3.1.2). Tek kaynak site.json olsun.
    if alan:
        (CIKTI / "CNAME").write_text(alan + "\n")

    sayilar = 0
    for md in sorted(KAYNAK.rglob("*.md")):
        goreli = md.relative_to(KAYNAK)
        hedef = CIKTI / goreli.with_suffix(".html")
        hedef.parent.mkdir(parents=True, exist_ok=True)

        # Göreli kök: sayfa ne kadar derindeyse o kadar "../".
        # Mutlak yol yazılsaydı site ya özel alan adının kökünde ya da
        # GitHub Pages'in alt yolunda çalışırdı, ikisinde birden değil.
        derinlik = len(goreli.parts) - 1
        kok = "../" * derinlik if derinlik else "./"

        # Kök sayfada "← Tüm uygulamalar" bağlantısı kendine dönerdi.
        komutlar = [
            "pandoc", str(md),
            "--from", "markdown+yaml_metadata_block",
            "--to", "html5",
            "--template", str(SABLON),
            "--variable", f"kok={kok}",
            "--output", "-",
        ]
        if derinlik:
            komutlar += ["--variable", "ustlink=1"]
        if yayinci:
            komutlar += ["--variable", f"yayinci={yayinci}"]

        sonuc = subprocess.run(
            komutlar,
            capture_output=True,
            text=True,
        )
        if sonuc.returncode != 0:
            print(f"pandoc hatası ({md}):\n{sonuc.stderr}", file=sys.stderr)
            return 1

        # Adres uygulamanın **klasör adından** türüyor: icerik/kademe/...
        # sayfaları kademe@alanadi görüyor. İki kazancı var: gelen kutusunda
        # hangi uygulamadan geldiği belli oluyor, ve yeni uygulama yine
        # yalnız bir klasör demek, site.json'a satır eklemek gerekmiyor.
        # Kök sayfa site genelindeki adresi kullanıyor.
        if derinlik and alan:
            sayfa_eposta = f"{goreli.parts[0]}@{alan}"
        else:
            sayfa_eposta = eposta

        html = sonuc.stdout.replace("{{EPOSTA}}", sayfa_eposta or "(iletişim adresi eklenmedi)")
        hedef.write_text(html)
        sayilar += 1
        print(f"  {md} → {hedef}")

    print(f"\n{sayilar} sayfa üretildi → {CIKTI}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
