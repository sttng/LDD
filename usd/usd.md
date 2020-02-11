Get cmake, install it, add path:
```
curl -L -o cmake-3.16.4-Darwin-x86_64.tar.gz https://github.com/Kitware/CMake/releases/download/v3.16.4/cmake-3.16.4-Darwin-x86_64.tar.gz
gunzip cmake-3.16.4-Darwin-x86_64.tar.gz
tar -xvf cmake-3.16.4-Darwin-x86_64.tar
mv CMake.app /Applications/

export PATH="$PATH:/Applications/CMake.app/Contents/bin"
```

Download source code archives from GitHub and clone the repository:
```terminal
cd $HOME
mkdir -p Projects/Pixar/
cd Projects/Pixar/

xcode-select --install 

git clone https://github.com/PixarAnimationStudios/USD
cd USD
git checkout dev
git pull

sudo mkdir -p /opt/local/USD
sudo chmod -R 777 /opt/local/USD/

sudo easy_install pip ( sudo python -m easy_install pip )
sudo pip install pyopengl
#sudo pip install --prefix /opt/local pyside2
sudo python -m pip install --index-url=https://download.qt.io/official_releases/QtForPython/ pyside2 --trusted-host download.qt.io
sudo pip install -Iv pyside2==5.12.2  (or 5.13.0)



#export PATH="$PATH:/opt/local/bin"
export RMANTREE=/Applications/Pixar/RenderManProServer-23.1/
#export PYTHONPATH="$PYTHONPATH:/opt/local/lib/python2.7/site-packages"
export PATH="$PATH:/Applications/CMake.app/Contents/bin"

python USD/build_scripts/build_usd.py --embree --prman /opt/local/USD

export PYTHONPATH="$PYTHONPATH:/opt/local/USD/lib/python"
export PATH="$PATH:/opt/local/USD/bin"

usdview ./USD/extras/usd/tutorials/convertingLayerFormats/Sphere.usda


See documentation at http://openusd.org/docs/RenderMan-USD-Imaging-Plugin.html for setting up the RenderMan plugin.

```


## Tested

| Software      | macOS 10.14.6 |
| ------------- | ------------ |
| C++ Compiler  |              |
| CMake         | 3.16.14      |
| Python        | 2.7.10       |
| Boost         |              |
| Intel TBB     |              |
| OpenSubdiv    |              |
| GLEW          |              |
| OpenImageIO   |              |
| OpenColorIO   |              |
| OSL           |              |
| Ptex          |              |
| PySide        |              |
| PyOpenGL      |              |
| Embree        |              |
| RenderMan     | 23.1         |
| Alembic       |              |
| OpenEXR       |              |
| Maya          |              |
| Katana        |              |
| Houdini       |              |
| MaterialX     |              |
| Jinja2        |              |
| Flex          |              |
| Bison         |              |
| Doxygen       |              |
| GraphViz      |              |


## Other Known Versions

These other versions have been known to work as well:

| Software      | macOS 10.14.6 |
| ------------- | ------------ |
| C++ Compiler  |              |
| Boost         |              |
| Alembic       |              |
| Maya          |              |
| PySide2       | 5.14.1       |
| HDF5          |              |
| Houdini       |              |
| OpenImageIO   |              |

