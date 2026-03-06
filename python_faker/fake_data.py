%pip install Faker
from faker import Faker
f = Faker()
print(f.name())
%pip install Panda
f= Faker(["uz_UZ"])
print (f.name())
print (f.address())
print (f.phone_number())
%pip install Faker
# Reuse the Faker instance, or create a new one if needed
from faker import Faker
f= Faker(["uz_UZ"])
print ("Names:")
for _ in range(5000):
    print(f.name())
%pip install Faker
%pip install Pandas
%pip install Numpy
from faker import Faker
import random, pandas as pd, numpy as np
from datetime import datetime, timedelta

fake = Faker('uz_UZ')
random.seed(42)
np.random.seed(42)

def rand_date():
    return fake.date_time_between(start_date='-3y', end_date='now')

def money(minv,maxv):
    return round(random.uniform(minv,maxv),2)

N = 10

departments = []
for i in range(1, N+1):
    departments.append({
        "DepartmentID": i,
        "DepartmentName": fake.job()
    })

df_departments = pd.DataFrame(departments)
df_departments.to_csv("departments.csv", index=False)
df_departments.head()

N = 4000

rows = []
for i in range(1, N+1):
    rows.append({
        "CustomerID": i,
        "FullName": fake.name(),
        "DOB": fake.date_of_birth(minimum_age=18, maximum_age=80),
        "Email": fake.email(),
        "PhoneNumber": fake.phone_number(),
        "Address": fake.address().replace("\n", ", "),
        "NationalID": fake.ssn(),
        "TaxID": "TAX" + str(random.randint(100,10000)),
        "EmploymentStatus": random.choice(["Ishlaydi","Ishsiz","Talaba","Nafaqada","Tadbirkor"]),
        "AnnualIncome": money(1000,20000),
        "CreatedAt": rand_date(),
        "UpdatedAt": rand_date()
    })

df_customers = pd.DataFrame(rows)
df_customers.to_csv("customers.csv", index=False)
df_customers.head()

N = 8000

rows = []
for i in range(1, N+1):
    rows.append({
        "AccountID": i,
        "CustomerID": random.randint(1,4000),
        "AccountType": random.choice(["Savings","Checking","Business"]),
        "Balance": money(0,100000000),
        "Currency": random.choice(["USD"]),
        "Status": random.choice(["Active","Dormant","Closed"]),
        "BranchID": random.randint(1,50),
        "CreatedDate": rand_date()
    })

df_accounts = pd.DataFrame(rows)
df_accounts.to_csv("accounts.csv", index=False)
df_accounts.head()

len(df_customers)
N = 20000

rows = []
for i in range(1, N+1):
    rows.append({
        "TransactionID": i,
        "AccountID": random.randint(1,8000),
        "TransactionType": random.choice(["Deposit","Withdrawal","Transfer","Payment"]),
        "Amount": money(10000,10000000),
        "Currency": random.choice(["UZS","USD","EUR"]),
        "Date": rand_date(),
        "Status": random.choice(["Completed","Pending","Failed"]),
        "ReferenceNo": fake.uuid4()
    })

df_transactions = pd.DataFrame(rows)
df_transactions.to_csv("transactions.csv", index=False)
df_transactions.head()

N = 50

rows = []
for i in range(1, N+1):
    rows.append({
        "BranchID": i,
        "BranchName": fake.city() + " filiali",
        "Address": fake.address().replace("\n",", "),
        "City": fake.city(),
        "State": "O‘zbekiston",
        "Country": "UZ",
        "ManagerID": None,
        "ContactNumber": fake.phone_number()
    })

df_branches = pd.DataFrame(rows)
df_branches.to_csv("branches.csv", index=False)
df_branches.head()

N = 500
[3/6/2026 11:58 PM] Javohir: rows=[]
for i in range(1,N+1):
    rows.append({
        "EmployeeID": i,
        "BranchID": random.randint(1,50),
        "FullName": fake.name(),
        "Position": random.choice(["Kassir","Menejer","IT mutaxassis","Analitik","Operator"]),
        "Department": random.choice(["IT","Moliyaviy","Xavfsizlik","Kadrlar","Operatsiyalar"]),
        "Salary": money(3000000,15000000),
        "HireDate": rand_date(),
        "Status": random.choice(["Active","On Leave","Resigned"])
    })

