from connect_db import Database


class Base:
    @staticmethod
    def select_1(table):
        query = """
        SELECT course.course_id, course.name, course.description, course.rating, mentor.first_name, mentor.last_name, course_status. name, language.name, course.price FROM course
            INNER JOIN mentor
                ON course.mentor_id = mentor.mentor_id
            INNER JOIN course_status
                ON course_status.course_status_id = course.course_status_id
            INNER JOIN language
                ON language.language_id = course.language_id
                """
        return Database.connect(query, "select")

    @staticmethod
    def korish(table, column, data):
        query = f"SELECT * FROM {table} WHERE {column} = {data}"
        return Database.connect(query, "select")

    @staticmethod
    def select(table):
        query = f"SELECT * FROM {table} ORDER BY {table}_id"
        return Database.connect(query, "select")

    @staticmethod
    def delete(table, column_name, data):
        if type(data) == int:
            query = f"DELETE FROM {table} WHERE {column_name} = {data}"
        else:
            query = f"DELETE FROM {table} WHERE {column_name} = '{data}'"

        return Database.connect(query, "delete")


class Course_status(Base):
    def __init__(self, name):
        self.name = name
        self.table = "course_status"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE course_status SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE course_status SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE course_status SET course_status_id = {new_id} WHERE course_status_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM course_status WHERE course_status_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (name) VALUES ('{self.name}')"""
        return Database.connect(query, "insert")


class Language(Base):
    def __init__(self, name):
        self.name = name
        self.table = "language"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE language SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE language SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE language SET language_id = {new_id} WHERE language_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM language WHERE language_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (name) VALUES ('{self.name}')"""
        return Database.connect(query, "insert")


class City(Base):
    def __init__(self, name):
        self.name = name
        self.table = "city"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE city SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE city SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE city SET city_id = {new_id} WHERE city_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM city WHERE city_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (name) VALUES ('{self.name}')"""
        return Database.connect(query, "insert")

class Users(Base):
    def __init__(self, first_name, last_name, age, city_id, email, password, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city_id = city_id
        self.email = email
        self.password = password
        self.birth_date = birth_date
        self.table = "users"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE users SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE users SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE users SET users_id = {new_id} WHERE users_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM users WHERE users_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (first_name, last_name, age, city_id, email, password, birth_date) VALUES ('{self.first_name}', '{self.last_name}', '{self.age}', '{self.city_id}', '{self.email}', '{self.password}', '{self.birth_date}')"""
        return Database.connect(query, "insert")


class Mentor(Base):
    def __init__(self, first_name, last_name, age, city_id, email, password, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city_id = city_id
        self.email = email
        self.password = password
        self.birth_date = birth_date
        self.table = "mentor"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE mentor SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE mentor SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE mentor SET mentor_id = {new_id} WHERE mentor = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM mentor WHERE mentor_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (first_name, last_name, age, city_id, email, password, birth_date) VALUES ('{self.first_name}', '{self.last_name}', '{self.age}', '{self.city_id}', '{self.email}', '{self.password}', '{self.birth_date}')"""
        return Database.connect(query, "insert")


class Course(Base):
    def __init__(self, name, description, rating, course_status_id, language_id, mentor_id, price):
        self.name = name
        self.description = description
        self.rating = rating
        self.course_status_id = course_status_id
        self.language_id = language_id
        self.mentor_id = mentor_id
        self.price = price
        self.table = "course"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE course SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE course SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE course SET course_id = {new_id} WHERE course_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM course_id WHERE course_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (name, description, rating, course_status_id, language_id, mentor_id, price) VALUES ('{self.name}', '{self.description}', '{self.rating}', '{self.course_status_id}', '{self.language_id}', '{self.mentor_id}', '{self.price}')"""
        return Database.connect(query, "insert")


class Comment(Base):
    def __init__(self, text):
        self.text = text
        self.table = "comment"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE comment SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE comment SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE comment SET comment_id = {new_id} WHERE comment_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM comment WHERE comment_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (text) VALUES ('{self.text}')"""
        return Database.connect(query, "insert")


class SpecalityCourse(Base):
    def __init__(self, specality_id, course_id):
        self.specality_id = specality_id
        self.course_id = course_id
        self.table = "specality_course"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE specality_course SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE specality_course SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE specality_course SET specality_course_id = {new_id} WHERE comment_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM specality_course WHERE specality_course_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (specality_id, course_id) VALUES ('{self.specality_id}', '{self.course_id}')"""
        return Database.connect(query, "insert")

class Modul(Base):
    def __init__(self, name, course_id, lesson_count):
        self.name = name
        self.course_id = course_id
        self.lesson_count = lesson_count
        self.table = "modul"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE modul SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE modul SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE modul SET modul_id = {new_id} WHERE modul_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM modul WHERE modul_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (name, course_id, lesson_count) VALUES ('{self.name}', '{self.course_id}', '{self.lesson_count}')"""
        return Database.connect(query, "insert")


class LessonStatus(Base):
    def __init__(self, name, modul_id,):
        self.name = name
        self.modul_id = modul_id
        self.table = "lesson_status"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE lesson_status SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE lesson_status SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE lesson_status SET lesson_status_id = {new_id} WHERE lesson_status_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM lesson_status WHERE lesson_status_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (name, modul_id) VALUES ('{self.name}', '{self.modul_id}')"""
        return Database.connect(query, "insert")

class Lesson(Base):
    def __init__(self, name, description, lesson_status_id):
        self.name = name
        self.description = description
        self.lesson_status_id = lesson_status_id
        self.table = "lesson"


    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE lesson SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE lesson SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE lesson SET lesson_id = {new_id} WHERE lesson_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM lesson WHERE lesson_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (name, description, lesson_status_id) VALUES ('{self.name}', '{self.description}', '{self.lesson_status_id}')"""
        return Database.connect(query, "insert")


class Specality(Base):
    def __init__(self, name):
        self.name = name
        self.table = "specality"

    @staticmethod
    def update(column_name, old_data, new_data):
        if type(old_data) == int:
            query = f"UPDATE specality SET {column_name} = {new_data} WHERE {column_name} = {old_data}"

        else:
            query = f"UPDATE specality SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def update_id(id, new_id):
        query = f"UPDATE specality SET specality_id = {new_id} WHERE specality_id = {id}"
        return Database.connect(query, "update")

    @staticmethod
    def delete_id(id):
        query = f"DELETE FROM specality WHERE specality_id={id}"
        return Database.connect(query, "delete")

    def insert(self):
        query = f"""INSERT INTO {self.table} (name) VALUES ('{self.name}')"""
        return Database.connect(query, "insert")
