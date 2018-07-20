import sys
import subprocess
from subprocess import PIPE, Popen
from threading  import Thread
from queue import Queue, Empty  # python 3.x

ON_POSIX = 'posix' in sys.builtin_module_names

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

p1 = Popen(['python', './__main__.py'], stdout=PIPE, bufsize=1, close_fds=ON_POSIX)
p2 = Popen(['python', './clients.py'], stdout=PIPE, bufsize=1, close_fds=ON_POSIX)
#p3 = Popen(['python', './servers/manage.py', 'runserver',  '0.0.0.0:8000'], stdout=PIPE, bufsize=1, close_fds=ON_POSIX)
q = Queue()
t = Thread(target=enqueue_output, args=(p1.stdout, q))
t.daemon = True # thread dies with the program
t.start()


# read line without blocking
try:  line = q.get_nowait() # or q.get(timeout=.1)
except Empty:
    pass
else: # got line
    print(line)

subprocess.call(['python', './servers/manage.py', 'runserver',  '0.0.0.0:8000'])
