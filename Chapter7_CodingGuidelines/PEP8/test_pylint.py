# pylint test_pylint.py --output-format colorized -j 4
# pylint --generate-rcfile > TARGET_PATH .pylintrc
# Also pylint can be enabled in VS Code (is default)
from __future__ import print_function
import logging

class Command(ScrapyCommand):
    @property
    def max_evel(self): 
        levels  = self.items.keys() + self.requests.keys()
        if levels: return max(levels)
        else: return 0
        
    def add_items(self, lvl, new_items):
        old_items = self.items.get(lvl, [])
        self.items[lvl] = old_items + new_items