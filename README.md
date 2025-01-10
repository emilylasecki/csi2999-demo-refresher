# csi2999-demo-refresher

This project visits my csi2999 project (or sophomore project) at https://csi-2999-project.onrender.com/ and creates an entry for a campsite reservation if the script hasn't been run within the last four days. Since we used supabase's free tier for our development, access to the database will be paused if there is no activity for 7 days. This will cause our website to display an error page. This script reads a file in the users directory to see when the script was last run. If the script hasn't been run in the last 4 days, it will create an entry in the database and update the file with the date it was updated. If the script has been updated in the last 4 days it will skip these steps. 

## To Run

### To Run Python File

Clone this repository. Download Selenium Webdriver and Google Chrome. Alter line 8 of the code to the path of Google Chrome on your machine. Create a .txt file in your users directory titled "dateRefresherLastRun.txt" and enter a date 4 or more previous days from today's date. Run campground.py to update the database.

### To Run Executable File

Download csi2999-reloader.exe. Create a .txt file in your users directory titled "dateRefresherLastRun.txt" and enter a date 4 or more previous days from today's date. Run the executable file. To automate the executable running on startup for windows, create a shortcut to the exe file and put it in the Startup folder.


