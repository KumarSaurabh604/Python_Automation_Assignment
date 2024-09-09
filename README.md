# Automation Testing Framework

This repository contains both **UI** and **API** automated tests using `pytest`. Below are instructions on how to set up the environment, run the tests, and view reports.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
  - [Running UI Tests](#running-ui-tests)
  - [Running API Tests](#running-api-tests)


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
    pip install selenium
    pip install pytest==8.3.2 pluggy==1.5.0 allure-pytest==2.13.5 pytest-bdd==7.2.0 pytest-html==4.1.1 pytest-html-reporter==0.2.9 pytest-metadata==3.1.1
    ```

## Running the Tests

### Running UI Tests

1. **Run all UI tests**:
    ```bash
    pytest  bddpytest\stepDef\stepDefinition.py
    ```

2. **Run UI tests in headless mode**:
    ```bash
    pytest uibddpytest/stepDef/stepDefinition.py --headless
    ```

### Running API Tests

1. **Run all API tests**:
    ```bash
    pytest  trello_api_framework/tests
    ```

2. **Run a specific API test**:
    ```bash
    pytest  trello_api_framework/tests/test_update_card.py
    ```
