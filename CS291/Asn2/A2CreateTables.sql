alter session set NLS_DATE_FORMAT='DD-MON-YY';
DROP TABLE Friend;
DROP TABLE Fan;
DROP TABLE Rent;
DROP TABLE Rate;
DROP TABLE WaitingList;
DROP TABLE Buy;
DROP Table Song;
DROP TABLE Album;
DROP TABLE Movie;
DROP TABLE Genre;
DROP TABLE Artist;
DROP TABLE Media;
DROP TABLE Customer;

CREATE TABLE Customer(
username		CHAR(20),
credit			INTEGER,
email			CHAR(32),
emailVisibility   	CHAR(1),
CHECK(emailVisibility = 'A' OR emailVisibility = 'F' OR emailVisibility = 'N'),
PRIMARY KEY(username));

CREATE TABLE Media(
id	INTEGER,
price 	INTEGER,
title	CHAR(20),
PRIMARY KEY(id));


CREATE TABLE Artist(
AId	INTEGER,
name	CHAR(32),
PRIMARY KEY(AId));


CREATE TABLE Genre(
name	CHAR(15),
PRIMARY KEY(name));


CREATE TABLE Movie(
mid		INTEGER,
director	CHAR(32),
quantity	INTEGER,
year		INTEGER,
s_rentFee	INTEGER,
l_rentFee	INTEGER,
genre		CHAR(15) NOT NULL,
PRIMARY KEY(mid),
FOREIGN KEY(mid) REFERENCES Media,
FOREIGN KEY(genre) REFERENCES Genre);

CREATE TABLE Album(
albumid	INTEGER,
year INTEGER, 
PRIMARY KEY(albumid),
FOREIGN KEY(albumid) REFERENCES Media);

CREATE TABLE Song(
albumid		INTEGER,
title		CHAR(32),
artistID	INTEGER NOT NULL,
PRIMARY KEY(albumid,title),
FOREIGN KEY(albumid) REFERENCES Album,
FOREIGN KEY (artistID) REFERENCES Artist);


CREATE TABLE Buy(
username	CHAR(20),
mediaID		INTEGER,
purchaseDate	DATE,
visibility	CHAR(1),
CHECK(visibility = 'A' OR visibility = 'F' OR visibility = 'N'),
PRIMARY KEY(username,mediaID),
FOREIGN KEY(mediaID) REFERENCES Media,
FOREIGN KEY(username) REFERENCES Customer);


CREATE TABLE WaitingList(
username	CHAR(20),
movieID		INTEGER,
since		DATE,
PRIMARY KEY(username,movieID),
FOREIGN KEY(username) REFERENCES Customer,
FOREIGN KEY(movieID) REFERENCES Movie);


CREATE TABLE Rate(
username	CHAR(20),
movieID		INTEGER,
rating		INTEGER,
PRIMARY KEY(username,movieID),
FOREIGN KEY(username) REFERENCES Customer,
FOREIGN KEY(movieID) REFERENCES Movie);


CREATE TABLE Rent(
username	CHAR(20),
movieID		INTEGER,
since		DATE,
rentmode	CHAR(1),
CHECK(rentmode = 'L' OR rentmode = 'S' OR rentmode ='R'),
visibility	CHAR(1),
CHECK(visibility = 'A' OR visibility = 'F' OR visibility = 'N'),
PRIMARY KEY(username,movieID,since),
FOREIGN KEY(username) REFERENCES Customer,
FOREIGN KEY(movieID) REFERENCES Movie);


CREATE TABLE Fan(
username	CHAR(20),
artistID	INTEGER,
since		DATE,
PRIMARY KEY(username,artistID),
FOREIGN KEY(username) REFERENCES Customer,
FOREIGN KEY(artistID) REFERENCES Artist);

CREATE TABLE Friend(
user1		CHAR(20),
user2		CHAR(20),
PRIMARY KEY(user1,user2),
FOREIGN KEY(user1) REFERENCES Customer,
FOREIGN KEY(user2) REFERENCES Customer);


