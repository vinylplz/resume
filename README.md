# resume
Greg Forties latest resume: [here][latest resume]


# Overview
This repo serves as a place to get a copy of my [latest resume] in multiple formats, as well as an example of how to automate any task using [fabric] and [travis-ci].  It relies on the [pandoc] command line utility for doing the actual document conversion from [markdown](./greg_forties_resume.md) to various other formats.

# Workflow
The basic workflow looks like this:

1. edit the main [markdown] file
2. convert it to various formats with `fab build`
3. check the converted files in build/ to make sure they are what you want
4. commit your changes back to github (.gitignore excludes build/ artifacts)  
  * triggers an [automated travis build](https://travis-ci.org/vinylplz/resume)
5. if everything still looks good, tag your commit and `push --tags` to github  
  * triggers another travis build AND creates a [release][latest resume] on githib using the [travis github release provider](http://docs.travis-ci.com/user/deployment/releases/)
6. enjoy not having to edit dozens of files

# See Also
**Fabric**  
[Homepage][fabric] - fabric's homepage  
[Installation Instructions](http://www.fabfile.org/installing.html) - use pip  
[API Docs](http://docs.fabfile.org/en/latest/) - Super useful   
[Fabric's own Fabfile](https://github.com/fabric/fabric/tree/master/fabfile)  
[fabfile/](./fabfile/) - this projects fabfile.  

**Travis**  
[Homepage][travis-ci]  
[Docs](http://docs.travis-ci.com/)  
[.travis.yml](./.travis.yml) - this project's travis configuration file

**Pandoc**  
[Homepage][pandoc]  
[Installation Instructions](http://johnmacfarlane.net/pandoc/installing.html)    
[Github](https://github.com/jgm/pandoc) - the README.md is especially useful if you're doing something complex  

**Markdown**  
[Adam P's Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)  
[https://stackedit.io/](https://stackedit.io/) - useful in-browser markdown editor with visual feedback.  great if you're just getting started with markdown.


[fabric]: http://www.fabfile.org/
[pandoc]: http://johnmacfarlane.net/pandoc/
[travis-ci]: https://travis-ci.org/
[latest resume]: https://github.com/vinylplz/resume/releases/latest
[markdown]: ./greg_forties_resume.md
