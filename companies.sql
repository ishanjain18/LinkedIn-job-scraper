drop table if exists companies;
create table companies(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(255), 
    company_description VARCHAR(1000),
    location VARCHAR(1000),
    subcareer_id INT,
    FOREIGN KEY (subcareer_id) REFERENCES subcareers(id) 
);
 