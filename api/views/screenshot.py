import hashlib
import os
import tempfile
import urllib.parse as urlparse
from datetime import datetime
from time import time

from django.conf import settings
from django.http import HttpResponse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_screenshot(request):
    """
    Take a screenshot and return a png file based on the url.
    """
    width = 1024
    height = 768
    h = hashlib.new("ripemd160")

    if request.method == "GET" and "url" in request.GET:
        url = request.GET.get("url", "")
        width = request.GET.get("w", width)
        height = request.GET.get("h", height)

        if url is not None and url != "":

            h.update(url.encode("utf-8"))
            h.update(str(width).encode("utf-8"))
            h.update(str(height).encode("utf-8"))

            img_name = h.hexdigest() + ".png"
            img_dir = tempfile.gettempdir() + "/screenshots"

            full_img_path = os.path.join(img_dir, img_name)

            if not os.path.exists(img_dir):
                os.makedirs(img_dir)

            [
                os.remove(file)
                for file in (
                    os.path.join(path, file)
                    for path, _, files in os.walk(img_dir)
                    for file in files
                )
                if os.stat(file).st_mtime < time() - (60 * 60)
            ]

            if os.path.isfile(full_img_path):
                response = HttpResponse(content_type="image/png")

                with open(full_img_path, mode="rb") as file:
                    response.write(file.read())

                return response

            else:
                driver = webdriver.Chrome(ChromeDriverManager().install(),)
                driver.get(url)

                driver.set_window_size(width, height)

                screenshot_img = driver.get_screenshot_as_png()
                driver.save_screenshot(full_img_path)

                driver.quit()

                response = HttpResponse(content_type="image/png")
                response.write(screenshot_img)

                return response

    return HttpResponse("needs ?url=<url> and optional &w=300&h=100")
