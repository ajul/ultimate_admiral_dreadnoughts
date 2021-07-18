import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt

figsize = (16, 9)
dpi = 120

min_range = 3.0
max_range = 30.0

chance_mult = [
    21.375,
    19.2375,
    3.6658125,
    2.9925,
    1.85,
]

chance_max_range = [
    0.000246,
    0.000246,
    0.00021923055,
    0.0002251557,
    0.0002251557,
    ]

curver = [
    0.2916, # 4"
    0.25515, # 8"
    0.5508, # 12"
    0.47952, # 16"
    0.47952, # 20"
]

range5 = [
    9,
    16.2,
    23.4,
    35.1,
    49.5,
]

linestyles = [
    (0, (1, 1)),
    (0, (4, 2)),
    (0, (9, 3)),
    (0, (16, 4)),
    (0, (25, 5)),
]

fig = plt.figure(figsize=figsize)
ax = plt.subplot(111)

for r, a, m, c, linestyle in zip(range5, chance_mult, chance_max_range, curver, linestyles):
    x = numpy.linspace(min_range, r, 2000)
    y = a * numpy.power(m, numpy.power(x / r, c))
    ax.loglog(x, y, linestyle=linestyle)

x = numpy.linspace(min_range, max_range, 2000)
ax.semilogy(x, 1 / x)
ax.semilogy(x, 10 / numpy.square(x))

ax.legend(['4"', '8"', '12"', '16"', '20"', 'Inv linear', 'Inv square'])
ax.set_xlabel('Range (km)')
ax.set_ylabel('Relative hit chance')
ax.set_xlim(min_range, max_range)
ax.set_ylim(bottom=5e-3,top=0.3)
xticks = [3, 4, 5, 6, 7, 8, 9, 10, 12.5, 15, 17.5, 20, 25, 30]
ax.set_xticks(xticks)
ax.set_xticklabels(['%0.1f' % x for x in xticks])
ax.grid()

plt.savefig('output/range_accuracy.png', dpi = dpi, bbox_inches = "tight")
