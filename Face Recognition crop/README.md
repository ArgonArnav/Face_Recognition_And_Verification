# Recognize, Crop and Save Faces as Images From Video

## QUICK DEMO

- Faces are Tracking, Cropping and Saving as Images from Video

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/30784383-d75e112c-a15c-11e7-88e9-ec9ded45f57b.gif">
</p>

- Images are Saving from Video With Appropriate Path Hierarchy

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/30775206-0d959a3c-a098-11e7-965e-add626987376.gif">
</p>

## THEORY

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/31285196-6670180a-aac3-11e7-95dc-f8d65d02195a.png">
</p>

## INSTALLATION

**1.) Python and pip**

Python is automatically installed on Ubuntu. Take a moment to confirm (by issuing a python -V command) that one of the following Python versions is already installed on your system:


- Python 2.7
- Python 3.3+

The pip or pip3 package manager is usually installed on Ubuntu. Take a moment to confirm (by issuing a *pip -V* or *pip3 -V* command) that pip or pip3 is installed. We strongly recommend version 8.1 or higher of pip or pip3. If Version 8.1 or later is not installed, issue the following command, which will either install or upgrade to the latest pip version:

    $ sudo apt-get install python-pip python-dev   # for Python 2.7
    $ sudo apt-get install python3-pip python3-dev # for Python 3.n
    
**2.) dlib**

Install dlib prerequisites

The dlib library only has four primary prerequisites:
Boost
Boost.Python
CMake
X11/XQuartx

Installing CMake, Boost, Boost.Python, and X11 can be accomplished easily with  **apt-get** :

    $ sudo apt-get install build-essential cmake
    $ sudo apt-get install libgtk-3-dev
    $ sudo apt-get install libboost-all-dev
    
    $ wget https://bootstrap.pypa.io/get-pip.py
    $ sudo python get-pip.py
    
Install dlib with Python bindings

The dlib library doesn’t have any real Python prerequisites, but if you plan on using dlib for any type of computer vision or image processing, I would recommend installing:


- NumPy
- SciPy
- scikit-image

These packages can be installed via pip :

    $ pip install numpy
    $ pip install scipy
    $ pip install scikit-image
    
Years ago, we had to compile dlib manually from source (similar to how we install OpenCV). However, we can now use pip  to install dlib as well:

    $ pip install dlib
    
**3.) face_recognition 1.2.1**
    
    pip install face_recognition

## USAGE

* Just run face_recognizer_webcam.py for real-time facial recognition and if you wish to stop the running script, press Ctrl+z and it will stop the webcam from running.

* For videos run face_recognizer_video1.py or face_recognizer_video2.py and you can also download some videos of your own to test them and make some changes in the code. 
