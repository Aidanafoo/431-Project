-- Database: Project431

-- DROP DATABASE IF EXISTS "Project431";

CREATE DATABASE "Project431"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	
	
CREATE TABLE store_pages(appid BIGINT, game_name TEXT, release_date TEXT, achievements BIGINT, header_image TEXT, dlc_count BIGINT, required_age BIGINT, 
						 price FLOAT, website TEXT, windows BOOLEAN, mac BOOLEAN, linux BOOLEAN, metacritic_score BIGINT,
						 metacritic_url TEXT, disclaimers TEXT, description TEXT, support_url TEXT, 
						 support_email TEXT, estimated_owners BIGINT, peak_ccu BIGINT, average_playtime_forever BIGINT, 
						 median_playtime_forever BIGINT, average_playtime_two_weeks BIGINT, median_playtime_two_weeks BIGINT, 
						 user_score BIGINT, positive BIGINT, negative BIGINT, score_rank BIGINT, recommendations TEXT, PRIMARY KEY(appid));
						 
						 
CREATE TABLE companies(company_name TEXT, PRIMARY_KEY(company_name));


CREATE TABLE categories(category_name TEXT, PRIMARY_KEY(category_name));


CREATE TABLE tags(tag_name TEXT, PRIMARY_KEY(tag_name));

CREATE TABLE genres(genre_name TEXT, PRIMARY_KEY(genre_name));

CREATE TABLE languages(language_name TEXT, PRIMARY_KEY(language_name));

CREATE TABLE trailer(appid BIGINT, trailer_url TEXT, PRIMARY_KEY(trailer_url), FOREGIN_KEY(appid) REFERENCES store_pages(appid));

CREATE TABLE screenshots(appid BIGINT, screenshot_url TEXT, PRIMARY_KEY(screenshot_url), FOREGIN_KEY(appid) REFERENCES store_pages(appid));

CREATE TABLE game_tags(appid BIGINT, tag_name TEXT, PRIMARY_KEY(appid, tag_name), FOREGIN_KEY(appid) REFERENCES store_pages(appid), FOREGIN_KEY(tag_name) REFERENCES tags(tag_name));

CREATE TABLE game_genres(appid BIGINT, genre_name TEXT, PRIMARY_KEY(appid, genre_name), FOREGIN_KEY(appid) REFERENCES store_pages(appid), FOREGIN_KEY(gwnew_name) REFERENCES genres(genre_name));

CREATE TABLE game_categories(appid BIGINT, category_name TEXT, PRIMARY_KEY(appid, category_name), FOREGIN_KEY(appid) REFERENCES store_pages(appid), FOREGIN_KEY(category_name) REFERENCES tags(category_name));

CREATE TABLE text_support(appid BIGINT, language_name TEXT, PRIMARY_KEY(appid, language_name), FOREGIN_KEY(appid) REFERENCES store_pages(appid), FOREGIN_KEY(language_name) REFERENCES languages(language_name));

CREATE TABLE audio_support(appid BIGINT, language_name TEXT, PRIMARY_KEY(appid, language_name), FOREGIN_KEY(appid) REFERENCES store_pages(appid), FOREGIN_KEY(language_name) REFERENCES languages(language_name));

CREATE TABLE developers(appid BIGINT, company_name TEXT, PRIMARY_KEY(appid, company_name), FOREGIN_KEY(appid) REFERENCES store_pages(appid), FOREGIN_KEY(company_name) REFERENCES company(company_name));

CREATE TABLE publishers(appid BIGINT, company_name TEXT, PRIMARY_KEY(appid, company_name), FOREGIN_KEY(appid) REFERENCES store_pages(appid), FOREGIN_KEY(company_name) REFERENCES company(company_name));




						 
						 