import requests
from PIL import Image

n = 0
i = 0
q = []

url_name = str(input("URL:"))
image_width = int(input("Image width:")) + 1
image_height = int(input("Image height:")) + 1
result_name = str(input("Result name:"))

if url_name == "":
    url_name = "http://data.closertovaneyck.be/verona/tiles/26-VIS-UH/16/"
if result_name == "":
    result_name = "result"

while n < image_width:

    output = str(n) + "_" + str(i) + ".jpg"
    print(output)
    headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
    url = url_name + output
    r = requests.get(url, headers=headers)

    open("Cell/" + output, "wb").write(r.content)
    q.append("Cell/" + str(n) + "_" + str(i) + ".jpg")
    i += 1
    if i == image_height:
        images = [
            Image.open(y) for y in q
        ]
        widths, heights = zip(*(i.size for i in images))

        max_width = max(widths)
        total_height = sum(heights)

        new_im = Image.new("RGB", (max_width, total_height))

        y_offset = 0
        for im in images:
            new_im.paste(im, (0, y_offset))
            y_offset += im.size[1]

        new_im.save("Vertical/" + str(n) + ".jpg")
        print(str(n+1) + "th vertical line composited " + "(" + str(n) + ".jpg" + ")")
        q = []
        n += 1
        i = 0
        continue

vert = []
vert_i = 0
while vert_i < image_width:
    vert.append("Vertical/" + str(vert_i) + ".jpg")
    vert_i += 1
images = [
    Image.open(x) for x in vert
]
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new("RGB", (total_width, max_height))

x_offset = 0
for im in images:
    new_im.paste(im, (x_offset, 0))
    x_offset += im.size[0]

new_im.save(result_name + ".jpg")
print(result_name + ".jpg")
print("DONE!")
