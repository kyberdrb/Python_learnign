# import required modules
# If you want to add another module, go to File -> Settings -> Project Interpreter -> click the little 'plus' button
import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"                  # convert 'name' to string with function 'str()'
    urllib.request.urlretrieve(url, full_name)      # download a image and save it in the project folder under random name

download_web_image("https://balau82.files.wordpress.com/2015/06/img_20150614_120234536.jpg")