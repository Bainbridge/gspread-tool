Gspread-Tool
===================


This is a tool that can turn a regular old spreadsheet file (*.csv) into a Google Spreadsheet!

--------
### Prerequisites:

- Get OAuth2 Service account
- Install gspread (via pip)
- Install OAuth2Client (via pip)

 

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