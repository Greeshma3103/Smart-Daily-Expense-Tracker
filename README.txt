SMART DAILY EXPENSE TRACKER (C + PYTHON)

Features:
- Record daily expenses with date, category, amount and note
- Save data in expenses.csv
- View all recorded expenses
- Monthly spending and remaining-budget report
- Warning when 80% of budget is used or budget is exceeded
- C performs calculation; Python manages menu, CSV data and interaction

Compile:
  Linux/macOS: gcc expense.c -o expense
  Windows (MinGW): gcc expense.c -o expense.exe

Run:
  Linux/macOS: python3 app.py
  Windows:     python app.py

Keep app.py, expense.c and the compiled C executable in the same folder.
The CSV file is created automatically when you first run the app.

Possible next upgrades:
- Tkinter desktop interface
- SQLite database
- monthly charts using matplotlib
- recurring bill reminders
- receipt photo / OCR input
- web or mobile dashboard
