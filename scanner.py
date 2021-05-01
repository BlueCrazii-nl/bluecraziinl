#!/usr/bin/env python3

# Basic scanner for indexing CDN, producing a list of sets that can then
# be added to the static generator input.
# Does a bunch of string munging with the paths to get out as much info as possible.

import os 
import yaml

ROOT = '/mnt/cdn'
VIDEO = ['mp4', 'mkv', 'vp8', 'vp9']

sets = []
for dir in os.listdir(ROOT):
    if os.path.isfile(dir):
        continue

    set = { 
        'name': '', 
        'link': dir, 
        'videos': []
    }
    sets.append(set)

    for file in os.listdir(f'{ROOT}/{dir}'):
        split = file.split('(')[0].split(' @ ', 1)
        ending = file.split('.')[-1]
        
        if set['name'] == '' and len(split) > 1:
            set['name'] = split[1].split('.')[0]

        if ending in VIDEO:
            set['videos'].append({
                'name': split[0],
                'url': f'{dir}/{file}',
                'videotype': ending
            })

with open('sets.yml', 'w') as f:
    yaml.safe_dump(sets, f)
