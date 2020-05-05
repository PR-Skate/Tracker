import os
import subprocess
import sys


def get_dependencies(file_path):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", file_path], stdout=open(os.devnull, 'wb'))
