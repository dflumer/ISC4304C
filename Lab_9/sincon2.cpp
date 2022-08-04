#!/usr/bin/env python
#
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
import math
import time
import sincon2_ext as sincon2


def plot(mymap):
    fig = plt.figure()
    im = plt.imshow(mymap,cmap=plt.get_cmap('jet'), vmin=0, vmax=255)
    plt.show()


if __name__ == '__main__':
    output=[]
    start = time.time()
    for x in range(1000):
        line=[]
        for y in range(1000):
            nx = x/100.
            ny = y/100.
            z = calc(nx,ny) * 255
            line.append(z)
        output.append(line)
    end = time.time()
    print("Time elapsed",end-start)
    try:
        import matplotlib.pyplot as plt
        plot(output)
    except ImportError as err:
        # Bail gracefully if we're using PyPy
        print ("Couldn't import Image or numpy:", str(err))


namespace python = boost::python;

BOOST_PYTHON_MODULE(sincon2)
{
  python::def(mymap);
}