import os, re, replay_parser, yaml

def rec_dir(dir, tags=()):
    objects = os.listdir(dir)
    regex = re.compile("(.SC2Replay$)|(.yaml$)", re.I)
    replays_here = False
    meta_options = {}
    matches = ()
    for a in objects:
        cd = os.path.join(dir, a)
        if(os.path.isdir(cd)):
            matches += rec_dir(cd, tags + (a,))
        else:
            if(regex.search(a)):
                if(a == "meta.yaml"):
                    stream = open(cd, 'r')
                    meta_options = yaml.load(stream)
                replays_here = True

    if(replays_here):
        matches += (replay_parser.parse_matchup(dir, tags, meta_options),)
    return matches
