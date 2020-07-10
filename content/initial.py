%%time
import os
import numpy
import pandas as pd
from matplotlib import pyplot as plt

% cd /content/
if not os.path.isdir("geriatrics"):
  % mkdir geriatrics

% cd /content/geriatrics/

% cd /content/geriatrics
if os.path.isdir("Geriatrics_Data"):
  print("Geriatrics_Data already Exists")
else:
  ! git clone https://github.com/saahil-jain/Geriatrics_Data.git
  % cd Geriatrics_Data
  ! git pull
  % cd /content/

% cd /content/geriatrics/
# checking if pwd is geriatrics_code dir
if os.getcwd().split("/")[-1] == "Geriatrics_Code":
  print("Current working directory is already Geriatrics_Code")
elif os.path.isdir("Geriatrics_Code"):
  print("Geriatrics_Code already Exists")
else:
  ! git clone https://github.com/saahil-jain/Geriatrics_Code.git

if os.path.isdir("Geriatrics_Code"):
  % cd Geriatrics_Code
! git pull

%cd /content/geriatrics/Geriatrics_Data/
if not os.path.isdir("test"):
  % mkdir test
  % cd test
  % mkdir Video_Fall
  % mkdir Video_Regular_Activity

  % cd '/content/geriatrics/Geriatrics_Data/Video/Video_Fall/'
  % mv fall-10-cam0.mp4 /content/geriatrics/Geriatrics_Data/test/Video_Fall/
  % mv fall-27-cam0.mp4 /content/geriatrics/Geriatrics_Data/test/Video_Fall/

  % cd '/content/geriatrics/Geriatrics_Data/Video/Video_Regular_Activity/'
  % mv adl-10-cam0.mp4 /content/geriatrics/Geriatrics_Data/test/Video_Regular_Activity/
  % mv adl-23-cam0.mp4 /content/geriatrics/Geriatrics_Data/test/Video_Regular_Activity/

% cd /content/geriatrics/Geriatrics_Data
% mv Video train
