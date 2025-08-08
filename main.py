from flask import Flask, send_file
import requests
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route('/generate-wallpaper')
def generate_wallpaper():
    # 1. Ambil teks dari API
    api_url = "https://11z.co/_w/6804/selection"
    response = requests.get(api_url)
    data = response.json()
    teks = data.get("value", "Teks default")

    # 2. Proses gambar
    image = Image.open("papan_tulis_kosong.jpg")
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    # 3. Tambahkan teks
    text_width = draw.textlength(teks, font=font)
    x = (image.width - text_width) / 2
    draw.text((x, 50), teks, fill="white", font=font)

    # 4. Kirim sebagai gambar
    img_buffer = io.BytesIO()
    image.save(img_buffer, format="JPEG")
    img_buffer.seek(0)
    return send_file(img_buffer, mimetype='image/jpeg')

# Catatan: Tidak perlu app.run() untuk Vercel