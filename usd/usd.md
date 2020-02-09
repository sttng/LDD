```terminal
cd $HOME
mkdir Projects
cd Projects
mkdir Pixar
cd Pixar

xcode-select --install 

git clone https://github.com/PixarAnimationStudios/USD

sudo mkdir /opt
sudo mkdir /opt/local
sudo mkdir /opt/local/USD
sudo chmod -R 777 /opt/local/USD/


pip install --prefix /myfolder [packages]

sudo easy_install pip
sudo pip install pyopengl
sudo pip install pyside2
export PATH="$PATH:/Applications/CMake.app/Contents/bin"

python USD/build_scripts/build_usd.py --embree --prman /opt/local/USD

export PYTHONPATH="$PYTHONPATH:/opt/local/USD/lib/python"
export PATH="$PATH:/opt/local/USD/bin"
```
