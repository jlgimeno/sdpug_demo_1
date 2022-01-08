import importlib
import pathlib


directories = [
    'about',
    'application',
    'page_objects',
]

BASE_DIR = pathlib.Path("./company")
results = 0

for directory in directories:
    folder = pathlib.Path(f"{BASE_DIR}/{directory}")
    for module in folder.iterdir():
        if module.stem.startswith("test_"):
            clsname = module.stem.title()
            clsname.replace("_", "")
            cls = getattr(importlib.import_module(f"company.{directory}.{module.stem}"), clsname.replace("_", ""))
            for attribute in dir(cls):
                if attribute.startswith("tc_"):
                    results += 1

print(f"Total number of test cases:  {results}")
