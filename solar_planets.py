import cv2

img = cv2.imread("solarsystem.jpg")


print(img)

cv2.putText(img,  
           "SUN",
           (100, 100),  
           cv2.FONT_HERSHEY_COMPLEX,
           1.7,  
           (0,0,255)
           )
cv2.imshow("Solar-system",img)
cv2.waitKey(0)
cv2.imwrite("Solor_systemwithname.jpg",img)

cv2.putText(img,  
           "Mercury",
           (130, 190),  
           cv2.FONT_HERSHEY_SIMPLEX,
           0.3,  
           (255,255,255)
           )
cv2.imshow("Solar-system",img)
cv2.waitKey(0)
cv2.imwrite("Solor_systemwithname.jpg",img)

cv2.putText(img,  
           "Venus",
           (200, 180),  
           cv2.FONT_HERSHEY_SIMPLEX,
           0.3,  
           (255,255,255)
           )
cv2.imshow("Solar-system",img)
cv2.waitKey(0)
cv2.imwrite("Solor_systemwithname.jpg",img)

cv2.putText(img,  
           "Earth",
           (300, 177),  
           cv2.FONT_HERSHEY_SIMPLEX,
           0.3,  
           (255,255,255)
           )
cv2.imshow("Solar-system",img)
cv2.waitKey(0)
cv2.imwrite("Solor_systemwithname.jpg",img)

cv2.putText(img,  
           "Mars",
           (390, 180),  
           cv2.FONT_HERSHEY_SIMPLEX,
           0.3,  
           (255,255,255)
           )
cv2.imshow("Solar-system",img)
cv2.waitKey(0)
cv2.imwrite("Solor_systemwithname.jpg",img)

cv2.putText(img,  
           "Jupiter",
           (580, 370),  
           cv2.FONT_HERSHEY_SIMPLEX,
           0.3,  
           (255,255,255)
           )
cv2.imshow("Solar-system",img)
cv2.waitKey(0)
cv2.imwrite("Solor_systemwithname.jpg",img)

cv2.putText(img,  
           "Saturn",
           (800,300),  
           cv2.FONT_HERSHEY_SIMPLEX,
           0.3,  
           (255,255,255)
           )
cv2.imshow("Solar-system",img)
cv2.waitKey(0)
cv2.imwrite("Solor_systemwithname.jpg",img)

cv2.putText(img,  
           "Uranus",
           (990, 300),  
           cv2.FONT_HERSHEY_SIMPLEX,
           0.3,  
           (255,255,255)
           )
cv2.imshow("Solar-system",img)
cv2.waitKey(0)
cv2.imwrite("Solor_systemwithname.jpg",img)

cv2.putText(img,  
           "Neptune",
           (1120, 300),  
           cv2.FONT_HERSHEY_SIMPLEX,
           0.3,  
           (255,255,255)
           )
cv2.imshow("Solar-system",img)
cv2.waitKey(0)
cv2.imwrite("Solor_systemwithname.jpg",img)

