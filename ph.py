from PIL import Image, ImageEnhance, ImageChops
import os
import glob
def adjust_image(image_path, contrast_factor=1.5, brightness_factor=1.5):
    original_image = Image.open(image_path)
    enhancer_contrast = ImageEnhance.Contrast(original_image)
    img_contrast = enhancer_contrast.enhance(contrast_factor)
    enhancer_brightness = ImageEnhance.Brightness(img_contrast)
    img_bright = enhancer_brightness.enhance(brightness_factor)
    return img_bright
def merge_images(image_path_1, image_path_2):
    image1 = Image.open(image_path_1)
    image2 = Image.open(image_path_2).resize(image1.size)
    return ImageChops.multiply(image1, image2)
image_folder_path = './/'
latest_images = sorted(glob.glob(f"{image_folder_path}*.jpg"), key=os.path.getctime, reverse=True)
if len(latest_images) >= 2:
    img1_path, img2_path = latest_images[:2]
    edited_img1 = adjust_image(img1_path, contrast_factor=2, brightness_factor=2)
    merged_image = merge_images(img1_path, img2_path)
    edited_img1.save("edited_image1.jpg")
    merged_image.save("merged_image.jpg")
else:
    print("There are not enough images in the directory.")
