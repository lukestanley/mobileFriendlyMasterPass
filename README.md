# mobileFriendlyMasterPass
To generate a mobile friendly password for a specific site using a master password and site name


sudo pip install scrypt

python mobileFriendlyMasterPass.py

Enter master pass, then enter site name

There is a browser DEMO here, hosted by an untrusted third party (no offence to them):


https://htmlpreview.github.io/?https://github.com/lukestanley/mobileFriendlyMasterPass/blob/master/main.html

The Android (Java) implementation is here:

https://github.com/chozabu/MobileFriendlyMasterPass-Android/blob/master/app/src/main/java/org/chozabu/pypocketpass/PPPActivity.java

There is an Android APK prebuilt here: http://chozabu.net/autopush/master-pass-app.apk

Note that bundle.js is main.js compiled with Browserify
It's contents belong to their respective authors. 



===Compiling and using the Javascript version===


Install Browserify, e.g: sudo npm install -g browserify

git clone git@github.com:lukestanley/mobileFriendlyMasterPass.git

npm install

browserify main.js -o bundle.js



python -m SimpleHTTPServer

firefox localhost:8000



To optionally compress the JS file(minify and reduce codepaths) using the Google's Closure service:

python compile_js.py

Modify line 21 of main.html to use compiled.js instead of bundle.js
