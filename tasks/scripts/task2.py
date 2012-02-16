from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

# Henter filstien til URL-filen fra testkonfigurasjonen
url_file_path = grinder.getProperties().getProperty('task2.urls')

class TestRunner:
    
    def __init__(self):
        pass # Lag tester for hver av URL-ene
    
    def __call__(self):
        pass # Gjør en GET request mot hver URL
