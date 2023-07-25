# django-feedback

A Django app to gather and send internal Government staff feedback, e.g. for open beta periods

## Installation

```
pip install django-feedback-govuk
```

1. Add `django-feedback` to your INSTALLED_APPS settings:

```py
INSTALLED_APPS = [
    ...
    'crispy_forms',
    'crispy_forms_gds',
    'django_feedback_govuk',
    ...
]
```

2. Create a new email template in the GovUk Notify service, making sure to create a ((feedback_url)) field.

> Note that ((feedback_url)) will be a link to the listing view, not an individual piece of feedback.

You'll need an API key and template ID from the gov.uk Notify service.

3. Add the following settings to the file:

```py
# Crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = ["gds"]
CRISPY_TEMPLATE_PACK = "gds"

# Gov Notify
GOVUK_NOTIFY_API_KEY="<your-api-key>"

# Django Feedback GovUK
DJANGO_FEEDBACK_GOVUK = {
    "SERVICE_NAME": "<your-service>",
    "FEEDBACK_NOTIFICATION_EMAIL_TEMPLATE_ID": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "FEEDBACK_NOTIFICATION_EMAIL_RECIPIENTS": ["email@example.com"],
    "COPY": {
        #...add any copy tags to override here
    }
}
```

The copy dict contains string IDs for all user-facing copy, defaulting to the following (override
just the fields you want to, using the `{{ service_name }}` variable if necessary for _title and _body strings):

```py
{
    "SUBMIT_TITLE": "Give feedback on {{ service_name }}",
    "CONFIRM_TITLE": "Feedback submitted",
    "CONFIRM_BODY": "Thank you for submitting your feedback.",
    "FIELD_SATISFACTION_LEGEND": "Overall, how did you feel about the service you received today?",
    "FIELD_COMMENT_LEGEND": "How could we improve this service?",
    "FIELD_COMMENT_HINT": "Do not include any personal or financial information, for example your National Insurance or credit card numbers.",
}
```

The email addresses are for every recipient that should get an email when feedback is submitted.

3. Build your own templates

Override the built-in templates by making new templates in your app under the
`django_feedback_govuk/templates` path. You'll need templates for `submit.html`, `confirm.html`
and `listing.html`, each of which should load its respective template tag from `feedback_submit`,
`feedback_confirm` and `feedback_listing`.

For example:

```py
{# /your-project/templates/django_feedback_govuk/templates/submit.html #}
{% extends "base.html" %}
{% load feedback_tags %}
{% block content %}
    {% feedback_submit %}
{% endblock content %}
```

> If you'd like to use the templatetags without causing page loads to new views

4. Add the URLs to your project

```py
from django_feedback_govuk import urls as feedback_urls


urlpatterns = [
    ...
    path("feedback/", include(feedback_urls)),
    ...
]
```

5. Set up user permissions

## Pushing to PyPI

- [PyPI Package](https://pypi.org/project/django-feedback-govuk/)
- [Test PyPI Package](https://test.pypi.org/project/django-feedback-govuk/)

Running `make build-package` will build the package into the `dist/` directory.

Running `make push-pypi-test` will push the built package to Test PyPI.

Running `make push-pypi` will push the built package to PyPI.

### Setting up poetry for pushing to PyPI

First you will need to add the test pypy repository to your poetry config:

```
poetry config repositories.test-pypi https://test.pypi.org/legacy/
```

Then go to https://test.pypi.org/manage/account/token/ and generate a token.

Then add it to your poetry config:

```
poetry config pypi-token.test-pypi XXXXXXXX
```

Then you also need to go to https://pypi.org/manage/account/token/ to generate a token for the real PyPI.

Then add it to your poetry config:

```
poetry config pypi-token.pypi XXXXXXXX
```

Now the make commands should work as expected.
