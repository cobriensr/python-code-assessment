# Beam Technical Assessment

## Technical Decision Making

In designing this solution, several technical decisions were made at various levels to ensure an efficient, maintainable, and high-quality codebase. The key considerations and trade-offs are outlined below:

### Technology Stack

* **Language**: Python was chosen as the primary language for this project due to its strong support for data manipulation, CSV parsing, and light ETL (Extract, Transform, Load) tasks. Python's simplicity, extensive ecosystem, and wide adoption make it an ideal choice for this type of work.

### Libraries

* **pandas**: The pandas library was selected for CSV file parsing, data cleaning, and data transformation. Pandas provides a powerful and intuitive interface for working with structured data, making it easy to load, manipulate, and analyze CSV files. While other options like the built-in `csv` module were also used, overall pandas offers a more feature-rich and efficient solution.

* **pytest**, **pytest-cov**, **pytest-html**: For testing and generating coverage reports, the pytest framework was chosen along with the pytest-cov and pytest-html plugins. Pytest provides a simple and flexible testing framework that integrates well with other tools. The pytest-cov plugin enables generating coverage reports to ensure comprehensive test coverage, while pytest-html allows generating HTML test reports for better visualization and reporting.

* **mypy**: To enhance code quality and catch potential type-related issues early, mypy was used for static type checking. By annotating function signatures and variables with type hints, mypy can perform static analysis and identify type inconsistencies. This helps improve code reliability and maintainability.

* **black**: Black was selected as the code formatter to enforce a consistent code style throughout the project. It eliminates the need for manual formatting decisions and ensures that the codebase adheres to a standardized style, improving readability and collaboration.

* **pylint** and **sonarlint**: For code linting and static code analysis, pylint and sonarlint were employed. These tools help identify potential issues, code smells, and style violations, promoting code quality and maintainability. They provide valuable insights and suggestions for improving the codebase.

### Design Decisions

* **CSV Data File Placement**: The decision was made to keep the CSV data file in the project's root directory for simplicity and ease of access. This allows the file to be easily imported and used across different parts of the application. While alternative approaches like storing the file in a separate data directory were considered, the current placement strikes a balance between simplicity and organization.

* **Package Management**: Poetry was chosen as the package management and dependency resolution tool. Poetry simplifies the process of managing project dependencies, creating virtual environments, and building distributions. It provides a declarative approach to specifying dependencies and ensures reproducible builds across different environments.

These technical decisions were made considering factors such as ease of use, maintainability, code quality, and alignment with the project's requirements. The combination of Python, pandas, pytest, mypy, black, pylint, and sonarlint enables efficient development, comprehensive testing, and high code quality. The design choices, such as keeping the CSV data file in the root directory and using Poetry for package management, contribute to a straightforward and organized project structure.

## Running your code

We have purposefully not written instructions on how we will run both your main program or your test suite.
This is to give you a chance to show us how you would structure a project like this.
Because of this, we ask that you include detailed instructions on how to both run your code and its test suite, and preferably which directory to run them from.

## Installation

**** Please download the csv data file from [this](https://docs.google.com/spreadsheets/u/1/d/1CAQJlbQBrIrKYCCNQFMeIG2u8BAuDjHfIje_07zDqvQ/edit?usp=sharing) google sheet and save it in the project root as ```car_sales_dataset.csv```*****

1. Make sure you have Poetry installed.
   1. Poetry should always be installed in a dedicated virtual environment to isolate it from the rest of your system. It should in no case be installed in the environment of the project that is to be managed by Poetry. This ensures that Poetry’s own dependencies will not be accidentally upgraded or uninstalled. (Each of the following installation methods ensures that Poetry is installed into an isolated environment.) In addition, the isolated virtual environment in which poetry is installed should not be activated for running poetry commands
2. Install pipx
   1. If pipx is not already installed, you can follow any of the options in the [official pipx installation instructions](https://pipx.pypa.io/stable/installation/). Any non-ancient version of pipx will do.
3. ```pipx install poetry```
   1. For detailed installation instructions, refer to the [Poetry Documentation](https://python-poetry.org/docs/#installation)
4. Clone this repository to your local machine:
   1. ```https://github.com/cobriensr/car-sales-code-kata```
   2. Navigate to the project directory:
      1. ```cd python_kata_main```
   3. Install the project dependencies using Poetry:
      1. ```poetry install```

## Usage

1. Activate the virtual environment created by Poetry:
   1. ```poetry shell```
2. Run the Python files:
   1. ```poetry run python avg_med_prices.py```
   2. ```poetry run python porsche_sales.py```
   3. ```poetry run python top_10_sales_ratio.py```

## Running Tests

This project uses [pytest](https://docs.pytest.org/) for testing. To run the tests, follow these steps:

1. Make sure you have activated the virtual environment:
   1. ```poetry shell```
2. Run the tests using the `python -m pytest` command
3. This will discover and run all the test files in your project directory and its subdirectories.
4. If you want to run tests with coverage, you can use the `--cov` option:
   1. ```python -m pytest --cov=your_package_name```
5. Replace `your_package_name` with the name of your Python package or module that you want to measure coverage for.
6. To generate a coverage report, you can add the `--cov-report` option:
   1. ```python -m pytest --cov=your_package_name --cov-report=html --self-contained-html test_file.py```
      1. Replace ```test_file.py``` with the name of the particular test file to run and make sure that the ```--cov=your_package_name``` matches the module of the file you are trying to test
7. This will generate an HTML coverage report in the `htmlcov` directory.

## Test Directory Structure

The tests for this project are located in the `tests` directory. The directory structure follows the standard convention:

* tests/
* test_module1.py
* test_module2.py

Each test file should be named `test_*.py` to be automatically discovered by pytest.
