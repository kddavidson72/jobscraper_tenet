import os


def get_spiders_list():
    # Convention: 'name' class attribute used for scrapy should match
    # the file name, minus the _spider string.
    files = ['{}'.format(name.replace('_spider.py', '')) for name in
             os.listdir('jobs/spiders') if name.endswith('py')
             and name not in ['__init__.py']]
    for k, v in enumerate(files):
        files[k] = '{}. {}'.format(k + 1, v)
    return '\n'.join(files)
