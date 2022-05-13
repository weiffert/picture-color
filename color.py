import sys, random, math
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def main():
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} ./path/to/image [sample-size-percentage between 0 and 1 (default is 0.01)]")
        exit(0)

    sample = sampleData(
        readImage(sys.argv[1]), 
        getSamplePercentage()
    )

    print(f"Graphing {len(sample)} data points...")
    generateColorGraph(sample)
    print(f"Done graphing. View file at {plotOutput(sample)}")

def readImage(path):
    image = Image.open(path)
    pixels = list(image.getdata())
    return pixels

def title():
    return sys.argv[1].split('.')[0]

def plotOutput(data):
    return f"{title()}-{len(data)}-graph.png"

def getSamplePercentage():
    if len(sys.argv) == 3:
        percentage = float(sys.argv[2])
        if percentage > 1 or percentage <= 0:
            print("Invalid sample percentage. Must be > 0 and <= 1")
            exit(1)
        return percentage
    return 0.01

def generateColorGraph(colorData):
    fig = plt.figure(figsize = (10, 7))
    ax = fig.add_subplot(111, projection = '3d')

    for (r, g, b) in colorData: 
        ax.scatter(r, g, b, color=colors.to_hex([r/255, g/255, b/255]), s=0.5)
    plt.title(f"{title()} Color Distribution of {len(colorData)} Data Points")
    plt.savefig(plotOutput(colorData))

def sampleData(data, percentage):
    return random.sample(
        data, 
        # Ensure doesn't exceed the number of pixels
        min(
            len(data),
            math.floor(len(data) * percentage), 
        )
    )

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

main()