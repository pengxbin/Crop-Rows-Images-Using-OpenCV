import numpy as np
import cv2


#referencecs: https://docs.opencv.org/3.2.0/d1/dee/tutorial_moprh_lines_detection.html

img = cv2.imread('../input/test_1.jpg')

#edges = cv2.Laplacian(img, cv2.CV_8U)
edges = cv2.Canny(img, 150, 200, 3)				# find edges of image

kernel = np.zeros((5, 11), np.uint8)			# kernel used to remove vetical and small horizontal lines using erosion

kernel[2, :] = 1
eroded = cv2.morphologyEx(edges, cv2.MORPH_ERODE, kernel)  # erode image to remove unwanted lines

indices = np.nonzero(eroded) 					# find (x,y) position of the horizontal lines

rows = np.unique(indices[0])   					# As indices contain all the points along horizontal line, so get unique rows only (indices[0] contains rows or y coordinate)


# now you have unique rows but edges are more than 1 pixel thick
# so remove lines which are near to each other using a certain threshold
filtered_rows = []
for idx in range(len(rows)):
    if idx == 0:
        filtered_rows.append(rows[idx])
    else:
        if np.abs(rows[idx] - rows[idx - 1]) >= 10:
            filtered_rows.append(rows[idx])

# Crop Line Of Table
for i in range(len(filtered_rows)):
    if i < len(filtered_rows)-1:
        cv2.imwrite('../output/line_{}.jpg'.format(i), img[filtered_rows[i]:filtered_rows[i+1], :, :])
        print('Crop line {} done !'.format(i+1))