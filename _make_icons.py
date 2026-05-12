"""budget-tracker PWA 아이콘 생성 (필요 시 실행).

원본: icon-source.png (1024x1024, WALKING BANKING 로고)
생성: icon-192.png, icon-512.png, apple-touch-icon.png, favicon-32.png, favicon.ico
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
SRC = ROOT / "icon-source.png"

src = Image.open(SRC).convert("RGBA")

# 다양한 사이즈로 리사이즈
sizes = {
    "icon-192.png": 192,
    "icon-512.png": 512,
    "apple-touch-icon.png": 180,
    "favicon-32.png": 32,
}
for name, sz in sizes.items():
    img = src.resize((sz, sz), Image.LANCZOS)
    img.save(ROOT / name, "PNG", optimize=True)
    print(f"  saved {name} ({sz}x{sz})")

# favicon.ico — 16/32/48 multi-resolution
ico_path = ROOT / "favicon.ico"
src.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
print(f"  saved favicon.ico (16/32/48)")
