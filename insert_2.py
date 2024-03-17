import classes
import main


def modul():
    modul_1 = input("""
        ______________________________\n
                    SERVICES

        ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

        """)

    if modul_1 == "1":
        if len(classes.Modul.select("modul")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n

                """)
        else:
            for i in classes.Modul.select("modul"):
                print(f"""
                        ID: {i[0]}
                        Course ID: {i[1]}
                        Lesson Count: {i[2]}
                        Create Date: {i[3]}
                    """)

        return modul()

    elif modul_1 == "2":
        name = input("Name: ")
        course_id = int(input("Course ID: "))
        lesson_id = input("Lesson ID: ")
        modul_1_1 = classes.Modul(name, course_id, lesson_id)
        print(modul_1_1.insert())
        return modul()

    elif modul_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Modul.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Modul.update(column_name.lower(), old_data, new_data))

        return modul()

    elif modul_1 == "4":
        table = "modul"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Modul.delete_id(int(old_data)))

        else:
            print(classes.Modul.delete(table, column_name.lower(), old_data))
        return modul()
    elif modul_1 == "0":
        return main.main()

    else:
        print("""
                <<<<<<_____________________>>>>>>
                         ERROR COMMAND!
                <<<<<<_____________________>>>>>>
                """)
        return modul()

def lesson_status():
    lesson_status_1 = input("""
        ______________________________\n
                    SERVICES

        ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

        """)

    if lesson_status_1 == "1":
        if len(classes.LessonStatus.select("lesson_status")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n

                """)
        else:
            for i in classes.LessonStatus.select("lesson_status"):
                print(f"""
                        ID: {i[0]}
                        Name : {i[1]}
                        Modul ID: {i[2]}
                        Create Date: {i[3]}
                    """)

        return lesson_status()

    elif lesson_status_1 == "2":
        name = input("Name: ")
        modul_id = int(input("Modul ID: "))
        lesson_status_1_1 = classes.LessonStatus(name, modul_id)
        print(lesson_status_1_1.insert())
        return lesson_status()

    elif lesson_status_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.LessonStatus.update_id(int(old_data), int(new_data)))

        else:
            print(classes.LessonStatus.update(column_name.lower(), old_data, new_data))

        return lesson_status()

    elif lesson_status_1 == "4":
        table = "lesson_status"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.LessonStatus.delete_id(int(old_data)))

        else:
            print(classes.LessonStatus.delete(table, column_name.lower(), old_data))

        return lesson_status()
    elif lesson_status_1 == "0":
        return main.main()

    else:
        print("""
                <<<<<<_____________________>>>>>>
                         ERROR COMMAND!
                <<<<<<_____________________>>>>>>
                """)
        return lesson_status()

def lesson():
    lesson_1 = input("""
        ______________________________\n
                    SERVICES

        ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

        """)

    if lesson_1 == "1":
        if len(classes.Lesson.select("lesson")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n

                """)
        else:
            for i in classes.Lesson.select("lesson"):
                print(f"""
                        ID: {i[0]}
                        Name : {i[1]}
                        Description : {i[2]}
                        lesson_status_id: {i[3]}
                    """)

        return lesson()

    elif lesson_1 == "2":
        name = input("Name: ")
        description = input("Description: ")
        lesson_status_id = input("Lesson Status ID: ")
        lesson_1_1 = classes.Lesson(name, description, lesson_status_id)
        print(lesson_1_1.insert())
        return lesson()

    elif lesson_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Lesson.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Lesson.update(column_name.lower(), old_data, new_data))

        return lesson()

    elif lesson_1 == "4":
        table = "lesson"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Lesson.delete_id(int(old_data)))

        else:
            print(classes.Lesson.delete(table, column_name.lower(), old_data))

        return lesson()
    elif lesson_1 == "0":
        return main.main()

    else:
        print("""
                <<<<<<_____________________>>>>>>
                         ERROR COMMAND!
                <<<<<<_____________________>>>>>>
                """)
        return lesson()