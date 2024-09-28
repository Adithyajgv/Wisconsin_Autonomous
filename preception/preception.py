from PIL import Image
import numpy as np
import cv2

img_wid =0
img_len =0



def setup(file):
    global img_wid
    global img_len

    img = Image.open(file)

    img_wid = img.size[0]
    img_len = img.size[1]

    data = np.asarray(img)

    l_arr = data[int(img_len//5):img_len,0:(img_wid//2)]
    r_arr = data[int(img_len//5):img_len,img_wid//2:img_wid +1]

    save1 = Image.fromarray(l_arr)
    save2 = Image.fromarray(r_arr)

    save1.save("temp/left.png")
    save2.save("temp/right.png")


def get_fit(file, x_offset, y_offset):
    img = cv2.imread(file)
    result = img.copy()
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    lower = np.array([155,210,90])
    upper = np.array([250,255,255])

    upper_mask = cv2.inRange(hsv_img, lower, upper)
    mask = upper_mask
    coord=cv2.findNonZero(mask)

    x = coord[:,:,0].flatten()
    y = coord[:,:,1].flatten()
    m, b = np.polyfit(x + x_offset, y + y_offset, 1)
    print(m, b)
    return m, b


def get_line(file, m, b):
    img = cv2.imread(file)
    x=0
    y=0
    size = img.shape
    for i in range(size[1]):
        y = int((m * i) + b)
        if(y>0 and y<= img_len):
            x =i
            break
    start = (x,y)

    for i in range(size[1],0,-1):
        y = int((m * i) + b)
        if(y>0 and y<= img_len):
            x =i
            break
    end = (x, y)

    return start, end

def draw_lines(file):
    setup(file)

    img = cv2.imread(file)

    left = "temp/left.png"
    right = "temp/right.png"

    m, b = get_fit(left, 0, int(img_len//5))
    start , end = get_line(file, m, b)
    half_result = cv2.line(img, start, end, (0, 0, 255), 5)

    m, b = get_fit(right, int(img_wid//4), -int(img_len//5))
    start , end = get_line(file, m, b)
    result = cv2.line(half_result, start, end, (0, 0, 255), 5)

    # Display the color of the image
    cv2.imwrite("answer.png", result)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

draw_lines("input.png")