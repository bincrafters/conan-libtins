[![badge](https://img.shields.io/badge/conan.io-libtins%2F3.5-green.svg?logo=data:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAABhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2ptJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAAAiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZua2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVIC4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC)](http://www.conan.io/source/libtins/3.5/bincrafters/stable) 
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![Build status](https://ci.appveyor.com/api/projects/status/5mbka78e73xn93jm?svg=true)](https://ci.appveyor.com/project/bincrafters/conan-libtins)
[![Build Status](https://travis-ci.org/bincrafters/conan-libtins.svg?branch=master)](https://travis-ci.org/bincrafters/conan-libtins)

# LIBTINS is a library for sniffing and crafting packets. 

[Conan.io](https://conan.io) package for [libtins](https://github.com/mfontanini/libtins) project

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/libtins/3.5/bincrafters/stable).

## Dependencies

Libtins depends on other libraries:
* Linux and Mac - libpcap
* Windows - WinPCAP or NPCAP 
* OpenSSL - Optional

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.

## Upload packages to server

    $ conan upload libtins/3.5@bincrafters/stable --all

## Reuse the packages

### Basic setup

    $ conan install libtins/3.5@bincrafters/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    libtins/3.5@bincrafters/stable
	
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

### License
[BSD-2](LICENSE)
