import io
import os
import re
import subprocess
import distutils.cmd
import distutils.log

from setuptools import find_packages
from setuptools import setup, Command

ingestfile='PDS4_IMG_1A10_1510_IngestLDD.xml'

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
    long_description = long_description.replace("\r","")
except OSError:
    print("Pandoc not found. Long_description conversion failure.")
    import io
    # pandoc is not installed, fallback to using raw contents
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')

class LDDToolCommand(distutils.cmd.Command):
    """A custom command to run PDS4 LDDTool on the ingest local data dictionary"""

    description = 'run lddtool on ingest ldd'

    user_options = [
        # The format is (long option, short option, description).
        ('lddtool-ingestfile=', None, 'path to IngestLDD file'),
    ]

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.
        self.lddtool_ingestfile = 'PDS4_IMG_IngestLDD.xml'

    def finalize_options(self):
        """Post-process options."""
        self.announce(
            'Using ingest ldd file: %s' % os.path.abspath(self.lddtool_ingestfile),
            level=distutils.log.INFO)
        assert os.path.exists(self.lddtool_ingestfile), (
            'IngestLDD file %s does not exist.' % self.lddtool_ingestfile)

    def run(self):
        """Run command."""
        command = ['lddtool -lpsnJ %s' % os.path.abspath(self.lddtool_ingestfile)]
        self.announce(
            'Running command: %s' % str(command),
            level=distutils.log.INFO)
        working_dir = os.path.join(os.path.dirname(__file__), 'build')
        if not os.path.exists(working_dir):
            os.mkdir('build')
        subprocess.check_call(command, shell=True, cwd=working_dir)

def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="ldd-img",
    version="1.6.0.0",
    url="https://github.com/nasa-pds-data-dictionaries/ldd-img",
    license='OSI Approved Apache Software License',

    author="PDS Operator",
    author_email="pds_operator@jpl.nasa.gov",

    description="The PDS4 Imaging Local Data Dictionary",

    long_description=long_description,

    packages=find_packages(exclude=('tests',)),

    include_package_data=True,

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    cmdclass={
        'lddtool': LDDToolCommand,
        'clean': CleanCommand,
    },
)
