# ClassDemo
Class demonstration for GIS presentation. Goal is to get zonal statistics histogram from a raster.

## Install QGIS

Naviate to the [QGIS webpage](https://www.qgis.org/en/site/) and download the most current stable release for your operating system.

#### Get the RasterStats Plugin

Plugins -> RasterStats

## Download Data

Navigate to the directory you wish to store the files and run the following command in the command prompt:

```
git clone https://github.com/TheAcademyofNaturalSciences/ClassDemo
```
Or, download directly from the GitHub web page.

## Install Anaconda

Naviate to the [Anaconda downlaods webpage](https://www.anaconda.com/download/) and download the most current stable release for your operating system.

#### Create a new Environment

It is generally good practice to have a dedicated python environment for each project you are working on. Open up the command prompt and enter the following:

```
conda create -n yourenvname python =2.7 anaconda
activate yourenvname
conda config --add channels conda-forge
conda install -n yourenvname [package]
```
