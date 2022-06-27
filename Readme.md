# Base Install

Use the basimage that comes preinstalled with the most important tools:
https://github.com/Qengineering/Jetson-Nano-image

another great source for getting things working on the jestson nano is this repository:
https://github.com/step305/pyFaceRec_jetson_nano/blob/master/setup.txt

## Test CSI Camera

Install  https://github.com/thehapyone/NanoCamera

sudo python3 setup.py install

Run ``python3 examples/CSI_camera.py``

### Troubleshooting:

Check if device is recognized:

``ls /dev/video0``

Check if openCV was built with all necessary option like CUDA and GStreamer support:

``python3``
``import cv2``
``print(cv2.getBuildInformation())´`

If you get "illegal instructions" error when trying to use CSI Camera (from https://stackoverflow.com/questions/65631801/illegal-instructioncore-dumped-error-on-jetson-nano) edit /~/.bashrc file an put the following line to the end of the file:

``export OPENBLAS_CORETYPE=ARMV8``


# Google Coral Install

From https://coral.ai/docs/m2/get-started/#2a-on-linux

First, add our Debian package repository to your system (be sure you have an internet connection):

``echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list``

``curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -``

``sudo apt-get update``

Then install the PCIe driver and Edge TPU runtime packages:

``sudo apt-get install gasket-dkms libedgetpu1-std``

Then install pycoral

``sudo apt-get install python3-pycoral``


install missing dependencies for TensorFlow

``sudo pip3 install astor``

``sudo pip3 install Pillow``

Test Coral

``mkdir coral && cd coral``
``git clone https://github.com/google-coral/pycoral.git``
``cd pycoral``
``bash examples/install_requirements.sh classify_image.py``

python3 examples/classify_image.py \
    --model test_data/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite \
    --labels test_data/inat_bird_labels.txt \
    --input test_data/parrot.jpg

# Other stuff you might need

## Install Jupyter Notbook 

``pip3 install --upgrade pip``

``pip3 install jupyter``

start jupyter and create a ssh tunel to access remote via localhost:8000

``jupyter notebook`` 

``ssh -L 8000:localhost:8888 jetson@192.168.178.49``

## Install bazel (version 4.1.0)

Install bazel if you need to build tools like mediapipe from source.

``sudo nvpmodel -m0 && sudo jetson_clocks --fan # enabling max performance mode``

``cd ~ && mkdir bazel && cd bazel && wget https://github.com/bazelbuild/bazel/releases/download/4.1.0/bazel-4.1.0-dist.zip``

``sudo apt-get install build-essential openjdk-8-jdk zip unzip``

``unzip bazel-4.1.0-dist.zip``

On Jetson Nano (2GB) you need to increase the JVM Memory before running compile.sh

``export BAZEL_JAVAC_OPTS="-J-Xms1536m -J-Xmx1536m"``

Run compile

``env EXTRA_BAZEL_ARGS="--host_javabase=@local_jdk//:jdk" bash ./compile.sh``

``sudo cp ~/bazel/output/bazel /usr/local/bin/``



xcv
