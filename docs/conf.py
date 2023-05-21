# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from pathlib import Path

# parent = Path(__file__).parent
# parents_parent = Path(__file__).parents[1]

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys, os
sys.path.insert(0,os.path.abspath('/home/pi/DocumentationTest/test_folder/'))
sys.path.insert(0,os.path.abspath('/home/pi/DocumentationTest/'))

# sys.path.append(os.path.abspath('..'))
# sys.path.append(os.path.abspath('test_folder/'))

print (sys.path)

project = 'Documentation Test'
copyright = '2023, Shivam Kundan'
author = 'Shivam Kundan'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

# extensions = ['autoapi.extension']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# autoapi_dirs = ['../']

# autodoc_mock_imports = ["ROOT"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']