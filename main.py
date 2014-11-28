import webapp2

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        #self.response.header['Content-Type'] = 'text/plain'
        #self.response.out.write('Hello, webapp2 World!')
        self.response.write("Hello, world!")
        
app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)
