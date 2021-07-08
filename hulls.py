import uad.parse
import uad.years
import uad.output

parts = uad.parse.parse_data('parts')

header = [
    'Name',
    'Type',
    'Countries',
    'Unlock year',
    'Min tonnage',
    'Max tonnage',
    'Hull weight',
    'Resistance',
    'Hull Form',
    'Stability',
    'Floatability',
]

def result_row(part):
    return (
        part['nameUi'],
        part['param.type'].upper(),
        ', '.join(x.title().replace('Usa', 'USA') for x in part['countries']),
        '%d' % part['unlockYear'],
        '%d' % part['tonnageMin'],
        '%d' % part['tonnageMax'],
        '%0.2f%%' % (part['hullWeightRatio'] * 100.0),
        '%0.1f' % part['stats.endurance'],
        '%0.1f' % part['stats.hull_form'],
        '%0.1f' % part['stats.stability'],
        '%0.1f' % part['stats.floatability']
        )

result_parts = []

for part in parts.values():
    if part['type'] != 'hull': continue
    if part.get('enabled', 1) == 0.0: continue
    if part['name'] not in uad.years.hull_introduce:
        print('Skip non-unlockable', part['name'])
        continue
    part['unlockYear'] = uad.years.hull_introduce[part['name']]
    result_parts.append(part)

uad.output.output_all('hulls', header, result_parts, result_row)
    
    
