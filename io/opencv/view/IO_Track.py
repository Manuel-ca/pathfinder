# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import numpy as np
import cv2


def track():
    cap = cv2.VideoCapture('http://192.168.0.2:8080/?action=stream')
    hauteur = cap.get(3) #hauteur
    largeur = cap.get(4) #largeur
    ct_img = 0 # compteur
    tx_img = cap.get(5) #total images
    tt_img = cap.get(7) # fps
    # params for ShiTomasi corner detection
    feature_params = dict( maxCorners = 8,qualityLevel = 0.9,minDistance = 7,blockSize = 25 )
    # Parameters for lucas kanade optical flow
    lk_params = dict( winSize  = (15,15),maxLevel = 2,criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    # Take first frame and find corners in it
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
    # Create a mask image for drawing purposes
    mask = np.zeros_like(old_frame)
    while (1) :
        ret,frame = cap.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ct_img = cap.get(1) # compteur
        # calculate optical flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

        # Select good points
        good_new = p1[st==1]
        good_old = p0[st==1]
        

        #    draw the tracks
        for i,(new,old) in enumerate(zip(good_new,good_old)):
            a,b = new.ravel()
            c,d = old.ravel()
            mask = cv2.line(mask, (a,b),(c,d), (24,27,172), 1)
            frame = cv2.circle(frame,(a,b),5,(50,40,232),-1)
            img = cv2.add(frame,mask)
    
# Now update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1,1,2)

        print(ct_img)
        k = cv2.waitKey(30) & 0xff
        if k == 113:
            break
        p2 = p0
        print(p1)
        cv2.imshow('frame',img)
    
    
   

    cv2.destroyAllWindows()
    cap.release()

track()
