"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_scrap.ipynb.

# %% auto 0
__all__ = ['DEBUG', 'BROWSERS', 'get_brow', 'get_href']

# %% ../nbs/01_scrap.ipynb 2
import asyncio
from playwright.async_api import async_playwright, Page, Playwright
import traceback
from .core import *

# %% ../nbs/01_scrap.ipynb 3
DEBUG = True
BROWSERS = {
    "ch": lambda pw: pw.chromium,
    "ff": lambda pw: pw.firefox,
    "wk": lambda pw: pw.webkit,
}

async def get_brow(pw: Playwright, brow_n: str):
    """
    return browser_name object from 
    ch -> chromium
    ff -> firefox
    wk -> webkit
    """
    browser_func = BROWSERS.get(brow_n)
    if not browser_func:
        raise ValueError(f"Unknown browser: {brow_n}")
    return await browser_func(pw).launch(headless=DEBUG==False)

# %% ../nbs/01_scrap.ipynb 5
async def get_href(page:Page):
    """
    Takes in Page object and get back all the href which are not part of `ignore_href`.\n
    It is doen by loop through all the a tags.
    """
    try:
        links = [await tag.get_attribute('href')  for tag in await page.query_selector_all('a')]
        return [ link for link in links if valid_href(link) ]
    except Exception as e:
        print(f"failed for {await page.url}")
        traceback.print_exc()
        raise e
