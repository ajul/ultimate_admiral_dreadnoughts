import uad.parse

import uad.technologies

data = uad.parse.parse_data('parts')

# Insert unlock/obsolete years for hulls.

for tech in uad.technologies.data.values():
    if 'effect.unlock' in tech:
        for unlock in tech['effect.unlock']:
            data[unlock]['unlock'] = tech['year']
    if 'effect.obsolete' in tech:
        for obsolete in tech['effect.obsolete']:
            data[obsolete]['obsolete'] = tech['year']

# Insert unlock/obsolete years for other parts.
for part in data.values():
    if 'param.need' not in part: continue
    ship_types = set()
    countries = set()
    need = part['param.need']
    unlock = False
    obsolete = False
    for hull in data.values():
        if hull['type'] != 'hull': continue
        tags = [hull['name'], hull['param.type']] + hull['param']
        match = all(any(x in tags for x in clause) for clause in need)
        if match:
            ship_types.add(hull['param.type'])
            countries.update(hull.get('countries', []))
            if 'unlock' in hull:
                unlock = min(unlock or uad.technologies.end_year, hull['unlock'])
            else:
                pass
                #unlock = True
            if 'obsolete' in hull:
                obsolete = max(unlock or uad.technologies.start_year, hull['obsolete'])
            else:
                obsolete = 'unlock' in hull
                
    part['shipTypes'] = [x for x in sorted(ship_types)]
    part['countries'] = [x for x in sorted(countries)]
    
    if unlock not in [False, True]:
        part['unlock'] = unlock
    if obsolete not in [False, True]:
        part['obsolete'] = obsolete
    if unlock is False and obsolete is False:
        print('Permanently locked part:', part['name'])
            