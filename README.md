# image-recognition-detection
my attempt at automatic car frame recognition

# Update 

`sudo apt-get update`

`sudo apt-get upgrade`

# Install Darkflow

the link to the repo is here : https://github.com/thtrieu/darkflow

git clone the repo

`git clone https://github.com/thtrieu/darkflow`

# Install Dependencies for Darkflow

python3 `sudo pip install python3`

tensorflow 1.0+ `sudo pip install tensorflow`

numpy `sudo pip install numpy`

opencv3 

# Install OpenCV3

1. Update Packages


`sudo apt-get update`

`sudo apt-get upgrade`


2. Install Dependencies

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

3. Install optional dependencies

`sudo apt-get install libprotobuf-dev protobuf-compiler`

`sudo apt-get install libgoogle-glog-dev libgflags-dev`

`sudo apt-get install libgphoto2-dev libeigen3-dev libhdf5-dev doxygen`

4. Install Python Libraries 

`sudo apt-get install python-dev python-pip python3-dev python3-pip`

`sudo -H pip2 install -U pip numpy`

`sudo -H pip3 install -U pip numpy`


# Download YOLO Weights

the link to yolo weights file : https://drive.google.com/drive/folders/0B1tW_VtY7onidEwyQ2FtQVplWEU

download the weights the same as the model you want to use

if you want to use `tiny-yolo-voc model`, then download `tiny-yolo-voc weights` etc..

# References

1. Thanks to the original author of darkflow and YOLO
https://pjreddie.com/

2. Thanks for the translated darkflow 
https://github.com/thtrieu/darkflow

3. Thanks to the author for process of installing OpenCV on Ubuntu
https://www.learnopencv.com/install-opencv3-on-ubuntu/
