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
    eposta = ayar.get("eposta", "")
    yayinci = ayar.get("yayinci", "")

    if not eposta:
        # Yayımlanmış bir gizlilik politikasında iletişim adresi zorunlu.
        # Derlemeyi durdurmuyoruz ki site kurulurken test edilebilsin, ama
        # sessizce geçmek de doğru değil.
        print("⚠️  site.json içinde 'eposta' boş — sayfalarda yer tutucu kalacak.")

    if CIKTI.exists():
        shutil.rmtree(CIKTI)
    CIKTI.mkdir()

    shutil.copytree("assets", CIKTI / "assets")
    # GitHub Pages varsayılan olarak Jekyll çalıştırıyor ve alt çizgiyle
    # başlayan dosyaları atlıyor. Bizim üretimimiz zaten bitmiş HTML.
    (CIKTI / ".nojekyll").write_text("")

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

        html = sonuc.stdout.replace("{{EPOSTA}}", eposta or "(iletişim adresi eklenmedi)")
        hedef.write_text(html)
        sayilar += 1
        print(f"  {md} → {hedef}")

    print(f"\n{sayilar} sayfa üretildi → {CIKTI}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
