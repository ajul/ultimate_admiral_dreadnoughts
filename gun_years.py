import uad.techs
import uad.output

gun_techs = []

for tech in uad.techs.techs.values():
    if tech['type'] in ['gun_sec', 'gun_main']:
        gun_techs.append(tech)

start_year = min(tech['year'] for tech in gun_techs)
end_year = max(tech['year'] for tech in gun_techs)



header = [
    'Year',
    ]
for inch in range(2, 21):
    header.append('%d"' % inch)

result = []

gun_marks = [''] * 21

for year in range(start_year, end_year+1):
    row = ['%d' % year]
    for tech in gun_techs:
        if tech['year'] == year:
            for inch in range(2, 21):
                key = 'effect.gun.%d' % inch
                if key in tech:
                    gun_marks[inch] = '%d' % tech[key]
    row += gun_marks[2:]
    result.append(row)

uad.output.output_all('gun_years', header, result)




