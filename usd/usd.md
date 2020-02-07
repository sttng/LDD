cd $HOME
mkdir Projects
cd Projects
mkdir Pixar
cd Pixar
git clone https://github.com/PixarAnimationStudios/USD

xcode-select --install 

sudo easy_install pip
sudo pip install pyopengl
sudo pip install pyside2
export PATH="$PATH:/Applications/CMake.app/Contents/bin"
