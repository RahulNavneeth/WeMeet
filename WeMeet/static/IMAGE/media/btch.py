from PIL import Image, ImageDraw, ImageFont

img = Image.open('C:/Users\HP/Documents/WeMeet/WeMeet/WeMeet/WeMeet/static/IMAGE/media/Batchprofile/BatchProfileBase.png')
d1 = ImageDraw.Draw(img)

d1.text((60, 80), "BATCH", fill =(0, 0, 0))
# img.show()
img.save("C:/Users\HP/Documents/WeMeet/WeMeet/WeMeet/WeMeet/static/IMAGE/media/Batchprofile/image_text.png")