#pip install Pillow

from PIL import Image
img1=Image.open(r"image path\image name.jpg")
im1=img1.convert('RGB')
im1.save(r"path where you want to save the image\image name.pdf")