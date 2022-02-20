import cv2
import os

WINDOW_NAME = "Window"
X, Y = 0, 0
video_path = ''
img_name = ''
label = 1


def mouse_fun(event, x, y, flags, params):
    global X, Y
    X, Y = x, y
    global label
    global img_name
    if event == cv2.EVENT_LBUTTONDOWN:
        # label += 1
        print(f"{x}, {y}")
        if not os.path.exists(f"src/data/{img_name}"):
            os.makedirs(f"src/data/{img_name}")
            #  print(f"Directory: src/data/{video_path[-10:-4]} Created! ")
        else:
            #  print(f"Directory: src/data/{video_path[-10:-4]} already exists! ")
            data = open(f"src/data/{img_name}_data.csv", "a")
            imgcropped = params[1]
            imgcropped = imgcropped[y - 10:y + 10, x - 10:x + 10]
            cv2.imwrite(f"src/data/{img_name}/{img_name}{label}.jpg", imgcropped)
            data.write(f"{params[0]},{x},{y}\n")
            label += 1
            data.close()


def main(path, cl_name):
    global video_path
    global img_name
    video_path = path
    img_name = cl_name
    video = cv2.VideoCapture(video_path)

    data_file_generator = open(f"src/data/{img_name}_data.csv", "a")
    data_file_generator.write(f"{video_path}\n")
    data_file_generator.close()

    if not video.isOpened():
        print("Error opening video file!")

    while True:
        global currentframe
        success, frame = video.read(1)
        currentframe = video.get(1)
        if success:
            cv2.imshow(WINDOW_NAME, frame)

            cv2.setMouseCallback(WINDOW_NAME, mouse_fun, [currentframe, frame])
            square_frame = cv2.rectangle(frame, (X - 10, Y - 10), (X + 10, Y + 10), (0, 0, 255), 1)
            cv2.imshow(WINDOW_NAME, square_frame)
            if cv2.waitKey(1) & 0xFF == ord(' '):

                while True:
                    cache = frame.copy()
                    nframe = cv2.rectangle(cache, (X - 11, Y - 11), (X + 11, Y + 11), (0, 0, 255), 1)

                    if cv2.waitKey(1) & 0xFF == ord(' '):
                        break

                    cv2.imshow(WINDOW_NAME, nframe)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break

    video.release()
    cv2.destroyWindow(WINDOW_NAME)
