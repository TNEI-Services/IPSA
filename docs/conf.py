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
version = 'v2.10.3'
reference = 'RG003'

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

autodoc_member_order = 'bysource'

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_logo = 'ipsa_wo_small.png'#'ipsa_circle_glow_small.png'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for pdf output
latex_engine = 'xelatex'
latex_elements = {
     'papersize': 'a4paper',
     'fontpkg': '',
     'fncychap': '',
     'maketitle': '',
     'pointsize': '11',
     'preamble': '',
     'releasename': '',
     'babel': '',
     'printindex': '',
     'fontenc': '',
     'inputenc': '',
     'classoptions': ',docversion='+version+',docreference='+reference,
     'utf8extra': '',
     'sphinxsetup': 'VerbatimColor={white},TableRowColorHeader={HTML}{e3b5c7},TableRowColorOdd={white},'
                    'TableRowColorEven={HTML}{e6e0eb}'
}
latex_docclass = {
   'howto': 'ipsa_2103',
   'manual': 'ipsa_2103',
}
latex_additional_files = ["_static/latex/ipsa_2103.cls", "_static/latex/Noto_Sans/NotoSans-Bold.ttf",
                          "_static/latex/Noto_Sans/NotoSans-BoldItalic.ttf",
                          "_static/latex/Noto_Sans/NotoSans-Italic.ttf",
                          "_static/latex/Noto_Sans/NotoSans-Regular.ttf",
                          "_static/latex/IpsaBigLogo.png",
                          "_static/latex/ipsalogo_dimmed.pdf"]


autosummary_generate = True
