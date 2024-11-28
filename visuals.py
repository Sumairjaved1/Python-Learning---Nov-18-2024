from PIL import Image, ImageFilter

# Open an image
img = Image.open("cEdDG.png")

# Check the mode of the image
print(img.mode)  # Example: 'L' for grayscale

# Convert the image to RGB
img_rgb = img.convert("RGB")

# Save the converted image
img_rgb.save("image_convert_rgb.png")



before = Image.open("image_convert_rgb.png")
after = before.filter(ImageFilter.BoxBlur(1))
after.save("blurimage.png")
