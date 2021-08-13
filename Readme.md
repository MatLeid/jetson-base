
# Install prepared image 

Follow this guide to install the prepared image onto an empty sd card with 64GB:

https://github.com/Qengineering/Jetson-Nano-image

## Resize sd card after installation to full size

Use a tool like GParted ``sudo apt-get install gparted`` to expand the image to larger SD cards.

# Basic Tools installation

## Test CSI Camera

Install https://github.com/JetsonHacksNano/CSI-Camera and run ``python3 simple_camera.py`` to test your CSI-Camera.

## Install Jupyter Notbook 

``pip3 install --upgrade pip``

``pip3 install jupyter``

start jupyter and create a ssh tunel to access remote via localhost:8000

``jupyter notebook`` 

``ssh -L 8000:localhost:8888 jetson@192.168.178.49``



# Installing Experimental Tools (work in progress)

## Mediapipe (first approach)

https://github.com/yockgen/mediapipe_jetson_nano


## Pose Estimation using TensorRT (wip)

### Install dependencies

``sudo -H pip3 install Pillow==6.1``

``sudo -H pip3 install tqdm``

``sudo -H pip3 install pycocotools``

``sudo apt-get install python3-matplotlib``

### Install Jetcam

``git clone https://github.com/NVIDIA-AI-IOT/jetcam``
``cd jetcam``
``sudo python3 setup.py install``
``cd ..``

### Install torch2trt
 
``git clone https://github.com/NVIDIA-AI-IOT/torch2trt``
``cd torch2trt``
``sudo python3 setup.py install``
``cd ..``

### Run trt_pose demo

``git clone https://github.com/NVIDIA-AI-IOT/trt_pose``
``cd trt_pose``
``sudo python3 setup.py install``
``cd ..``


## Install mediapipe from binary files

warning: work in progress...

``curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=1_GRGQDwsl169TN9w_qWUs1cx9g_d4wMd" > /dev/null``

``CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"``

``curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=1_GRGQDwsl169TN9w_qWUs1cx9g_d4wMd" -o mediapipe-0.8.5_cuda102-cp36-none-linux_aarch64.whl``

``sudo pip3 install mediapipe-0.8.5_cuda102-cp36-none-linux_aarch64.whl``


# Optional stuff 

You don't need this to get the basic stuff running, but it can be useful if you want to play around with more tools

## Install bazel (version 4.1.0)

Install bazel if you need to build tools like mediapipe from source.

``sudo nvpmodel -m0 && sudo jetson_clocks --fan # enabling max performance mode``

``cd ~ && mkdir bazel && cd bazel && wget https://github.com/bazelbuild/bazel/releases/download/4.1.0/bazel-4.1.0-dist.zip``

``sudo apt-get install build-essential openjdk-8-jdk zip unzip``

``unzip bazel-4.1.0-dist.zip``

``export BAZEL_JAVAC_OPTS="-J-Xms1536m -J-Xmx1536m"``

``env EXTRA_BAZEL_ARGS="--host_javabase=@local_jdk//:jdk" bash ./compile.sh``

``sudo cp ~/bazel/output/bazel /usr/local/bin/``





