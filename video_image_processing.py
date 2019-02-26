import cv2
import time

def video2iamge():
    vidcap = cv2.VideoCapture('./videos/cory.mp4')
    count = 0

    # FPS you want
    fps = 30

    # to get fps of video
    v_fps = vidcap.get(cv2.CAP_PROP_FPS)
    v_length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    r = int(v_fps)/fps

    # s_time = time.time()

    while (vidcap.isOpened()):
        ret, image = vidcap.read()

        if (int(vidcap.get(1)) % r == 0):
            # l_time = time.time()
            if(int(vidcap.get(1)) == v_length): break
            cv2.imwrite("./images/cory/%d.jpg" % count, image)
            print('Saved frame%d.jpg' % count)
            count += 1
            # if(int(vidcap.get(1)) % 30 == 0):
            #     print(l_time - s_time)

    vidcap.release()

def image2video():
    cv2.namedWindow('please', cv2.WINDOW_NORMAL)
    cv2.resizeWindow("please", 852, 480)
    s_time = time.time()
    for i in range(1234):
        frame = cv2.imread("./images/cory/"+ str(i) +".jpg")
        cv2.imshow("please", frame)
        cv2.waitKey(23)
    l_time = time.time()
    print(l_time - s_time)

if __name__ == '__main__':
    image2video()