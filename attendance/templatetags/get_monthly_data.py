from django import template

register = template.Library()

@register.filter
def get_monthly_data(monthly_attendance, month_num):
    """Retrieve the attendance data for the given month number."""
    return monthly_attendance.get(int(month_num), None)
