"""
the function will mark target areas on original image by specific colour
And mark areas are transparent!

img: original image --numpy 0-255
pred: prediction image
img_dir: where to save original image
result_dir: where to save result image
name: file name
foreground: foreground areas in prediction image(target areas)
B, G, R: 0-255
"""

import numpy as np
import cv2 
import imageio

def save_visualization(img, pred, img_dir, result_dir, name, foreground, B, G, R):
  
    if not os.path.exists(img_dir):
        try:
            os.makedirs(img_dir)
            logging.info('Save directory is created.')
        except OSError:
            pass

    if not os.path.exists(result_dir):
        try:
            os.makedirs(result_dir)
            logging.info('Save directory is created.')
        except OSError:
            pass

    img_dir = img_dir + name + '.png'
    result_dir = result_dir + name + '.png'
    
    #save original image
    imageio.imsave(img_dir, img)

    # convert original image into 3 channels
    img3 = img.copy()
    img3 = cv2.cvtColor(img3, cv2.COLOR_GRAY2BGR)


    # convert prediction image into 3 channels
    tmp = pred.copy()
    tmp = tmp.astype(np.uint8)
    tmp = cv2.cvtColor(tmp, cv2.COLOR_GRAY2BGR)

    for i in range(pred.shape[0]):
        for j in range(pred.shape[0]):
            if pred[i, j] == foreground:
                tmp[i, j, 0] = B
                tmp[i, j, 1] = G
                tmp[i, j, 2] = R
                
    cv2.imwrite('test3.png',tmp)
    
    #add marks on original image
    result = cv2.addWeighted(tmp, 0.3, img3, 0.7, 0,dtype = cv2.CV_32F)
    
    #save result 
    cv2.imwrite(result_dir, result)
