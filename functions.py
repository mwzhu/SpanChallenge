# This file contains the 3 functions specified on the Google document

import json
import dateutil.parser as dp

# This function takes in a list of notifications in the old format and returns a list of notifications in the new format
def legacy_notification_port(old_notifications):
    new_formatted_json_object = []

    for notification in old_notifications:
        old_datestring = notification["datestring"]
        old_priority = notification["priority"]
        old_msg = notification["msg"]
        old_deduplication_id = notification["deduplication_id"]

        new_notification = {}

        new_notification["timestamp"] = int(dp.parse(old_datestring).timestamp() * 1000)

        priority_dict = {"LOW": 0, "MID": 1, "HIGH": 2}
        new_notification["priority"] = priority_dict[old_priority]

        colon_index = old_msg.index(':')
        new_notification["body"] = old_msg[colon_index + 2:]
        new_notification["title"] = old_msg[:colon_index]

        new_notification["deduplication_id"] = old_deduplication_id

        new_formatted_json_object.append(new_notification)

    return new_formatted_json_object

# This function removes duplicate notifications using the deduplication_id
def deduplicating(duplicate_notifications):
    no_duplicates = []

    sorted_notifications = sorted(sorted_notifications, key = lambda x: x["priority"], reverse=True)
    sorted_notifications = sorted(sorted_notifications, key = lambda x: x["timestamp"], reverse=True)

    seen_deduplication_id = []
    for notification in duplicate_notifications:
        if notification["deduplication_id"] not in seen_deduplication_id:
            no_duplicates.append(notification)
            seen_deduplication_id.append(notification["deduplication_id"])

    return no_duplicates


# This function sorts notifications in order of timestamp (ascending) and then by priority (descending)
def sorting(notifications):
    sorted_notifications = sorted(notifications, key = lambda x: x["timestamp"])
    sorted_notifications = sorted(sorted_notifications, key = lambda x: x["priority"], reverse=True)
    return sorted_notifications
