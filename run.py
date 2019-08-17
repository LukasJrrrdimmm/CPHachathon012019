from azure.cognitiveservices.language.luis.authoring import LUISAuthoringClient
from msrest.authentication import CognitiveServicesCredentials

import datetime, json, os, time

key_var_name = '8cd51b2f9b594164ad87f4d8b88b6d3b'
if not key_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
authoring_key = os.environ[key_var_name]

region_var_name = 'westus'
if not region_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(region_var_name))
region = os.environ[region_var_name]
endpoint = "https://{}.api.cognitive.microsoft.com".format(region)