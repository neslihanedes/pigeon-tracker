# pigeon-tracker
Use Python and OpenCV to track pigeons for automated analysis of animal behavior experiments.

This repository currently mainly consists of some basic code for exploring the OpenCV capabilities.

## Depdencies
Installing `opencv3` from `menpo` repository should be enough for the examples to work in a miniconda environment.

Because of Python foobar, it's necessary to install `pango` from `asmeurer` repo when running on Fedora.

The working conda environment  consists of following packages (Fedora 28):
```
# Name                    Version                   Build  Channel
blas                      1.0                         mkl  
bzip2                     1.0.6                h14c3975_5  
ca-certificates           2018.03.07                    0  
cairo                     1.14.12              h7636065_2  
certifi                   2018.4.16                py36_0  
ffmpeg                    4.0                  h04d0a96_0  
fontconfig                2.12.6               h49f89f6_0  
freetype                  2.8                  hab7d2ae_1  
glib                      2.56.1               h000015b_0  
graphite2                 1.3.11               h16798f4_2  
harfbuzz                  1.7.6                h5f0a787_1  
hdf5                      1.10.2               hba1933b_1  
icu                       58.2                 h9c2bf20_1  
intel-openmp              2018.0.3                      0  
jasper                    1.900.1              hd497a04_4  
jpeg                      9b                   h024ee3a_2  
libedit                   3.1.20170329         h6b74fdf_2  
libffi                    3.2.1                hd88cf55_4  
libgcc-ng                 7.2.0                hdf63c60_3  
libgfortran-ng            7.2.0                hdf63c60_3  
libopencv                 3.4.1                h1a3b859_1  
libopus                   1.2.1                hb9ed12e_0  
libpng                    1.6.34               hb9fc6fc_0  
libprotobuf               3.5.2                h6f1eeef_0  
libstdcxx-ng              7.2.0                hdf63c60_3  
libtiff                   4.0.9                he85c1e1_1  
libvpx                    1.7.0                h439df22_0  
libxcb                    1.13                 h1bed415_1  
libxml2                   2.9.8                h26e45fe_1  
mkl                       2018.0.3                      1  
mkl_fft                   1.0.1            py36h3010b51_0  
mkl_random                1.0.1            py36h629b387_0  
ncurses                   6.1                  hf484d3e_0  
numpy                     1.14.5           py36hcd700cb_0  
numpy-base                1.14.5           py36hdbf6ddf_0  
opencv3                   3.1.0                    py36_0    menpo
openssl                   1.0.2o               h20670df_0  
pango                     1.36.8                        3    asmeurer
pcre                      8.42                 h439df22_0  
pip                       10.0.1                   py36_0  
pixman                    0.34.0               hceecf20_3  
py-opencv                 3.4.1            py36h0676e08_1  
python                    3.6.5                hc3d631a_2  
readline                  7.0                  ha6073c6_4  
setuptools                39.2.0                   py36_0  
sqlite                    3.24.0               h84994c4_0  
tk                        8.6.7                hc745277_3  
wheel                     0.31.1                   py36_0  
xz                        5.2.4                h14c3975_4  
zlib                      1.2.11               ha838bed_2  

```