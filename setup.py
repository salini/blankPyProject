
import os, sys
from distutils.core import setup, Command

import subprocess

import myProject


CWD=os.path.realpath(os.path.dirname(__file__))


cmdclass = {}
try:
    from sphinx.setup_command import BuildDoc # add a command for building the html doc
    cmdclass['build_doc'] = BuildDoc
except ImportError:
    pass


class RunTestCmd(Command):
    description = 'run all tests in tests folder'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        res = os.system("python "+CWD+"/tests/runAllTests.py")
        if res != 0:
            sys.exit(1)

cmdclass["run_test"] = RunTestCmd


class RunPyLintCmd(Command):
    description = 'run pylint on myProject Package'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        res = os.system("pylint myProject")
        if res != 0:
            sys.exit(1)

cmdclass["run_pylint"] = RunPyLintCmd




class BuildExeCmd(Command):
    description = 'build stand alone executable of the package'
    user_options = [
        ('oneFile', None, "create a stand alone zipped in one executable file"),
    ]

    def initialize_options(self):
        self.oneFile = None

    def finalize_options(self):
        pass

    def run(self):
        #os.chdir("project")
        if self.oneFile:
          subprocess.call(["pyinstaller", "project/project_onefile_freeze.spec"])
        else:
          subprocess.call(["pyinstaller", "project/project_freeze.spec"])

cmdclass["build_exe"] = BuildExeCmd




with open('README.md', 'r') as f:
    readme = f.read()


setup(
    name='myProject',
    version=myProject.version(),
    description='a simple project as a basic template package',
    long_description=readme,
    license='GPL',
    author=['joseph salini'],
    author_email=['josephsalini@gmail.com'],
    url='https://github.com/salini/blankPyProject',
    packages=['myProject'],
    requires=['PyQt4'],
    cmdclass=cmdclass,
)
