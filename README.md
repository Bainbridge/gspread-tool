Gspread-Tool
===================


This is a tool that can turn a regular old spreadsheet file (*.csv) into a Google Spreadsheet!

--------
### Prerequisites:

- Get OAuth2 Service account
- Install gspread (via pip)
- Install OAuth2Client (version 1.5.2) (via pip)
- Install PyOpenSSL (via easy_install)
- Changing the "/path/to/file" in spreadTool.py to the path of your service account credentials

 

### Getting OAuth2 Permission:
1. Go to [Google Developer's Console](http://developers.google.com/console)
2. Create a project
3. Enable the Drive API
4. Create a Service Account OAuth2

Next, you need to share your spreadsheet file with that service account.  You can find the account name under 'Service Account'. It should be some randomly generated garbage followed by @developer.gserviceaccount.com.

### Usage:

This is very easy, the only things you need to do is manually create a Google Spreadsheet and share it with your OAuth service account.  Then just run the following program!

```sh
$ spreadtool.py -f "LameSpreadsheet.csv" -n "Google Spreadsheet Name"
```
If you'd like to specify the sheet that you'd like to write to, use the -s argument (defaults to 0)
```sh
$ spreadtool.py -f "LameSpreadsheet.csv" -n "Google Spreadsheet Name" -s 0
```