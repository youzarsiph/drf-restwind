# drf-restwind

[![CI](https://github.com/youzarsiph/drf-restwind/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/drf-restwind/actions/workflows/ci.yml)
[![CD](https://github.com/youzarsiph/drf-restwind/actions/workflows/cd.yml/badge.svg)](https://github.com/youzarsiph/drf-restwind/actions/workflows/cd.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/drf-restwind?logo=pypi&logoColor=white)](https://pypi.org/project/drf-restwind/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/drf-restwind?logo=python&logoColor=white)](https://pypi.org/project/drf-restwind/)
[![PyPI - License](https://img.shields.io/pypi/l/drf-restwind?logo=pypi&logoColor=white)](https://pypi.org/project/drf-restwind/)

## Overview

Welcome to `drf-restwind`, a modern re-imagining of the Django REST Framework.
This project utilizes TailwindCSS and daisyUI to provide flexible and
customizable UI solutions with minimal coding effort.

## Key Features

- **Modern UI**: Crafted with TailwindCSS and daisyUI for an appealing and
  contemporary design.
- **Diverse Themes**: Offers a selection of visually appealing themes to choose
  from.
- **Responsive Design and RTL Support**: Adapts seamlessly to various screen sizes and locales for optimal
  user experience.
- **Accessibility**: Built with accessibility as a priority.
- **Code Highlighting**: Integrates Highlight.js for enhanced code visibility.

## Screenshots

![API Root](https://github.com/user-attachments/assets/8fb41d88-bf9c-4e3f-bdb4-83f334c90d05)

![List View](https://github.com/user-attachments/assets/3edb4b6e-cada-4e24-b621-b0ad16f43e0d)

![Detail View](https://github.com/user-attachments/assets/7428301f-6417-4709-aebc-89f42b0499ef)

## Quick Start Guide

To get started with `drf-restwind`, follow these steps:

1. **Install the package**:

   ```bash
   pip install drf-restwind
   ```

2. **Update `INSTALLED_APPS`**:

   Modify `project/settings.py` as follows:

   ```python
   # Application definition
   INSTALLED_APPS = [
       # Add rest_wind to INSTALLED_APPS
       "rest_wind",
       "rest_framework",
       ...
   ]
   ```

## Guides

Please check our [GUIDES](GUIDES.md) for advanced usage.

## Contributing

We encourage community contributions! Please check our
[CONTRIBUTING](CONTRIBUTING.md) guide for detailed instructions on how to
contribute effectively. Your input and support play an essential role in the
ongoing enhancement of this project.

## Support

If you have any questions or require assistance, feel free to open an issue.
We welcome community engagement and cherish your feedback!

## Licensing

This project is licensed under the MIT License. You can find the full terms of
the license in the [LICENSE](LICENSE) file.
