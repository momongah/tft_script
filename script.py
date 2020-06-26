from PIL import Image
import numpy as np
import os, os.path

path = './test'
styles = [
	{
	"style": 1,  # bronze
	"rgb": (143, 102, 64)
	},
	{
	"style": 2,  # silver
	"rgb": (144, 165, 168)
	},
    {
	"style": 3,  # gold
	"rgb": (175, 132, 41)
	},
	{
	"style": 4,  # chromatic
	"rgb": (255, 255, 255)
    }
]

for style in styles:
	rgb = style['rgb'] #background color rbg values

	#create folders for style backgrounds
	style_path = "./" + str(style['style']) + "/"	
	os.makedirs(style_path, mode=0o777, exist_ok=True)

	#open each image and replace background colors with each
	#style's rbg values
	for img in os.listdir(path):
		im = Image.open(os.path.join(path, img))
		im = im.convert('RGBA')
		
		data = np.array(im)
		r, g, b, a = data.T

		grey_areas = (r == 146) & (g == 146) & (b == 146)
		data[..., :-1][grey_areas.T] = rgb  

		im2 = Image.fromarray(data)
		# im2.show()
		im2.save(style_path + img)

'''
styles: 
0 = none (0, 0, 0)
1 = bronze (108, 74, 43)
2 = silver (144, 165, 168)
3 = gold (175, 132, 41)
4 = chromatic (255, 255, 255)
'''
