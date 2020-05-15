import os
import pathlib
import re
import subprocess
import sys

PATH = '{path}{directory_sep}requirements.txt'.format(path=pathlib.Path(__file__).parent.absolute(), directory_sep=os.path.sep)

def install_dependencies(file_path):
    subprocess.check_call([sys.executable, '-m', "pip", "install", "-r", file_path], stdout=open(os.devnull, 'w'))


def get_project_dependencies():
    dependencies = dict()
    with open(PATH, mode='r') as file:
        file.seek(0)
        line = file.readline()
        while line:
            if line and re.sub('\#.*', '', line):
                dependencies.update({re.sub('\#.*', '', line).strip(): re.sub('.+?(?=\#)\#', '', line).strip()})
            line = file.readline()
    return dependencies


def get_local_dependencies():
    proc = subprocess.Popen(["pip", "freeze"], stdout=subprocess.PIPE, text=True)
    result, err = proc.communicate()
    dependencies = list()
    for line in result.split('\n'):
        if line:
            dependencies.append(re.sub('\=\=.*', '', line).strip())
    return dependencies


def add_dependencies(project_dependencies):
    fill = len(max(project_dependencies.keys(), key=lambda element: len(element)))
    with open(PATH, 'w') as file:
        for dependency, comment in project_dependencies.items():
            print('Adding new dependency to requirements.txt: {}'.format(dependency), end='\n')
            dependency_text = "%-{fill}s".format(fill=fill) % dependency
            file.write("{dependency}  #{comment}\n".format(dependency=dependency_text, comment=comment))


def get_comment_for_dependency(dependency, custom=False):
    if custom:
        print('What is the main purpose of the dependency called {}? \n'.format(dependency))
        text = sys.stdin.readline()
    else:
        text = 'TODO add comment'
    return text


def main(do_user_input=False):
    local_dependencies = get_local_dependencies()
    prev_project_dependencies = get_project_dependencies()
    new_project_dependencies = prev_project_dependencies.copy()

    add_dependency = False
    for dependency in local_dependencies:
        if dependency not in list(prev_project_dependencies.keys()):
            print('found new dependency', end='\n')
            new_project_dependencies.update({dependency: get_comment_for_dependency(dependency, do_user_input)})
            add_dependency = True

    if add_dependency:
        add_dependencies(new_project_dependencies)

    if len(new_project_dependencies.keys()) > len(prev_project_dependencies.keys()):
        print('Installing dependencies from project requirements...', end='\n')
        install_dependencies(file_path=PATH)
    else:
        print('All required dependencies are installed.')


if __name__ == '__main__':
    main()
