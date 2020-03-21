import os

for item in os.listdir():
    print('<link rel="stylesheet" href="{}">'.format(item))
