"""Template tags to update Login/Logout snippets"""

from django import template
from django.urls import NoReverseMatch, reverse
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe


# Create your template tags here.
register = template.Library()


@register.simple_tag
def optional_login(request) -> str:
    """Include a login snippet if REST framework's login view is in the URLconf."""

    try:
        login_url = reverse("rest_framework:login")

    except NoReverseMatch:
        return ""

    return mark_safe(
        format_html(
            """
            <li>
              <a href="{href}?next={next}" class="flex items-center gap-4">
                <i data-lucide="log-in" class="size-4 lg:size-6"></i>
                <span>Login</span>
              </a>
            </li>
            """,
            href=login_url,
            next=escape(request.path),
        )
    )


@register.simple_tag
def optional_logout(request, user, csrf_token) -> str:
    """Include a logout snippet if REST framework's logout view is in the URLconf."""

    try:
        logout_url = reverse("rest_framework:logout")

    except NoReverseMatch:
        return ""

    return mark_safe(
        format_html(
            """
            <li>
              <form id="logoutForm" class="hidden" method="post" action="{href}?next={next}">
                <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
              </form>

              <button type="submit" form="logoutForm" class="flex items-center gap-4">
                <i data-lucide="log-out" class="size-4 lg:size-6"></i>
                <span>Logout</span>
              </button>
            </li>
            """,
            user=escape(user),
            href=logout_url,
            next=escape(request.path),
            csrf_token=csrf_token,
        )
    )
