img = imread('voiture-rouge.jpg');
    
img=imsubtract(img(:,:,1),rgb2gray(img)); %soustrait le rouge de l'image puis transforme en échelle de gris
img=medfilt2(img,[5,5]); %filtre qui permet de réduire le bruit de l'image

img=imbinarize(img,0.25); %transforme l'image en image binaire pour n'avoir plus que du noir ou blanc
%Pour octave utiliser:
img=im2double(img);

img=bwareaopen(img,300); %permet de retirer tous les pixels blancs inférieur à 300px
imshow(img);
