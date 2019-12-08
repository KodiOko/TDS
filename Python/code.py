from PIL import Image
import cv2
import numpy as np
#import matplotlib.pyplot as mat
from skimage.morphology import convex_hull_image
from skimage import filters

#IMAGE A TRAITER
img_voiture=Image.open('/mnt/c/Users/KodiAk/OneDrive/Documents/tdsProject/voiture-rouge.jpg')
img_voiture.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge.jpg')

#TRANSFORMATION EN ARRAY POUR TRAITER
img_voiture_array=np.array(img_voiture)

#TRANSFORMATION EN HUE
img_voiture_array_hue=img_voiture_array[:,:,0]
img_voiture_hue=Image.fromarray(img_voiture_array_hue)
img_voiture_hue.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_hue.jpg')

#RGB2GRAY EQUIVALENT
img_voiture_gray=img_voiture.convert('L')
img_voiture_gray.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_gray.jpg')

#TRANSFORMATION GRAY EN ARRAY
img_voiture_gray_array=np.array(img_voiture_gray)

#SUBTRACT DE HUE-GRAY SIMPLE
img_voiture_array_subtract=img_voiture_array_hue - img_voiture_gray_array

#LES 2 LIGNES SUIVANTES NE SONT PLUS NECESSAIRES
#img_voiture_subtract=Image.fromarray(img_voiture_array_subtract)
#img_voiture_subtract.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_subtract.jpg')

#SUPPRIME LE BLANC TROP CLAIRE
def rearange(img) :	
	h,l=img.shape
	for i in range(h) :
		for j in range(l) :
			if img[i][j]>200 :
				img[i][j]=0
	return img

img_voiture_array_subtract_rearranged = rearange(img_voiture_array_subtract)
img_voiture_subtract_rearranged = Image.fromarray(img_voiture_array_subtract_rearranged)
img_voiture_subtract_rearranged.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_subtract_rearranged.jpg')

#BINARIZE THE IMAGE
def binarize(img) :
	h,l=img.shape
	for i in range(h) :
		for j in range(l) :
			if img[i][j]>35 :
				img[i][j]=230
			else :
				img[i][j]=0
	return img
img_voiture_array_binarized=binarize(img_voiture_array_subtract_rearranged)
img_voiture_binarized=Image.fromarray(img_voiture_array_binarized)
img_voiture_binarized.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_binarized.jpg')


#CONTOUR DE L'IMAGE
#img_voiture_array_contours = convex_hull_image(img_voiture_array_binarized)

#img_voiture_contours = Image.fromarray(img_voiture_array_contours)
#img_voiture_contours.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_contours.jpg')
