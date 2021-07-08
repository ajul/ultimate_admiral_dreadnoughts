import uad.parse

techs = uad.parse.parse_data('technologies')
parts = uad.parse.parse_data('parts')

start_year = min(tech['year'] for tech in techs.values() if (tech['year'] or 0) > 0)
end_year = max(tech['year'] for tech in techs.values() if (tech['year'] or 0) > 0)

# guns
gun_introduce = {}
gun_obsolete = {}

gun_inches = [x for x in range(2, 21)]
gun_marks = [0] * 21
for tech in techs:
    for inch in gun_inches:
        key = 'effect.gun.%d' % inch
        if key in tech:
            mark = tech[key]
            gun_introduce[(inch, mark)] = tech['year']
            gun_obsolete[(inch, mark-1)] = tech['year']

# hulls



hull_introduce = {}
hull_obsolete = {}

for tech in techs.values():
    if 'effect.unlock' in tech:
        for unlock in tech['effect.unlock']:
            hull_introduce[unlock] = tech['year']
    if 'effect.obsolete' in tech:
        for obsolete in tech['effect.obsolete']:
            hull_obsolete[obsolete] = tech['year']
            
# parts

part_introduce = {}
part_obsolete = {}

for name, part in parts.items():
    if part['type'] == 'hull': continue
    introduce = None
    obsolete = None
    for need in part.get('param.need', []):
        if need in hull_introduce:
            introduce = min(hull_introduce[need], introduce or start_year)
        if need in hull_obsolete:
            obsolete = max(hull_obsolete[need], obsolete or end_year)
    if introduce is not None:
        part_introduce[name] = introduce
    if obsolete is not None:
        part_obsolete[name] = obsolete
