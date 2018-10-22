import bilby as bb
from pylab import *

ifo = bb.gw.detector.get_empty_interferometer('H1')

ra = 0
dec = 0
time = 0
psi = 0
mode = 'cross'

response = []

for ifo.longitude in range(-180, 181):
    result_lon = []
    for ifo.latitude in range(-90, 91):
        result_lon.append(ifo.antenna_response(ra=ra, dec=dec, time=time,
                                               psi=psi, mode=mode))
    response.append(result_lon)

lat, lon = np.meshgrid(range(-90, 91), range(-180, 181))
plt.contourf(lon, lat, response)
plt.colorbar()
plt.show()
