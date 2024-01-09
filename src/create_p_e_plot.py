#!/usr/bin/env python3

from os import path

from matplotlib import pyplot, rcParams

from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive

if __name__ == '__main__':
    rcParams['font.size'] = '18'
    rcParams['figure.subplot.top'] = 0.95
    rcParams['figure.subplot.bottom'] = 0.15
    rcParams['figure.subplot.right'] = 0.95
    rcParams['figure.subplot.left'] = 0.125


    data = NasaExoplanetArchive.query_criteria(
        table='PSCompPars',
        select='*',
        where='pl_orbper < 20'
    ).to_pandas()
    giant = data['pl_radj'] > 0.3
    pyplot.semilogx(data['pl_orbper'][giant],
                    data['pl_orbeccen'][giant],
                    'o',
                    markersize=7,
                    fillstyle='full',
                    label='Gas Giants ($R_{pl}>0.3R_{jup}$)')
    non_giant = data['pl_radj'] <= 0.3
    pyplot.semilogx(data['pl_orbper'][non_giant],
                    data['pl_orbeccen'][non_giant],
                    'o',
                    markersize=7,
                    fillstyle='full',
                    label='Smaller Planets ($R_{pl}<=0.3R_{jup}$)')
    pyplot.xlabel('Orbital Period [days]')
    pyplot.ylabel('Eccentricity')
    pyplot.legend()
    plot_fname = path.join(
        path.dirname(
            path.dirname(
                path.abspath(__file__)
            )
        ),
        'period_eccentricity.pdf'
    )
    pyplot.savefig(plot_fname)
