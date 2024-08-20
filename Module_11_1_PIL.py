from PIL import Image

image_path_1 = r'C:\Users\evgen\pythonProject\Images\image_1.jpeg'

img = Image.open(image_path_1)
img.show()
print(f'Размер изображения: {img.size}, формат изображения: {img.format}, цветовая схема: {img.mode}')

img_resize = img.resize((900, 900))

img_res_conv = img_resize.convert('L')

img_res_conv.save('C:\\Users\\evgen\\pythonProject\\Images\\img_res_conv.png', 'PNG')

image_path_2 = r'C:\Users\evgen\pythonProject\Images\img_res_conv.png'

img_2 = Image.open(image_path_2)
img_2.show()
print(f'Размер изображения: {img_2.size}, формат изображения: {img_2.format}, цветовая схема: {img_2.mode}')









