import os
import sys
sys.path.insert(0, os.path.abspath('../'))
#import src
# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'PyIPSA'
copyright = 'IPSA'
author = 'IPSA'

release = '1.0'
version = 'v2.10.0'

html_css_files = ['css/custom.css']
# -- General configuration

master_doc = 'index'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.inheritance_diagram',
]

def setup(app):
   app.add_css_file('css/custom.css')

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

source_suffix = '.rst'

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_logo = 'ipsa_wo_small.png'#'ipsa_circle_glow_small.png'

# -- Options for EPUB output
epub_show_urls = 'footnote'

autosummary_generate = True
