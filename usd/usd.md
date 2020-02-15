1) Download cmake, extract it, add cmake to path:
```
curl -L -o ~/Downloads/cmake-3.16.4-Darwin-x86_64.tar.gz https://github.com/Kitware/CMake/releases/download/v3.16.4/cmake-3.16.4-Darwin-x86_64.tar.gz
tar -xzvf  ~/Downloads/cmake-3.16.4-Darwin-x86_64.tar.gz -C ~/Downloads/
mv ~/Downloads/cmake-3.16.4-Darwin-x86_64/CMake.app /Applications/

export PATH="$PATH:/Applications/CMake.app/Contents/bin"
```

2) Prepare source directories (for source and build), download source code archives from GitHub and clone the repository:
```terminal
cd $HOME
mkdir -p Projects/Pixar/
cd Projects/Pixar/

xcode-select --install

sudo mkdir -p /opt/local/USD
sudo chmod -R 777 /opt/local/USD/

git clone https://github.com/PixarAnimationStudios/USD
cd USD
git checkout dev
git pull
```

3) Install pip and required packages (pyopengl, pyside2)
```terminal
sudo easy_install pip ( sudo python -m easy_install pip )

sudo pip install pyopengl
sudo python -m pip install --index-url=https://download.qt.io/official_releases/QtForPython/ pyside2 --trusted-host download.qt.io

#sudo pip install pyopengl --prefix /opt/local
#sudo python -m pip install --index-url=https://download.qt.io/official_releases/QtForPython/ pyside2 --trusted-host download.qt.io --prefix /opt/local
```

4) Set RenderMan environment variable: RMTREE. Start building.
```terminal
export RMANTREE=/Applications/Pixar/RenderManProServer-23.1/
#export PYTHONPATH="$PYTHONPATH:/opt/local/lib/python2.7/site-packages"

python USD/build_scripts/build_usd.py --prman /opt/local/USD
#python USD/build_scripts/build_usd.py --embree --embree-location /opt/local/lib --prman /opt/local/USD

export PYTHONPATH="$PYTHONPATH:/opt/local/USD/lib/python"
export PATH="$PATH:/opt/local/USD/bin"

usdview ./USD/extras/usd/tutorials/convertingLayerFormats/Sphere.usda


See documentation at http://openusd.org/docs/RenderMan-USD-Imaging-Plugin.html for setting up the RenderMan plugin.
```


## Tested

| Software      | macOS 10.14.6 |
| ------------- | ------------ |
| Xcode         | 10.311.3.1 (11C504) |
| C++ Compiler  | AppleClang 10.0.1 |
| CMake         | 3.16.14      |
| Python        | 2.7.10       |
| Boost         | 1.61.0       |
| Intel TBB     |              |
| OpenSubdiv    | 3.1.1        |
| GLEW          | 2.0.0        |
| OpenImageIO   |              |
| OpenColorIO   |              |
| OSL           |              |
| Ptex          |              |
| PySide2       | 5.14.1 https://download.qt.io/official_releases/QtForPython/pyside2/PySide2-5.14.1-5.14.1-cp27-cp27m-macosx_10_13_intel.whl (147.9 MB) |
| Shiboken (as required by PySide2) | 5.14.1       |
| PyOpenGL      | 3.1.5        |
| Embree        |              |
| RenderMan     | 23.1         |
| Alembic       |              |
| OpenEXR       | 2.2.0        |
| Maya          |              |
| Katana        |              |
| Houdini       |              |
| MaterialX     |              |
| Jinja2        |              |
| Flex          |              |
| Bison         |              |
| Doxygen       |              |
| GraphViz      |              |

