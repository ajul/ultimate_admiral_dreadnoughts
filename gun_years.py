import uad.output
import uad.years

techs = uad.parse.parse_data('technologies')

header = [
    'Year',
    ]
for inch in range(2, 21):
    header.append('%d"' % inch)

result = []

gun_marks = [''] * 21

for year in range(uad.years.start_year, uad.years.end_year+1):
    row = ['%d' % year]
    for tech in techs.values():
        if tech['year'] == year:
            for inch in range(2, 21):
                key = 'effect.gun.%d' % inch
                if key in tech:
                    gun_marks[inch] = '%d' % tech[key]
    row += gun_marks[2:]
    result.append(row)

uad.output.output_all('gun_years', header, result)




