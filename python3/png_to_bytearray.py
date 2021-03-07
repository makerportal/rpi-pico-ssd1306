import io
from PIL import Image

filename_in  = 	'makerportal_logo.png'
filename_out = 'result.bmp'
img = Image.open(filename_in)
img = img.transpose(Image.FLIP_LEFT_RIGHT)

threshold = 65
func = lambda x : 255 if x > threshold else 0 
img = img.convert('L').point(func,mode='1')
img.save(filename_out)

img = Image.open(filename_out,mode='r')
img_bytes = io.BytesIO()
img.save(img_bytes,format='BMP')
img_bytes = img_bytes.getvalue()

print('Bitmap to Copy to imgfile.py:')
print('\n')
print(img_bytes)
print('\n')
print('Image Dimensions: ({0},{1})'.format(img.width,img.height))
