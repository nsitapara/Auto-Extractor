
# import time module, Observer, FileSystemEventHandler 
import time 
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
import zipfile
import os 

#define the directory to watch and extract if you want it on a seperate location, by default it will extract to same location.
extractDirectory = watchDirectory = r"C:\Users\NS\Downloads\Compressed"
# extractDirectory =  r"C:\Users\NS\Downloads\Compressed"

#extracts the zip file for the given directory when its called.
def extractfiles():
    file = next(os.walk(watchDirectory))[2]
    filename = os.path.join(watchDirectory,file[-1])
    extractfoldername = os.path.join(watchDirectory,file[-1].strip('.zip'))
    with zipfile.ZipFile(filename) as zip_ref:
        zip_ref.extractall(extractfoldername)
    os.remove(filename)

def firstmethod():
    try:
        extractfiles()
    except:
        pass
    try:
        extractfiles()
    except:
        pass
    
##using eventhandler to figure out when to call. 
class EventHandler(FileSystemEventHandler):

    def on_any_event(self,event):
        print(event.event_type)
        if event.event_type == 'created':
            print("CREATED FILE")
            if ".zip" in event.src_path:
                firstmethod()
            
 #setting up the observer and event handler that gets scheduled and starts to scan.
observer = Observer() 
event_handler = EventHandler() 
observer.schedule(event_handler, watchDirectory, recursive = False) 
observer.start()
print("Started") 
try: 
    while True:
        time.sleep(5) 
except: 
    observer.stop() 
    print("Observer Stopped") 
observer.join() 

























#
# FindFirstChangeNotification sets up a handle for watching
#  file changes. The first parameter is the path to be
#  watched; the second is a boolean indicating whether the
#  directories underneath the one specified are to be watched;
#  the third is a list of flags as to what kind of changes to
#  watch for. We're just looking at file additions / deletions.
#
# change_handle = win32file.FindFirstChangeNotification (
#   path_to_watch,
#   0,
#   win32con.FILE_NOTIFY_CHANGE_FILE_NAME
# )


# print(change_handle)
# result = win32event.WaitForSingleObject (change_handle, 500)
# print(result)

#
# Loop forever, listing any file changes. The WaitFor... will
#  time out every half a second allowing for keyboard interrupts
#  to terminate the loop.
#
# try:

#   old_path_contents = dict ([(f, None) for f in os.listdir (path_to_watch)])
#   while 1:
#     result = win32event.WaitForSingleObject (change_handle, 500)

#     #
#     # If the WaitFor... returned because of a notification (as
#     #  opposed to timing out or some error) then look for the
#     #  changes in the directory contents.
#     #
#     if result == win32con.WAIT_OBJECT_0:
#       new_path_contents = dict ([(f, None) for f in os.listdir (path_to_watch)])
#       added = [f for f in new_path_contents if not f in old_path_contents]
#       deleted = [f for f in old_path_contents if not f in new_path_contents]
#       if added: print(f"Added: {added}")
#       if deleted: print(f"Deleted: {deleted}")

#       old_path_contents = new_path_contents
#       win32file.FindNextChangeNotification (change_handle)

# finally:
#   win32file.FindCloseChangeNotification (change_handle)