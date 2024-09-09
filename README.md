# Automation Testing Framework

This repository contains both **UI** and **API** automated tests using `pytest`. Below are instructions on how to set up the environment, run the tests, and view reports.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
  - [Running UI Tests](#running-ui-tests)
  - [Running API Tests](#running-api-tests)
- [Generating Reports](#generating-reports)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- `pip` (Python package manager)
- ChromeDriver (for UI testing with Selenium)
- Git

### Browser Setup for UI Tests

Ensure you have a compatible version of **ChromeDriver** installed and accessible via your system's `PATH`.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your_username/your_repo.git
    cd your_repo
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    # Activate the virtual environment
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate     # For Windows
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Tests

### Running UI Tests

1. **Run all UI tests**:
    ```bash
    pytest tests/ui --alluredir=reports/allure-results
    ```

2. **Run a specific UI test**:
    ```bash
    pytest tests/ui/test_login.py --alluredir=reports/allure-results
    ```

3. **Run UI tests in headless mode**:
    ```bash
    pytest tests/ui --headless --alluredir=reports/allure-results
    ```

### Running API Tests

1. **Run all API tests**:
    ```bash
    pytest tests/api --alluredir=reports/allure-results
    ```

2. **Run a specific API test**:
    ```bash
    pytest tests/api/test_create_card.py --alluredir=reports/allure-results
    ```

## Generating Reports

### Allure Reports

To generate **Allure** reports after running the tests:

1. **Install Allure** (if not already installed):
    - For macOS:
      ```bash
      brew install allure
      ```
    - For Windows, download and install from the [Allure official website](https://docs.qameta.io/allure/).

2. **Generate the report**:
    ```bash
    allure serve reports/allure-results
    ```

### HTML Reports (Optional)

If you prefer HTML reports, you can generate them as follows:

1. Add the `pytest-html` plugin in your `requirements.txt`:
    ```
    pytest-html
    ```

2. **Run the tests with HTML report generation**:
    ```bash
    pytest --html=reports/test_report.html
    ```

3. View the report in your browser by opening the `test_report.html` file.

