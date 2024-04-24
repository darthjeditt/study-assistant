import types
import importlib
import os

# TODO CHANGE TO OS ENVIRON VAR


def reloadModules(modules: list[types.ModuleType | str]):

    for mod in modules:
        if isinstance(mod, str):
            print(f"Importing module {mod}")
            mod = importlib.import_module(mod)
        print(f"Reloading module {mod.__name__}")
        mod = importlib.reload(mod)
