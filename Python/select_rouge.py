from PIL import Image
import numpy as np
from skimage.morphology import convex_hull_image
from skimage import feature

#***************************************INTERESSANT, LE BLEU PEUT ETRE 'SELECTIONNE'
def traitement(img_voiture_array) :
	#IMAGE A TRAITER
	#img_voiture=Image.open('/mnt/c/Users/KodiAk/Pictures/test/image_001.jpg')
	#img_voiture.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge.jpg')

	#TRANSFORMATION EN ARRAY POUR TRAITER
	img_voiture=Image.fromarray(img_voiture_array)
	#img_voiture_array=np.array(img_voiture)

	#TRANSFORMATION EN HUE
	img_voiture_array_hue=img_voiture_array[:,:,0]
	img_voiture_hue=Image.fromarray(img_voiture_array_hue)
	#img_voiture_hue.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_hue.jpg')

	#TRANSFORMATION EN SAL
	img_voiture_array_sal=img_voiture_array[:,:,1]
	img_voiture_sal=Image.fromarray(img_voiture_array_sal)
	#img_voiture_sal.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_sal.jpg')

	#RGB2GRAY EQUIVALENT
	img_voiture_gray=img_voiture.convert('L')
	#img_voiture_gray.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_gray.jpg')

	#TRANSFORMATION GRAY EN ARRAY
	img_voiture_array_gray=np.array(img_voiture_gray)

	#SUBTRACT DE GRAY - HUE SIMPLE (le plus precis)
	img_voiture_array_sub = img_voiture_array_gray - img_voiture_array_hue
	img_voiture_sub = Image.fromarray(img_voiture_array_sub)
	#img_voiture_sub.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_sub.jpg')

	#FOCNTION DE RETOUCHE DU SUBTRACT
	def retouche(img) :
		h, l = img.shape
		for i in range(h) :
			for j in range(l) :
				if img[i][j]>76 or img[i][j]<45 :
					img[i][j] = 0
		return img
	
	#BLEU -> 88-35 + gray-hue / 76-43 ballons video
	#ROUGE -> 180-90 + gray-hue
	#VERT -> 80-10 + utiliser sal-hue
	
	#UTILISATION DE LA FONCTION PRECEDENTE
	img_voiture_array_binaire = retouche(img_voiture_array_sub)
	img_voiture_binaire = Image.fromarray(img_voiture_array_binaire)
	#img_voiture_binaire.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_binaire.jpg')

	#CONTOUR DE L'IMAGE
	img_voiture_array_contours = convex_hull_image(img_voiture_array_binaire)
	img_voiture_contours = Image.fromarray(img_voiture_array_contours)
	#img_voiture_contours.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_contours.jpg')

	#FONCTION EXISTANTE POUR LE CONTOUR
	edges = feature.canny(img_voiture_array_contours)
	imageed = Image.fromarray(edges)
	#imageed.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_canny.jpg')

	#TEST AJOUT
	#img_voiture_RGB = img_voiture_contours.convert('RGB')
	#img_voiture_array = img_voiture_RGB + img_voiture_array
	#img_voiture_finale = Image.fromarray(img_voiture_array)
	#img_voiture_finale.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_finale.jpg')

	#AUTRE TEST (FONCTIONNE)
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
	img_voiture.paste(transparent, (0, 0), transparent)
	#img_voiture.save('/mnt/c/Users/KodiAk/Desktop/voiture_rouge_blend.jpg')
	return np.array(img_voiture)
	
#Image.fromarray(traitement(np.array(Image.open('/mnt/c/Users/KodiAk/Desktop/test_ballons.jpg')))).save('/mnt/c/Users/KodiAk/Desktop/result_test.png')
