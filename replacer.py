from importlib import import_module


def replace(func):
    def replacement():
        return "replaced"

    module = import_module(func.__module__)
    setattr(module, func.__name__, replacement)
