#!/usr/bin/env python3

import os
import jinja2
import yaml

# Load input data & jinja
env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'))
with open('data.yml') as f:
    data = yaml.safe_load(f)

# Create a directory, ignore if it already exists
def mkdir(name):
    try:
        os.mkdir(name)
    except:
        pass
# Create all required directories
mkdir('watch/')
mkdir('sets/')
for set in data['livesets_menu']:
    mkdir(f'watch/{set["link"]}')
for set in data['livesets_cards']:
    mkdir(f'watch/{set["link"]}')

# Get template with given name
def tem(name):
    return env.get_template(f'{name}.html')

# Write a rendered template to the given path.
def write(dat, location):
    with open(f'{location}.html', 'w') as f:
        f.write(dat)

# Create and write index and stream pages
write(tem('index').render(data=data), 'index')
write(tem('contact').render(data=data), 'contact')
for stream in data['streams']:
    stream['resolutions'] = data['resolutions']
    write(tem('player').render(data=data, stream=stream), f'watch/{stream["link"]}')

# Create and write liveset and individual video pages
def liveset(sets):
    for set in sets:
        write(tem('liveset').render(data=data, set=set), f'sets/{set["link"]}')
        for vid in set['videos']:
            # Move some stuff around to make it fit with the player template
            vid['resolutions'] = []
            vid['filetype'] = vid['videotype']
            vid['videourl'] = vid['url']
            if 'poster' in set:
                vid['poster'] = set['poster']
            name = vid['name']
            vid['name'] = name + ' @ ' + set['name']
            write(tem('player').render(data=data, stream=vid), f'watch/{set["link"]}/{name}')
liveset(data['livesets_menu'])
liveset(data['livesets_cards'])