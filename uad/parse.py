import csv
import re
import os

def parse_data(name):
    for filename in os.listdir('data'):
        if name.lower() in filename.lower():
            return parse_csv(os.path.join('data', filename))
    raise OSError('No file found for ' + name)

def parse_csv(path):
    headers = None
    data = {}
    with open(path, encoding='utf-8') as infile:
        reader = csv.reader(infile)
        for row in reader:
            if row[0][0] == '#': continue
            if row[0][0] == '@':
                headers = []
                for cell in row:
                    if len(cell) >= 1 and cell[0] in ['#', '@']:
                        cell = cell[1:]
                    headers.append(cell)
                continue
            if headers is None: continue
            row_data = {}
            for header, cell in zip(headers, row):
                if header in effect_headers:
                    row_data.update(parse_effect(header, cell))
                elif header in list_headers:
                    row_data[header] = parse_list(cell)
                elif header[:-1] == 'range_':
                    row_data[header] = float(cell.replace(',', '.'))
                else:
                    row_data[header] = try_cast_number(cell)
            data[row_data[headers[0]]] = row_data
    return data

def try_cast_number(x):
    try: return int(x)
    except: pass
    try: return float(x)
    except: pass
    return x

effect_headers = ['Comp_Needs', 'effect', 'param', 'stats']
list_effects = ['need', 'needs_component', 'not_component', 'obsolete', 'unlock', 'var']
dict_effects = ['cost', 'gun', 'stat', 'tonnage', 'turret_b_accuracy', 'turret_b_reload', 'turret_b_rotation', 'weight']
reverse_dict_effects = ['main_barrels', 'sec_barrels', 'torpedo_tubes']
    
def parse_effect(header, cell):
    cell = cell.replace(' ', '')
    result = {}
    # Any effects with no arguments are listed in the header itself.
    result[header] = []
    
    for effect_text in re.split(r'\s*,\s*', cell):
        m = re.match(r'([a-z_]+)\((.*)\)', effect_text)
        if not m:
            result[header].append(effect_text)
            continue
        effect = m.group(1)
        args = re.split(r'\s*;\s*', m.group(2))
        if effect in dict_effects:
            if len(args) != 2:
                raise RuntimeError('Got unexpected number of arguments for dict effect', effect_text)
            key = header + '.' + effect + '.' + args[0]
            result[key] = float(args[1])
        elif effect in reverse_dict_effects:
            value = float(args[0])
            for arg in args[1:]:
                key = header + '.' + effect + '.' + arg
                result[key] = value
        elif effect in list_effects:
            key = header + '.' + effect
            if key not in result:
                result[key] = args
            else:
                result[key] += args
        else:
            if len(args) > 1:
                raise RuntimeError('Got unexpected multiple arguments for unary effect ' + effect_text)
            key = header + '.' + effect
            result[key] = try_cast_number(args[0])
    return result

list_headers = ['countries', 'effect', 'param', 'similar', 'shipType']

def parse_list(cell):
    return re.split(r'\s*,\s', cell)

