# Banking_System_Project

## Overview
This project implements a relational **banking system database** using SQL. It models various banking operations such as customer management, accounts, transactions, loans, credit cards, and fraud monitoring. The project also includes analytical SQL queries to extract insights from banking data.

## Technologies Used
- SQL
- Python
- Faker
- Pandas
- NumPy

## Database Structure
The database contains multiple interconnected tables representing banking services:

### Core Banking
- Customers
- Accounts
- Transactions
- Branches
- Employees

### Financial Services
- Loans
- LoanPayments
- CreditCards
- CreditCardTransactions
- Investments
- StockTradingAccounts
- ForeignExchange

### Digital Banking
- OnlineBankingUsers
- MobileBankingTransactions
- BillPayments

### Risk & Compliance
- FraudDetection
- AMLCases
- KYC
- DebtCollection
- CreditScores

### Additional Services
- InsurancePolicies
- Claims
- Merchants
- MerchantTransactions
- UserAccessLogs
- CyberSecurityIncidents



## Data Generation
To simulate a realistic banking environment, large-scale synthetic datasets were generated using **Python and the Faker library (uz_UZ locale)**. The generated data includes thousands of records for customers, accounts, transactions, loans, and digital banking activities. All datasets were exported as **CSV files** and imported into the SQL database.

## Key Performance Indicators (KPIs)
The project includes analytical SQL queries for banking insights:

- Top 3 customers by total account balance
- Customers with multiple active loans
- High-risk fraud transactions
- Loan distribution by branch
- Suspicious large transactions within a short time window
- Rapid transactions from different locations

## Conclusion
This project demonstrates **relational database design, synthetic data generation, and SQL-based financial analytics** in a simulated banking ecosystem.
