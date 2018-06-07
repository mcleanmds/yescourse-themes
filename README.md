# yescourse-themes
Officially supported public themes for YesCourse


# Theme Package Format

Themes are organised into subdirectories with the following required files/folders:
```dir
.
├── config.json
├── css
│   ├── theme.css
├── images
│   ├── images_file_1.png
│   ├── images_file_2.jpg
│   └── etc...
├── js
│   └── theme.js
└── templates
    ├── template_file_1.html
    ├── template_file_2.css
    └── etc...

```


## config.json

```json
{
  "meta": {_see meta section below_},
  "templates": {_list of template filenames_},
  "extcss" : [_list of external css files_],
  "extjs" : [_list of external js files_],
  "vars": {_see vars section below_},
  "build_ui": {_see build_ui section below_},
  "images": [_list of image filenames_]
}
```


### meta
The Theme meta data is used to identify and descript the theme.
These fields must be included:
* a unique short name for the theme
* a title for the theme
* the theme author
* a description of the theme


Example meta:
```json
{
  "short_name": "helium",
  "title": "Helium",
  "author": "YesCourse Pty Ltd",
  "description": "A simple light weight theme - the default for YesCourse Courses"
}
```

### templates

#### Required Templates
At a minimum, the following templates need to be supplied with the theme:
* default-page
* academy-page
* home-page
* bundle-page
* course-page
* module-page
* lesson-page
* sales-page
* content-page
* course-thank-you-page
* user-config-css
* 403-page
* 404-page

#### Additional templates
Additional template may be specified, and imported into the above templates.
The naming convention for additional templates is to start with a "-", e.g. "-site-header"
templates can be included in other templates using the "include" tag. e.g.
```html
{% include "-site-header" %}
```

#### Template Tags

##### include
TODO
##### setTitle
TODO
##### term
TODO

#### Template Blocks

##### breadcrumbs
TODO
##### module_lessons_menu
TODO
##### page_content
TODO

#### Template Context
##### Using context
Context values can be used within a template by enclosing the context variable name in double brackets.


##### Available context
###### default-page
TODO
###### academy-page
TODO
###### home-page
TODO
###### bundle-page
TODO
###### course-page
TODO
###### module-page
TODO
###### lesson-page
TODO
###### sales-page
TODO
###### content-page
TODO
###### course-thank-you-page
TODO
###### user-config-css
TODO
###### 403-page
TODO
###### 404-page
TODO

### extcss
This is a list of urls that will be loaded before the theme.css is loaded.
Here you can add urls to external css files that you wish to be loaded with the theme.

### extjs
This is a list of urls that will be loaded, after the theme css files and before the theme.js is loaded.
Here you can add urls to external js files that you wish to be loaded with the theme.

### vars
Theme variable allow parts of the theme to be modified by the end user.
There are a number of variable types that can be used, each with different preperties, see the Variable Types below

#### Variable Types
##### boolean
Boolean variables are useful for providing a way to enable or disable features or styling on a page.
The themebuilder interface represents a boolean variable as a checkbox input.
Example definition:
```json
"registration_button_in_banner": {
  "type": "boolean",
  "default": true
}
```
Example template use:
```
{% rego_button onlyIf=theme_config.registration_button_in_banner %}
```
```
{% include "-std-banner-text" notIf=theme_config.banner_has_custom_text %}
```
Example css use:
```css
&:not(.registration_button_in_banner) {
  #rego-btn-banner {
    display: none;
  }
}
```

##### choice
Choice variables are useful when there are two or more options to choose between.
The themebuilder interface represents a choice variabl as a dropdown selection input.
Example definition:
```json
"banner_text_position": {
  "type": "choice",
  "choices": [
    ["LEFT", "Left"],
    ["RIGHT", "Right"],
    ["BOT", "Bottom"]
  ],
  "default": "RIGHT"
}
```
Example template use:
```
{% addThemeDataAttributes "banner_background_scaling" "banner_text_position" %}
```
Example css use:
```css
#yc-page[data-banner_text_position='left'] #sales_banner {
  css_here
}
#yc-page[data-banner_text_position='right'] #sales_banner {
  css_here
}
#yc-page[data-banner_text_position='bottom'] #sales_banner {
  css_here
}
```

##### color
color variables allow the color value to be selectable.
The themebuilder interface represents a color variable as a color selection box.
Example definition:
```json
"menu_background_color": {
  "type": "color",
  "default": "#4c4c54"
}
```
Example template/css use (in user-config.css):
```css
aside {
    background-color: {{ theme_config.menu_background_color }} !important;
}
```

##### colour-alpha
color variables allow the color value, including alpha, to be selectable.
The themebuilder interface represents a color variable as a color selection box, with an alpha slider.
Example definition:
```json
"rego_button_background_color": {
  "type": "color-alpha",
  "default": "rgba(0,0,0,0.52)"
},
```
Example template/css use (in user-config.css):
```css
.yc-rego-button {
    background-color: {{ theme_config.rego_button_background_color }} !important;
}
```

##### html
HTML variables are useful for providing sections of editable content on a page.
The themebuilder interface provides a full ckeditor experience for each HTML variable.
Example definition:
```json
"academy_banner_text": {
  "type": "html",
  "default": "<h1>{{academy.title}}</h1>"
}
```
Example template use:
```html
{% theme_html "academy_banner_text" class="academy-banner-text" %}
```

##### image
HTML variables are useful for providing sections of editable content on a page.
The themebuilder interface provides a full ckeditor experience for each HTML variable.
Example definition:
```json
"academy_banner_image": {
  "type": "image",
  "default": "none"
},
```
Example template/css use (in user-config.css):
```html
.academy-page .banner {
  background-image: {{ theme_config.academy_banner_image }} !important;
}
```

#### Variable Levels
Variable can optionally be limited to a level of theme
Available levels are:
* A = Academy level - applies to entire academy, customisations saved with the academy.
* C = Course level - applies to course and course related pages, customisations saved with the course.
* L = Lesson level (not used, lesson customisation applies to the course level)
* S = Sales Page level - applies to sales page, customisations saved with the sales page.
* P = Content Post level - applies to blogs / pages, customisations saved with the blog/page

To limit when variables are shown in the themebuilder interface, a level

#### Variable Pages
No effect at the moment.


### build_ui
This defines how the themebuilder displays the theme customisation options.
theme variables are grouped together in logical groupings,
with each group displayed in it's own expandable box in the themebuilder

#### groups


### images
For all images included in the theme, the filenames to be listed here,
and match the file stored in the "images/" directory.
e.g.
```json
"images": [
  "default_pic.png",
  "loading.gif",
  "ppt.jpg"
]
```
TODO - are the certain image files required?
Note: We recomend minimising the use of image files by using svg in css where possible.
