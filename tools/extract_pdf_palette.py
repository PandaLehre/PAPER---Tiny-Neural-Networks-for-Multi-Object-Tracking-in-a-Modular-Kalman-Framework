"""Extract dominant colors from a PDF page and print hex codes."""
from pathlib import Path
import fitz  # pymupdf
from PIL import Image
import numpy as np

pdf_path = Path('submissions_previous/submitted_to_arXiv/MOT_ML_.pdf')
if not pdf_path.exists():
    raise SystemExit('PDF not found: ' + str(pdf_path.resolve()))

# Render first page to image
doc = fitz.open(pdf_path)
page = doc.load_page(0)
pix = page.get_pixmap(dpi=150)
img = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)

# Resize small for speed
img_small = img.resize((img.width // 4, img.height // 4))

# Quantize to 6 colors
img_q = img_small.convert('P', palette=Image.ADAPTIVE, colors=6)
palette = img_q.getpalette()
color_counts = sorted(img_q.getcolors(), reverse=True)

hex_colors = []
for count, idx in color_counts[:6]:
    r = palette[idx * 3]
    g = palette[idx * 3 + 1]
    b = palette[idx * 3 + 2]
    hex_colors.append('#{:02x}{:02x}{:02x}'.format(r, g, b))

print('Dominant colors (hex):')
for col in hex_colors:
    print(col)
