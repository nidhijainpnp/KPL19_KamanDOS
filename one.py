import ephem
import pandas as pd
from astropy.coordinates import SkyCoord, GCRS, EarthLocation, AltAz
from operator import itemgetter
from astropy import units as u
import numpy as np
from astropy.time import Time


df = pd.read_csv("data.csv")


ra= []
for i in range(274):
    ra.append(df.loc[:, "Column 2"][i] * u.deg)

dec= []
for i in range(274):
    dec.append(df.loc[:, "Column 3"][i] * u.deg)

idi= []
for i in range(274):
    idi.append(df.loc[:, "Column 1"][i])


def closest_five(X):
    """
    FUnction to find five closest stars

    Parameters
    ----------
    X : int, mandatory
        ID of the star

    """
    iit = EarthLocation(lat=31.7754*u.deg, lon=76.9861*u.deg, height=1044*u.m)
    time = Time('2019-5-15 21:00:00')
    index = idi.index(X)
    sepa = []
    sepa_withoutaltaz = []
    alt = []
    x_coord = SkyCoord(ra=ra[index], dec=dec[index], frame='gcrs')
    for i in range(274):
        p_coord = SkyCoord(ra=ra[i], dec=dec[i], frame='gcrs')
        p_altaz = p_coord.transform_to(AltAz(obstime=time,location=iit))
        if p_altaz.alt.value>=0:
            sepa.append((x_coord.separation(p_coord).degree, i+1))
        sepa_withoutaltaz.append((x_coord.separation(p_coord).degree, i+1))
        sepa.sort(key=itemgetter(0))
        sepa_withoutaltaz.sort(key=itemgetter(0))
    return sepa[1:6], sepa_withoutaltaz[1:6]
