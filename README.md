
# proof of concept
  - cheap BT gamepads
  - RPi3
  - RPi NoIR v2 cam
  - any projector with enough brightness
  - (extra IR leds?)

# developer/architectural docs
  - open docs/overview.html in a browser
  
# how to install
  - rpi: install opencv
    - http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/
    - http://www.pyimagesearch.com/2015/10/26/how-to-install-opencv-3-on-raspbian-jessie
  - rpi: pip install "picamera[array]"
  - rpi: https://www.rs-online.com/designspark/building-distributed-node-red-applications-with-mqtt
  = rpi: pip install paho-mqtt
  - pc: install http://python.cocos2d.org
  
# todo
  - make test setup
  - rpi: simplify contours from findcontours
  - rpi: post contours to mqtt
  - pc: show the contours in image
  - rpi: speedup make a threaded version
  - pc: game layer collision detection will need to be rewritten
  
At that moment we can make games
  
# Credits
  - Sprites by Unlucky Studio, see http://opengameart.org/content/free-top-down-car-sprites-by-unlucky-studio/
