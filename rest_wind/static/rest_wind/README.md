# UI Styles

Basic commands to get started.

First `cd` into dir:

```console
cd rest_wind/static/rest_wind
```

To generate the styles:

```console
npm install
npx @tailwindcss/cli -i ../static/rest_wind/css/app.css -o ../static/rest_wind/css/styles.css --cwd ../../templates -m -w
```

To format the templates:

```console
npx prettier -w ../../templates
```
