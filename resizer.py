import os
import cv2
import csv

video_path = ''
rl = 0
label = 1
img_name = ''


def main(path, lent, imgname):
    global video_path
    global rl
    global label
    global img_name
    img_name = imgname
    rl = lent

    frames = []
    coord = []

    with open(path, "r") as data:
        reader = csv.reader(data, delimiter=',')
        for idx, row in enumerate(reader):
            if idx == 0:
                video_path = row[0]
            else:
                frames.append(float(row[0]))
                coord.append((int(row[1]), int(row[2])))

    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print("Error! No file found!")

    i = 0

    while i < len(frames):
        video.set(1, frames[i])
        ret, frame = video.read()
        img_resized = frame
        if not os.path.exists(f"src/data/{img_name}/resized{rl}"):
            os.makedirs(f"src/data/{img_name}/resized{rl}")
        else:
            img_resized = img_resized[(coord[i][1] - rl):(coord[i][1] + rl), (coord[i][0] - rl):(coord[i][0] + rl)]
            cv2.imwrite(f"src/data/{img_name}/resized{rl}/frame{i}.jpg", img_resized)
            print(f"i : {i} :: frame: {frames[i]} _ x,y:({coord[i][0]},{coord[i][1]})")
        i += 1

    print("Success!")
    video.release()
