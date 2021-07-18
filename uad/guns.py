import uad.technologies

# (inch, mark) -> year
gun_unlock = {}
gun_obsolete = {}

gun_inches = [x for x in range(2, 21)]
gun_marks = [0] * 21
for tech in uad.technologies.data.values():
    for inch in gun_inches:
        key = 'effect.gun.%d' % inch
        if key in tech:
            mark = tech[key]
            gun_unlock[(inch, mark)] = tech['year']
            gun_obsolete[(inch, mark-1)] = tech['year']
