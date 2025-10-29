from PIL import Image, ImageDraw, ImageFont
import os

# إنشاء المجلدات لو ما كايناش
os.makedirs("static/images", exist_ok=True)

# الحروف A-Z
for i in range(ord('A'), ord('Z')+1):
    char = chr(i)
    img = Image.new('RGB', (100, 100), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((30,30), char, fill=(0,0,0))
    img.save(f"static/images/{char.lower()}.png")

# الأرقام 1-99
for i in range(1, 100):
    img = Image.new('RGB', (100, 100), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((30,30), str(i), fill=(0,0,0))
    img.save(f"static/images/{i}.png")

