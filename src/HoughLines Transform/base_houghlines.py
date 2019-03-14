#import necessery lib

import numpy as np 
import math
import cv2

#------------------------

class Hough_Transform:

	def convert_rgb(rgb):
		'''
			using numpy convert rgb pixel array to grayscale
		'''
		return np.dot(rgb[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)

	def HoughLines(img, angle_step = 1,line_white = True, threshold = 5):
		'''
			Base HoughLines Transfrom from scratch.
			INPUT:
				img: input images of HoughLines function, it is numpy array
				angle_step : Step of Angle when we try theta and rho for each edges (from -90 to 90 degree)
							default angle_step = 1
				line_white: True: if line detect is white ( binary image)
				threshold: We must set threshold to find edges. We can use Canny(), Laplacian(), Sobel(),... for find edges
							Value of each pixel above or below threshold are edges.

			RETURN:
				accumulator: 2D numpy array of the hough transform.
				theta:  Array of angles(radians) used to find point perpendicular from original to straight pass by each edges.
				rhos : array of rho values. 

		'''


		# setup rho & theta ranges
		h, w = img.shape
		len_diagonal = int(round(math.sqrt(h*h + w*w))) 	# pitago
		rhos = np.linspace(-len_diagonal, len_diagonal, num = len_diagonal*2) # array of rho
		theta = np.deg2rad(np.arange(-90.0, 90.0, angle_step))

		# rho = xcos(theta) + ysin(theta)

		sin_t = np.sin(theta)
		cos_t = np.cos(theta)
		num_thetas = len(theta)

		# setup accumulator
		acc = np.zeros((len_diagonal * 2 , len(theta)), dtype = np.uint8)
		# index(row, column) of pixel is edge
		edges = img > threshold if line_white else img < threshold
		y_indexs, x_indexs = np.nonzero(edges)

		# Vote in the hough accumulator
		for i in range(len(x_indexs)):
			x = x_indexs[i]
			y = y_indexs[i]
			for t_idx in range(num_thetas):
				# Calculate rho. diag_len is added for a positive index
				rho = len_diagonal + int(round(x * cos_t[t_idx] + y * sin_t[t_idx]))
				acc[rho, t_idx] += 1

		return acc, theta, rhos


if __name__ == '__main__':
	Hough_Transform.HoughLines(Hough_Transform.convert_rgb(cv2.imread('../../input/test_1.jpg')))
