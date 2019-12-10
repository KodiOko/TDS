import cv2 as cv
import os

#VIDEO
vi = cv.VideoCapture('/mnt/c/Users/KodiAk/OneDrive/Documents/tdsProject/video_pull_rouge.mp4')

nb_frames = vi.get(cv.CAP_PROP_FRAME_COUNT)
longueur = len(str(int(nb_frames)))
fps = vi.get(cv.CAP_PROP_FPS)

while vi.get(cv.CAP_PROP_POS_FRAMES)!=nb_frames :
	r, frame = vi.read()
	nom_image = '/mnt/c/Users/KodiAk/Pictures/test/' + 'image_' + str(int(vi.get(cv.CAP_PROP_POS_FRAMES))).zfill(longueur) + '.jpg'
	cv.imwrite(nom_image, frame)
vi.release()



liste = sorted(os.listdir('/mnt/c/Users/KodiAk/Pictures/test/'))
frame=cv.imread('/mnt/c/Users/KodiAk/Pictures/test/'+liste[0])
h, l, c = frame.shape

fourcc = cv.VideoWriter_fourcc(*'XVID')
vid = cv.VideoWriter('output.avi', fourcc, fps, (l,h))
for i in range(len(liste)) : 
	frame=cv.imread('/mnt/c/Users/KodiAk/Pictures/test/'+liste[i])
	vid.write(frame)
vid.release()