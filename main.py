#!/usr/bin/env python3

import os
import jinja2
import yaml

with open('data.yml') as f:
    data = yaml.safe_load(f)

try:
    os.mkdir('watch/')
except:
    pass

env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'))

def write(dat, location):
    with open(location, 'w') as f:
        f.write(dat)

write(env.get_template('index.html').render(data=data), 'index.html')
for stream in data['streams']:
    write(env.get_template('player.html').render(data=data, stream=stream), 'watch/' + stream['link'] + '.html')