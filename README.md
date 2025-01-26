# drf-app

[![CI](https://github.com/youzarsiph/drf-app/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/drf-app/actions/workflows/ci.yml)
[![CD](https://github.com/youzarsiph/drf-app/actions/workflows/cd.yml/badge.svg)](https://github.com/youzarsiph/drf-app/actions/workflows/cd.yml)
[![Code Style: Black](https://github.com/youzarsiph/drf-app/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/drf-app/actions/workflows/black.yml)
[![Code Linting: Ruff](https://github.com/youzarsiph/drf-app/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/drf-app/actions/workflows/ruff.yml)
[![Code Testing](https://github.com/youzarsiph/drf-app/actions/workflows/tests.yml/badge.svg)](https://github.com/youzarsiph/drf-app/actions/workflows/tests.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/drf-app?logo=pypi&logoColor=white)](https://pypi.org/project/drf-app/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/drf-app?logo=python&logoColor=white)](https://pypi.org/project/drf-app/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/drf-app?logo=pypi&logoColor=white)](https://pypi.org/project/drf-app/)
[![PyPI - License](https://img.shields.io/pypi/l/drf-app?logo=pypi&logoColor=white)](https://pypi.org/project/drf-app/)

## Overview

This repository serves as a comprehensive Python application template designed to facilitate robust development practices. Leveraging modern tools and methodologies, this template is tailored for developers aiming to build maintainable, scalable applications. It emphasizes dependency management, code quality, and seamless integration with DevOps pipelines.

## Key Features

- **CI/CD Pipelines**: Automated using GitHub Actions to ensure consistent and reliable deployment processes.
- **Dependency Management**: Powered by Poetry, a sophisticated tool for managing project dependencies with precision and reliability.
- **Code Formatting**: Automatically formatted with Black to maintain a consistent and readable codebase.
- **Code Linting**: Utilizes Ruff to identify and address potential issues early, enhancing code quality and maintainability.
- **Code Testing**: Utilizes Django to run tests.
- **Configuration Files**: Includes `.gitignore`, `pyproject.toml`, and other essential configuration files to streamline setup.

## Quick Start Guide

To initiate a new project using this template, follow these steps:

1. **Create a Repository from Template**:
   - Navigate to the repository on GitHub.
   - Click on the `Use this template` button.
   - Customize the new repository with your project details.

2. **Clone Your New Repository**:

   ```bash
   git clone https://github.com/your-username/your-new-project.git
   cd your-new-project
   ```

3. **Set Up the Environment**:
   - Install Poetry if not already installed:

     ```bash
     pip install poetry
     ```

   - Install the project dependencies:

     ```bash
     poetry install
     ```

4. **Create a new Django project**:

   ```bash
   poetry run python -m django startproject core
   mv core/* .
   ```

5. **Configure the app**:

   Open `core/settings.py`:

   ```python
   # Add the following line
   AUTH_USER_MODEL = "users.User"

   # Application definition
   INSTALLED_APPS = [
      # Add the app to INSTALLED_APPS
      "app",
      "app.books",
      "app.users",
      "drf_redesign",
      "rest_framework",
      # Default apps
      ...
   ]
   ```

   Open `core/urls.py`:

   ```python
   # Import `include`
   from django.urls import path, include
   
   
   urlpatterns = [
      # Include `app.urls`
      path("", include("app.urls")),
      ...
   ]
   ```

6. **Run the Application**:

   ```bash
   poetry run python manage.py runserver
   ```

## Contributing

We warmly welcome contributions from the community. Please refer to our [CONTRIBUTING](CONTRIBUTING.md) guide for detailed instructions on how to contribute effectively. Your feedback and participation are essential for the continued improvement of this template.

## Support

For inquiries or support, please open an issue or join the discussion in the [GitHub Discussions](https://github.com/youzarsiph/drf-app/discussions) section to engage with the community.

## Licensing

This project is licensed under the MIT License. A detailed copy of the terms can be found in the [LICENSE](LICENSE) file.
