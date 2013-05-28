import os
from watchdog.events import FileSystemEventHandler
from threading import Timer

class SequenceScheduler(FileSystemEventHandler):
    def __init__(self, process_callback, on_finish):
        self.process_callback = process_callback
        self.on_finish = on_finish
        self.__open_events = 0
        self.__path_table = {}

    # we are about: create files, modify directory
    def on_modified(self, event):
        if not event.is_directory:
            self.__path_table[os.path.dirname(event.src_path)] = True
        else:
            self.__path_table[event.src_path] = True
        self.open_event()

    def on_created(self, event):
        if not event.is_directory:
            self.__path_table[os.path.dirname(event.src_path)] = True
        self.open_event()

    def open_event(self):
        self.__open_events += 1
        t = Timer(2, self.close_event)
        t.start()

    def close_event(self):
        self.__open_events -= 1
        if self.__open_events == 0:
            print("Begin sequencing...")
            self.start_sequence()

    def start_sequence(self):
        paths = [k for k in self.__path_table]
        self.on_finish(self.process_callback(paths))
        self.__path_table = {}

    def idle(self):
        return self.__open_events > 0
