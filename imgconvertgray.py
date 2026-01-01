import cv2

image = cv2.imread(input("Enter the image path:\n===> "))

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ask = input("Do you want to see the image (yes/no): ").lower()
    if ask == "yes":
        cv2.imshow("Image in Grayscale", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    ask2 = input("Do you want to save the image (yes/no): ").lower()
    if ask2 == "yes":
        filepath = input("Enter the new file name to save the image (with extension): ")
        success = cv2.imwrite(filepath, gray)
        if success:
            print(f"File successfully saved as {filepath}")
        else:
            print("Image could not be saved")
    else:
        print("Thank you for using us")

else:
    print("Error: image is not loaded")


