# RelayActivation
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Navigation Commands:

Once logged in it will open in the home directory location "vbreathe@raspberrypi:~ $"
To navigate in the terminal use the following commands:
ls - to show your current location and the files it contains (Blue files are folders which can be accessed using the "cd" command).
cd /"Folder Name" - to move to a folder in your current location.
cd - to move back to the home directory.
cd .. - to move back one level.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Starting Test Sequence:

To start a testing session please follow these steps outlined below:
1. Once in the home directory enter command "tmux"
2. In the tmux session enter command cd "/RelayActivation" to get to the relay test code folder location.
3. Depending on the test you want to carry out will define if the logging script is required:
	3.1 	For Button press testing "log_button_press.py" will be required
		Run logging code by entering command "python log_button_press.py -l <filename>.csv"
		Once code is running create another tmux screen in the same session by entering command "Control-b + c"
	3.2	For Lid rotation testing "log_lid_position.py" will be required
		Run logging code by entering command "python log_lid_position.py -l <filename>.csv"
		Once code is running create another tmux screen in the same session by entering command "Control-b + c"
4. Then enter command "python RelayControl.py" to run the main test code. Follow the code prompts to enter the parameters of the test.
5. Once code is running, send script to run in the background by entering the following command "Control-b + d".
6. This should take you back to the original screen which you can now close using the X in the top right, and the code should still run in the background.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Review Running Code:

You can review the status of the code while it is running by logging back into the pi as per above and re-attaching the terminal to the running tmux session using the command "tmux a".
To switch between the tmux session screen enter the command "Control-b + n".
Again to dettach the tmux session so you can close the pi terminal use command "Control-b + d".
Note: Do not close the pi terminal while still in the tmux session as this will stop the code and you will to restart the code again. Ensure you are dettached from the session prior to closure.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Retrieving Test Logs Via SSH:

When the code is complete, csv files should be created which have logged the test's cycles and performance.
The pi's cycle log will be found in the "/home/RelayActivation/Archive" directory as filename:
<DD-MM-YY>_<SerialNo.>_<Test rig>_CycleInfo.csv
The Max registered sensor information will be found in the "/home/RelayActivation" directory as filename:
<Your input through the log code>.csv

To retreive these files and their information use the following command from the windows command prompt "cmd":
"pscp -P 22 vbreathe@192.168.5.168:/home/vbreathe/RelayActivation/Archive/<file_name>.csv <name_of_file>.csv"

The file copies to the working directory

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Miscellaneous Commands:

Control-c - stops code
Control-z - pauses code
fg - resumes paused code
