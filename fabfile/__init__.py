"""
fabfile for generating the resume in multiple formats using pandoc
"""

from __future__ import with_statement

import os
import sys

from fabric.api import abort, local, task, hide, puts
#from string import Template

from contextlib import contextmanager

resume_name = 'resume.md'
project_root = os.path.normpath(os.path.join(__file__, os.path.pardir,
               os.path.pardir))
build_dir = os.path.join(project_root, 'formats')

all_build_formats = ['docx', 'html', 'html5', 'pdf']
default_build_formats = all_build_formats

@task
def build(type='default'):
    """
    :$type - convert resume to file $type. Ex. fab build:docx 
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
         local('pandoc {} -o {}'.format(input_file, output_file))


@contextmanager
def msg(txt):
    puts(txt + "...", end='', flush=True)
    with hide('everything'):
        yield
    puts("done.", show_prefix=False, flush=True)


