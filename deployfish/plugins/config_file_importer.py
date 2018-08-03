from string import Template
import yaml

from deployfish.hooks import register_config_hook

@register_config_hook('file')
def load_external_yaml_config(*args, **kwargs):
    yaml_arg_str = args[0]
    yaml_args = yaml_arg_str.split("|")
    filebase = yaml_args[0]
    filename = "{}.yml".format(filebase)

    data = {}
    if len(yaml_args) > 1:
        data_str = yaml_args[1]
        data_list = data_str.split(",")
        for item in data_list:
            item_pieces = item.split(":")
            if len(item_pieces) == 2:
                data[item_pieces[0].strip()] = item_pieces[1].strip()

    with open(filename, 'r') as f:
        raw = f.read()
        t = Template(raw)
        contents = t.safe_substitute(data)
        return yaml.load(contents)
