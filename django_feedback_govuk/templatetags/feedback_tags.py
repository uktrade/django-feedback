from django import template
from django.utils.module_loading import import_string

from django_feedback_govuk.settings import DEFAULT_FEEDBACK_ID, dfg_settings


register = template.Library()


@register.inclusion_tag(
    "django_feedback_govuk/partials/submit.html", takes_context=True
)
def feedback_submit(context, form_id: str = DEFAULT_FEEDBACK_ID):
    feedback_config = dfg_settings.FEEDBACK_FORMS[form_id]
    feedback_form = import_string(feedback_config["form"])
    if "form" in context:
        form = context["form"]
    else:
        initial = {}
        initial["submitter"] = context.request.user

        form = feedback_form(initial=initial)

    new_context = {
        "form": form,
        "form_id": form_id,
        "service_name": dfg_settings.SERVICE_NAME,
        "submit_title": dfg_settings.COPY_SUBMIT_TITLE,
    }
    return new_context


@register.inclusion_tag(
    "django_feedback_govuk/partials/confirm.html", takes_context=True
)
def feedback_confirm(context):
    new_context = {
        "service_name": dfg_settings.SERVICE_NAME,
        "confirm_title": dfg_settings.COPY_CONFIRM_TITLE,
        "confirm_body": dfg_settings.COPY_CONFIRM_BODY,
    }
    return new_context


@register.inclusion_tag(
    "django_feedback_govuk/partials/listing.html", takes_context=True
)
def feedback_listing(context):
    return context


@register.inclusion_tag(
    "django_feedback_govuk/partials/submitted.html", takes_context=True
)
def feedback_submitted(context):
    return context


@register.filter()
def get_feedback_value(object, field_name):
    get_f_display = f"get_{field_name}_display"
    if value := getattr(object, get_f_display, None):
        return value()
    return getattr(object, field_name)


@register.filter()
def get_feedback_form_label(form, field_name):
    field = form.fields.get(field_name, None)
    if field and field.label:
        return field.label
    return field_name.replace("_", " ").capitalize()


@register.filter()
def get_elided_page_range(page):
    return page.paginator.get_elided_page_range(page.number, on_each_side=1, on_ends=1)


@register.simple_tag(takes_context=True)
def get_pagination_url(context, page):
    request = context["request"]

    query_params = request.GET.copy()
    query_params["page"] = page

    return "?" + query_params.urlencode()
