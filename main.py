import classes
import insert
import insert_2

def users():
    userss = input("""
       ______________________________\n
                    SERVICES

       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

                       """)

    if userss == "1":
        if len(classes.Users.select("users")) == 0:
            print("""
                    ------------------------------\n
                        MA'LUMOTLAR MAVJUD EMAS
                    ------------------------------\n
                    """)

        else:
            for i in classes.Users.select("users"):
                print(f"""
                            ID: {i[0]}
                            First Name: {i[1]}
                            Last Name: {i[2]}
                            Age: {i[3]}
                            email: {i[4]}
                            password: {i[5]}
                            birth Date: {i[6]}
                            Creata Date: {i[6]}
                        """)
        return users()

    elif userss == "2":
        first_name = input("first_name: ")
        last_name = input("last_name: ")
        age = input("age: ")
        city_id = input("city_id: ")
        email = input("Email kiritng: ")
        a = ["@gmail.com", "@gmail.ru", "@mail.com", "@mail.ru"]
        k = True
        while k:
            if not (email.endswith(a[0]) or email.endswith(a[1]) or email.endswith(a[2]) or email.endswith(a[3])):
                print("""
                                    Namuna: qwert123@gmail.com \n 
                                    """)
                print("@gmail.com kiritilgan bolishi shart !!")
                email = input("Email kiritng:  ")
            else:
                k = False

        password = input("Parol oylab toping : ")
        password_1 = input("Oylab topgan parolingizni yana bir bor kiriting : ")
        while password != password_1:
            print("Kiritilgan parolar bir xil bolishi kerak")
            print("Iltimos bir xiligni tekshiring! :")
            password_1 = input("Kiritish :")
        birth_date = input("birth_date: ")
        userss_1 = classes.Users(first_name, last_name, age, city_id, email, password, birth_date)
        print(userss_1.insert())
        return users()

    elif userss == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Users.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Users.update(column_name.lower(), old_data, new_data))

        return users()

    elif userss == "4":
        table = "users"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Users.delete_id(int(old_data)))

        else:
            print(classes.Users.delete(table, column_name.lower(), old_data))

        return users()
    elif userss == "0":
        return main()

    else:
        print("""
                <<<<<<_____________________>>>>>>
                         ERROR COMMAND!
                <<<<<<_____________________>>>>>>
                """)
        return users()


def city():
    cityt = input("""
           ______________________________\n
                        SERVICES

           ------------------------------\n
               1. SELECT _>
               2. INSERT _>
               3. UPDATE _>
               4. DELETE _>
               0. Back _>

                   """)

    if cityt == "1":
        if len(classes.City.select("city")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                """)

        else:
            for i in classes.City.select("city"):
                print(f"""
                        ID: {i[0]}
                        Name: {i[1]}
                        Craeta Date: {i[2]}
                    """)
        return city()

    elif cityt == "2":
        name = input("Name: ")
        city_1 = classes.City(name)
        print(city_1.insert())
        return language()

    elif cityt == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.City.update_id(int(old_data), int(new_data)))

        else:
            print(classes.City.update(column_name.lower(), old_data, new_data))

        return city()

    elif cityt == "4":
        table = "city"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.City.delete_id(int(old_data)))

        else:
            print(classes.City.delete(table, column_name.lower(), old_data))

        return city()
    elif cityt == "0":
        return main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return city()

def language():
    languages = input("""
       ______________________________\n
                    SERVICES

       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

               """)

    if languages == "1":
        if len(classes.Language.select("language")) == 0:
            print("""
            ------------------------------\n
                MA'LUMOTLAR MAVJUD EMAS
            ------------------------------\n
            """)

        else:
            for i in classes.Language.select("language"):
                print(f"""
                    ID: {i[0]}
                    Name: {i[1]}
                    Craeta Date: {i[2]}
                """)
        return language()

    elif languages == "2":
        name = input("Name: ")
        languages_1 = classes.Language(name)
        print(languages_1.insert())
        return language()

    elif languages == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Language.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Language.update(column_name.lower(), old_data, new_data))

        return language()

    elif languages == "4":
        table = "language"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Language.delete_id(int(old_data)))

        else:
            print(classes.Language.delete(table, column_name.lower(), old_data))

        return language()

    elif languages == "0":
        return main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return language()

def course_status():
    courses_status = input("""
       ______________________________\n
                    SERVICES

       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

               """)

    if courses_status == "1":
        if len(classes.Course_status.select("course_status")) == 0:
            print("""
            ------------------------------\n
                MA'LUMOTLAR MAVJUD EMAS
            ------------------------------\n
            """)

        else:
            for i in classes.Course_status.select("course_status"):
                print(f"""
                    ID: {i[0]}
                    Name: {i[1]}
                    Craeta Date: {i[2]}
                """)
        return course_status()

    elif courses_status == "2":
        name = input("Name: ")
        course_status_1 = classes.Course_status(name)
        print(course_status_1.insert())
        return course_status()

    elif courses_status == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Course_status.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Course_status.update(column_name.lower(), old_data, new_data))

        return course_status()

    elif courses_status == "4":
        table = "course_status"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Course_status.delete_id(int(old_data)))

        else:
            print(classes.Course_status.delete(table, column_name.lower(), old_data))

        return courses_status

    elif courses_status == "0":
        return main()

    else:
        print("""
                <<<<<<_____________________>>>>>>
                         ERROR COMMAND!
                <<<<<<_____________________>>>>>>
                """)
        return course_status()


def main():
    print("""
    <<<<<<_____________________>>>>>>
                MAIN MENYU
    <<<<<<_____________________>>>>>>
    """)

    servises = input("""
    1.  Course Status_>
    2.  Language _>
    3.  City _>
    4.  User _>
    5.  Mentor _>
    6.  Course _>
    7.  Comment _>
    8.  Specality _>
    9.  Specality Course _>
    10.  Modul _>
    11.  Lesson Status _>
    12.  Lesson _>
        >>>>>""")
    if servises == "1":
        return course_status()

    elif servises == "2":
        return language()

    elif servises == "3":
        return city()

    elif servises == "4":
        return users()

    elif servises == "5":
        return insert.mentor()

    elif servises == "6":
        return insert.course()

    elif servises == "7":
        return insert.comment()

    elif servises == "8":
        return insert.specality()

    elif servises == "9":
        return insert.specality_course()

    elif servises == "10":
        return insert_2.modul()

    elif servises == "11":
        return insert_2.lesson_status()

    elif servises == "12":
        return insert_2.lesson()

    else:
        print("""
        <<<<<<_____________________>>>>>>
                 ERROR COMMAND!
        <<<<<<_____________________>>>>>>
        """)
        return main()


if __name__ == '__main__':
    main()
