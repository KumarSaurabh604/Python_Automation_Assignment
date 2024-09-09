import pytest_html
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from pathlib import Path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ['call', 'setup'] and (report.failed or report.skipped):
        if not hasattr(report, 'wasxfail') or report.failed:
            screenshot_dir = Path("reports/htmlReport/screenshot")  # Use a path relative to the report
            screenshot_path = screenshot_dir / (report.nodeid.replace("::", "_") + ".png")
            browser = item.funcargs.get('browser')
            if browser:
                _capture_screenshot(browser, screenshot_path)
                # Use relative path in the HTML
                relative_path = screenshot_path.relative_to(screenshot_dir.parent)
                html = f'<div><img src="{relative_path}" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(item.config.pluginmanager.getplugin('html').extras.html(html))
    report.extra = extra


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = Path('reports/htmlReport')
    report_dir.mkdir(parents=True, exist_ok=True)
    config.option.htmlpath = report_dir / "report.html"
    config.option.self_contained_html = True


def _capture_screenshot(browser, screenshot_path):
    screenshot_path.parent.mkdir(parents=True, exist_ok=True)
    if browser.save_screenshot(str(screenshot_path)):
        print(f"Screenshot saved at {screenshot_path}")
    else:
        print("Failed to save screenshot")


def pytest_html_report_title(report):
    report.title = "Automation report"


# Set up the WebDriver session
@pytest.fixture(scope="session", autouse=True)
def browser():
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    # options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU rendering (not required but good for stability)
    options.add_argument("--window-size=1920x1080")  # Set a consistent window size

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()
