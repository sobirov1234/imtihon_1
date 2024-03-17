from connect_db import Database

def tables():

    course_status_tables = """
        CREATE TABLE course_status(
            course_status_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now()
        )
    """

    language_tables = """
        CREATE TABLE language(
            language_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            last_updated DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now()
        )
    """

    city_tables = """
        CREATE TABLE city(
            city_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            craete_date TIMESTAMP DEFAULT now()
        )
    """

    user_tables = """
        CREATE TABLE users(
            users_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            age SMALLINT,
            city_id INT REFERENCES city(city_id),
            email VARCHAR(30) NOT NULL,
            password VARCHAR(30) NOT NULL,
            birth_date DATE,
            create_date TIMESTAMP DEFAULT now()
        )
    """

    mentors_tables = """
        CREATE TABLE mentor(
            mentor_id SERIAL PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            age SMALLINT,
            city_id INT REFERENCES city(city_id),
            email VARCHAR(30) NOT NULL,
            password VARCHAR(30) NOT NULL,
            birth_date DATE,
            create_date TIMESTAMP DEFAULT now()
        )
    """

    course_tables = """
        CREATE TABLE course(
            course_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            description VARCHAR(30),
            rating INT,
            course_status_id INT REFERENCES course_status(course_status_id),
            language_id INT REFERENCES language(language_id),
            mentor_id INT REFERENCES mentor(mentor_id),
            price FLOAT,
            craete_date TIMESTAMP DEFAULT now()
        )
    """

    comment_tables = """
        CREATE TABLE comment(
            comment_id SERIAL PRIMARY KEY,
            text TEXT,
            course_id INT REFERENCES course(course_id)
        )
    """

    specality_tables = """
        CREATE TABLE specality(
            specality_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            creata_date TIMESTAMP DEFAULT now()
        )
    """

    specality_course_tables = """
        CREATE TABLE specality_course(
            specality_course_id SERIAL PRIMARY KEY,
            specality_id INT REFERENCES specality(specality_id),
            course_id INT REFERENCES course(course_id),
            create_date TIMESTAMP DEFAULT now()
        )
    """

    modul_tables = """
        CREATE TABLE modul(
            modul_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            course_id INT REFERENCES course(course_id),
            lesson_count VARCHAR(30),
            create_date TIMESTAMP DEFAULT now()
        )
    """

    lesson_status_tables = """
        CREATE TABLE lesson_status(
            lesson_status_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            modul_id INT REFERENCES modul(modul_id),
            creata_date TIMESTAMP DEFAULT now()
        )
    """

    lesson_tables = """
        CREATE TABLE lesson(
            lesson_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            description VARCHAR(30),
            lesson_status_id INT REFERENCES lesson_status(lesson_status_id)
        )
    """

    data = {
        "course_status_tables": course_status_tables,
        "language_tables": language_tables,
        "city_tables": city_tables,
        "user_tables": user_tables,
        "mentors_tables": mentors_tables,
        "course_tables": course_tables,
        "comment_tables": comment_tables,
        "specality_tables": specality_tables,
        "specality_status_tables": specality_course_tables,
        "module_tables": modul_tables,
        "lesson_status_tables": lesson_status_tables,
        "lesson_tables": lesson_tables
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    tables()