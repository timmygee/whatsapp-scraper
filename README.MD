In order to get this thing going you will need to be able to run python3 programs on your mac.

## Steps

1\. Install Xcode from https://developer.apple.com/xcode/. Let me know if you have any issues there (a reboot may be required)
2\. Launch the "Terminal" program from the "Applications" folder and run

    `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

This will install homebrew which allows you to install Python 3

3\. Run:

    `echo export "PATH='/usr/local/opt/python/libexec/bin:$PATH'" >> ~/.profile`

4\. Run:

    `brew install python`

5\. Set up https://web.whatsapp.com/ in Chrome to work with the All Out phone

6\. Extract the contents of the zip file attached to this card somewhere on your hard drive

7\. Navigate to that directory where you put the files in the Terminal program and run:

    `pip install -r requirements.txt`

8\. Finally, run the script with

    `./scrape.py`

If successful after running you should have a contacts.csv file in that location!

Note that I treat anything as a phone number if it has a digit in it. This is to make sure all phone numbers are picked up even if their formatting is different. There will not be any duplicates in the list and every time you run the script it will overwrite the contacts.csv file with a new copy.

This script is at the mercy of how WhatsApp chooses to lay out the WhatsApp web page. If they make changes to the page the script could stop working until it is updated by me to accommodate any new changes. For now, for me, it works!