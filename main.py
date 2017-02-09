import webapp2
import jinja2
import os
import re

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


form="""
<!DOCTYPE html>
<html>
<form method="post">
<div>
    <label for="username">Username</label>
    <input type="text name="username" value='%(username)s' pattern="[a-zA-Z0-9_-]{3,20}$" required>
</div>
    <br>
<div>
    <label for="password">Password</label>
    <input type="password" name="password" pattern=".{3,20}$" required>
    <span style="color:red">%(password)s</span>
</div>
    <br>
<div>
    <label for="verify">Verify Password</label>
    <input type="password" name="verify" patterm = ".{3,20}$" required>
</div>
    <br>
<div>
    <label for="email">Email(optional)</label>
    <input type="text" name="email" value='%(email)s' pattern="[\S]+@[\S]+\.[\S]+$">
</div>
    <input type="button" onclick="location.href='welcome.html';" value="submit" />
</div>
</form>
</html>
"""
def password_verify(password, verify):
    if password == verify:
        return True

class MainPage(webapp2.RequestHandler):
    def writeform(self, username="", password="", email=""):
        value = {
        "username": username,
        "password": password,
        "email": email
        }
        self.response.write(form % value)

    def get(self):
        self.writeform()

    def post(self):
        user_name = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        passwords= password_verify(password, verify)

        if not passwords:
            self.writeform(user_name, "Passwords do not match!", email)
        else:
            self.writeform()


app = webapp2.WSGIApplication([('/', MainPage)],
                               debug=True)
