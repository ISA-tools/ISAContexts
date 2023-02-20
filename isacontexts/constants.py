from os import path

HERE_PATH = path.abspath(path.dirname(__file__))
VOCAB_PATH = path.join(HERE_PATH, '..', 'contexts')
SCHEMAS_PATH = path.join(HERE_PATH, 'resources', 'schemas')

JSON_REPORT_PATH = path.join(HERE_PATH, 'resources', 'report.json')
HTML_REPORT_PATH = path.join(HERE_PATH, '..',  'dist')
