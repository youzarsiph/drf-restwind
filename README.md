# drf-restwind

[![CI](https://github.com/youzarsiph/drf-restwind/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/drf-restwind/actions/workflows/ci.yml)
[![CD](https://github.com/youzarsiph/drf-restwind/actions/workflows/cd.yml/badge.svg)](https://github.com/youzarsiph/drf-restwind/actions/workflows/cd.yml)
[![Code Style: Black](https://github.com/youzarsiph/drf-restwind/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/drf-restwind/actions/workflows/black.yml)
[![Code Linting: Ruff](https://github.com/youzarsiph/drf-restwind/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/drf-restwind/actions/workflows/ruff.yml)
[![Code Testing](https://github.com/youzarsiph/drf-restwind/actions/workflows/tests.yml/badge.svg)](https://github.com/youzarsiph/drf-restwind/actions/workflows/tests.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/drf-restwind?logo=pypi&logoColor=white)](https://pypi.org/project/drf-restwind/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/drf-restwind?logo=python&logoColor=white)](https://pypi.org/project/drf-restwind/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/drf-restwind?logo=pypi&logoColor=white)](https://pypi.org/project/drf-restwind/)
[![PyPI - License](https://img.shields.io/pypi/l/drf-restwind?logo=pypi&logoColor=white)](https://pypi.org/project/drf-restwind/)

## Overview

Welcome to `drf-restwind`, a modern re-imagining of the Django REST Framework. This project utilizes TailwindCSS and DaisyUI to provide flexible and customizable UI solutions with minimal coding effort.

## Key Features

- **Modern UI**: Crafted with TailwindCSS and DaisyUI for an appealing and contemporary design.
- **Diverse Themes**: Offers a selection of visually appealing themes to choose from.
- **Responsive Design**: Adapts seamlessly to various screen sizes for optimal user experience.
- **Accessibility**: Built with accessibility as a priority.
- **Code Highlighting**: Integrates Highlight.js for enhanced code visibility.
- **CI/CD Automation**: Utilizes GitHub Actions for automated deployment and integration, ensuring reliability and consistency.
- **Efficient Dependency Management**: Employs Poetry for meticulous project dependency management.
- **Consistent Code Formatting**: Uses Black for automatic code formatting, enhancing code readability.
- **Thorough Code Linting**: Implements Ruff to proactively identify and resolve potential code issues, boosting code quality and maintainability.
- **Comprehensive Testing**: Leverages Django’s testing framework for effective test management.
- **Essential Configuration Files**: Includes necessary files such as `.gitignore` and `pyproject.toml` for streamlined project setup.

## Screenshots

![API Root](https://github.com/user-attachments/assets/5197b47d-8bb6-426b-a62b-232cfc34198d)

![List View](https://github.com/user-attachments/assets/7665d4c8-e57a-4337-93af-4bb974a4f2d4)

![Detail View](https://github.com/user-attachments/assets/76bddab0-8747-42ae-b79b-b3be7802a729)

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

## Customization Guides

To customize `drf-restwind`, follow these steps:

1. **Add Required Templates**:

   In your app's templates directory, create a folder named `rest_framework` and add a file called `api.html`:

   ```bash
   mkdir app/templates/rest_framework
   touch app/templates/rest_framework/api.html
   ```

2. **Populate Your Template**:

   In `api.html`, include the following line:

   ```html
   {% extends 'rest_framework/base.html' %}
   ```

Now you can proceed with the following customization guides.

### Changing the Theme

To modify the theme, update your `api.html`:

Sure! Here’s the continuation of the instructions for changing the theme and other customization options:

```html
{% extends 'rest_framework/base.html' %}

{% block theme %}dracula{% endblock %}

<!-- The default theme is light. To use a dark theme, set the highlight_theme accordingly to support dark themes -->
{% block highlight_theme %}
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/base16/dracula.min.css">
{% endblock %}
```

### Removing theme selector

To remove the theme selector, update your `api.html`:

```html
{% extends 'rest_framework/base.html' %}

{% block theme_selector %}{% endblock %}
```

### Customizing the Brand and Adding Links

To change the brand name and add custom links, modify your `api.html`:

```html
{% extends 'rest_framework/base.html' %}

{% load i18n %}

{% block title %}{% translate 'YOUR_BRAND' %}{% endblock %}

{% block branding %}
<li class="tooltip tooltip-right tooltip-primary" data-tip="{% translate 'YOUR_BRAND' %}">
  <a href="https://www.django-rest-framework.org/" class="btn btn-square btn-primary lg:btn-lg">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-brain-circuit lg:size-8">
      <path d="M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z" />
      <path d="M9 13a4.5 4.5 0 0 0 3-4" />
      <path d="M6.003 5.125A3 3 0 0 0 6.401 6.5" />
      <path d="M3.477 10.896a4 4 0 0 1 .585-.396" />
      <path d="M6 18a4 4 0 0 1-1.967-.516" />
      <path d="M12 13h4" />
      <path d="M12 18h6a2 2 0 0 1 2 2v1" />
      <path d="M12 8h8" />
      <path d="M16 8V5a2 2 0 0 1 2-2" />
      <circle cx="16" cy="13" r=".5" />
      <circle cx="18" cy="3" r=".5" />
      <circle cx="20" cy="21" r=".5" />
      <circle cx="20" cy="8" r=".5" />
    </svg>
    <span class="sr-only">{% translate 'YOUR_BRAND' %}</span>
  </a>
</li>
{% endblock %}

{% block userlinks %}
<li class="tooltip tooltip-right" data-tip="{% translate 'Home' %}">
  <a href="https://github.com/youzarsiph" class="btn btn-square btn-ghost">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-house size-5 lg:size-6">
      <path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8" />
      <path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
    </svg>
    <span class="sr-only">{% translate 'Home' %}</span>
  </a>
</li>
{% endblock %}
```

## Contributing

We encourage community contributions! Please check our [CONTRIBUTING](CONTRIBUTING.md) guide for detailed instructions on how to contribute effectively. Your input and support play an essential role in the ongoing enhancement of this project.

## Support

If you have any questions or require assistance, feel free to open an issue or join our discussions in the [GitHub Discussions](https://github.com/youzarsiph/drf-restwind/discussions) section. We welcome community engagement and cherish your feedback!

## Licensing

This project is licensed under the MIT License. You can find the full terms of the license in the [LICENSE](LICENSE) file.
