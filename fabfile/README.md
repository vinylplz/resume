`fabric` is a command line tool for running scripts (usually) against remote hosts, using python.  you can also abuse it to run local commands as logical *tasks*, which is what I'm doing here.

To convert the resume.md file to a docx, for instance, you can call fabric like this:

```bash
$ fab build:docx
Building docx...done.
Finished building.

Done.
$
```

fabric homepage: [http://fabfile.org] 
fabric docs:     [http://docs.fabfile.org/en/1.10/]

You will also need `pandoc` installed.  Pandoc is a document conversion utility.
pandoc homepage: [http://johnmacfarlane.net/pandoc/]


