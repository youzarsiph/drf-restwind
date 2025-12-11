# drf-restwind

[![CI](https://github.com/youzarsiph/drf-restwind/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/drf-restwind/actions/workflows/ci.yml)
[![CD](https://github.com/youzarsiph/drf-restwind/actions/workflows/cd.yml/badge.svg)](https://github.com/youzarsiph/drf-restwind/actions/workflows/cd.yml)
[![Code Style: Black](https://github.com/youzarsiph/drf-restwind/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/drf-restwind/actions/workflows/black.yml)
[![Code Linting: Ruff](https://github.com/youzarsiph/drf-restwind/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/drf-restwind/actions/workflows/ruff.yml)
[![Code Testing](https://github.com/youzarsiph/drf-restwind/actions/workflows/tests.yml/badge.svg)](https://github.com/youzarsiph/drf-restwind/actions/workflows/tests.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/drf-restwind?logo=pypi&logoColor=white)](https://pypi.org/project/drf-restwind/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/drf-restwind?logo=python&logoColor=white)](https://pypi.org/project/drf-restwind/)
[![PyPI - License](https://img.shields.io/pypi/l/drf-restwind?logo=pypi&logoColor=white)](https://pypi.org/project/drf-restwind/)

## Overview

Welcome to `drf-restwind`, a modern re-imagining of the Django REST Framework.
This project utilizes TailwindCSS and DaisyUI to provide flexible and
customizable UI solutions with minimal coding effort.

## Key Features

- **Modern UI**: Crafted with TailwindCSS and DaisyUI for an appealing and
  contemporary design.
- **Diverse Themes**: Offers a selection of visually appealing themes to choose
  from.
- **Responsive Design and RTL Support**: Adapts seamlessly to various screen sizes and locales for optimal
  user experience.
- **Accessibility**: Built with accessibility as a priority.
- **Code Highlighting**: Integrates Highlight.js for enhanced code visibility.
- **CI/CD Automation**: Utilizes GitHub Actions for automated deployment and
  integration, ensuring reliability and consistency.
- **Efficient Dependency Management**: Employs Poetry for meticulous project
  dependency management.
- **Consistent Code Formatting**: Uses Black for automatic code formatting,
  enhancing code readability.
- **Thorough Code Linting**: Implements Ruff to proactively identify and resolve
  potential code issues, boosting code quality and maintainability.
- **Comprehensive Testing**: Leverages Django’s testing framework for effective
  test management.
- **Essential Configuration Files**: Includes necessary files such as
  `.gitignore` and `pyproject.toml` for streamlined project setup.

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

## Customization Guides

To customize `drf-restwind`, follow these steps:

1. **Add Required Templates**:

   In your app's templates directory, create a folder named `rest_framework` and
   add a file called `api.html`:

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

You can view all available themes on [daisyUI](https://daisyui.com/) website. To
modify the theme, update your `api.html`:

```html
{% extends 'rest_framework/base.html' %}

<!-- Main theme -->
{% block theme %}luxury{% endblock %}

<!-- Light or Dark theme to toggle between -->
{% block toggle_theme %}silk{% endblock %}

<!-- Set the highlight_theme accordingly -->
{% block highlight_theme %}
<link
  rel="stylesheet"
  href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/base16/github-dark.min.css"
>
{% endblock %}
```

If you want to update code highlight theme for API documentation (written in
`Markdown` in `View`'s `docstring`):

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
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/base16/github-dark.min.css"
  >

  <!-- Include styles -->
  <link rel="stylesheet" href="{% static 'app/css/highlight.css' %}">
  {% endblock %}
  ```

### Creating your own theme

Can not find what you are looking for? Create your own theme:

1. Go to daisyUI [theme generator](https://daisyui.com/theme-generator/).
2. Select a theme or Click the `Random` button to generate a random theme.
3. Customize the defaults.
4. After customization click the `CSS` button to copy CSS variables.
5. Follow the steps:
   - Create `static` folder in your `app`:

     ```console
     mkdir -p app/static/app
     cd app/static/app
     ```

   - Install dependencies:

     ```console
     npm install tailwindcss '@tailwindcss/cli'
     npm install -D daisyui
     ```

   - Create your `css` folder and `styles`:

     ```console
     mkdir css
     touch css/app.css
     ```

   - Open your `app.css` and add the following lines:

     ```css
     @import "tailwindcss";

     @plugin "daisyui";

     /* Add your customized theme here */
     @plugin "daisyui/theme" {
       name: "lemon";
       default: false;
       prefersdark: false;
       color-scheme: "light";
       --color-base-100: oklch(98% 0.031 120.757);
       --color-base-200: oklch(96% 0.067 122.328);
       --color-base-300: oklch(93% 0.127 124.321);
       --color-base-content: oklch(40% 0.101 131.063);
       --color-primary: oklch(0% 0 0);
       --color-primary-content: oklch(100% 0 0);
       --color-secondary: oklch(62% 0.265 303.9);
       --color-secondary-content: oklch(97% 0.014 308.299);
       --color-accent: oklch(55% 0.013 58.071);
       --color-accent-content: oklch(98% 0.001 106.423);
       --color-neutral: oklch(40% 0.101 131.063);
       --color-neutral-content: oklch(98% 0.031 120.757);
       --color-info: oklch(78% 0.154 211.53);
       --color-info-content: oklch(30% 0.056 229.695);
       --color-success: oklch(84% 0.238 128.85);
       --color-success-content: oklch(27% 0.072 132.109);
       --color-warning: oklch(75% 0.183 55.934);
       --color-warning-content: oklch(26% 0.079 36.259);
       --color-error: oklch(71% 0.202 349.761);
       --color-error-content: oklch(28% 0.109 3.907);
       --radius-selector: 2rem;
       --radius-field: 0rem;
       --radius-box: 2rem;
       --size-selector: 0.25rem;
       --size-field: 0.25rem;
       --border: 1.5px;
       --depth: 1;
       --noise: 0;
     }
     ```

   - Generate your `styles`:

     ```console
     npx @tailwindcss/cli -i css/app.css -o css/styles.css
     ```

   - Include your `styles.css` in your templates:

     ```html
     {% extends 'rest_framework/base.html' %}{% load static %}
     
     <!-- Add your styles -->
     {% block styles %}
     {{ block.super }}
     <link rel="stylesheet" href="{% static 'app/css/styles.css' %}">
     {% endblock %}

     <!-- Your custom theme -->
     {% block theme %}lemon{% endblock %}
     ```

   - Run your app to view the result.

Now, you have a theme that matches your brand.

### Removing package details

Update your `api.html`:

```html
{% extends 'rest_framework/base.html' %}

{% block package %}{% endblock %}
```

### Removing theme selector

To remove the theme selector, update your `api.html`:

```html
{% extends 'rest_framework/base.html' %}

{% block theme_selector %}{% endblock %}
```

```html
<!-- rest_framework/login.html -->
{% extends 'rest_framework/login_base.html' %}

{% block theme_selector %}{% endblock %}
```

### Removing the search bar

To remove the search bar, update your `api.html`:

```html
{% extends 'rest_framework/base.html' %}

{% block navbar_center %}{% endblock %}
```

### Removing theme toggle

To remove theme toggle, update your `api.html`:

```html
{% extends 'rest_framework/base.html' %}

{% block theme_toggle %}{% endblock %}
```

```html
<!-- rest_framework/login.html -->
{% extends 'rest_framework/login_base.html' %}

{% block theme_selector %}{% endblock %}
```

### Customizing the Brand and Adding Links

To change the brand name and add custom links, modify your `api.html`:

```html
{% extends 'rest_framework/base.html' %}{% load i18n %}

{% block title %}{% trans 'YOUR_BRAND' %}{% endblock %}

<!-- Branding -->
{% block branding %}
<li
  class="tooltip tooltip-right tooltip-primary rtl:tooltip-left"
  data-tip="{% trans 'YOUR_BRAND' %}"
>
  <a
    href="https://your.domain.com/"
    class="btn btn-sm btn-square btn-ghost lg:btn-md"
  >
    <img 
      class="size-8 2xl:size-10" 
      alt="{% trans 'YOUR_BRAND' %}"
      src="{% static 'path/to/your/logo.png' %}"
    />
  </a>
</li>
{% endblock %}

<!-- Add your brand text -->
{% block drawer_branding %}
<li
  class="tooltip tooltip-right tooltip-primary rtl:tooltip-left"
  data-tip="{% trans 'YOUR_BRAND' %}"
>
  <a
    href="https://your.domain.com/"
    class="btn btn-sm btn-square btn-ghost lg:btn-md"
  >
    <img 
      class="size-8 2xl:size-10" 
      alt="{% trans 'YOUR_BRAND' %}"
      src="{% static 'path/to/your/logo.png' %}"
    />
  </a>
</li>
{% endblock %}

<!-- Add your links -->
{% block userlinks %}
<li
  class="is-drawer-close:tooltip is-drawer-close:tooltip-right rtl:is-drawer-close:tooltip-left"
  data-tip="{% trans 'Home' %}"
>
  <a href="https://your.domain.com/">
    <i data-lucide="home" class="size-4 lg:size-6"></i>
    <span class="is-drawer-close:sr-only">
      {% trans 'Home' %}
    </span>
  </a>
</li>
{% endblock %}
```

```html
<!-- rest_framework/login.html -->
{% extends 'rest_framework/login_base.html' %}

<!-- Branding -->
{% block branding %}
<li
  class="tooltip tooltip-right tooltip-primary rtl:tooltip-left"
  data-tip="{% trans 'YOUR_BRAND' %}"
>
  <a
    href="https://your.domain.com/"
    class="btn btn-sm btn-square btn-ghost lg:btn-md"
  >
    <img 
      class="size-8 2xl:size-10" 
      alt="{% trans 'YOUR_BRAND' %}"
      src="{% static 'path/to/your/logo.png' %}"
    />
  </a>
</li>
{% endblock %}
```

### Adding menu items to profile menu

To add menu items to profile menu, modify your `api.html`:

```html
{% extends 'rest_framework/base.html' %}{% load i18n %}

{% block profile_links %}
<li
  class="is-drawer-close:tooltip is-drawer-close:tooltip-right rtl:is-drawer-close:tooltip-left"
  data-tip="{% trans 'Profile' %}"
>
  <a href="https://your.domain.com/me/">
    <i data-lucide="user" class="size-4 lg:size-6"></i>
    <span class="is-drawer-close:sr-only">
      {% trans 'Profile' %}
    </span>
  </a>
</li>
{% endblock %}
```

### Generating CSS styles

To generate the CSS styles, run:

```console
cd rest_wind/static/rest_wind

# Install deps
npm install

# Generate the styles using TailwindCSS
npx @tailwindcss/cli -i ../static/rest_wind/css/app.css -o ../static/rest_wind/css/styles.css --cwd ../../templates -m
```

## Contributing

We encourage community contributions! Please check our
[CONTRIBUTING](CONTRIBUTING.md) guide for detailed instructions on how to
contribute effectively. Your input and support play an essential role in the
ongoing enhancement of this project.

## Support

If you have any questions or require assistance, feel free to open an issue or
join our discussions in the
[GitHub Discussions](https://github.com/youzarsiph/drf-restwind/discussions)
section. We welcome community engagement and cherish your feedback!

## Licensing

This project is licensed under the MIT License. You can find the full terms of
the license in the [LICENSE](LICENSE) file.
