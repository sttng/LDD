```terminal
cd $HOME
mkdir -p Projects/Pixar/
cd Projects/Pixar/

xcode-select --install 

git clone https://github.com/PixarAnimationStudios/USD

sudo mkdir -p /opt/local/USD
sudo chmod -R 777 /opt/local/USD/

sudo easy_install pip
sudo pip install --prefix /opt/local pyopengl
sudo pip install --prefix /opt/local pyside2
sudo python -m pip install --index-url=https://download.qt.io/official_releases/QtForPython/ pyside2 --trusted-host download.qt.io
sudo pip install -Iv pyside2==5.12.2  (or 5.13.0)

export PATH="$PATH:/opt/local/bin"
export RMANTREE=/Applications/Pixar/RenderManProServer-23.1/
export PYTHONPATH="$PYTHONPATH:/opt/local/lib/python2.7/site-packages"
export PATH="$PATH:/Applications/CMake.app/Contents/bin"

python USD/build_scripts/build_usd.py --embree --prman /opt/local/USD

export PYTHONPATH="$PYTHONPATH:/opt/local/USD/lib/python"
export PATH="$PATH:/opt/local/USD/bin"




See documentation at http://openusd.org/docs/RenderMan-USD-Imaging-Plugin.html for setting up the RenderMan plugin.

```
