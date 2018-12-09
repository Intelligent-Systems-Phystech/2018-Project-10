import numpy as np
import argparse
import glob
import cv2
import tqdm

def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
 
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
 
    # return the edged image
    return edged

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
    help="path to input dataset of images")
ap.add_argument("-o", "--output", required=True,
    help="path to output folder where to save result")
args = vars(ap.parse_args())
 
# loop over the images
for imagePath in tqdm.tqdm(glob.glob(args["input"] + "/*.jpg"),desc=args["input"]):
    
    outputPath = args["output"] + "/" + imagePath.split("/")[-1]
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    auto = auto_canny(blurred)
    cv2.imwrite(outputPath, auto)