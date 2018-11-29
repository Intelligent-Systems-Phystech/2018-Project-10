import argparse
import glob
import cv2
import tqdm
import numpy as np

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

    cdst = cv2.cvtColor(auto, cv2.COLOR_GRAY2BGR)
    lines = cv2.HoughLinesP(auto, 1, np.pi/180.0, 40, np.array([]), 50, 10)
    a,b,c = lines.shape
    for i in range(a):
        cv2.line(cdst, 
                 (lines[i][0][0], lines[i][0][1]), 
                 (lines[i][0][2], lines[i][0][3]), 
                 (0, 0, 255), 
                 3, 
                 cv2.LINE_AA
                )
    cv2.imwrite(outputPath, cdst)
    
    
        