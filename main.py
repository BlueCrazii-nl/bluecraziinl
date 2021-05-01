#!/usr/bin/env python3

import os
import jinja2
import yaml

with open('data.yml') as f:
    data = yaml.safe_load(f)

def mkdir(name):
    try:
        os.mkdir(name)
    except:
        pass

mkdir('watch/')
mkdir('sets/')
for set in data['livesets_menu']:
    mkdir('watch/' + set['link'])
for set in data['livesets_cards']:
    mkdir('watch/' + set['link'])

env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'))

def write(dat, location):
    with open(location, 'w') as f:
        f.write(dat)

write(env.get_template('index.html').render(data=data), 'index.html')
for stream in data['streams']:
    stream['resolutions'] = data['resolutions']
    write(env.get_template('player.html').render(data=data, stream=stream), 'watch/' + stream['link'] + '.html')

def liveset(sets):
    for set in sets:
        write(env.get_template('liveset.html').render(data=data, set=set), 'sets/' + set['link'] + '.html')
        for vid in set["videos"]:
            vid["resolutions"] = []
            vid["filetype"] = "mkv"
            vid["poster"] = set["poster"]
            name = vid["name"]
            vid["name"] = name + ' @ ' + set["name"]
            write(env.get_template('player.html').render(data=data, stream=vid), 'watch/' + set['link'] + '/' + name + '.html')
liveset(data['livesets_menu'])
liveset(data['livesets_cards'])