df_employees = pd.DataFrame(rows)
df_employees.to_csv("employees.csv", index=False)
df_employees.head()

N = 2500

rows=[]
for i in range(1,N+1):
    rows.append({
        "CardID": i,
        "CustomerID": random.randint(1,4000),
        "CardNumber": fake.credit_card_number(),
        "CardType": random.choice(["Visa","MasterCard","Amex"]),
        "CVV": fake.credit_card_security_code(),
        "ExpiryDate": fake.credit_card_expire(),
        "Limit": money(5000000,50000000),
        "Status": random.choice(["Active","Blocked","Expired"])
    })

df_cards = pd.DataFrame(rows)
df_cards.to_csv("credit_cards.csv", index=False)
df_cards.head()

N = 10000

rows=[]
for i in range(1,N+1):
    rows.append({
        "TransactionID": i,
        "CardID": random.randint(1,2500),
        "Merchant": fake.company(),
        "Amount": money(5000,20000000),
        "Currency": "UZS",
        "Date": rand_date(),
        "Status": random.choice(["Completed","Declined","Pending"])
    })

df_cc_tx = pd.DataFrame(rows)
df_cc_tx.to_csv("cc_transactions.csv", index=False)
df_cc_tx.head()

N=3000

rows=[]
for i in range(1,N+1):
    rows.append({
        "UserID": i,
        "CustomerID": random.randint(1,4000),
        "Username": fake.user_name(),
        "PasswordHash": fake.sha256(),
        "LastLogin": rand_date()
    })

df_users = pd.DataFrame(rows)
df_users.to_csv("online_users.csv", index=False)
df_users.head()

N=5000

rows=[]
for i in range(1,N+1):
    rows.append({
        "PaymentID": i,
        "CustomerID": random.randint(1,4000),
        "BillerName": random.choice(["Elektr","Gaz","Internet","Mobil aloqa"]),
        "Amount": money(20000,2000000),
        "Date": rand_date(),
        "Status": random.choice(["Completed","Pending","Failed"])
    })

df_bills = pd.DataFrame(rows)
df_bills.to_csv("bill_payments.csv", index=False)
df_bills.head()

N=12000

rows=[]
for i in range(1,N+1):
    rows.append({
        "TransactionID": i,
        "CustomerID": random.randint(1,4000),
        "DeviceID": fake.uuid4(),
        "AppVersion": f"{random.randint(1,3)}.{random.randint(0,9)}",
        "TransactionType": random.choice(["Transfer","Payment","BalanceCheck"]),
        "Amount": money(10000,5000000),
        "Date": rand_date()
    })

df_mobile = pd.DataFrame(rows)
df_mobile.to_csv("mobile_transactions.csv", index=False)
df_mobile.head()

N = 1200

rows=[]
for i in range(1,N+1):
    start = rand_date()
    end = start + timedelta(days=30*random.choice([12,24,36,60]))
    rows.append({
        "LoanID": i,
        "CustomerID": random.randint(1,4000),
        "LoanType": random.choice(["Mortgage","Personal","Auto","Business"]),
        "Amount": money(5000000,500000000),
        "InterestRate": round(random.uniform(5,25),2),
        "StartDate": start,
        "EndDate": end,
        "Status": random.choice(["Active","Closed","Defaulted"])
    })

df_loans = pd.DataFrame(rows)
df_loans.to_csv("loans.csv", index=False)
df_loans.head()

N = 5000

rows=[]
for i in range(1,N+1):
    loan_id = random.randint(1,1200)
    paid = money(100000,5000000)
    rows.append({
        "PaymentID": i,
        "LoanID": loan_id,
        "AmountPaid": paid,
        "PaymentDate": rand_date(),
        "RemainingBalance": money(0,300000000)
    })

df_loan_payments = pd.DataFrame(rows)
df_loan_payments.to_csv("loan_payments.csv", index=False)
df_loan_payments.head()

N = 4000

rows=[]
for i in range(1,N+1):
    rows.append({
        "CustomerID": i,
        "CreditScore": random.randint(300,850),
        "UpdatedAt": rand_date()
    })
[3/6/2026 11:58 PM] Javohir: df_credit_scores = pd.DataFrame(rows)
df_credit_scores.to_csv("credit_scores.csv", index=False)
df_credit_scores.head()

N = 200

