import os, re, replay_parser, yaml

root_dir = "/"

def matchup_finder(directories):
    print("processing {0} directories".format(len(directories)))
    matches = []
    for path in directories:
        if not os.path.exists(path):
            continue
        meta_options = replays_in_dir(path)
        if meta_options != None:
            print("processing matchup...")
            matches.append(replay_parser.parse_matchup(path, tags_from_path(path), meta_options))
    return matches

def tags_from_path(path):
    # rd = re.compile(root_dir)
    regex = re.compile("^set[\d]", re.I)
    tags = re.sub( root_dir+"/", '', path ).split("/")
    if len(tags) > 0 and regex.search(tags[len(tags)-1]):
        tags = tags[:len(tags)-1]
    return tags

# returns None or the meta object if there is one
def replays_in_dir(dir):
    regex = re.compile("(.SC2Replay$)", re.I)
    yx = re.compile(".yaml$", re.I)
    objects = os.listdir(dir)
    meta_options = {}
    found_files = False
    for src in objects:
        if yx.search(src):
            stream = open(os.path.join(dir,src), 'r')
            meta_options = yaml.load(stream)
            return meta_options
        elif os.path.isfile(os.path.join(dir,src)) and regex.search(src):
            found_files = True
    if found_files:
        return meta_options

    return None