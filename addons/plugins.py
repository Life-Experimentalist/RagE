from fastapi import FastAPI

class PluginBase:
    def activate(self):
        raise NotImplementedError("Plugins must implement the activate method.")

class ExamplePlugin(PluginBase):
    def activate(self):
        print("Example plugin activated!")

plugins = [
    ExamplePlugin(),
]

def activate_plugins():
    for plugin in plugins:
        plugin.activate()