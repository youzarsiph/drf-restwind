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

![API Root](https://github.com/user-attachments/assets/86706c8c-392b-447d-8380-d852fd3b04df)

![List View](https://github.com/user-attachments/assets/f0f966f7-3d2e-4eba-9147-247b2d588194)

![Detail View](https://github.com/user-attachments/assets/52d79530-2b0d-4f1b-9924-4923d2070704)

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

3. **Add your `app` to `INSTALLED_APPS`**

   In `project/settings.py`:

   ```python
   # Application definition
   INSTALLED_APPS = [
       # Add your app
       "app",
       "rest_wind",
       "rest_framework",
       ...
   ]
   ```

Now you can proceed with the following customization guides.

### Changing the Theme

To modify the theme, update your `api.html`:

```html
{% extends 'rest_framework/base.html' %}

<!-- Main theme -->
{% block theme %}luxury{% endblock %}

<!-- Light or Dark theme to toggle between -->
{% block toggle_theme %}silk{% endblock %}

<!-- Set the highlight_theme accordingly -->
{% block highlight_theme %}
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/base16/github-dark.min.css">
{% endblock %}
```

If you want to update code highlight theme for API documentation (written in `Markdown` in `View`'s `docstring`):

- Install `markdown` and `pygments`:

  ```console
  pip install markdown pygments
  ```

- Select a style form available [styles](https://pygments.org/styles).
- Generate the `css` file for selected styles:

  ```console
  pygmentize -S github-dark -f html > app/static/app/css/highlight.css
  ```

- Include the generated `css` file in your `api.html`:

  ```html
  {% extends 'rest_framework/base.html' %}{% load static %}

  <!-- Main theme -->
  {% block theme %}luxury{% endblock %}

  <!-- Light or Dark theme to toggle between -->
  {% block toggle_theme %}silk{% endblock %}

  <!-- Set the highlight_theme accordingly -->
  {% block highlight_theme %}
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/base16/github-dark.min.css">

  <!-- Include styles -->
  <link rel="stylesheet" href="{% static 'app/css/highlight.css' %}">
  {% endblock %}
  ```

### Removing theme selector

To remove the theme selector, update your `api.html`:

```html
{% extends 'rest_framework/base.html' %}

{% block theme_selector %}{% endblock %}
```

### Updating `View` documentation styles

To update `View` documentation **typography** styles, update your `api.html`:

```html
{% extends 'rest_framework/base.html' %}

{% block markdown_styles %}lg:prose-xl{% endblock %}
```

### Removing the search bar

To remove the search bar, update your `api.html`:

```html
{% extends 'rest_framework/base.html' %}

{% block searchbar %}{% endblock %}
```

### Removing theme toggle

To remove theme toggle, update your `api.html`:

```html
{% extends 'rest_framework/base.html' %}

{% block searchbar_right %}{% endblock %}

{% block sidebar_styles %}lg:h-[calc(100dvh-1rem)] lg:max-h-[calc(100dvh-1rem)]{% endblock %}
{% block content_styles %}lg:h-[calc(100dvh-1rem)] lg:max-h-[calc(100dvh-1rem)]{% endblock %}
```

**Note**: This also removes the theme selector.

### Customizing the Brand and Adding Links

To change the brand name and add custom links, modify your `api.html`:

```html
{% extends 'rest_framework/base.html' %}{% load i18n %}

{% block title %}{% trans 'YOUR_BRAND' %}{% endblock %}

{% block branding %}
<li
  class="tooltip tooltip-right tooltip-primary"
  data-tip="{% trans 'YOUR_BRAND' %}"
>
  <a
    href="https://www.django-rest-framework.org/"
    class="btn btn-sm btn-square btn-ghost lg:btn-md"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
      class="lucide lucide-graduation-cap size-5 lg:size-6"
    >
      <path
        d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"
      />
      <path d="M22 10v6" />
      <path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5" />
    </svg>

    <span class="sr-only">{% trans 'YOUR_BRAND' %}</span>
  </a>
</li>
{% endblock %}

{% block branding_text %}
<!-- Add your brand -->
<h1 class="hidden text-xl font-semibold text-primary lg:block">{% trans 'YOUR_BRAND' %}</h1>

<!-- Or an empty div to center the search bar -->
<div class="hidden lg:block"></div>
{% endblock %}

{% block userlinks %}
<li
  class="tooltip tooltip-right tooltip-secondary"
  data-tip="{% trans 'Home' %}"
>
  <a
    href="https://www.django-rest-framework.org/"
    class="btn btn-sm btn-square btn-ghost lg:btn-md"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
      class="lucide lucide-house size-5 lg:size-6"
    >
      <path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8" />
      <path
        d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"
      />
    </svg>

    <span class="sr-only">{% trans 'Home' %}</span>
  </a>
</li>
{% endblock %}
```

### Adding menu items to profile menu

To add menu items to profile menu, modify your `api.html`:

```html
{% extends 'rest_framework/base.html' %}{% load i18n %}

{% block profile_menu %}
<li>
  <a href="/users/me" class="flex items-center gap-4">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
      class="lucide lucide-circle-user size-5 lg:size-6"
    >
      <circle cx="12" cy="12" r="10" />
      <circle cx="12" cy="10" r="3" />
      <path
        d="M7 20.662V19a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v1.662"
      />
    </svg>

    <span>{% translate 'Profile' %}</span>
  </a>
</li>
{% endblock %}

```

### Generating CSS styles

To generate the CSS styles, run:

```console
cd /rest_wind/static/rest_wind

# Install deps
npm install

# Generate the styles using TailwindCSS
npx @tailwindcss/cli -i ../static/rest_wind/css/app.css -o ../static/rest_wind/css/styles.css --cwd ../../templates -m
```

## Contributing

We encourage community contributions! Please check our [CONTRIBUTING](CONTRIBUTING.md) guide for detailed instructions on how to contribute effectively. Your input and support play an essential role in the ongoing enhancement of this project.

## Support

If you have any questions or require assistance, feel free to open an issue or join our discussions in the [GitHub Discussions](https://github.com/youzarsiph/drf-restwind/discussions) section. We welcome community engagement and cherish your feedback!

## Licensing

This project is licensed under the MIT License. You can find the full terms of the license in the [LICENSE](LICENSE) file.
