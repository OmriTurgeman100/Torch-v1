import subprocess
from threading import Thread
from multiprocessing import Process

def run_system(script):
    subprocess.Popen(script, shell=True)

scripts = [
    "python app.py",
    "npm run dev"
]

if __name__ == "__main__":
    processes = []

    for script in scripts:
        process = Process(target=run_system, args=(script,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

