import cv2 as cv
import os
from select_rouge import traitement
#import pdb
from PIL import Image
import numpy as np

#VIDEO
vi = cv.VideoCapture('/mnt/c/Users/KodiAk/OneDrive/Documents/tdsProject/video_ballons.mp4')

nb_frames = vi.get(cv.CAP_PROP_FRAME_COUNT)
longueur = len(str(int(nb_frames)))
fps = vi.get(cv.CAP_PROP_FPS)

framearray = []
passe = True
while vi.get(cv.CAP_PROP_POS_FRAMES)!= nb_frames :
	r, frame = vi.read()
	
	if passe :
		frame_traitementRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
		frame_traitee = traitement(frame_traitementRGB)
		#Image.fromarray(frame_traitementRGB).save('/mnt/c/Users/KodiAk/Desktop/test_ballons.jpg')
		frame_traiteeBGR = cv.cvtColor(frame_traitee, cv.COLOR_RGB2BGR)
		framearray.append(frame_traiteeBGR)
		passe = False
	#nom_image = '/mnt/c/Users/KodiAk/Pictures/test/' + 'image_' + str(int(vi.get(cv.CAP_PROP_POS_FRAMES))).zfill(longueur) + '.png'
	#cv.imwrite(nom_image, frame)
	else :
		framearray.append(frame)
		passe = True
vi.release()



#liste = sorted(os.listdir('/mnt/c/Users/KodiAk/Pictures/test/'))
#frame=cv.imread('/mnt/c/Users/KodiAk/Pictures/test/'+liste[0])
#frame=cv.cvtColor(framearray[0], cv.COLOR_BGR2RGB)
#frame_trait = traitement(frame)
#frame_img = Image.fromarray(frame_trait)
#frame_img.save('/mnt/c/Users/KodiAk/Pictures/test/test.png')
#frame_img_array = np.array(frame_img)
#frame_cv = cv.cvtColor(frame_img_array, cv.COLOR_RGB2BGR)
#cv.imwrite('/mnt/c/Users/KodiAk/Pictures/test/test2.png', frame_cv)

h, l, c = framearray[0].shape

fourcc = cv.VideoWriter_fourcc(*'XVID')
vid = cv.VideoWriter('/mnt/c/Users/KodiAk/Desktop/output.avi', fourcc, fps, (l,h))
for i in range(len(framearray)) : 
	#frame=cv.imread('/mnt/c/Users/KodiAk/Pictures/test/'+liste[i])
	frame = framearray[i]
	vid.write(frame)
vid.release()