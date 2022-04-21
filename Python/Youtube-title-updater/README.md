# Youtube-title-updater
The amount of likes on your video will be shown in the video's caption.
This code runs after every 5 minutes.
Steps to make this shit work (kinda):
1) Set up and make a console and make a project. Set the API keys and the OAUTH client. Refer this site for more:-  https://developers.google.com/youtube/v3/getting-started?hl=en
2) Get the secret client id.json file and save it somewhere.
3) Open your terminal and install the following pips:
	a) pip install --user google-auth-oauthlib
	b) pip install --user google-api-python-client

4) Get the code, change the video id and the secret client id.json
5) Save the code after changing the video id and secret client id.json
6) Make a folder and save both your a) secret client id AND b) the code IN ONE FOLDER
7) Run the code from terminal
8) The code will give an authentication link. Copy paste it in your browser.
9) Google will ask to log-in. Log-in with your account, give the required permissions and continue. 
10) If google shows with a warning like "This app is not verified by Google and is unsafe to proceed" then just click proceed anyway.
11) The repeat point 9.
12) After doing the above steps, you will get a success state message and you will get an authetication id. Copy it and paste the id in the terminal.
13) And you're done. The code should be working.



Please forgive my shitty instructions.
