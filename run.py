import subprocess
from threading import Thread

def run_system(script):
    subprocess.Popen(script, shell=True)

scripts = [
    "python app.py",
    "npm run dev"
]

threads = []

for script in scripts:
    thread = Thread(target=run_system, args=(script,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

