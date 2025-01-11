# csi2999-demo-refresher

This project visits my csi2999 project (or sophomore project) at https://csi-2999-project.onrender.com/ and creates an entry for a campsite reservation if the script hasn't been run within the last four days. Since we used Supabase's free tier for our development, database access will pause if there is no activity for seven days which results in our website displaying an error page. To combat this, this script reads a file in the user’s directory to see when the script was last run. If the script hasn't been run in the last 4 days, it will create an entry in the database and update the file with the date it was updated. If the script has been updated in the last 4 days, it will skip these steps.

## Project Features

-	Automates campsite reservation submission to prevent the database from pausing
-	Runs silently in the background without any pop-ups or user interaction
-	Executes every 4 days upon system startup

## To Run

Clone this repository. Download Selenium WebDriver and Google Chrome. Alter line 8 of the code to the path of Google Chrome on your machine. Create a .txt file in your user’s directory titled "dateRefresherLastRun.txt" and enter a date 4 or more previous days from today's date in YYYY-MM-DD format. Run campground.py to update the database.

To create executable file, confirm that the script runs as intended. Download PyInstaller and run the following command

pyinstaller --onefile --noconsole campground.py

The executable, campground.exe will generate in a subdirectory named “dist”. To automate the script running on system startup for windows, create a shortcut to the exe file and place in it the startup folder on your device.



