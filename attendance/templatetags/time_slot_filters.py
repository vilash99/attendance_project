from django import template

register = template.Library()

@register.filter
def time_range(time_slots):
    if not time_slots.exists():
        return ''

    # Extract start time from the first time slot
    time_slots_list = time_slots.values_list('slot', flat=True)

    first_slot = time_slots_list.first()
    first_start_time = first_slot.split(' - ')[0]

    # Extract end time from the last time slot
    last_slot = time_slots_list.last()
    last_end_time = last_slot.split(' - ')[1]

    total_slots = time_slots.count()
    if total_slots > 1:
        total_slot_str = '{} slots'.format(total_slots)
    else:
        total_slot_str = '{} slot'.format(total_slots)

    # Return the combined time range
    return '{} to {} - [{}]'.format(first_start_time, last_end_time, total_slot_str)
