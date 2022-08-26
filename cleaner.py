from email_validator import validate_email, EmailNotValidError
import pandas as pd

def check_email(email):
    try:
        v = validate_email(email, check_deliverability=True)
        email = v["email"]
        return True
    except EmailNotValidError:
        return False

File = pd.ExcelFile('mails.xlsx')
dataFrame = File.parse('mails')
validEmails = []
InvalidEmails = []
emails_list = dataFrame['mails']
print(f"Total of emais: {len(emails_list)}")
emails_list = list(set(emails_list))
print("Process started")
for emialToSend in emails_list:
    emialToSend = emialToSend.lower()
    if check_email(emialToSend):
        validEmails.append(emialToSend)
    else:
        InvalidEmails.append(emialToSend)
filepath = f'bd_cleaned_valid.xlsx'
df = pd.DataFrame(zip(validEmails), columns=["Valid emails"])
df.to_excel(filepath, index=False)
filepath = f'bd_cleaned_invalid.xlsx'
df = pd.DataFrame(zip(InvalidEmails), columns=["Invalid emails"])
df.to_excel(filepath, index=False)
print(f"Valid emails: {len(validEmails)}, Invalid emails: {len(InvalidEmails)}")
print("Process finished")