"""
fabfile for generating the resume in multiple formats using pandoc
"""

from __future__ import with_statement

import os
import sys

from fabric.api import abort, local, task, hide, puts
from platform import linux_distribution, system

#from string import Template

from contextlib import contextmanager

resume_name = 'greg_forties_resume.md'
project_root = os.path.normpath(os.path.join(__file__, os.path.pardir,
               os.path.pardir))
build_dir = os.path.join(project_root, 'formats')

all_build_formats = ['docx', 'html', 'html5', 'pdf', 'plain', 'asciidoc', 'odt']
disabled_build_formats = ['pdf', 'rtf']
default_build_formats = [fmt for fmt in set(all_build_formats) - set(disabled_build_formats)]


@task
def build(type='default'):
    """
    :$type=default - convert resume to file $type. Ex. fab build:docx
    """
    if type == 'all':
        formats = all_build_formats
    elif type == 'default':
        formats = default_build_formats
    elif type not in all_build_formats:
        puts("Unsupported format: '{}'".format(type))
        puts("Default formats:   {}".format(default_build_formats))
        puts("Supported formats: {}".format(all_build_formats))
        sys.exit(1)
    else:
        formats = [type]

    for fmt in formats:
        _convert_to_fmt(fmt)

    puts("Finished building.")

def _convert_to_fmt(output_fmt):
    input_file = os.path.join(project_root, resume_name)
    output_file = os.path.join(build_dir, resume_name.split('.')[0] + '.' +
                  output_fmt)
    with msg("Building {}".format(output_fmt)):
        if output_fmt == 'plain':
            output_file = output_file.replace('.plain','.txt')
            local('pandoc {} -o {} -t plain'.format(input_file, output_file))
        else:
            local('pandoc {} -o {}'.format(input_file, output_file))


@task
def install_pandoc(with_pdf=True):
    """
    :with_pdf=True - install pandoc command line tools needed for build().  if you don't need pdf, install_pandoc:with_pdf=False
    """
    unsupported_os = False
    system_type = system()
    puts("System Type: {}".format(system_type))
    if system_type == 'Linux':
        distro = linux_distribution()[0]
        puts("Linux Distro: {}".format(distro))
        if distro == 'Ubuntu':
            packages = ['pandoc']  #, 'pandoc-citeproc']
            if with_pdf == True:
                packages += ['texlive']
            msg("Installing pandoc")
            local('sudo apt-get install -y {}'.format(' '.join(tuple(packages))))
        else:
            unsupported_os = True
    else:
        unsupported_os = True

    if unsupported_os == True:
        puts("Unsupported OS. See the following for installation instructions")
        puts("http://johnmacfarlane.net/pandoc/installing.html")


@contextmanager
def msg(txt):
    puts(txt + "...", end='', flush=True)
    with hide('everything'):
        yield
    puts("done.", show_prefix=False, flush=True)


