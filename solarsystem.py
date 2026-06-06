import cv2

img = cv2.imread("assets/img/solar-system.jpg")

cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )
cv2.putText(img,
            "mercurio",
            (100,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (200,200,200)
            )
cv2.putText(img,
            "venus",
            (200,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (200,200,200)
            )
cv2.putText(img,
            "terra",
            (300,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (220,220,220)
            )
cv2.putText(img,
            "marte",
            (400,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (220,220,220)
            )
cv2.putText(img,
            "jupiter",
            (500,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (220,220,220)
            )
cv2.putText(img,
            "saturno",
            (800,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (220,220,220)
            )
cv2.putText(img,
            "urano",
            (1000,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,0)
            )
cv2.putText(img,
            "netuno",
            (1200,200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (220,220,220)
            )

cv2.imshow("resultado",img)
cv2.waitKey(0)


cv2.imwrite("assets/img/Solar-system-with-names.jpg",img)
