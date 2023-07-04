import cv2

#https://pyimagesearch.com/2015/09/07/blur-detection-with-opencv/

def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()

def detect_blur(list_images, threshold=100):
    for imagePath in list_images:
        # load the image, convert it to grayscale, and compute the
        # focus measure of the image using the Variance of Laplacian
        # method
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)
        text = "Not Blurry"
        color = (0, 255, 255)
        # if the focus measure is less than the supplied threshold,
        # then the image should be considered "blurry"
        if fm < threshold:
            text = "Blurry"
            color = (0, 0, 255)
        # show the image
        cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 3)
        cv2.imshow("Image", image)
        key = cv2.waitKey(0)

images = ['img/1.jpg','img/2.jpg', 'img/3.jpg', 'img/4.jpg', 'img/5.jpg', 'img/6.jpg', 'img/7.jpg', 'img/8.jpg', 'img/9.jpg', 'img/10.jpg', 'img/11.jpg']

detect_blur(images, threshold=300)