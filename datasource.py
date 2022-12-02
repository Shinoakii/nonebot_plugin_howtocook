import os
from pathlib import Path
import json
import re

read_path = Path(__file__).parent
dishes_path = read_path / "dishes"
EATLISTPATH = read_path / 'eat_list.json'

def creat_eat_json():
    type_list = os.listdir(dishes_path)
    eat_list = {}
    for l in type_list:
        temp_list = os.listdir(dishes_path / l)
        for n in temp_list:
            if n == "template":
                continue
            if '.md' in n:
                nn = n[:n.index('.md')]
                eat_list[nn] = {}
                eat_list[nn]['path'] = str(dishes_path / l / n)
                eat_list[nn]['type'] = 'file'
            else:
                eat_list[n] = {}
                eat_list[n]['type'] = "dir"
                eat_list[n]['path'] = str(dishes_path / l / n)
                temp_list = os.listdir(dishes_path / l / n)
                for t in temp_list:
                    if '.md' in t:
                        eat_list[n]['path'] = str(dishes_path / l / n)
                        eat_list[n]['name'] = t
                set_root_path_and_save(eat_list[n]['path'], eat_list[n]['name'])
    
    data = json.dumps(eat_list, ensure_ascii=False, indent=4)
    save_mode = "w" if os.path.exists(EATLISTPATH) else "x"
    with open(EATLISTPATH, mode=save_mode, encoding="UTF-8") as f:
        f.write(data)
    
    return eat_list

def read_eat_list():
    with open(EATLISTPATH, "r", encoding="UTF-8") as f:
        data = f.read()
    return json.loads(data)

def set_root_path_and_save(PATH, name):
    
    FILENAME = PATH + '\\' + name
    with open(FILENAME, 'r', encoding= 'utf8') as f:
        data = f.read()
    
    PATH = PATH.replace('\\', "\\\\")
    path = str('(' + PATH + "\\\\")
    data = re.sub(r'\(./', path, data)
    save_mode = "w" if os.path.exists(FILENAME) else "x"
    with open(FILENAME, mode=save_mode, encoding="UTF-8") as f:
        f.write(data)