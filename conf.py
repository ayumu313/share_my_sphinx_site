# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ayumu Kitagawa'
copyright = '2024, Ayumu Kitagawa'
author = 'Ayumu Kitagawa'
release = '2024.04.15'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


# The name of the HTML file that is the homepage of the docs
html_title = "Ayumu Kitagawa"


# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
# html_theme = 'furo'



html_css_files = [
    'custom.css',
]
html_static_path = ['_static']




#---------
from docutils.parsers.rst import roles
from docutils import nodes

def nolink_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    return [nodes.Text(text)], []

roles.register_local_role('nolink', nolink_role)


