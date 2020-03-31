-- Table: public.divorce_by_occupation

CREATE TABLE public.divorce_by_occupation
(
    occ bigint NOT NULL,
    rate double precision,
    medsal bigint,
    name text COLLATE pg_catalog."default",
    category text COLLATE pg_catalog."default",
    CONSTRAINT divorce_by_occupation_pkey PRIMARY KEY (occ)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.divorce_by_occupation
    OWNER to postgres;


-- Table: public.national_divorce

CREATE TABLE public.national_divorce
(
    year text COLLATE pg_catalog."default" NOT NULL,
    "Divorces & annulments" text COLLATE pg_catalog."default",
    "Population" text COLLATE pg_catalog."default",
    "Rate per 1,000 total population" text COLLATE pg_catalog."default",
    CONSTRAINT national_divorce_pkey PRIMARY KEY (year)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.national_divorce
    OWNER to postgres;


-- Table: public.national_marriage

CREATE TABLE public.national_marriage
(
    year text COLLATE pg_catalog."default" NOT NULL,
    "Marriages" text COLLATE pg_catalog."default",
    "Population" text COLLATE pg_catalog."default",
    "Rate per 1,000 total population" text COLLATE pg_catalog."default",
    CONSTRAINT national_marriage_pkey PRIMARY KEY (year)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.national_marriage
    OWNER to postgres;
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



