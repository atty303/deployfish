from operator import itemgetter

_config_hooks = {}

def register_config_hook(config_identifier, fn=None):

    if fn is None:
        def decorator(fn):
            register_config_hook(config_identifier, fn)
            return fn
        return decorator

    _config_hooks[config_identifier] = fn

def get_config_hook(config_identifier):
    if config_identifier in _config_hooks:
        return _config_hooks[config_identifier]

    return None
