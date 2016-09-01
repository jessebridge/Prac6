"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                   "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
for short_state, state_name in STATE_NAMES.items():
    print("{:5} is {}".format(short_state, state_name))




