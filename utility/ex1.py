import cv2
import os
from pathlib import Path


def make_folder(path2video):
    # Split and create name for folder
    p = Path(path2video)
    string1 = p.name
    string2 = ".mp4"
    string3 = string1.replace(string2, '')

    # Make folder base on the name, then return the new folder path
    os.makedirs("resources/images/" + str(string3), exist_ok=True)
    des = ("resources/images/" + str(string3))
    print("Folder " + des + " is made")
    return des


def convert_video2image(path2video, frame_step, starting_frame, destination):
    # Open .mp4 file and create index
    cap = cv2.VideoCapture(path2video)
    i = 0

    # Check if video opened successfully or not
    if not cap.isOpened():
        print("Error opening video or file")
        cap.release()
        return
    else:
        print("Processing" + path2video)

    while cap.isOpened():

        # Capture the video frame by frame
        ret, frame = cap.read()
        if ret:
            if (i == starting_frame) or (i % frame_step == 0):
                # Write the resulting frame
                b = cv2.resize(frame, (1280, 720))

                filename = destination + "/frame_%i.jpg" % i
                cv2.imwrite(filename, b)
                print("frame " + str(i) + " created")

            i += 1
        else:
            break

    # After the loop release the cap object
    cap.release()

    # Destroy all the windows
    cv2.destroyAllWindows()
