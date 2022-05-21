import cv2



image_name =input('enter the name of the image'  ) ##enter file details
image_dir = input('enter the file directory'  )


color_image = cv2.imread(image_dir+image_name) # show image
cv2.imshow('image_not_processed',color_image)
cv2.waitKey()
cv2.destroyAllWindows()

cartoon_image_style_1 = cv2.stylization(color_image, sigma_s=200, sigma_r=0.3) ## Cartoonify process.
cv2.imshow('cartoon_1', cartoon_image_style_1)
cv2.waitKey()
cv2.destroyAllWindows()
