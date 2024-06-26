import pytest
import selenium.webdriver


@pytest.fixture
def browser():
    #Initialize the ChromeDriver instance
    b = selenium.webdriver.Chrome()

    #Make its calls wait up to 20 scds for elements to appear
    b.implicitly_wait(20)

    #Return the WebDriver instance  for the setup
    yield b

    #Quit the WebDriver instance for the cleanup
    b.quit()
