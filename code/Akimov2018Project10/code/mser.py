import argparse
import glob
import cv2
import tqdm

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
    vis = image.copy()
    mser = cv2.MSER_create()
    regions = mser.detectRegions(gray)[0]
    hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
    cv2.polylines(vis, hulls, 1, (0, 255, 0))
    cv2.imwrite(outputPath, vis)