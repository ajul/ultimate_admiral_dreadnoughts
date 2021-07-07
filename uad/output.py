import csv

def direct_output(row):
    return row

def output_wiki(file_base, header, rows, result_row_fn=direct_output):
    result = '{| class = "wikitable sortable"\n'
    result += '! ' + ' !! '.join(header) + '\n'
    for row in rows:
        result += '|-\n'
        result += '| ' + ' || '.join(result_row_fn(row)) + '\n'
    result += '|}\n'
    with open('output/' + file_base + '.txt',
              mode='w', encoding='utf-8') as outfile:
        outfile.write(result)
        
def output_csv(file_base, header, rows, result_row_fn=direct_output):
    with open('output/' + file_base + '.csv',
              mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(result_row_fn(row) for row in rows)

def output_all(file_base, header, rows, result_row_fn=direct_output):
    output_wiki(file_base, header, rows, result_row_fn)
    output_csv(file_base, header, rows, result_row_fn)
