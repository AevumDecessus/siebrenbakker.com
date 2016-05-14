from flask import Flask, render_template_string, request
from flask_flatpages import FlatPages
from flask_flatpages.utils import pygmented_markdown
from flask.ext.images import Images

def jinja_renderer(text):
  prerendered_body = render_template_string(text)
  return pygmented_markdown(prerendered_body)

app = Flask(__name__)

# Default Values for config
app.config['SECTION_MAX_LINKS'] = 10
app.config['FLATPAGES_HTML_RENDERE'] = jinja_renderer
app.config.from_object('config')
pages = FlatPages(app)
images = Images(app)

from fragforce.views import pages

app.register_blueprint(pages.mod)
