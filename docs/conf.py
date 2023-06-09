# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys, os
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../sensor_pages/'))

sys.path.append(os.path.abspath('../assets/'))
sys.path.append(os.path.abspath('../resources/'))
sys.path.append(os.path.abspath('../general_pages/'))
sys.path.append(os.path.abspath('../freqshow_code/'))

project = 'Tricorder-Rpi'
copyright = '2023, Shivam Kundan'
author = 'Shivam Kundan'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
