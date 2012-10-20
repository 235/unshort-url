from mako.template import Template
import cherrypy
import urllib
import mako

import os
TPATH = os.path.dirname(os.path.realpath(__file__)) +'/templates/'
#TPATH = '/var/www/virtual/9p.org.ua/htdocs/r/templates/'

URL = 'http://9p.org.ua/r/'

class Resolver:
    @cherrypy.expose
    def index(self, u=None):
        mako.runtime.UNDEFINED = ''
        if u:  # parameter with a URL to resolve
            try:
                resolve = urllib.urlopen(u)
                #newurl = unicode( urllib.unquote( resolve.geturl() ) )
                newurl = resolve.geturl()
                return Template(filename=TPATH + 'i.html', default_filters=['decode.utf8']).render(new=newurl, old=u, url=URL)
            except IOError:
                return Template(filename=TPATH + 'i.html').render(message="Sorry, cannot resolve it!", old=u, url=URL)
        else:
            return Template(filename=TPATH + 'i.html').render()


def setup_server():
    # Set up site-wide config. Do this first so that,
    # if something goes wrong, we get a log.
    cherrypy.config.update({'environment': 'production',
                            })
    #                        'log.screen': False,
    #                        'log.error_file': 'site.log',
    #                        'show_tracebacks': True})

    cherrypy.tree.mount(Resolver())

# For locall debug
if __name__ == '__main__':
   cherrypy.config.update({
                           #'server.socket_host': '151.236.4.7',
                           'server.socket_port': 8080,
                           'show_tracebacks': True
                         })
   cherrypy.quickstart(Resolver())
