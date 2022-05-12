import sys, os
from PIL import Image
from sklearn.cluster import KMeans

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} ./path/to/image clusters")
        exit(0)

    imageFile = sys.argv[1]
    k = sys.argv[2]

    pixels = readImage(imageFile)

    # model = KMeans(k)
    # model.fit(pixels)
    # print(model.labels_)
    # print(model.cluster_centers_)

def readImage(path):
    image = Image.open(path)
    pixels = list(image.getdata())

    print(image.format)
    print(image.size)
    print(image.mode)
    with open("pixels.txt", 'x') as f:
        for (r, g, b) in pixels:
            f.write(f"{r}, {g}, {b}\n")
    
    return pixels


main()