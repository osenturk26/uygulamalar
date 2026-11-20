#!/usr/bin/env python3
"""Marka görsellerini Logo.astro ile AYNI geometriden üretir.

Tek kaynak burası ve Logo.astro; ikisi de aşağıdaki sabitleri kullanıyor.
Geometri değişirse ikisini birden değiştir.

    python3 kontrol/marka-gorselleri.py
"""
import math, os, pathlib
from PIL import Image, ImageDraw, ImageFilter, ImageFont

os.chdir(pathlib.Path(__file__).resolve().parent.parent)

CX = CY = 22.0; R = 21.0; ACI = 38.0; W = 4.2; KUTU = 44.0
AMBER = (233, 162, 59); GOLGE = (20, 19, 15); ISIK = (245, 241, 232)
KAGIT = (250, 248, 243); MUREKKEP = (26, 24, 19); AMBER_KOYU = (138, 90, 0)
FONT = pathlib.Path.home() / "Desktop/Kademe/kademe_app/.claude/worktrees/kanka-website-setup-f64fb9/kademe_app/assets/fonts/Inter-Variable.ttf"
S = 8  # supersampling: Pillow kenar yumuşatma yapmıyor

def yarik(uzak=34.0):
    """Gölge yarığının dörtgeni — merkezden kenarın DIŞINA uzanıyor."""
    d = math.radians(ACI); ux, uy = math.cos(d), math.sin(d); px, py = -uy, ux
    return [(CX + W*px, CY + W*py),
            (CX + uzak*ux + W*px, CY + uzak*uy + W*py),
            (CX + uzak*ux - W*px, CY + uzak*uy - W*py),
            (CX - W*px, CY - W*py)]

def maske(boyut):
    """Kadran eksi yarık — gri tonlu maske."""
    n = boyut * S
    k = n / KUTU
    m = Image.new("L", (n, n), 0)
    d = ImageDraw.Draw(m)
    d.ellipse([(CX-R)*k, (CY-R)*k, (CX+R)*k, (CY+R)*k], fill=255)
    d.polygon([(x*k, y*k) for x, y in yarik()], fill=0)
    return m.resize((boyut, boyut), Image.LANCZOS)

def isaret(boyut, zemin=None, pay=0.0):
    """Markayı üretir. zemin None ise saydam."""
    ic = round(boyut * (1 - 2*pay))
    m = maske(ic)
    kat = Image.new("RGBA", (ic, ic), AMBER + (0,))
    kat.putalpha(m)
    tuval = Image.new("RGBA", (boyut, boyut), (zemin + (255,)) if zemin else (0, 0, 0, 0))
    o = (boyut - ic) // 2
    tuval.alpha_composite(kat, (o, o))
    return tuval

def font(px, agirlik=700):
    f = ImageFont.truetype(str(FONT), px)
    try: f.set_variation_by_axes([14, agirlik])
    except Exception: pass
    return f

def main():
    pathlib.Path("public").mkdir(exist_ok=True)

    # SVG favicon: tarayıcı her boyutta keskin çizsin
    d = math.radians(ACI); ux, uy = math.cos(d), math.sin(d); px, py = -uy, ux
    t = math.sqrt(R*R - W*W)
    f = lambda q: f"{round(q[0],2)} {round(q[1],2)}"
    yol = (f"M{f((CX+t*ux+W*px, CY+t*uy+W*py))} A{R} {R} 0 1 1 "
           f"{f((CX+t*ux-W*px, CY+t*uy-W*py))} L{f((CX-W*px, CY-W*py))} "
           f"L{f((CX+W*px, CY+W*py))} Z")
    pathlib.Path("public/favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 44">'
        f'<path d="{yol}" fill="#E9A23B"/></svg>\n')
    pathlib.Path("public/logo.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 44">'
        f'<path d="{yol}" fill="currentColor"/></svg>\n')

    isaret(32).save("public/favicon-32.png")
    # Apple dokunma ikonu saydamlık kabul etmiyor; zemin opak, glif güvenli alanda
    isaret(180, zemin=GOLGE, pay=0.14).save("public/apple-touch-icon.png")

    # OG görseli 1200×630
    # Site açık temaya geçince OG de açık oldu; paylaşım önizlemesi
    # sayfanın kendisiyle aynı şeyi göstermeli.
    #
    # Sol üstten gelen ışık: bulanıklaştırılmış elips maskesiyle yumuşak
    # geçiş. İç içe elips çizmek bantlanma yapıyordu.
    taban = Image.new("RGB", (1200, 630), KAGIT)
    sicak = Image.new("RGB", (1200, 630), (253, 240, 216))
    isik_m = Image.new("L", (1200, 630), 0)
    ImageDraw.Draw(isik_m).ellipse([-440, -540, 880, 540], fill=255)
    isik_m = isik_m.filter(ImageFilter.GaussianBlur(200))
    og = Image.composite(sicak, taban, isik_m)
    d2 = ImageDraw.Draw(og)
    og.paste(isaret(104), (84, 74), isaret(104))
    d2.text((84, 232), "Göremediğin şeyi,", font=font(72, 720), fill=MUREKKEP)
    d2.text((84, 318), "iş işten geçmeden", font=font(72, 720), fill=MUREKKEP)
    d2.text((84, 404), "gösteririz.", font=font(72, 720), fill=MUREKKEP)
    d2.text((84, 522), "Gnomon Studio", font=font(30, 600), fill=AMBER_KOYU)
    og.save("public/og.png", optimize=True)

    for y in ("public/favicon.svg", "public/logo.svg", "public/favicon-32.png",
              "public/apple-touch-icon.png", "public/og.png"):
        print(f"  {y}  ({pathlib.Path(y).stat().st_size:,} bayt)")

if __name__ == "__main__":
    main()
