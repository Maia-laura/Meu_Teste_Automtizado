import os
import time 
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options 
from datetime import datetime 
import allure



def before_all(context):
    edge_options = Options()
    service = EdgeService("C:\\drivers\\msedgedriver.exe")
    context.driver = webdriver.Edge(service=service, options=edge_options)
    context.driver.maximize_window()
    


def after_scenario(context, scenario):
    if scenario.status == "failed":
        screenshot_dir = os.path.join("reports", "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshot_dir, f"{scenario.name}_{timestamp}.png")

        context.driver.save_screenshot(screenshot_path)

        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name=f"Screenshot_{scenario.name}", attachment_type=allure.attachment_type.PNG)

    