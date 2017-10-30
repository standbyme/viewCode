import os
from Html2PDF import Html2PDF

for root, dirs, files in os.walk('./code'):
    for file in files:
        print(file)
        os.system(
            'pygmentize -f html -O full -o ./html/{file}.html ./code/{file}'.format(file=file))
        Html2PDF('./html/{file}.html'.format(file=file),'./pdf/{file}.pdf'.format(file=file))