rows=[]
for i in range(1,N+1):
    rows.append({
        "DebtID": i,
        "CustomerID": random.randint(1,4000),
        "AmountDue": money(100000,50000000),
        "DueDate": rand_date(),
        "CollectorAssigned": fake.name()
    })

df_debt = pd.DataFrame(rows)
df_debt.to_csv("debt_collection.csv", index=False)
df_debt.head()

N = 4000

rows=[]
for i in range(1,N+1):
    rows.append({
        "KYCID": i,
        "CustomerID": i,
        "DocumentType": random.choice(["Passport","ID Card","Haydovchilik guvohnomasi"]),
        "DocumentNumber": fake.bothify(text="??######"),
        "VerifiedBy": fake.name()
    })

df_kyc = pd.DataFrame(rows)
df_kyc.to_csv("kyc.csv", index=False)
df_kyc.head()

N = 500

rows=[]
for i in range(1,N+1):
    rows.append({
        "FraudID": i,
        "CustomerID": random.randint(1,4000),
        "TransactionID": random.randint(1,20000),
        "RiskLevel": random.choice(["Low","Medium","High"]),
        "ReportedDate": rand_date()
    })

df_fraud = pd.DataFrame(rows)
df_fraud.to_csv("fraud_detection.csv", index=False)
df_fraud.head()

N = 100

rows=[]
for i in range(1,N+1):
    rows.append({
        "CaseID": i,
        "CustomerID": random.randint(1,4000),
        "CaseType": random.choice(["Large Transfer","Identity Fraud","Suspicious Activity"]),
        "Status": random.choice(["Open","Closed","Under Investigation"]),
        "InvestigatorID": random.randint(1,500)
    })

df_aml = pd.DataFrame(rows)
df_aml.to_csv("aml_cases.csv", index=False)
df_aml.head()

N = 200

rows=[]
for i in range(1,N+1):
    rows.append({
        "ReportID": i,
        "ReportType": random.choice(["Monthly","Quarterly","AML","Audit"]),
        "SubmissionDate": rand_date()
    })

df_reports = pd.DataFrame(rows)
df_reports.to_csv("regulatory_reports.csv", index=False)
df_reports.head()

N = 10

rows=[]
for i in range(1,N+1):
    rows.append({
        "DepartmentID": i,
        "DepartmentName": random.choice(["IT","Moliya","Audit","Kadrlar","Risk","Xavfsizlik"]),
        "ManagerID": random.randint(1,500)
    })

df_departments = pd.DataFrame(rows)
df_departments.to_csv("departments.csv", index=False)
df_departments.head()

N = 500

rows=[]
for i in range(1,N+1):
    rows.append({
        "SalaryID": i,
        "EmployeeID": i,
        "BaseSalary": money(4000000,15000000),
        "Bonus": money(0,3000000),
        "Deductions": money(0,1000000),
        "PaymentDate": rand_date()
    })

df_salaries = pd.DataFrame(rows)
df_salaries.to_csv("salaries.csv", index=False)
df_salaries.head()

N = 5000

rows=[]
for i in range(1, N+1):
    check_in = fake.date_time_this_year()
    check_out = check_in + timedelta(hours=random.randint(6,10))
    rows.append({
        "AttendanceID": i,
        "EmployeeID": random.randint(1,500),
        "CheckInTime": check_in,
        "CheckOutTime": check_out,
        "TotalHours": (check_out - check_in).seconds // 3600
    })

df_att = pd.DataFrame(rows)
df_att.to_csv("employee_attendance.csv", index=False)
df_att.head()

N = 1200

rows=[]
for i in range(1, N+1):
    rows.append({
        "InvestmentID": i,
        "CustomerID": random.randint(1,4000),
        "InvestmentType": random.choice(["Deposit","Bond","ETF","Fund"]),
        "Amount": money(1000000,500000000),
        "ROI": round(random.uniform(1,20),2),
        "MaturityDate": rand_date()
    })

df_invest = pd.DataFrame(rows)
df_invest.to_csv("investments.csv", index=False)
df_invest.head()

N = 1500

rows=[]
for i in range(1, N+1):
    rows.append({
        "AccountID": i,
        "CustomerID": random.randint(1,4000),
        "BrokerageFirm": random.choice(["Freedom Finance","TBC Capital","Xalq Broker"]),
        "TotalInvested": money(2000000,300000000),
        "CurrentValue": money(2000000,350000000)
    })

