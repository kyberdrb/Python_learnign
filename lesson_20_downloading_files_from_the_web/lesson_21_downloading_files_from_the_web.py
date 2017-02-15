from urllib import request      # this is the same as "import urllib.request"

goog_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=0&b=15&c=2017&d=1&e=15&f=2017&g=d&ignore=.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)      # convert the entire response to a string, which will make life easier later on
    lines = csv_str.split('\\n')    # splits a long csv one-line string into lines
    dest_url = r'goog.csv'

    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + '\n')

    fx.close()

download_stock_data(goog_url)