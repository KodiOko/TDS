from PIL import Image
import cv2
import numpy as np
from skimage.morphology import convex_hull_image
from skimage import feature

#IMAGE A TRAITER
img_voiture=Image.open('/mnt/c/Users/KodiAk/OneDrive/Documents/tdsProject/voiture-rouge.jpg')
img_voiture.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge.jpg')

#TRANSFORMATION EN ARRAY POUR TRAITER
img_voiture_array=np.array(img_voiture)

#TRANSFORMATION EN HUE
img_voiture_array_hue=img_voiture_array[:,:,0]
img_voiture_hue=Image.fromarray(img_voiture_array_hue)
img_voiture_hue.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_hue.jpg')

#TRANSFORMATION EN SAL
img_voiture_array_sal=img_voiture_array[:,:,1]
img_voiture_sal=Image.fromarray(img_voiture_array_sal)
img_voiture_sal.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_sal.jpg')

#RGB2GRAY EQUIVALENT
img_voiture_gray=img_voiture.convert('L')
img_voiture_gray.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_gray.jpg')

#TRANSFORMATION GRAY EN ARRAY
img_voiture_array_gray=np.array(img_voiture_gray)

#SUBTRACT DE GRAY - HUE SIMPLE (le plus precis)
img_voiture_array_sub = img_voiture_array_gray - img_voiture_array_hue
img_voiture_sub = Image.fromarray(img_voiture_array_sub)
img_voiture_sub.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_sub.jpg')

#FOCNTION DE RETOUCHE DU SUBTRACT
def retouche(img) :
	h, l = img.shape
	for i in range(h) :
		for j in range(l) :
			if img[i][j]>180 or img[i][j]<50 :
				img[i][j] = 0
	return img

#UTILISTION DE LA FONCTION PRECEDENTE
img_voiture_array_binaire = retouche(img_voiture_array_sub)
img_voiture_binaire = Image.fromarray(img_voiture_array_binaire)
img_voiture_binaire.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_binaire.jpg')

#CONTOUR DE L'IMAGE
img_voiture_array_contours = convex_hull_image(img_voiture_array_binaire)
img_voiture_contours = Image.fromarray(img_voiture_array_contours)
img_voiture_contours.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_contours.jpg')

#FONCTION EXISTANTE
edges = feature.canny(img_voiture_array_contours)
imageed = Image.fromarray(edges)
imageed.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_canny.jpg')
