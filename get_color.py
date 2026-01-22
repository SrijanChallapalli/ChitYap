from PIL import Image
from collections import Counter

def get_bg_color(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")
        # Sample the top-left pixel for background color
        bg_color = img.getpixel((0, 0))
        # Also get the most common color to be sure
        # width, height = img.size
        # pixels = img.getdata()
        # most_common = Counter(pixels).most_common(1)[0][0]
        
        print(f"Top-left pixel color: #{bg_color[0]:02x}{bg_color[1]:02x}{bg_color[2]:02x}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_bg_color("assets/logo-new.jpg")
