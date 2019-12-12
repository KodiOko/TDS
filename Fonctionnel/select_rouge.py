from PIL import Image
import numpy as np
from skimage.morphology import convex_hull_image
from skimage import feature

def traitement(img_voiture_array) :
	#TRANSFORMATION EN IMAGE POUR TRAITER
	img_voiture=Image.fromarray(img_voiture_array)

	#TRANSFORMATION EN HUE
	img_voiture_array_hue=img_voiture_array[:,:,0]
	img_voiture_hue=Image.fromarray(img_voiture_array_hue)
	#img_voiture_hue.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_hue.jpg')

	#TRANSFORMATION EN SAT
	img_voiture_array_sat=img_voiture_array[:,:,1]
	img_voiture_sat=Image.fromarray(img_voiture_array_sat)
	#img_voiture_sat.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_sal.jpg')

	#RGB2GRAY EQUIVALENT
	img_voiture_gray=img_voiture.convert('L')
	img_voiture_array_gray=np.array(img_voiture_gray)
	#img_voiture_gray.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_gray.jpg')

	#SUBTRACT DE GRAY - HUE SIMPLE (le plus precis)
	img_voiture_array_sub = img_voiture_array_gray - img_voiture_array_hue
	img_voiture_sub = Image.fromarray(img_voiture_array_sub)
	#img_voiture_sub.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_sub.jpg')

	#FONCTION DE RETOUCHE DU SUBTRACT
	#REND LES PIXELS NOIRS ET BLANCS, NOIRS
	def retouche(img) :
		h, l = img.shape
		for i in range(h) :
			for j in range(l) :
				if img[i][j]>180 or img[i][j]<90 :
					img[i][j] = 0
		return img
	
	#BLEU -> 88-35 + gray-hue / 76-43 ballons video
	#ROUGE -> 180-90 + gray-hue
	#VERT -> 80-10 + utiliser sal-hue
	
	#UTILISATION DE LA FONCTION PRECEDENTE
	img_voiture_array_binaire = retouche(img_voiture_array_sub)
	img_voiture_binaire = Image.fromarray(img_voiture_array_binaire)
	#img_voiture_binaire.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_binaire.jpg')

	#CONTOUR DE L'IMAGE + REMPLISSAGE
	img_voiture_array_contours = convex_hull_image(img_voiture_array_binaire)
	img_voiture_contours = Image.fromarray(img_voiture_array_contours)
	#img_voiture_contours.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_contours.jpg')

	#FONCTION EXISTANTE POUR LE CONTOUR
	edges = feature.canny(img_voiture_array_contours)
	imageed = Image.fromarray(edges)
	#imageed.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_canny.jpg')

	#FONCTION POUR RENDRE LES PIXELS NOIRS TRANSPARENTS
	def transp(img) :
		img1 = img.convert('RGBA')
		datas = img1.getdata()
		newData = []
		for pixel in datas :
			if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0 :
				newData.append((0, 0, 0, 0))
			else :
				newData.append(pixel)
		img1.putdata(newData)
		return img1

	transparent = transp(imageed)
	#transparent.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_transparent.png')
	
	#AJOUT DU CONTOUR A L'IMAGE DE BASE
	img_voiture.paste(transparent, (0, 0), transparent)
	#img_voiture.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_blend.jpg')
	return (np.array(img_voiture), transparent)
	
#Image.fromarray(traitement(np.array(Image.open('/mnt/c/Users/KodiAk/Desktop/test_ballons.jpg')))).save('/mnt/c/Users/KodiAk/Desktop/result_test.png')
