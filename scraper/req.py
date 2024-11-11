"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_req.ipynb.

# %% auto 0
__all__ = ['h2t', 'cleaner']

# %% ../nbs/02_req.ipynb 2
import requests
from pathlib import Path
from html2text import HTML2Text  
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import traceback
from .core import *
from lxml.html import fromstring, HtmlElement, tostring
from lxml_html_clean import Cleaner

h2t = HTML2Text(bodywidth=1000_000)
h2t.ignore_links = True
h2t.mark_code = True
h2t.ignore_images = True
cleaner = Cleaner(javascript=True, style=True)