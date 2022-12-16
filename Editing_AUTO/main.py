from PIL import Image,ImageEnhance,ImageFilter
import os

in_path = "./pics"
out_path = "./editedpics"

for filename in os.listdir(in_path):

  
  image = Image.open(f"{in_path}/{filename}")
  
  edited_image = image.filter(ImageFilter.DETAIL)
  edited_image = image.filter(ImageFilter.SHARPEN)
  enhancer = ImageEnhance.Contrast(edited_image) 
  edited_image= enhancer.enhance(1.25)

  newname = os.path.splitext(filename)[0]
  edited_image.save(f'{out_path}/edited_{newname}.jpg')