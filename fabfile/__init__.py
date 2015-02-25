"""
fabfile for generating the resume in multiple formats using pandoc
"""

from __future__ import with_statement

from fabric.api import abort, local, task, hide, puts
from string import Template

from contextlib import contextmanager


@task
def build(type='all'):
    """
    :$type - convert resume to file $type (default 'all').  Valid values: docx, all
    """
    if type in ['docx','all']:
        build_docx()

    puts("Finished building.")
   

def build_docx():
    """
    Build a docx document from input file
    """
    with msg("Building docx"):
        local('pandoc resume.md -o formats/resume.docx')




@contextmanager
def msg(txt):
    puts(txt + "...", end='', flush=True)
    with hide('everything'):
        yield
    puts("done.", show_prefix=False, flush=True)


