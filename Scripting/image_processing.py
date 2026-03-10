from PIL import Image, ImageFilter

img =Image.open('./tokyo.jpg')
new_img = img.resize((400,400))
new_img.save('resized.png', 'png')
new_img.show()