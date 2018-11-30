
```
from selenium import webdriver

from selenium.webdriver import Remote



driver = Remote(command_executor='http://10.16.89.183:31353/wd/hub',
                desired_capabilities={
                      "browserName": "chrome",
                })
driver.get("https://baidu.com")
driver.quit()
```
