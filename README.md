![](http://pinaxproject.com/pinax-design/patches/pinax-ratings.svg)

# Pinax Ratings

[![](https://img.shields.io/pypi/v/pinax-ratings.svg)](https://pypi.python.org/pypi/pinax-ratings/)

[![CircleCi](https://img.shields.io/circleci/project/github/pinax/pinax-ratings.svg)](https://circleci.com/gh/pinax/pinax-ratings)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-ratings.svg)](https://codecov.io/gh/pinax/pinax-ratings)
[![](https://img.shields.io/github/contributors/pinax/pinax-ratings.svg)](https://github.com/pinax/pinax-ratings/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-ratings.svg)](https://github.com/pinax/pinax-ratings/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-ratings.svg)](https://github.com/pinax/pinax-ratings/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Table of Contents

* [About Pinax](#about-pinax)
* [Important Links](#important-links)
* [Overview](#overview)
  * [Supported Django and Python Versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Settings](#settings)
  * [Templates](#templates)
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)


## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## Important Links

Where you can find what you need:
* Releases: published to [PyPI](https://pypi.org/search/?q=pinax) or tagged in app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Global documentation: [Pinax documentation website](https://pinaxproject.com/pinax/)
* App specific documentation: app repos in the [Pinax GitHub organization](https://github.com/pinax/)
* Support information: [SUPPORT.md](https://github.com/pinax/.github/blob/master/SUPPORT.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Contributing information: [CONTRIBUTING.md](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) file in the [Pinax default community health file repo](https://github.com/pinax/.github/)
* Current and historical release docs: [Pinax Wiki](https://github.com/pinax/pinax/wiki/)


## pinax-ratings

### Overview

``pinax-ratings`` is a ratings app for Django.

#### Supported Django and Python Versions

Django / Python | 3.6 | 3.7 | 3.8
--------------- | --- | --- | ---
2.2  |  *  |  *  |  *
3.0  |  *  |  *  |  *


## Documentation

### Installation

To install pinax-ratings:

```shell
    $ pip install pinax-ratings
```

Add `pinax.ratings` to your ``INSTALLED_APPS`` setting:

```python
    INSTALLED_APPS = [
        # other apps
        "pinax.ratings",
    ]
```

Add `pinax.ratings.urls` to your project urlpatterns:

```python
    urlpatterns = [
        # other urls
        url(r"^ratings/", include("pinax.ratings.urls", namespace="pinax_ratings")),
    ]
```

Finally, view the list of [settings](#settings) to modify pinax-ratings's default behavior and make adjustments for your website.

Optionally, if want to use the ratings category feature of `pinax-ratings` then you will need to add the `pinax-RATINGS_CATEGORY_CHOICES` setting in your `settings.py`:

```python
    PINAX_RATINGS_CATEGORY_CHOICES = {
        "app.Model": {
            "exposure": "How good is the exposure?",
            "framing": "How well was the photo framed?",
            "saturation": "How would you rate the saturation?"
        },
        "app.Model2": {
            "grammar": "Good grammar?",
            "complete": "Is the story complete?",
            "compelling": "Is the article compelling?"
        }
    }
```

### Usage

Integrating `pinax-ratings` into your project is just a matter of using a couple of
template tags and wiring up a bit of javascript. The rating form is intended
to function via AJAX and as such returns JSON.

First add load the template tags for `pinax-ratings`:

```django
    {% load pinax_ratings_tags %}
```

Then pick a template tag for display or obtaining rating data.

### Template Tags

#### overall_rating

Display an overall rating average for an object:

```django
    {% overall_rating obj as the_overall_rating %}

    <div class="overall_rating">{{ the_overall_rating }}</div>
```

Display overall rating average _for a specific category_ for an object:

```django
    {% overall_rating obj "accuracy" as category_rating %}

    <div class="overall_rating category-accuracy">
        {{ category_rating }}
    </div>
```

#### user_rating

Display a specific user's rating:

```django
    {% user_rating request.user obj as the_user_rating %}

    <div class="user_rating">{{ the_user_rating }}</div>
```

Display specific user rating _for a specific category_ for an object:

```django
    {% user_rating request.user obj "accuracy" as category_rating %}

    <div class="user_rating category-accuracy">
        {{ category_rating }}
    </div>
```

#### user_rating_js

If you want to add an AJAX form for allowing a user to set a rating, add the
following in the appropriate location on your page:

```django
    <div id="user_rating"></div>
```

And then add this near the end of your HTML `<body>` to emit some Javascript
libraries and hook up the ratings UI:

```django
    {% user_rating_js request.user obj %}
```

Hook up the ratings UI for a specific category:


```django
    <div id="user_rating" class="category-accuracy"></div>

    {% user_rating_js request.user obj "accuracy" %}
```

#### ratings

Returns all Ratings for an object type, regardless of category:

```django
    {% ratings obj as the_ratings %}
    {% for rating in the_ratings %}
        Rating: {{ rating.rating }}
    {% endfor %}
```

#### user_rating_url

Returns a URL for user to post a rating for an object:

```django
    {% user_rating_url request.user obj as rating_url %}
    {{ rating_url }}
```

#### rating_count

Returns the number of ratings for an object type:

```django
    {% rating_count obj as count %}
    {{ obj }} has {{ count }} ratings
```

### Settings

#### PINAX_RATINGS_NUM_OF_RATINGS

Default: 5

Defines the number of different rating choices there will be.

#### PINAX_RATINGS_CATEGORY_CHOICES

Default: `None`

Defines a dictionary of rating category choices for application models.
Each model specified has a dictionary of rating categories, with associated rating prompt string.
Only rating categories associated with a model in this setting are allowed.

```python
    PINAX_RATINGS_CATEGORY_CHOICES = {
        "app.Photo": {
            "exposure": "How good is the exposure?",
            "framing": "How well was the photo framed?",
            "saturation": "How would you rate the saturation?"
        },
        "app.Story": {
            "grammar": "Good grammar?",
            "complete": "Is the story complete?",
            "compelling": "Is the article compelling?"
        }
    }
```

### Templates

`pinax-ratings` comes with two minimal template snippets rendered
by template tags for displaying the rating form.

Templates are found in "pinax/ratings/" subdirectory for your project.

#### `_rating.html`

#### `_script.html`

This is a snippet that renders the bundled Javascript and a simple AJAX posting and
hooking up of a rating UI. This is optional and overridable by the site developer.


## Change Log

### 5.0.0

* Takeover by Novel-T
* Support Django 4
* Add missing migration

### 4.0.0

* Drop Django 1.11, 2.0, and 2.1, and Python 2,7, 3.4, and 3.5 support
* Add Django 2.2 and 3.0, and Python 3.6, 3.7, and 3.8 support
* Update packaging configs
* Direct users to community resources

### 3.0.3

* Improve test clarity and coverage
* Improve documentation

### 3.0.2

* Add templatetag tests, model tests

### 3.0.1

* Import reverse from django.urls

### 3.0.0

* Add Django 2.0 compatibility testing
* Drop Django 1.8, 1.9, 1.10, and Python 3.3 support
* Add URL namespacing (BI: urlname "pinax_ratings_rate" is now "pinax_ratings:rate")
* Move documentation into README and standardize layout
* Convert CI and coverage to CircleCi and CodeCov
* Add PyPi-compatible long description

### 2.0.0

* converted category on ratings.Rating and `ratings.OverallRating` models to be
  a CharField that is the actual category label rather than a runtime generated
  ID. _upgrading will require you manually update the database values_

### 1.0.0

* @@@ write change log

### 0.3

* renamed from agon_ratings to pinax-ratings

### 0.2.1

* added ability in overall_rating template tag to omit the category
  label and get an average rating without concern for category
  averages.
* added ability to get average rating over all categories for a
  particular user and particular object.

### 0.2

* added support for ratings to have categories instead of just a single
  rating for an object
* dropped natural language of template tags

#### Migrations

Added a category model and updated the unique index on both models:

    ALTER TABLE "agon_ratings_overallrating" ADD COLUMN "category" int;
    ALTER TABLE "agon_ratings_rating" ADD COLUMN "category" int;
    CREATE UNIQUE INDEX "agon_ratings_overallrating_unq_object_id_content_type_id_category_idx"
        ON "agon_ratings_overallrating" (object_id, content_type_id, category);
    CREATE UNIQUE INDEX "agon_ratings_rating_unq_object_id_content_type_id_user_id_category_idx"
        ON "agon_ratings_rating" (object_id, content_type_id, user_id, category);
    ALTER TABLE "agon_ratings_rating" DROP CONSTRAINT
        IF EXISTS "agon_ratings_rating_object_id_content_type_id_user_id_key";
    ALTER TABLE "agon_ratings_overallrating" DROP CONSTRAINT
        IF EXISTS "agon_ratings_overallrating_object_id_content_type_id_key";

### 0.1.2

* added a tag, `user_rating_url`, for getting the POST url for posting a rating
* changed `user_rate_form` and documented javascript wiring to a single
  `user_rating_js` inclusion tag that output all the javascript and removed
  the need for a form.

### 0.1

* initial release


## Contribute

[Contributing](https://github.com/pinax/.github/blob/master/CONTRIBUTING.md) information can be found in the [Pinax community health file repo](https://github.com/pinax/.github).


## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a [Code of Conduct](https://github.com/pinax/.github/blob/master/CODE_OF_CONDUCT.md). We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject) and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-present James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
