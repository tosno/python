with open('cisco_sw.txt') as src, open('result.txt', 'w') as dest:
    for line in src:
        if line.strip().endswith('portfast') or line.strip().endswith('trap'):
            continue
        else:
            print(line.rstrip())
            dest.write(line)


