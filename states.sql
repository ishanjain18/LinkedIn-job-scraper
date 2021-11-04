drop table if exists states;

create table states(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(255) NOT NULL
);

insert into states 
	(state)
values
	('Andaman and Nicobar'),
	('Andhra Pradesh'),
	('Arunachal Pradesh'),
	('Assam'),
	('Bihar'),
	('Chandigarh'),
	('Chhattisgarh'),
	('Dadra and Nagar Haveli'),
	('Daman and Diu'),
	('Delhi'),
	('Goa'),
	('Gujarat'),
	('Haryana'),
	('Himachal Pradesh'),
	('Jammu and Kashmir'),
	('Jharkhand'),
	('Karnataka'),
	('Kerala'),
	('Lakshadweep'),
	('Madhya Pradesh'),
	('Maharashtra'),
	('Manipur'),
	('Meghalaya'),
	('Mizoram'),
	('Nagaland'),
	('Orissa'),
	('Puducherry'),
	('Punjab'),
	('Rajasthan'),
	('Sikkim'),
	('Tamil Nadu'),
	('Tripura'),
	('Uttar Pradesh'),
	('Uttarakhand'),
	('West Bengal');
