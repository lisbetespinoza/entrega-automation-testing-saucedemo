from selenium import webdriver

def before_scenario(context,scenario):
    context.driver = webdriver.chrome()
    
def after_scenario(context,scenario):
    context.driver.quit()