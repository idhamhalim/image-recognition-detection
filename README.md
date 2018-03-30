# image-recognition-detection
my attempt at automatic car frame recognition

## Update 

`sudo apt-get update`

`sudo apt-get upgrade`

## Install Darkflow

the link to the repo is here : https://github.com/thtrieu/darkflow

git clone the repo

`git clone https://github.com/thtrieu/darkflow`

& add the `predictidham.py` and `captureframe.py` python scripts to your darkflow folder

oor just clone this repo !!!



## Install Dependencies for Darkflow

python3 `sudo pip install python3`

tensorflow 1.0+ `sudo pip install tensorflow`

numpy `sudo pip install numpy`

cython `sudo pip install cython`

opencv3 

## Install OpenCV3

### 1. Update Packages


`sudo apt-get update`

`sudo apt-get upgrade`


### 2. Install Dependencies

`sudo apt-get install build-essential checkinstall cmake pkg-config yasm`

`sudo apt-get install git gfortran`

`sudo apt-get install libjpeg8-dev libjasper-dev libpng12-dev`

`sudo apt-get install libtiff5-dev` - for Ubuntu 16.04


`sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev`

`sudo apt-get install libxine2-dev libv4l-dev`

`sudo apt-get install libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev`

`sudo apt-get install qt5-default libgtk2.0-dev libtbb-dev`

`sudo apt-get install libatlas-base-dev`

`sudo apt-get install libfaac-dev libmp3lame-dev libtheora-dev`

`sudo apt-get install libvorbis-dev libxvidcore-dev`

`sudo apt-get install libopencore-amrnb-dev libopencore-amrwb-dev`

`sudo apt-get install x264 v4l-utils`

### 3. Install optional dependencies

`sudo apt-get install libprotobuf-dev protobuf-compiler`

`sudo apt-get install libgoogle-glog-dev libgflags-dev`

`sudo apt-get install libgphoto2-dev libeigen3-dev libhdf5-dev doxygen`

### 4. Install Python Libraries 

`sudo apt-get install python-dev python-pip python3-dev python3-pip`

`sudo -H pip2 install -U pip numpy`

`sudo -H pip3 install -U pip numpy`

### 5. Download OpenCV and OpenCV_contrib

#### 5.a) Download OpenCV from Github

`git clone https://github.com/opencv/opencv.git`

`cd opencv`

`git checkout 3.3.1` <- you can change to latest version

`cd ..`

#### 5.b) Download OpenCV_contrib from Github

`git clone https://github.com/opencv/opencv_contrib.git`

`cd opencv_contrib`

`git checkout 3.3.1` <- you can change to latest version

`cd ..`

#### 6.a) Make directory

`cd opencv`

`mkdir build`

`cd build`

#### 6.b) Run cmake


`cmake -D CMAKE_BUILD_TYPE=RELEASE \`

      -D CMAKE_INSTALL_PREFIX=/usr/local \`
      
      -D INSTALL_C_EXAMPLES=ON \`
      
      -D INSTALL_PYTHON_EXAMPLES=ON \`
      
      -D WITH_TBB=ON \`
      
      -D WITH_V4L=ON \`
      
      -D WITH_QT=ON \`
      
      -D WITH_OPENGL=ON \`
      
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \`
      
      -D BUILD_EXAMPLES=ON ..`
      
      
     
     
     
     
#### 6.c) Compile & Install    

find out number of CPU cores in your machine

`nproc`

substitute 4 by output of nproc

`make -j4`

`sudo make install`

`sudo sh -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf'`

`sudo ldconfig`

      


## Download YOLO Weights

the link to yolo weights file : https://drive.google.com/drive/folders/0B1tW_VtY7onidEwyQ2FtQVplWEU

download the weights the same as the model you want to use

if you want to use `tiny-yolo-voc model`, then download `tiny-yolo-voc weights` etc.. 

and save it to the root of darkflow folder

## Getting started

You can choose one of the following three ways to get started with darkflow.

Just build the Cython extensions in place. NOTE: If installing this way you will have to use ./flow in the cloned darkflow directory instead of flow as darkflow is not installed globally.

1. `python3 setup.py build_ext --inplace`

Let pip install darkflow globally in dev mode (still globally accessible, but changes to the code immediately take effect)

2. `pip install -e` .

Install with pip globally

3. `pip install .`

 !!! I recommend doing number 3 , then number 1
 
 ## Testing your darkflow installation
 
 you can check by typing the flow help menu
 
 `flow --h` or `./flow --h`
 
 ## Capturing frames
 
 You can  start capture frames from live feed or any url using the script. To do just that, navigate to your darkflow folder
 and type 
 
 `python framecapture.py`
 
 ## Processing saved frames to darkflow
 
 You can filter frames with car from a specified folder and output it to another folder. To try it, type
 
 `python predictidham.py`


## Advanced usage

### Automating the process

set up crontab for automatic frame capture and filter frame with car 

`sudo crontab -e` --> to configure cronjob


### Setting up Python PATH

append the darkflow packages to the python path

`export PYTHONPATH:/your/path/to/darkflow/packages`


for example mine is : 

`export PYTHONPATH: /usr/local/lib/python3.5/dist-packages/darkflow`

you can check where darkflow packages is by trying to uninstall darkflow, but dont uninstall it

`sudo pip uninstall darkflow`



# References

1. Thanks to the original author of darkflow and YOLO
https://pjreddie.com/

2. Thanks for the translated darkflow 
https://github.com/thtrieu/darkflow

3. Thanks to the author for process of installing OpenCV on Ubuntu
https://www.learnopencv.com/install-opencv3-on-ubuntu/

4. Setting up PYTHONPATH here to include darkflow packages
https://scipher.wordpress.com/2010/05/10/setting-your-pythonpath-environment-variable-linuxunixosx/

5. Huge thanks to r/Computer Vision, StackOverflow & GitHub community 
