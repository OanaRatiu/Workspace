#!/usr/bin/env python

DATA = {
   'FrontPage': 'Bine ai venit pe aceasta aplicatie web miraculoasa care contine si un SecretPage!',
   'SecretPage': 'Aici e pagina secreta!'
}


from wsgiref.simple_server import make_server
from cgi import parse_qs
import Cookie
import re

from templates import render_edit_page, render_view_page


linkify = re.compile('([A-Z][a-z]*){2,}')


def get_content(page_name):
   return DATA.get(page_name, '')


def set_content(page_name, page_content):
   DATA[page_name] = page_content


def front_page(environ, start_response):
   start_response('302 FOUND', [
      ('Content-Type', 'text/html'),
      ('Content-Length', '0'),
      ('Location', '/FrontPage/')
   ])
   return []


def view_page(environ, start_response, page_name):
   page_content = get_content(page_name)
   cookie = limits(environ)
   if not page_content:
      start_response('302 FOUND', [
         ('Set-Cookie', cookie.OutputString()),
         ('Content-Type', 'text/html'),
         ('Content-Length', '0'),
         ('Location', '/edit/%s/' % page_name)
      ])
      return []

   
   start_response('200 OK', [
      ('Set-Cookie', cookie.OutputString()),
      ('Content-Type', 'text/html')
   ])
   return [render_view_page(page_name, linkify.sub('<a href="/\g<0>/">\g<0></a>', page_content), cookie)]


def edit_page(environ, start_response, page_name):
   cookie = limits(environ)
   start_response('200 OK', [
      ('Content-Type', 'text/html')
   ])
   return [render_edit_page(page_name, get_content(page_name))]


def save_page(environ, start_response, page_name):
   body = environ['wsgi.input'].read(int(environ['CONTENT_LENGTH']))
   parsed_body = parse_qs(body)
   set_content(page_name, ''.join(parsed_body['content']))
   start_response('302 FOUND', [
      ('Content-Type', 'text/html'),
      ('Content-Length', '0'),
      ('Location', '/%s/' % page_name)
   ])
   return []


def application(environ, start_response):

   path_info = environ['PATH_INFO']

   print path_info
   if path_info.rstrip('/') == '':
      return front_page(environ, start_response)

   is_edit = path_info.startswith('/edit/')
   is_save = path_info.startswith('/save/')

   page_name = path_info.strip('/')      
   if is_edit or is_save:
      _, page_name = path_info.strip('/').split('/', 1)

   error_response = check_page_name(page_name, start_response)
   if error_response is not None:
      return error_response

   if is_edit:
      return edit_page(environ, start_response, page_name)
   elif is_save:
      return save_page(environ, start_response, page_name)
   return view_page(environ, start_response, page_name)


def check_page_name(page_name, start_response):
   if '/' in page_name:
      start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
      return ['The page is not here.']






def limits(environ):
    if 'HTTP_COOKIE' in environ:
        cookies = environ.get('HTTP_COOKIE')
        cookies = cookies.split('; ')
        handler = {}
        for cookie in cookies:
            cookie = cookie.split('=')
            handler[cookie[0]] = cookie[1]

        if 'count' in handler:
            number = int(handler['count'])
            cookie = Cookie.SimpleCookie()
            cookie['count'] = number + 1
            cookie['count']['expires'] = 86400
            return cookie['count']
    else:
        c = Cookie.SimpleCookie('count=1')
        return  c['count']




httpd = make_server('localhost', 8052, application)
httpd.serve_forever()
