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
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                        viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                        stroke-linecap="round" stroke-linejoin="round" 
                        class="lucide lucide-log-in size-4">
                        <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4" />
                        <polyline points="10 17 15 12 10 7" />
                        <line x1="15" x2="3" y1="12" y2="12" />
                    </svg>
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
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                        viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                        stroke-linecap="round" stroke-linejoin="round"
                        class="lucide lucide-log-out size-4">
                        <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" />
                        <polyline points="16 17 21 12 16 7" />
                        <line x1="21" x2="9" y1="12" y2="12" />
                    </svg>
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
