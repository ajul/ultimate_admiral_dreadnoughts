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
                    if cell[0] in ['#', '@']:
                        cell = cell[1:]
                    headers.append(cell)
                continue
            if headers is None: continue
            row_data = {}
            for header, cell in zip(headers, row):
                if header in effect_headers:
                    row_data.update(parse_effect(cell))
                elif header in list_headers:
                    row_data[header] = parse_list(cell)
                else:
                    row_data[header] = try_float(cell)
            data[row_data[headers[0]]] = row_data
    return data

def try_float(x):
    try:
        return float(x)
    except:
        return x

effect_headers = ['Comp_Needs', 'effect']
list_effects = ['need', 'needs_component', 'not_component', 'obsolete', 'unlock']
dict_effects = ['cost', 'gun', 'stat', 'tonnage', 'turret_b_accuracy', 'turret_b_reload', 'turret_b_rotation', 'var', 'weight']
reverse_dict_effects = ['main_barrels', 'sec_barrels', 'torpedo_tubes']
    
def parse_effect(cell):
    result = {}
    for effect_text in re.split(r'\s*,\s*', cell):
        m = re.match(r'([a-z_]+)\((.*)\)', effect_text)
        if not m:
            result[effect_text] = True
            continue
        effect = m.group(1)
        args = re.split(r'\s*;\s*', m.group(2))
        if effect in dict_effects:
            if len(args) != 2:
                raise RuntimeError('Got unexpected number of arguments for dict effect', effect_text)
            if effect not in result:
                result[effect] = {}
            key = effect + '.' + args[0]
            result[key] = float(args[1])
        elif effect in reverse_dict_effects:
            if effect not in result:
                result[effect] = {}
            value = float(args[0])
            for arg in args[1:]:
                key = effect + '.' + arg
                result[key] = value
        elif effect in list_effects:
            result[effect] = args
        else:
            if len(args) > 1:
                raise RuntimeError('Got unexpected multiple arguments for unary effect ' + effect_text)
            result[effect] = try_float(args[0])
    return result
        

list_headers = ['effect', 'param', 'similar', 'shipType']

def parse_list(cell):
    return re.split(r'\s*,\s', cell)

