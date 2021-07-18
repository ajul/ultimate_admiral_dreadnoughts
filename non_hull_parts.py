import uad.parts
import uad.output

# funnels

funnels = []

for part in uad.parts.data.values():
    if part['type'] != 'funnel': continue
    if part.get('enabled', 1) == 0: continue
    if len(part['shipTypes']) == 0: continue
    if len(part['countries']) == 0: continue
    funnels.append(part)

funnel_header = [
    'Name',
    'Types',
    'Countries',
    'Unlock',
    'Obsolete',
    'Ton',
    'Cost (k)',
    'Funnel capacity',
    'Smoke',
]

def funnel_row(part):
    return (
        part['nameUi'],
        ', '.join(part['shipTypes']),
        ', '.join(part['countries']),
        ('%d' % part['unlock'] if 'unlock' in part else ''),
        ('%d' % part['obsolete'] if 'obsolete' in part else ''),
        '%d' % part['weight'],
        '%0.1f' % (part['cost'] / 1000),
        '%0.1f' % part['stats.fcap'],
        '%0.1f' % part['stats.smoke'],
    )

uad.output.output_all('funnels', funnel_header, funnels, funnel_row)

main_towers = []


for part in uad.parts.data.values():
    if part['type'] != 'tower_main': continue
    if part.get('enabled', 1) == 0: continue
    if len(part['shipTypes']) == 0: continue
    if len(part['countries']) == 0: continue
    main_towers.append(part)

main_tower_header = [
    'Name',
    'Types',
    'Countries',
    'Unlock',
    'Obsolete',
    'Ton',
    'Cost (k)',
    'Spot (km)',
    'Aim speed',
    'Accuracy',
    'Long-range accuracy',
    'Smoke',
]

def main_tower_row(part):
    return (
        part['nameUi'],
        ', '.join(part['shipTypes']),
        ', '.join(part['countries']),
        ('%d' % part['unlock'] if 'unlock' in part else ''),
        ('%d' % part['obsolete'] if 'obsolete' in part else ''),
        '%d' % part['weight'],
        '%0.1f' % (part['cost'] / 1000),
        '%0.3f' % (part.get('stats.tspot', 0.0) / 1000.0),
        '%0.1f' % part.get('stats.aim', 0.0),
        '%0.1f' % part.get('stats.acc', 0.0),
        '%0.1f' % part.get('stats.acc_long', 0.0),
        '%0.1f' % -part.get('stats.smoke', 0.0),
    )

uad.output.output_all('main_towers', main_tower_header, main_towers, main_tower_row)

secondary_towers = []

for part in uad.parts.data.values():
    if part['type'] != 'tower_sec': continue
    if part.get('enabled', 1) == 0: continue
    if len(part['shipTypes']) == 0: continue
    if len(part['countries']) == 0: continue
    secondary_towers.append(part)

secondary_tower_header = [
    'Name',
    'Types',
    'Countries',
    'Unlock',
    'Obsolete',
    'Ton',
    'Cost (k)',
    'Spot (km)',
    'Aim speed',
    'Accuracy',
    'Long-range accuracy',
    'Smoke',
]

def secondary_tower_row(part):
    return (
        part['nameUi'],
        ', '.join(part['shipTypes']),
        ', '.join(part['countries']),
        ('%d' % part['unlock'] if 'unlock' in part else ''),
        ('%d' % part['obsolete'] if 'obsolete' in part else ''),
        '%d' % part['weight'],
        '%0.1f' % (part['cost'] / 1000),
        '%0.3f' % (part.get('stats.tspot', 0.0) / 1000.0),
        '%0.1f' % part.get('stats.aim', 0.0),
        '%0.1f' % part.get('stats.acc', 0.0),
        '%0.1f' % part.get('stats.acc_long', 0.0),
        '%0.1f' % -part.get('stats.smoke', 0.0),
    )

uad.output.output_all('secondary_towers', secondary_tower_header, secondary_towers, secondary_tower_row)
