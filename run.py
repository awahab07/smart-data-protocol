import sys
import time
import subprocess
from subprocess import PIPE, Popen
from threading  import Thread
from queue import Queue, Empty  # python 3.x

# Django Thread
def start_django():
    subprocess.call(['python', './servers/manage.py', 'runserver',  '0.0.0.0:8000'])

djangoThread = Thread(target=start_django, name="Django Thread")
djangoThread.start()


time.sleep(2)

def start_clients():
    subprocess.call(['python', './clients.py'])

clientsThread = Thread(target=start_clients, name="Clients Thread")
clientsThread.start()


time.sleep(3)

def start_simulation():
    subprocess.call(['python', './__main__.py'])

simulationThread = Thread(target=start_simulation, name="Simulation Thread")
simulationThread.start()


