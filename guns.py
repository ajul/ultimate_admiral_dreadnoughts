import uad.guns
import uad.output

raw_guns = uad.parse.parse_data('guns')
raw_params = uad.parse.parse_data('params')

# constructor ammo weight seems to be determined by formula

copy_keys = [
    'hitChanceCurver',
    'hitChanceMult',
    'hitChanceMaxRange',
    'caliberInch',
    'damageMod',
    'baseWeight',
    'ammo',
]

mark_keys = [
    'barrelW',
    'firerate',
    'range',
    'accuracy',
    'penetration',
    ]

guns = []

for inch, raw_gun in raw_guns.items():
    try:
        inch = int(inch)
    except:
        continue

    for mark in range(1, 6):
        gun = {'mark' : mark}
        for key in copy_keys:
            gun[key] = raw_gun[key]
        for key in mark_keys:
            raw_key = key + '_' + str(mark)
            gun[key] = raw_gun[raw_key]
        gun['year'] = uad.guns.years[(inch, mark)]
        if (inch, mark) in uad.guns.obsolete_years:
            gun['obsoleteYear'] = uad.guns.obsolete_years[(inch, mark)]
        else:
            gun['obsoleteYear'] = 2000
        guns.append(gun)

ranges = [1.0, 2.5, 5.0, 7.5, 10.0, 15.0, 20.0, 25.0, 30.0]

header = [
    'Inch', 'Mark', 'Year', 'Obs. year',
    'Turret weight', 'Barrel weight',
    'Traverse (deg/s)',
    'Dmg',
    'RPM',
    'Range (km)',
] + ['%0.1f km' % r for r in ranges]

def compute_rotation_speed(gun):
    a = (gun['caliberInch'] - 2.0) / 18.0
    small_speed = raw_params['rotation_speed_gun_2']['value']
    big_speed = raw_params['rotation_speed_gun_18']['value']
    speed = small_speed + a * (big_speed - small_speed)
    return speed
    

def compute_accuracy(gun, km):
    if gun['range'] < km:
        return ''
    else:
        range_fraction = km / gun['range']
        x = range_fraction ** gun['hitChanceCurver']
        accuracy = gun['hitChanceMult'] * gun['hitChanceMaxRange'] ** x
        return '%0.2f%%' % (accuracy * 100.0)
        

def gun_row(gun):
    return [
        '%d' % gun['caliberInch'],
        '%d' % gun['mark'],
        '%d' % gun['year'],
        '%d' % gun['obsoleteYear'],
        '%0.2f' % gun['baseWeight'],
        '%0.2f' % gun['barrelW'],
        '%0.2f' % compute_rotation_speed(gun),
        '%0.1f' % (40.0 * gun['damageMod']),
        '%0.2f' % gun['firerate'],
        '%0.2f' % gun['range']
        ] + [compute_accuracy(gun, r) for r in ranges]

uad.output.output_all('guns', header, guns, gun_row)
        
