import cv2 as cv
from select_rouge import traitement
from PIL import Image
import numpy as np

#VIDEO
vi = cv.VideoCapture('/mnt/c/Users/Nathan/OneDrive/Documents/tdsProject/video_pull_rouge.mp4')

nb_frames = vi.get(cv.CAP_PROP_FRAME_COUNT)
longueur = len(str(int(nb_frames)))
fps = vi.get(cv.CAP_PROP_FPS)

framearray = []
count = 1

while vi.get(cv.CAP_PROP_POS_FRAMES)!= nb_frames :
	r, frame = vi.read()
	
	frame_traitementRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
	
	if count==1 :
		frame_img, mask = traitement(frame_traitementRGB)
		frame_finale = cv.cvtColor(frame_img, cv.COLOR_RGB2BGR)
		framearray.append(frame_finale)
		count = 10
	else :
		frame_image = Image.fromarray(frame_traitementRGB)
		frame_image.paste(mask, (0, 0), mask)
		frame_same = cv.cvtColor(np.array(frame_image), cv.COLOR_RGB2BGR)
		framearray.append(frame_same)
		count-=1
	
vi.release()


h, l, c = framearray[0].shape

fourcc = cv.VideoWriter_fourcc(*'XVID')
vid = cv.VideoWriter('/mnt/c/Users/Nathan/Desktop/output.avi', fourcc, fps, (l,h))
for frame in framearray :
	vid.write(frame)
	
vid.release()