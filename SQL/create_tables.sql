[11/27/2025 9:19 PM] SQL: CREATE TABLE Customers (
    CustomerID INT,
    FullName VARCHAR(255),
    DOB DATE,
    Email VARCHAR(255),
    PhoneNumber VARCHAR(50),
    Address VARCHAR(255),
    NationalID VARCHAR(50),
    TaxID VARCHAR(50),
    EmploymentStatus VARCHAR(50),
    AnnualIncome DECIMAL(18,2),
    CreatedAt DATETIME,
    UpdatedAt DATETIME
);

CREATE TABLE Accounts (
    AccountID INT,
    CustomerID INT,
    AccountType VARCHAR(50),
    Balance DECIMAL(18,2),
    Currency VARCHAR(10),
    Status VARCHAR(50),
    BranchID INT,
    CreatedDate DATETIME
);

CREATE TABLE Transactions (
    TransactionID INT,
    AccountID INT,
    TransactionType VARCHAR(50),
    Amount DECIMAL(18,2),
    Currency VARCHAR(10),
    Date DATETIME,
    Status VARCHAR(50),
    ReferenceNo VARCHAR(100)
);

CREATE TABLE Branches (
    BranchID INT,
    BranchName VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    Country VARCHAR(100),
    ManagerID INT,
    ContactNumber VARCHAR(50)
);

CREATE TABLE Employees (
    EmployeeID INT,
    BranchID INT,
    FullName VARCHAR(255),
    Position VARCHAR(100),
    DepartmentID INT,
    Salary DECIMAL(18,2),
    HireDate DATE,
    Status VARCHAR(50)
);

CREATE TABLE CreditCards (
    CardID INT,
    CustomerID INT,
    CardNumber VARCHAR(20),
    CardType VARCHAR(50),
    CVV VARCHAR(10),
    ExpiryDate DATE,
    Limit DECIMAL(18,2),
    Status VARCHAR(50)
);

CREATE TABLE CreditCardTransactions (
    TransactionID INT,
    CardID INT,
    Merchant VARCHAR(255),
    Amount DECIMAL(18,2),
    Currency VARCHAR(10),
    Date DATETIME,
    Status VARCHAR(50)
);

CREATE TABLE OnlineBankingUsers (
    UserID INT,
    CustomerID INT,
    Username VARCHAR(100),
    PasswordHash VARCHAR(255),
    LastLogin DATETIME
);

CREATE TABLE BillPayments (
    PaymentID INT,
    CustomerID INT,
    BillerName VARCHAR(255),
    Amount DECIMAL(18,2),
    Date DATETIME,
    Status VARCHAR(50)
);

CREATE TABLE MobileBankingTransactions (
    TransactionID INT,
    CustomerID INT,
    DeviceID VARCHAR(100),
    AppVersion VARCHAR(50),
    TransactionType VARCHAR(50),
    Amount DECIMAL(18,2),
    Date DATETIME
);

CREATE TABLE Loans (
    LoanID INT,
    CustomerID INT,
    LoanType VARCHAR(50),
    Amount DECIMAL(18,2),
    InterestRate DECIMAL(5,2),
    StartDate DATE,
    EndDate DATE,
    Status VARCHAR(50)
);

CREATE TABLE LoanPayments (
    PaymentID INT,
    LoanID INT,
    AmountPaid DECIMAL(18,2),
    PaymentDate DATE,
    RemainingBalance DECIMAL(18,2)
);

CREATE TABLE CreditScores (
    CustomerID INT,
    CreditScore INT,
    UpdatedAt DATETIME
);

CREATE TABLE DebtCollection (
    DebtID INT,
    CustomerID INT,
    AmountDue DECIMAL(18,2),
    DueDate DATE,
    CollectorAssigned VARCHAR(255)
);

CREATE TABLE KYC (
    KYCID INT,
    CustomerID INT,
    DocumentType VARCHAR(50),
    DocumentNumber VARCHAR(100),
    VerifiedBy VARCHAR(255)
);

CREATE TABLE FraudDetection (
    FraudID INT,
    CustomerID INT,
    TransactionID INT,
    RiskLevel VARCHAR(50),
    ReportedDate DATETIME
);

CREATE TABLE AMLCases (
    CaseID INT,
    CustomerID INT,
    CaseType VARCHAR(100),
    Status VARCHAR(50),
    InvestigatorID INT
);

CREATE TABLE RegulatoryReports (
    ReportID INT,
    ReportType VARCHAR(100),
    SubmissionDate DATE
);

CREATE TABLE Departments (
    DepartmentID INT,
    DepartmentName VARCHAR(100),
    ManagerID INT
);

CREATE TABLE Salaries (
    SalaryID INT,
    EmployeeID INT,
    BaseSalary DECIMAL(18,2),
    Bonus DECIMAL(18,2),
    Deductions DECIMAL(18,2),
    PaymentDate DATE
);

CREATE TABLE EmployeeAttendance (
    AttendanceID INT,
    EmployeeID INT,
    CheckInTime DATETIME,
    CheckOutTime DATETIME,
    TotalHours DECIMAL(5,2)
);

CREATE TABLE Investments (
    InvestmentID INT,
    CustomerID INT,
    InvestmentType VARCHAR(50),
    Amount DECIMAL(18,2),
    ROI DECIMAL(5,2),
    MaturityDate DATE
);
[11/27/2025 9:19 PM] SQL: CREATE TABLE StockTradingAccounts (
    AccountID INT,
    CustomerID INT,
    BrokerageFirm VARCHAR(100),
    TotalInvested DECIMAL(18,2),
    CurrentValue DECIMAL(18,2)
);

CREATE TABLE ForeignExchange (
    FXID INT,
    CustomerID INT,
    CurrencyPair VARCHAR(20),
    ExchangeRate DECIMAL(10,4),
    AmountExchanged DECIMAL(18,2)
);

CREATE TABLE InsurancePolicies (
    PolicyID INT,
    CustomerID INT,
    InsuranceType VARCHAR(100),
    PremiumAmount DECIMAL(18,2),
    CoverageAmount DECIMAL(18,2)
);

CREATE TABLE Claims (
    ClaimID INT,
    PolicyID INT,
    ClaimAmount DECIMAL(18,2),
    Status VARCHAR(50),
    FiledDate DATE
);

CREATE TABLE UserAccessLogs (
    LogID INT,
    UserID INT,
    ActionType VARCHAR(100),
    Timestamp DATETIME
);

CREATE TABLE CyberSecurityIncidents (
    IncidentID INT,
    AffectedSystem VARCHAR(100),
    ReportedDate DATETIME,
    ResolutionStatus VARCHAR(50)
);

CREATE TABLE Merchants (
    MerchantID INT,
    MerchantName VARCHAR(255),
    Industry VARCHAR(100),
    Location VARCHAR(255)
);

CREATE TABLE MerchantTransactions (
    TransactionID INT,
    MerchantID INT,
    CustomerID INT,
    Amount DECIMAL(18,2),
    PaymentMethod VARCHAR(50),
    Date DATETIME
);
