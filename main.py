#!/usr/bin/env python3

import jinja2
import yaml

with open('data.yml') as f:
    data = yaml.safe_load(f)

env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'))
index = env.get_template('index.html').render(data=data)

with open('index.html', 'w') as f:
    f.write(index)