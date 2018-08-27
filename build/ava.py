"""
    ~~~ Ava Theme Builder ~~~
ava.py [config_path] [target_path]
"""

import re
import sys


BASE_THEME = 'base.json'


def split_pair(s, sep=' '):
    return (s[:s.find(sep)], s[s.rfind(sep) + 1:])


def read_config(path):
    file = open(path, 'r')
    config = {}

    for line in file.readlines():
        line = line.strip()

        if line == '' or line[0] == '#':
            continue

        pair = split_pair(line)
        config[pair[0]] = pair[1]

    file.close()
    return config


def compile(config, source_path, target_path):
    source = open(source_path, 'r')
    target = open(target_path, 'w+')

    find_pattern = re.compile(r'.*#(.*)?#.*', re.IGNORECASE)
    sub_pattern = re.compile(r'#(.*)?#', re.IGNORECASE)

    replaced = 0

    for line in source.readlines():
        m = find_pattern.match(line)

        if m:
            color = config[m.group(1).lower()]
            line = sub_pattern.sub(color, line)
            replaced += 1

        target.write(line)

    source.close()
    target.close()

    return replaced


if len(sys.argv) <= 2:
    print(__doc__)
    exit(-1)

config = read_config(sys.argv[1])
status = compile(config, BASE_THEME, sys.argv[2])

print('\033[0;32mOK:\033[0m replaced %d tokens' % status)
