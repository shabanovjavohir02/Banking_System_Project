USE BankingSystem 

--1-KPI
SELECT TOP 3 
    c.CustomerID,
    c.FullName,
    SUM(A.Balance) AS TotalBalance
FROM Customers c
JOIN Accounts a ON c.CustomerID = a.CustomerID
GROUP BY c.CustomerID, c.FullName
ORDER BY TotalBalance DESC

--2-KPI
SELECT * FROM Loans 
SELECT * FROM Customers 
	
SELECT
	c.FullName,
    COUNT(*) AS ActiveLoanCount
FROM Customers c
JOIN Loans l ON c.CustomerID = l.CustomerID
WHERE l.Status = 'Active'
GROUP BY c.CustomerID, c.FullName
HAVING COUNT(*) > 1
ORDER BY ActiveLoanCount DESC

--3-KPI
SELECT * FROM FraudDetection 
SELECT * FROM Customers 
SELECT * FROM Accounts 
SELECT * FROM Transactions 

select 
	 c.FullName,
	 fd.FraudID,
	 a.CustomerID,
	 fd.RiskLevel,
	 fd.ReportedDate,
	 t.Amount,
	 t.Currency,
	 t.TransactionType,
	 t.Date as TransactionDate
from FraudDetection as fd
left join Transactions t on fd.TransactionID = t.TransactionID 
left join Accounts a on a.AccountID = t.AccountID
left join Customers c on fd.CustomerID = c.CustomerID 
where fd.RiskLevel = 'High'
Order by fd.ReportedDate Desc

--4-KPI
SELECT * FROM Loans 
SELECT * FROM Customers 
SELECT * FROM Accounts 
SELECT * FROM Branches 

SELECT 
    b.BranchID,
    b.BranchName,
    SUM(l.Amount) AS TotalLoanAmount
FROM Loans l
JOIN Accounts a ON l.CustomerID = a.CustomerID
JOIN Branches b ON a.BranchID = b.BranchID
GROUP BY b.BranchID, b.BranchName
ORDER BY TotalLoanAmount DESC;

--5-KPI     
select * from Transactions 
select * from Accounts
select * from Customers 

--Amountni 10.000 dan 5000 ga o'zgartirdim. 10.000 da hech narsa chiqmadi chunki.

WITH LargeTx AS (
    SELECT 
        t.TransactionID,
        a.CustomerID,
        t.Amount,
        t.Date
    FROM Transactions t
    JOIN Accounts a ON t.AccountID = a.AccountID
    WHERE t.Amount > 5000
),
Pairs AS (
    SELECT 
        L1.CustomerID,
        L1.TransactionID AS Tx1,
        L2.TransactionID AS Tx2,
        L1.Amount,
        L1.Date AS Time1,
        L2.Date AS Time2,
        DATEDIFF(MINUTE, L1.Date, L2.Date) AS DiffMinutes
    FROM LargeTx L1
    JOIN LargeTx L2 
        ON L1.CustomerID = L2.CustomerID
       AND L1.TransactionID < L2.TransactionID
       AND ABS(DATEDIFF(MINUTE, L1.Date, L2.Date)) < 60
)
SELECT DISTINCT CustomerID
FROM Pairs
ORDER BY CustomerID;

--6-KPI
select * from Customers 
select * from Accounts
select * from Branches 
select * from Transactions 

--2 ta narsani o'zgartirdim:
--1) Country ni State ga almashtirdim. Chunki hammasi USA edi menda.
--2) 10 minutni 30 minut qildim. 10 minutda hech narsa chiqmadi chunki.

WITH Tx AS (
    SELECT 
        t.TransactionID,
        t.AccountID,
        t.Date AS TxTime,
        b.State,
        a.CustomerID,
        c.FullName
    FROM Transactions t
    JOIN Accounts a ON t.AccountID = a.AccountID
    JOIN Customers c ON a.CustomerID = c.CustomerID
    JOIN Branches b ON a.BranchID = b.BranchID
),
Pairs AS (
    SELECT 
        t1.CustomerID,
        t1.FullName,
        t1.TransactionID AS Tx1,
        t1.State AS State1,
        t1.TxTime AS Time1,
        t2.TransactionID AS Tx2,
        t2.State AS State2,
        t2.TxTime AS Time2,
        DATEDIFF(MINUTE, t1.TxTime, t2.TxTime) AS DiffMinutes
    FROM Tx t1
    JOIN Tx t2 
        ON t1.CustomerID = t2.CustomerID
        AND t1.TransactionID < t2.TransactionID      -- o‘zini o‘ziga qo‘shmaslik
        AND t1.State <> t2.State                     -- different states
        AND ABS(DATEDIFF(MINUTE, t1.TxTime, t2.TxTime)) <= 30
)
SELECT *
FROM Pairs
ORDER BY DiffMinutes;

