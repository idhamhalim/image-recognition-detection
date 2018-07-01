# image-recognition-detection
my attempt at automatic car frame recognition


Using-tiny-yolo model , shorter processing time , less accurate

<p align="center"> <a href="https://imgflip.com/gif/2d6ymj"><img src="https://i.imgflip.com/2d6ymj.gif" title="tiny-yolo-road"/width="720" height="360" border="10" /></a>> </p>


Using yolo-model, longer processing time, more objects detected

<p align="center"> <a href="https://imgflip.com/gif/2d6z42"><img src="https://i.imgflip.com/2d6z42.gif" title="yolo-road"/ width="720" height="360" border="10" /></a>> </p>

or check the full demo here:

https://www.youtube.com/watch?v=MrcocpcbRHQ

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

run `pip install -r requirements.txt` - this will install tensorflow, numpy & cython which are needed for this project.

opencv3 --> Look at wiki !

     
      


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

1. Thanks to the original author of darknet and YOLO
https://pjreddie.com/

2. Thanks for the translated darkflow 
https://github.com/thtrieu/darkflow

3. Thanks to the author for process of installing OpenCV on Ubuntu
https://www.learnopencv.com/install-opencv3-on-ubuntu/

4. Setting up PYTHONPATH here to include darkflow packages
https://scipher.wordpress.com/2010/05/10/setting-your-pythonpath-environment-variable-linuxunixosx/

5. Huge thanks to r/Computer Vision, StackOverflow & GitHub community 
