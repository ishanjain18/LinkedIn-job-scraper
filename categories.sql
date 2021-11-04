drop table if exists subcareers;
drop table if exists careers;

create table careers(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    career VARCHAR(255) NOT NULL
);

create table subcareers(
	id INT NOT NULL auto_increment primary key,
    career_id INT,
    subcareer VARCHAR(255) NOT NULL,
    FOREIGN KEY(career_id) REFERENCES careers(id)
);