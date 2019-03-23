import numpy as np
import pandas as pd
import csv
import math

#variables:
valid_points = 40
time_out_frames = 30
search_frames = 200
max_correlation_dist = 7


def find_distance(x1,y1,z1,x2,y2,z2):
    distance = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2)+math.pow(z2-z1,2))
    return distance

# raw_trajectories = pd.read_csv("~/Downloads/RawTrajectories/Subj10_Trial4_Trajectories_100.csv")
# print(raw_trajectories[3])
trajectories = []
with open('Subj10_Trial4_Trajectories_100.csv') as raw_trajectories:
    csv_reader = csv.reader(raw_trajectories)
    line_count = 0

    for row in csv_reader:
        line_count += 1
        row_len = len(row)

    trajectories = np.empty([line_count,row_len])
    print(trajectories.shape)
    line_count = 0
    for row in csv_reader:
        trajectories[line_count] = row
        line_count += 1
    # for row in csv_reader:
    #     if line_count <= 2:
    #         line_count += 1
    #     elif line_count == 3:
    #         trajectories = np.array(row)
    #         line_count += 1
    #     else:
    #         line = np.array(row)
    #         trajectories = np.vstack((trajectories,line))
    #         line_count += 1
    print(trajectories.shape)
row_count = 0
for row in trajectories:
    i = 0
    while i <= valid_points:
        if row[i*3] == 0:
            is_continued = False
            #check if continues
            for j in range(row_count+time_out_frames):
                if trajectories[j,i*3] != 0:
                    is_continued = True
                    break
            #find another row
            closest_point = (0,0)
            closest_dist = 9999999999
            if not is_continued:
                k = row_count
                while k < search_frames:
                    l = valid_points
                    while l < len(row):
                        if trajectories[k,l] != 0:
                            dist = find_distance(row[i*3],row[i*3+1],row[i*3+2],trajectories[k,l],trajectories[k,l+1],trajectories[k,l+1])
                            closest_dist = min(closest_dist,dist)
                            if closest_dist == dist:
                                #find
                                closest_point = (k,l)
                    l += 1
                k += 1
        i += 1
    row_count += 1

