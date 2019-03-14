from base_houghlines import Hough_Transform
import numpy as np 
import imageio
import matplotlib as plt

def main()
	imgpath = '../../input/test_1.jpg'
	img = imageio.imread(imgpath)
	if img.ndim == 3:
	    img = Hough_Tranform.convert_rgb(img)
	accumulator, thetas, rhos = Hough_Transform.HoughLines(img)
	show_hough_line(img, accumulator, thetas, rhos, save_path='../../output/show.jpg')


if __name__ == '__main__':
	main()