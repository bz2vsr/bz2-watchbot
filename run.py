import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class RestartHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.start_bot()

    def start_bot(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        print("\n[RELOAD] Starting bot...")
        self.process = subprocess.Popen([sys.executable, 'main.py'])

    def on_modified(self, event):
        if event.src_path.endswith(('.py', '.json')):
            print(f"\n[RELOAD] {event.src_path} changed. Restarting bot...")
            self.start_bot()

if __name__ == "__main__":
    handler = RestartHandler()
    observer = Observer()
    observer.schedule(handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[EXIT] Stopping bot and file watcher...")
        if handler.process:
            handler.process.terminate()
        observer.stop()
    observer.join() 