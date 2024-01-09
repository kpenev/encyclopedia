#!/bin/bash

~/projects/git/poet/scripts/run_debugging_evolution.py \
    --plot \
    '(age - 0.2) * 1e9:Time [yr]:eccentricity:example_evolution_eccentricity.pdf' \
    'eccentricity' \
    --plot \
    '(age - 0.2) * 1e9:Time [yr]:Period [days]:example_evolution_periods.pdf' \
    '2.0 * pi * primary_envelope_inertia / envelope_angmom:$P_\star$' \
    '2.0 * pi * 3.0242030576789932e-06 / planet_angmom:$P_{pl}$' \
    'orbital_period:$P_{orb}$' \
    'orbital_period * (1.0 + 3.0 * eccentricity**2 + 3.0 / 8.0 * eccentricity**4) * (1.0 - eccentricity**2)**1.5 / (1.0 + 7.5 * eccentricity**2 + 45.0 / 8.0 * eccentricity**4 + 5.0 / 16.0 * eccentricity**2):$P_{ps}$::' \
    --secondary-mass 0.0009545942339693249 \
    --secondary-radius 0.10276268506540176 \
    --secondary-initial-angmom 6.33387607264541e-07 \
    --disk-dissipation-age 0.2 \
    --disk-lock-frequency 1.2566370614359172 \
    --eccentricity-expansion-fname \
    /Users/kpenev/projects/git/poet/eccentricity_expansion_coef_O30.sqlite \
    --plot-x-scale log \
    --primary-reference-dissipation 4e-6 6.283185307179586e-2 0.0 1.0 \
    --secondary-reference-dissipation 2e-5 6.283185307179586e-2 0.0 1.0 \
    --max-time-step 1e-5 \
    --initial-eccentricity 0.4 \
    --initial-orbital-period 15.0
