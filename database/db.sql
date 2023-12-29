-- Active: 1703487294317@@127.0.0.1@3306@nft_project
Create DATABASE IF NOT EXISTS NFT_PROJECT;
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

INSERT INTO NFT_DETAILS VALUES (001, "Axie Infinity Axis", 30, "It is a INFINITY AXS game-based nft where you can buy your private areas to
          play, you can have your private island in the game so that you can play, 
          enjoy and meetup their. Then what are you waiting for go buy and enjoy with your friends.");
INSERT INTO NFT_DETAILS VALUES
    (002, "THE SANDBOX SAND", 65, "It is a SANDBOX SAND game-based nft where you can buy your private areas to
          play, you can have your private island in the game so that you can play, 
          enjoy and meetup their. Then what are you waiting for go buy and enjoy with your friends.");
INSERT INTO NFT_DETAILS VALUES(003, "CRYPTO PUNK", 85, "Cryptopunks is an NFT project released on the Ethereum blockchain by Larva Labs,
          and consists of 10,000 unique pixelated characters. Some are human, some aliens,
          some zombies and some apes. 
          Each punk has certain attributes that are of a different level of rarity amongst the entire fleet");
INSERT INTO NFT_DETAILS VALUES(004, "Net Artwork", 41, "It is a NFT made by Gen-z and you can get assets of the pure art of modern tech so what are you waiting for just go and grab a new and trendy art of modern world.");
INSERT INTO NFT_DETAILS VALUES(005, "Annual FUNCTION token", 54, "It is a NFT that gives you assets of annual function tokens and fest so what are you waiting for grab your toke of enjoyment.");