-- Rename columns in table national_marriage
ALTER TABLE national_marriage
RENAME COLUMN "Marriages" TO marriages;
ALTER TABLE national_marriage
RENAME COLUMN "Population" TO population;
ALTER TABLE national_marriage
RENAME COLUMN "Rate per 1,000 total population" TO marriage_rate;

-- Rename colulmns in table national_divorce
ALTER TABLE national_divorce
RENAME COLUMN "Divorces & annulments" TO divorces;
ALTER TABLE national_divorce
RENAME COLUMN "Population" TO population;
ALTER TABLE national_divorce
RENAME COLUMN "Rate per 1,000 total population" TO divorce_rate;

-- JOIN two tables
SELECT national_divorce.year, divorces, marriages, divorce_rate, marriage_rate
INTO national_rate
FROM national_divorce 
JOIN national_marriage 
ON national_divorce.year = national_marriage.year;
ALTER TABLE national_rate
ADD PRIMARY KEY (year);
SELECT * FROM national_rate;



