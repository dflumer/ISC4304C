#import <iostream>
#include <fstream>
#include <cmath>
#include <complex>
#include <cstring>


double calcz(std::complex<double> z, std::complex<double> c)
{
  long nitmax = 1000;
  long nit = 1;
  while( abs(z) < 10.0 && nit < nitmax)
    z = z * z + c;
  double ratio = 255.0  * nit / nitmax;
  return ratio;
}

void julia_loop(double ***julia, long im_width, long im_height, double xwidth, double yheight, double xmin, double ymin, long nitmax)
{
  int nit = 0;
  double zabsmax = 10.0;
  //complex<double> z;
  std::complex<double> c(-0.1,0.65);
  std::vector<double> julia(im_width * im_height, 0.0);
  for (int ix=0; ix < im_width; ++ix)
    {
      for (int iy=0; iy < im_height; ++iy)
	{
	  nit = 0;
	  // Map pixel position to a point in the complex plane
	  std::complex<double> z((1.0 * ix) / im_width * xwidth + xmin, (1.0 * iy) / im_height * yheight + ymin);
	  // Do the iterations
	  julia[ix*im_width+iy] = calcz(z,c,zabsmax);
	}
    }
  return toPythonList(julia);
}

int main(int arc, char **argv)
{
  // define the variables then call the function over all pixels
  julia_loop(&julia, im_midth, im_height, width, yheight, xmin, ymin, nitmax);
  // write out julia to a file that then is read by juliaplot.py (see zip package)
}
