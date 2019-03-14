# Crop-Rows-Images-Using-OpenCV
hough transform, morphology

# DEPENDENCY
    opencv-python: pip install opencv-python
    numpy        : pip install numpy
    matplotlib: pip install matplotlib
    imageio: pip install imageio
# TREE
    /                
        input:       # Contain input image
        output:      # Contain output image
        src/         # Contain Source of projetct
             HoughLines Transform/
                                 base_houghlines.py   # file base houghlines transform from scratch                   
                                 show_houghlines.py   # file setup show houghlines                                
                                 check_show.py        # file check show houghlines
                                 
                                 more:  https://bit.ly/2T20gxX
                                        https://docs.opencv.org/3.1.0/d6/d10/tutorial_py_houghlines.html
                                 
             use_morphology.py      # using morphology crop rows table in images
                                    # more: https://docs.opencv.org/3.1.0/d9/d61/tutorial_py_morphological_ops.html
                                            https://docs.opencv.org/3.2.0/d1/dee/tutorial_moprh_lines_detection.html
                                            
           

