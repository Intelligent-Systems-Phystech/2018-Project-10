import argparse
import glob
import os

ap = argparse.ArgumentParser()
ap.add_argument("--no-light", action="store_false",
    help="launch light algorithms(default True)")
ap.add_argument("--heavy", action="store_true",
    help="launch heavy computaional algorithms")
args = vars(ap.parse_args())

inputImagesFolder = "../data/input_images"
outputImagesFolder = "../data/output_images"

def runAlgorithm(algorithm):
    
    print("Algorithm:", algorithm)
    outputAlgorithmFolder = outputImagesFolder + "_" + algorithm
    
    if not os.path.exists(outputAlgorithmFolder):
        os.makedirs(outputAlgorithmFolder)

    for imagesFolderPath in glob.glob(inputImagesFolder + "/*"):
        imagesFolder = imagesFolderPath.split("/")[-1]
        outputFolder = outputAlgorithmFolder + "/" + imagesFolder
        if not os.path.exists(outputFolder):
            os.makedirs(outputFolder)
        os.system("python %s.py -i %s -o %s" % (algorithm, imagesFolderPath, outputFolder))    

algorithms_light = [
    "auto_canny",
    "houph_lines",
    "mser",
    "swt",
    "swt_full",
]

algorithms_heavy = [
    "text_detect",  #computantionally heavy
]

algorithms = []

if args["no_light"]:
    algorithms += algorithms_light

if args["heavy"]:
    algorithms += algorithms_heavy
    
if not os.path.exists(inputImagesFolder):
    print("Input folder doesn't exist");
    exit(1);

print("Next algorithms will be launched:", *algorithms)
    
for algo in algorithms:
    runAlgorithm(algo)