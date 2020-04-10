import hashlib
import os
import tempfile
from time import time

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse
from selenium import webdriver

from api.models import Screenshot


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

            screenshot, created = Screenshot.objects.get_or_create(name=img_name)

            if not created and screenshot.file:

                response = HttpResponse(content_type="image/png")
                response.write(screenshot.file.read())

                return response

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")

            driver = webdriver.Chrome("chromedriver", chrome_options=chrome_options)

            driver.get(url)

            driver.set_window_size(width, height)

            png = driver.get_screenshot_as_png()
            screenshot.file.save(name=img_name, content=ContentFile(png))
            screenshot.save()

            driver.quit()

            response = HttpResponse(content_type="image/png")
            response.write(png)

            return response

    return HttpResponse("needs ?url=<url> and optional &w=300&h=100")
