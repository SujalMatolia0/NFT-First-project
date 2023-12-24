USE NFT_PROJECT;
CREATE TABLE USER_DETAILS (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    FIRST_NAME VARCHAR(255),
    LAST_NAME VARCHAR(255),
    EMAIL VARCHAR(255) UNIQUE,
    PASS VARCHAR(255),
    CON_PASS VARCHAR(255),
    CREDIT_CARD VARCHAR(16),
    CVV INT,
    BALANCE INT,
    REGISTRATION_DATE DATE
);

CREATE TABLE NFT_DETAILS (
    NFT_ID INT PRIMARY KEY,
    NFT_NAME VARCHAR(255),
    PRICE INT,
    DESCIPTION TEXT
);

CREATE TABLE USER_NFT (
    ID VARCHAR(255),
    NFT_ID INT,
    QUANTITY INT,
    Foreign Key (ID) REFERENCES USER_DETAILS(EMAIL),
    Foreign Key (NFT_ID) REFERENCES NFT_DETAILS(NFT_ID)
);

CREATE TABLE USER_TRANSACTION (
    TRANS_ID INT PRIMARY KEY,
    ID VARCHAR(255),
    NFT_ID INT,
    TRANS_DATE DATE,
    STATUS VARCHAR(50) CHECK (STATUS IN ('Success','Fail')),
    Foreign Key (ID) REFERENCES USER_DETAILs(EMAIL),
    Foreign Key (NFT_ID) REFERENCES NFT_DETAILS(NFT_ID)
);

