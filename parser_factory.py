import importlib

def get_parser(channel_id):
    try:
        module_name = f"parsers.{channel_id}"
        parser_module = importlib.import_module(module_name)
        return parser_module.simplify_message
    except ModuleNotFoundError:
        return None