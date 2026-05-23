# bank-statement-reader
This program will read bank statements PDFs using *determined pdf compiler* (probably pdfplumber??), storing the raw output into a tab within a raw-statements.csv. \n
It will then categorize the data depending on the type of purchase made into sorted-statements.csv, populating a list of vendors and storing them within a vendor.txt file.\n
Finally, sorted-statements.csv will be exported into a Google sheet and used to observe spending habits, helping the user develop more transparency on their spending practices.\n\n

Steps:\n
1. Parse bank statement PDFs\n
  a. Parse monthly statements, trimming unessential strings from the output.\n
  b. Append trimmed data to raw-statements.csv using a PDF analyzer. Individual entries will consist of Vendor, Amount, and Date.\n
  c. Categorize data, cross-referencing between "Vendor" and vendors.txt.\n
  d. In the event of a Vendor that doesn't appear in vendors.txt, it gets stored in a "Misc." category.\n
  e. Append categorized output to sorted-statements.csv.\n
2. Upload to Google Sheets\n
  a. Import sorted-statements.csv into hidden tab on Google Sheet\n
  b. Using "Category" (ignoring misc.), append statement entries into hidden Category tabs.\n
  c. Calculate weekly and monthly sums of each Category in collector tabs.\n
  d. Compile important data in summary tab.\n
  e. Store last-uploaded line no. in line-sync.txt to preserve continuity and prevent unnecessary API calls.\n
3. Sorting Miscellaneous Vendors\n
  a. Pull Misc. statements as needed into misc.csv\n
  b. Edit misc.csv to Categorize the unsorted Vendors.\n
  c. Run sync-vendors.py to read sorted-statements.csv, only processing entries in the Misc. category.\n
  d. Check for identical entries (besides Vendor) between misc.csv and sorted-statements.csv, updating sorted-statements.csv with the Vendors from misc.csv\n