df_stocks = pd.DataFrame(rows)
df_stocks.to_csv("stock_trading_accounts.csv", index=False)
df_stocks.head()

N = 2500

pairs = ["USD/UZS","EUR/UZS","RUB/UZS","CNY/UZS"]
[3/6/2026 11:58 PM] Javohir: rows=[]
for i in range(1, N+1):
    rows.append({
        "FXID": i,
        "CustomerID": random.randint(1,4000),
        "CurrencyPair": random.choice(pairs),
        "ExchangeRate": round(random.uniform(1000,15000),2),
        "AmountExchanged": money(100,10000)
    })

df_fx = pd.DataFrame(rows)
df_fx.to_csv("foreign_exchange.csv", index=False)
df_fx.head()

N = 2000

rows=[]
for i in range(1, N+1):
    rows.append({
        "PolicyID": i,
        "CustomerID": random.randint(1,4000),
        "InsuranceType": random.choice(["Life","Auto","Health","Property"]),
        "PremiumAmount": money(50000,3000000),
        "CoverageAmount": money(10000000,300000000)
    })

df_insurance = pd.DataFrame(rows)
df_insurance.to_csv("insurance_policies.csv", index=False)
df_insurance.head()

N = 800

rows=[]
for i in range(1, N+1):
    rows.append({
        "ClaimID": i,
        "PolicyID": random.randint(1,2000),
        "ClaimAmount": money(1000000,50000000),
        "Status": random.choice(["Pending","Approved","Rejected"]),
        "FiledDate": rand_date()
    })

df_claims = pd.DataFrame(rows)
df_claims.to_csv("claims.csv", index=False)
df_claims.head()

N = 15000

actions = ["Login","Logout","Password Change","Failed Login","View Statement"]

rows=[]
for i in range(1, N+1):
    rows.append({
        "LogID": i,
        "UserID": random.randint(1,4000),
        "ActionType": random.choice(actions),
        "Timestamp": rand_date()
    })

df_logs = pd.DataFrame(rows)
df_logs.to_csv("user_access_logs.csv", index=False)
df_logs.head()

N = 400

rows=[]
for i in range(1, N+1):
    rows.append({
        "IncidentID": i,
        "AffectedSystem": random.choice(["Core Banking","Mobile App","Website","Internal Network"]),
        "ReportedDate": rand_date(),
        "ResolutionStatus": random.choice(["Resolved","Open","Under Investigation"])
    })

df_cyber = pd.DataFrame(rows)
df_cyber.to_csv("cyber_security_incidents.csv", index=False)
df_cyber.head()

N = 2000

industries = ["Supermarket","Restaurant","Tech","Clothing","Pharmacy","Services"]

rows=[]
for i in range(1, N+1):
    rows.append({
        "MerchantID": i,
        "MerchantName": fake.company(),
        "Industry": random.choice(industries),
        "Location": fake.address().replace("\n"," "),
        "CustomerID": random.randint(1,4000)
    })

df_merchants = pd.DataFrame(rows)
df_merchants.to_csv("merchants.csv", index=False)
df_merchants.head()

N = 12000

payments = ["Card","Transfer","Cash","QR"]

rows=[]
for i in range(1, N+1):
    rows.append({
        "TransactionID": i,
        "MerchantID": random.randint(1,2000),
        "Amount": money(5000,5000000),
        "PaymentMethod": random.choice(payments),
        "Date": rand_date()
    })

df_merchant_tx = pd.DataFrame(rows)
df_merchant_tx.to_csv("merchant_transactions.csv", index=False)
df_merchant_tx.head()

import pandas as pd
import random
from faker import Faker

fake = Faker('uz_UZ')

num_branches = 50  


employee_ids = list(range(1, 5001))

branches = []

for i in range(1, num_branches + 1):
    branch = {
        "BranchID": i,
        "BranchName": fake.company(),
        "Address": fake.address().replace("\n", ", "),
        "City": fake.city(),
        "State": fake.state(),  # use state() instead of region()
        "Country": "Uzbekistan",
        "ManagerID": random.choice(employee_ids),   # INT BO‘LDI!
        "ContactNumber": fake.phone_number()
    }
    branches.append(branch)

df = pd.DataFrame(branches)
df.to_csv("branches.csv", index=False, encoding="utf-8-sig")

df.head()
len(df)
%pip install pyodbc pandas
