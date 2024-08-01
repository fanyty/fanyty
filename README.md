# Web Automation Framework

This is a web automation testing framework using Selenium and Pytest.

## Project Structure
web_automation_framework/

├── config/

│ ├── init.py

│ ├── config.py

│ └── logger.py

├── tests/

│ ├── init.py

│ └── test_group.py

├── pages/

│ ├── init.py

│ ├── login_page.py

│ ├── group_page.py

│ └── base_page.py

├── utils/

│ └── init.py

├── reports/

│ └── init.py

├── requirements.txt

├── conftest.py

├── pytest.ini

└── README.md


## Setup

### Prerequisites

- Python 3.12
- pip (Python package installer)
- Chrome browser
- ChromeDriver (ensure the version matches your Chrome browser version)

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/fanyty/fanyty/web_automation_framework.git
    cd web_automation_framework
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Download ChromeDriver**:

    - Download the ChromeDriver from [ChromeDriver Download](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Place the `chromedriver.exe` in the `web_automation_framework` directory.

## Running Tests

To run the tests and generate an HTML report:

```sh
pytest tests/test_group.py --html=reports/test_report.html

he HTML report will be generated in the reports directory.

Configuration
config/config.py
Update the configuration settings as per your requirements:
class Config:
    BASE_URL = "https://example.com"
    USERNAME = "test_user"
    PASSWORD = "test_password"
    TIMEOUT = 10
Logging
Logging is configured in config/logger.py:
import logging

def setup_logger():
    logger = logging.getLogger("web_automation")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

logger = setup_logger()
Directory Structure
config: Contains configuration files and logger setup.
tests: Contains test cases.
pages: Contains page object models.
utils: Contains utility functions (if any).
reports: Contains test reports.
conftest.py: Contains pytest fixtures.
Contributing
Contributions are welcome! Please fork the repository and create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.


