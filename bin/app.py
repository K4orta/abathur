import sys, abathur, pprint
from watchdog.observers import Observer
from abathur.fs_events import SequenceScheduler

def watch(path):

    event_handler = SequenceScheduler(abathur.matchup_finder, echo_matches)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("Abathur is watching {0} for changes...".format(path))
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def process(path):
    print("Processing {0}".format(path))
    matchups = abathur.rec_dir(path)
    echo_matches(matchups)

def echo_matches(matches):
    print('Finished processing {0} matches'.format(len(matches)))
    for match in matches:
        pprint.pprint(match.to_object(), width=20, indent=2)

def main():
    path = sys.argv[2] if len(sys.argv) > 1 else '.'
    abathur.path_process.root_dir = path
    command = sys.argv[1]
    commands = {
        'watch': watch,
        'process': process
    }

    if command in commands:
        commands[command](path)
    else:
        print("invalid command: {0}".format(command))

if __name__ == "__main__":
    main()

