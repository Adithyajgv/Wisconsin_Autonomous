from PIL import Image
import numpy as np
import cv2

#global variables for the height and width measurement of the image in pixles
img_wid =0
img_len =0

# Since Python uses an interpreter, the main body of the program must be at the very bottom

def setup(file):
    """
    This function exists to set up the global variables for the program, as well as to split the image into two in order to use linear regressing on red pixels more easily.
    This function has one perameter: path of the input image file (String)
    This function does not return anything
    """
    #referenceing global variable declaration for these two vars within this function
    global img_wid
    global img_len

    img = Image.open(file) #opens the passed in image with Image class from PIL

    #sets the correct values to length and with global variables.
    img_wid = img.size[0]
    img_len = img.size[1]

    #turns Image type to numpy array
    data = np.asarray(img)

    # splits the numpy array into two vertically in order to detect left and rifght cones seperately.
    # The following two lines also remove the top part of the array in order to prevent extra data that could interfear with the linear regression
    l_arr = data[int(img_len//5):img_len,0:(img_wid//2)]
    r_arr = data[int(img_len//5):img_len,img_wid//2:img_wid +1]

    #turns numpy arrays back into Image type
    save1 = Image.fromarray(l_arr)
    save2 = Image.fromarray(r_arr)

    #saves the left and right numpy arrays as images in the temp folder
    save1.save("temp/left.png")
    save2.save("temp/right.png")


def get_fit(file, x_offset, y_offset):
    """
    This function exists to get the linear regression line's equation from an image.
    This function has three perameters: path of the image (String), x-axis offsets (Int), and y-axis offsets(Int)
    This function returns two items: the slope of the line (float), and the constant of the line (float)
    """

    img = cv2.imread(file) #using OpenCV to opne thee image file passed in as the perameter
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #turns BGR image to HSV for use with OpenCV

    #setting up the lower and uppter boundries for OpenCV mask
    lower = np.array([155,210,90])
    upper = np.array([250,255,255])

    mask = cv2.inRange(hsv_img, lower, upper) # defines th emask using the numpy arrays and upper and lower bounds from before
    
    coord=cv2.findNonZero(mask) # creates a 2d array of coordinates of red pixels protected by the mask

    # slices and flattens the xy coords 2D array into individual X and Y arrays
    x = coord[:,:,0].flatten()
    y = coord[:,:,1].flatten()

    m, b = np.polyfit(x + x_offset, y + y_offset, 1) #creates a linear regression model using all the read pixels coordinates with the offsets added along.

    return m, b # returns the slope and constant of the linear reegression line


def get_line(file, m, b):
    """
    This function uses a linear regression line to create start and end coordinates for the creating of the lines
    This function has 3 perameters: path to the image file (String), slope of line (float), constant of the line (float)
    This function returns two items: the starting coordinates (Tuple of x,y), and the ending coordinates (Tuple of x,y)
    """
    img = cv2.imread(file) #loads the passed in image for OpenCV

    #sets default x and y values to 0
    x=0 
    y=0

    size = img.shape #gets the shape of the image for processing

    #attempts to find the starting (x,y) coordinates by looping from the first x coordinate until a y coordinate the first y-coordinate that fits within the image is found
    for i in range(size[1]):
        y = int((m * i) + b) # makes sure that the output is an integer so that it can be directly used as an index
        if(y>0 and y<= img_len):
            x =i
            break
    start = (x,y)

    #attempts to find the ending (x,y) coordinates by looping from the last x coordinate until a y coordinate the last y-coordinate that fits within the image is found
    for i in range(size[1],0,-1):
        y = int((m * i) + b) # makes sure that the output is an integer so that it can be directly used as an index
        if(y>0 and y<= img_len):
            x =i
            break
    end = (x, y)

    return start, end #returns the start and end points as tuples

def draw_lines(file):
    """
    This function utilizes all the other functions to get a linear regression model and use it to draw liens onto the output image
    This function has one perameter: path to the input image file (String)
    This function does not return anything
    """

    setup(file) #calls the setup function to geth the program ready

    img = cv2.imread(file) #opens the image file with OpenCV

    #variables for the path of the left and right side of the passed in image, created by the setup function
    left = "temp/left.png"
    right = "temp/right.png"

    #left side processing
    m1, b1 = get_fit(left, 0, int(img_len//5)) # getting thfe line equation for the left side image
    start , end = get_line(file, m1, b1) #getting the start and end coords of the left side image line
    half_result = cv2.line(img, start, end, (0, 0, 255), 5) # drawing the left side line using OpenCV onto the final image

    #right side processing
    m2, b2 = get_fit(right, int(img_wid//4), -int(img_len//5)) # getting thfe line equation for the right side image
    start , end = get_line(file, m2, b2) #getting the start and end coords of the right side image line
    result = cv2.line(half_result, start, end, (0, 0, 255), 5)# drawing the right side line using OpenCV onto the final image that already has the left side line

    # Display the color of the image
    cv2.imwrite("answer.png", result) # creates an image file "answer.png" with the final output

# main body:
draw_lines("input.png") #calls the dray_lines function to create the output image