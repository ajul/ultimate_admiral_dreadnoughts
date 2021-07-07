import uad.parse

techs = uad.parse.parse_data('technologies')

unlock_years = {}
obsolete_years = {}

for tech in techs.values():
    if 'effect.unlock' in tech:
        for unlock in tech['effect.unlock']:
            unlock_years[unlock] = tech['year']
    if 'effect.obsolete' in tech:
        for obsolete in tech['effect.obsolete']:
            obsolete_years[obsolete] = tech['year']
