CREATE DATABASE Manufacturer;

CREATE SCHEMA Prod_Compt;

CREATE SCHEMA Compt_Supp;


CREATE TABLE [Prod_Compt].[Prod_Compt](
	[prod_id] INT NOT NULL,
	[comp_id] INT NOT NULL,
	[quantitiy_comp] [int] NOT NULL,
	PRIMARY KEY ([prod_id], [comp_id])
	);


CREATE TABLE [Compt_Supp].[Compt_Supp](
	[supp_id] INT NOT NULL,
	[comp_id] INT NOT NULL,
	[order_date] [int] NOT NULL,
	[quantity] [date] NOT NULL,
	PRIMARY KEY ([supp_id], [comp_id])
	);

CREATE TABLE [Compt_Supp].[Supplier](
	[supp_id] [int],
	[supp_name] [nvarchar](50) Not NULL,
	[supp_location] [nvarchar](50) Not NULL,
	[supp_country] [nvarchar](50) Not NULL,
	[is_active] [bit] Not NULL
	PRIMARY KEY ([supp_id])
	);

CREATE TABLE [Prod_Compt].[Product](
	[prod_id] [int],
	[prod_name] [nvarchar](50) Not NULL,
	[quantity] [int] Not NULL
	PRIMARY KEY ([prod_id])

	);

CREATE TABLE [Prod_Compt].[Component](
	[comp_id] [int],
	[comp_name] [nvarchar](50) Not NULL,
	[description] [nvarchar](50) Not NULL,
	[quantity_comp] [int] Not NULL
	PRIMARY KEY ([comp_id])

	);

ALTER TABLE Prod_Compt.Prod_Compt ADD CONSTRAINT FK_prod FOREIGN KEY (prod_id)
REFERENCES Prod_Compt.Product (prod_id) 
ON UPDATE NO ACTION
ON DELETE NO ACTION
ALTER TABLE Prod_Compt.Prod_Compt ADD CONSTRAINT FK_comp FOREIGN KEY (comp_id)
REFERENCES Prod_Compt.Component (comp_id) 

ALTER TABLE Compt_Supp.Compt_Supp ADD CONSTRAINT FK_supp FOREIGN KEY (supp_id)
REFERENCES Compt_Supp.Supplier (supp_id) 

ALTER TABLE Compt_Supp.Compt_Supp ADD CONSTRAINT FK_supp FOREIGN KEY (supp_id)
REFERENCES Compt_Supp.Supplier (supp_id) 

ALTER TABLE Compt_Supp.Compt_Supp ADD CONSTRAINT FK_comp FOREIGN KEY (comp_id)
REFERENCES Prod_Compt.Component (comp_id)