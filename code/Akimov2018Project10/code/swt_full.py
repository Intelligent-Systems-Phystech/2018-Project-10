import argparse
import glob
import tqdm
import os

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
    os.system("./DetectTextFull %s %s 1 > log.txt" % (imagePath, outputPath))
    