#!/usr/bin/env python3

"""Create a plot of the equilibrium angular momentum."""

from os import path

from matplotlib import pyplot, rcParams, patheffects
from astropy import units as u, constants as c
import numpy

def final_angmom(final_semimajor,
                 mplanet=c.M_jup,
                 mstar=c.M_sun,
                 iplanet=0.275 * c.M_jup * c.R_jup**2,
                 istar=0.07 * c.M_sun * c.R_sun**2):
    """Return the equilibrium angular momentum for the given system."""

    return (
        (iplanet + istar) * numpy.sqrt(c.G * (mplanet + mstar)
                                       /
                                       final_semimajor**3)
        +
        mplanet * mstar * numpy.sqrt(c.G * final_semimajor / (mplanet + mstar))
    )

if __name__ == '__main__':
    a_units = c.R_sun
    angmom_units = c.M_sun * c.R_sun**2 / u.day
    plot_a = 10.0 ** (numpy.linspace(0, 3, 1000)) * c.R_sun
    plot_final_angmom = final_angmom(plot_a)

    rcParams['font.size'] = '18'
    rcParams['figure.subplot.top'] = 0.95
    rcParams['figure.subplot.bottom'] = 0.15
    rcParams['figure.subplot.left'] = 0.15
    rcParams['figure.subplot.right'] = 0.95
    pyplot.semilogx(
        plot_a.to_value(a_units),
        plot_final_angmom.to_value(angmom_units),
        '-k'
    )
    ymin = plot_final_angmom.to_value(angmom_units).min()
    pyplot.axhspan(
        ymin=0,
        ymax=ymin,
        color='0.5'
    )
    pyplot.xlabel(r'Equilibrium semi-major axis [$R_\odot$]')
    pyplot.ylabel(r'Angular momentum [$M_\odot R_\odot^2 / day$]')
    text = pyplot.text(numpy.sqrt(1000.0),
                       ymin / 2, 'Planet engulfed',
                       ha='center',
                       va='center',
                       color='white')
    text.set_path_effects([patheffects.Stroke(linewidth=3, foreground='black'),
                           patheffects.Normal()])
    pyplot.ylim(0, 1)
    pyplot.xlim(1, 1000)

    plot_fname = path.join(
        path.dirname(
            path.dirname(
                path.abspath(__file__)
            )
        ),
        'equilibrium_angmom.pdf'
    )
    pyplot.savefig(plot_fname)
