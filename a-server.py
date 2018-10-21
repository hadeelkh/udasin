#!/usr/bin/env python3
#
# Udacian activity to practice get and post http
#

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

memory = []
form = '''<!DOCTYPE html>
  <title>Udacian</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="name">name</textarea>
    <br>
    <textarea name="city">city</textarea>
    <br>
    <textarea name="enrollment">enrollment</textarea>
    <br>
    <textarea name="nanodegree">nanodegree</textarea>
    <br>
    <textarea name="status">status</textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):

      length = int(self.headers.get('Content-length', 0))
      data = self.rfile.read(length).decode()
      message = parse_qs(data)
      item=''

      for x in message:

        x = message[x][0]
        # Escape HTML tags in the message so users can't break world+dog.
        x = x.replace("<", "&lt;")

        item+= x+','

      # Store it in memory.
      memory.append(item)
  
      

      self.send_response(303)  # redirect via GET
      self.send_header('Location', '/')
      self.end_headers()

      
      
      



    def do_GET(self):

      self.send_response(200)

        # Then send headers.
      self.send_header('Content-type', 'text/html; charset=utf-8')
      self.end_headers()

      #join 
      mesg = form.format("\n".join(memory))
      self.wfile.write(mesg.encode())



if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()