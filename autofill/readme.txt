This code is intended as an addon to the 3D software suit Blender
This addon allows a user to save a series of inputs to re-use them later

The Python notebook HowToRunTheseAddons.ipynb explains how to run the addon

To run:
Download Blender 3.0 and run it as an administrator
go to Edit>Preferences>Display and check 'Developer Extras'

click on the 'scripting' tab at the top middle of the screen
click the 'new text' button in the text editor view

copy the code from 'AddonsInstaller.py'
click run
this should set up the addons used in the later stages

Now delete the previous code and paste the code from the file 'AdddonSetup.py'
click run

return to your normal modeling scene and open a new info window (it can be tiny and in the corner, but it must be open)
enter edit mode and begin editing your model. Avoid changing selections during this time

now hit f3 to open the operator search menu
search for 'CopyInfoToFile' and click the operator you see there
this will save all of your inputs since the last time you entered edit mode

next hit f3 and search for 'PlayFromMemory' and click the operator
this will replay all of your previous inputs

selecting a new face and hitting 'PlayFromMemory' will do the sme thing again
this code can be reused any number of times until you re-record with a new 'CopyInfoToFile' command
