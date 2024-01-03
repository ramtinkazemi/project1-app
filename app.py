
import os
import requests
import datetime
from flask import Flask, render_template

app = Flask(__name__)
default_image_url = "https://sbs-test-project-static-resources.s3.amazonaws.com/sbs-world-cup.jpeg"

@app.route('/')
def home():
    # Get the public IP of the server
    ip = requests.get('https://api.ipify.org').text
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Read the S3 URL from an environment variable with a default value
    image_url = os.getenv('IMAGE_URL', default_image_url)
    return render_template('index.html', image_url=image_url, ip=ip, date=date)

if __name__ == '__main__':
    app.run()
