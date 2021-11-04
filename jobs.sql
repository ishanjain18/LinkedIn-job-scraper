drop table if exists jobs;
create table jobs(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    job_position VARCHAR(255),
    company VARCHAR(255),
    location VARCHAR(1000)
);