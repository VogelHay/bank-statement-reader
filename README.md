# bank-statement-reader
This program will read bank statements PDFs using *determined pdf compiler*, storing the raw output into a tab within a raw-statements.csv.
It will then categorize the data depending on the type of purchase made into sorted-statements.csv, populating a list of vendors and storing them within a vendor.txt file.
Finally, sorted-statements.csv will be exported into a Google sheet and used to observe spending habits, helping the user develop more transparency on their spending practices.

Steps:
1. Parse bank statement PDFs
  a. Parse monthly statements, trimming unessential strings from the output.
  b. Append trimmed data to raw-statements.csv using a PDF analyzer. Individual entries will consist of Vendor, Amount, and Date.
  c. Categorize data, cross-referencing between "Vendor" and vendors.txt.
  d. In the event of a Vendor that doesn't appear in vendors.txt, it gets stored in a "Misc." category.
  e. Append categorized output to sorted-statements.csv.
2. Upload to Google Sheets
  a. Import sorted-statements.csv into hidden tab on Google Sheet
  b. Using "Category" (ignoring misc.), append statement entries into hidden Category tabs.
  c. Calculate weekly and monthly sums of each Category in collector tabs.
  d. Compile important data in summary tab.
  e. Store last-uploaded line no. in line-sync.txt to preserve continuity and prevent unnecessary API calls.
3. Sorting Miscellaneous Vendors
  a. Pull Misc. statements as needed into misc.csv
  b. Edit misc.csv to Categorize the unsorted Vendors.
  c. Run sync-vendors.py to read sorted-statements.csv, only processing entries in the Misc. category.
  d. Check for identical entries (besides Vendor) between misc.csv and sorted-statements.csv, updating sorted-statements.csv with the Vendors from misc.csv
