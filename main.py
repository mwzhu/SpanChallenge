''' This is the main driver function that takes in a JSON file in the old format which is stored in the old_files directory
and returns the corresponding JSON file in the new format which is stored in the new_files directory '''

from functions import *
import sys

def main(old_file):
    with open("old_files/" + old_file) as read_file:
        json_object = json.load(read_file)

    new_json_object = legacy_notification_port(json_object)
    # deduplicated_json_object = deduplicating(new_json_object)
    # sorted_json_object = sorting(deduplicated_json_object)

    new_file = "new_" + old_file
    with open("new_files/" + new_file, "w") as outfile:
        json.dump(new_json_object, outfile)

file_name = sys.argv[1]
main(file_name)
