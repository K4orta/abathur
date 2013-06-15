import sys, abathur, pprint
from watchdog.observers import Observer
from abathur.fs_events import SequenceScheduler

def echo_matches(matches):
    # pp = pprint.PrettyPrinter(indent=4)
    print('Finished processing {0} matches'.format(len(matches)))
    # for match in matches:
        # pr = pprint.pformat(match.to_object(), width=20)
        # print(pr+"\n\n\n\n")
        # sys.stdout.write(pr)
        # pp(match.to_object())

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = SequenceScheduler(abathur.matchup_finder, echo_matches)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("Abathur is watching {0} for changes".format(path))

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()

