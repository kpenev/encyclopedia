#!/usr/bin/env python3

"""Create a plot of the pseudo-synchronous spin vs eccentricity."""

from os import path

from matplotlib import pyplot, rcParams, patheffects
import numpy


#e is more readable than eccentricity in this case
#pylint: disable=invalid-name
def get_hut_pseudo_synchronous_spin(e):
    """
    Return the ratio of pseudo-synchronous to orbital angular velocity.

    Direct implementation of Hut (1981) Eq. 42.
    """

    return (
        1.0 + 7.5 * e**2 + 45.0 / 8.0 * e**4 + 5.0 / 16.0 * e**6
    ) / (
        (1.0 + 3.0 * e**2 + 3.0 / 8.0 * e**4) * (1.0 - e**2)**1.5
    )

def get_pericenter_angvel(e):
    """
    Return the pericenter angular velocity.

    Direct implementation of Hut (1981) Eq. 44.
    """

    return (1.0 + e)**2 / (1.0 - e**2)**1.5
#pylint: enable=invalid-name

if __name__ == '__main__':
    rcParams['font.size'] = '18'
    rcParams['figure.subplot.top'] = 0.95
    rcParams['figure.subplot.bottom'] = 0.15
    rcParams['figure.subplot.left'] = 0.1
    rcParams['figure.subplot.right'] = 0.95

    plot_e = numpy.linspace(0.0, 1.0, 1000)
    plot_ps_orb = get_hut_pseudo_synchronous_spin(plot_e)
    plot_ps_peri = plot_ps_orb / get_pericenter_angvel(plot_e)
    orb_color = pyplot.plot(plot_e,
                            plot_ps_orb,
                            '-',
                            linewidth=2)[0].get_color()
    peri_color = pyplot.plot(plot_e,
                             plot_ps_peri,
                             '-',
                             linewidth=2)[0].get_color()
    pyplot.axhline(1.0, color='k', linestyle=':', linewidth=2)
    orb_label_e = 0.35
    peri_label_e = 0.8
    pyplot.text(orb_label_e,
                get_hut_pseudo_synchronous_spin(orb_label_e),
                '$\Omega_{ps}/\Omega_{orb}$',
                color=orb_color,
                ha='left',
                va='top')
    pyplot.text(peri_label_e,
                (
                    get_hut_pseudo_synchronous_spin(peri_label_e)
                    /
                    get_pericenter_angvel(peri_label_e)
                ),
                '$\Omega_{ps}/\Omega_{peri}$',
                color=peri_color,
                ha='center',
                va='bottom')

    pyplot.ylim(0.75, 2.0)
    pyplot.xlim(0, 1)
    pyplot.xlabel('Eccentricity')
    plot_fname = path.join(
        path.dirname(
            path.dirname(
                path.abspath(__file__)
            )
        ),
        'pseudosync_spin.pdf'
    )
    pyplot.savefig(plot_fname)
