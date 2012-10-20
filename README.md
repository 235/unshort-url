unshort-url
===========

Resolve shortened links to full URLs with a bookmarklet. Demo online: [http://9p.org.ua/r](http://9p.org.ua/r). 

![Screenshot of the demo](https://raw.github.com/235/unshort-url/master/screenshot.png)

Developed using Python and **[CherryPy](http://www.cherrypy.org) web framework** with **[Mako templates](http://www.makotemplates.org/)**.

Also, it has a **bookmarklet** which replaces all short links on an active page, and it that can be dragged into you toolbar for later use.

This tiny project I developed back in Dec 2008 when some people got [tinyulr.com](http://tinyurl.com/) blocked. It resolves any shortened URL into a full one on a server-side, so escaping any filtration or censorship. 

## Installation

1. Clone this repository

2. Initialise [`virtualenv`](http://pypi.python.org/pypi/virtualenv) and enter it

2. Install required modules `pip install -r require.txt Run `bootstrap_venv.sh` to initialise a virtual environment

3. Configure your local settings in `unshort.py`

4. Run locally `python unshort.py` and  and browse to [`http://localhost:8080`](http://localhost:8080)

5. Write a server config using example in `.htaccess` or read CherryPy [Deployment Guide](http://docs.cherrypy.org/stable/deployguide/index.html)

