#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
import json
import os
import cv2
from os import listdir
from os.path import isfile, join

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("P")
    args = parser.parse_args()
    return args

args = parse_args()
empty_list = []
x = [f for f in listdir('{}'.format(args.P)) if isfile(join('{}'.format(args.P), f))]
face_cascade = cv2.CascadeClassifier('.\ModelFiles\haarcascade_frontalface_default.xml')

for i in range(len(x)):
    img = cv2.imread('{}\{}'.format(args.P,x[i]))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for k in range(len(faces)):
        s = {"iname": x[i], "bbox" : faces[k].tolist()}
        empty_list.append(s)
        
import json
#the result json file name
output_json = "results.json"
#dump json_list to result.json
with open(output_json, 'w') as f:
    json.dump(empty_list, f)


# In[92]:



    
    


# In[ ]:




