import uad.parse

data = uad.parse.parse_data('technologies')

start_year = min(tech['year'] for tech in data.values() if (tech['year'] or 0) > 0)
end_year = max(tech['year'] for tech in data.values() if (tech['year'] or 0) > 0)
