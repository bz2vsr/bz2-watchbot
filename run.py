import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent
import subprocess

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_reload = 0
        self.process = None
        self.reloading = False
        
    def on_modified(self, event):
        if not isinstance(event, FileModifiedEvent):
            return
            
        if event.src_path.endswith('.py'):
            current_time = time.time()
            
            if self.reloading:
                return
                
            if current_time - self.last_reload < 2:
                return
                
            self.reloading = True
            self.last_reload = current_time
            
            logger.info("[RELOAD] Starting bot...")
            
            if self.process:
                self.process.kill()
                self.process.wait()
            
            self.process = subprocess.Popen([sys.executable, 'main.py'])
            time.sleep(1)
            self.reloading = False

def main():
    handler = ChangeHandler()
    observer = Observer()
    observer.schedule(handler, path='.', recursive=False)
    observer.start()

    handler.process = subprocess.Popen([sys.executable, 'main.py'])
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        if handler.process:
            handler.process.kill()
            handler.process.wait()
    observer.join()

if __name__ == "__main__":
    main() 