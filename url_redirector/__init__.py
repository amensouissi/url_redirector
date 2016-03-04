
from url_redirector.storage import RedirectionStorage


def add_storage_to_root(root, registery):
    root['urls_storage'] = RedirectionStorage()


def includeme(config):
    config.scan()
