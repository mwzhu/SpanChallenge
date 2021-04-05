# JSON Converter

This module converts JSON files containing notification data from an old format to a new format, removes duplicate notifications, and sorts notifications based on timestamp (ascending) and then by priority (descending).

## Installation

1. Download the ZIP file
2. Download the dateutil depdendency: `pip install python-dateutil`
3. Open terminal and navigate to this directory: `cd Downloads/SpanChallenge-master`
4. Install using setup.py: `python setup.py install`

## Usage

1. Upload your JSON file that you want to be converted into the old_files folder
2. In terminal, run this command: `python main.py [File_Name.json]`. For example, if your old JSON file is called notifications.json you would run:
`python main.py notifications.json`
3. Your new formatted JSON file will be in the new_files folder with the title "new_" added to the beginning of the file name. For example if your old file is called notifications.json the new file will be called new_notifications.json

## Testing

To test the code with the given unit tests, run: `python -m unittest test`.
