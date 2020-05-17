
out = []

with open('bkp') as f:
    for line in f:
        number = int(line.strip().replace(',',''))
        if number > 10:
            out.append(number)

with open('individualpcaps_experiment_10.gnudata', 'w') as f:
    for val in out:
        f.write(str(val)+",\n")