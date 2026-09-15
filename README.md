# Python Playwright E-commerce Testing Suite

End-to-end UI automation suite built with Python, Pytest, and Playwright.

The project tests key e-commerce workflows in
[Practice Software Testing](https://practicesoftwaretesting.com/) and demonstrates
modern browser-automation practices for a QA Automation portfolio.

## Project Status

Work in progress.

Current coverage:

- Homepage availability
- Product list visibility

Planned MVP coverage:

- Product search and empty results
- Category filtering
- Product sorting
- Product details
- Shopping cart operations
- Form validation
- Smoke and regression test selections

The initial scope is limited to approximately 12–16 stable end-to-end tests.

## Tech Stack

- Python 3.12
- Pytest
- Playwright
- pytest-playwright
- Page Object Model
- Ruff
- pytest-html
- GitHub Actions

## Current Project Structure

```text
python-playwright-ecommerce-testing/
├── pages/
│   ├── __init__.py
│   └── home_page.py
├── tests/
│   └── test_homepage.py
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Setup

Clone the repository:

```bash
git clone git@github.com:nahuelseoane/python-playwright-ecommerce-testing.git
cd python-playwright-ecommerce-testing
```

Create and activate a virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Install the Python dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Install Chromium for Playwright:

```bash
python -m playwright install chromium
```

## Running the Tests

Run the test suite in headless Chromium:

```bash
python -m pytest --browser chromium
```

Run it in headed mode:

```bash
python -m pytest --browser chromium --headed
```

Run smoke tests only:

```bash
python -m pytest -m smoke --browser chromium
```

## Code Quality

Check the project with Ruff:

```bash
python -m ruff check .
python -m ruff format --check .
```

Apply automatic formatting:

```bash
python -m ruff format .
```

## Testing Approach

The suite follows these principles:

- Page Object Model for reusable page interactions
- Playwright web-first assertions
- Automatic waiting instead of fixed delays
- Accessible locators where possible
- Independent and readable tests
- Small, controlled abstractions
- Smoke and regression test markers

## Author

Juan Nahuel Seoane

- [Portfolio](https://jnahuel.com)
- [GitHub](https://github.com/nahuelseoane)
- [LinkedIn](https://www.linkedin.com/in/nahuel-seoane/)
