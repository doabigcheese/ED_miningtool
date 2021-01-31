# ED_miningtool
Elite Dangerous Miningtool for announcing percentage of Painite when prospecting
Feature:
- announcement only when value higher than set threshold
- zonk-sound (moooooo) if lower then threshold
- additional announced information if core is in the rock

Usage:
Start miningtool.py only when elite dangerous is already started, as it looks for latest logfile and stays in this file...
Just prospect as usual

Requirements:
python 3.x
pip install pywin32
pip install requests
setup your windows folder where the logfiles of elite are
adjust the threshold to your favour
it is looking for Painite, if anything else, you need to adjust this as well
