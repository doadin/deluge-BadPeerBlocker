from deluge.plugins.init import PluginInitBase

class CorePlugin(PluginInitBase):
    def __init__(self, plugin_name):
        from .core import Core
        self.plugin = Core(plugin_name)