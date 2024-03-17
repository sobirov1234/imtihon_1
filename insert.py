import classes
import main



def specality():
    specality_1 = input("""
    ______________________________\n
                SERVICES

    ------------------------------\n
       1. SELECT _>
       2. INSERT _>
       3. UPDATE _>
       4. DELETE _>
       0. Back _>

    """)

    if specality_1 == "1":
        if len(classes.Specality.select("specality")) == 0:
            print("""
            ------------------------------\n
                MA'LUMOTLAR MAVJUD EMAS
            ------------------------------\n

            """)
        else:
            for i in classes.Specality.select("specality"):
                print(f"""
                    ID: {i[0]}
                    Name: {i[1]}
                    Create Date: {i[2]}
                """)

        return specality()

    elif specality_1 == "2":
        name = input("Name: ")
        specality_1_1 = classes.Specality(name)
        print(specality_1_1.insert())
        return specality()

    elif specality_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Specality.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Specality.update(column_name.lower(), old_data, new_data))

        return specality()

    elif specality_1 == "4":
        table = "specality"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Specality.delete_id(int(old_data)))

        else:
            print(classes.Specality.delete(table, column_name.lower(), old_data))

        return specality()
    elif specality_1 == "0":
        return main.main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return specality()


def specality_course():
    speclaity_course_1 = input("""
    ______________________________\n
                SERVICES

    ------------------------------\n
       1. SELECT _>
       2. INSERT _>
       3. UPDATE _>
       4. DELETE _>
       0. Back _>
""")

    if speclaity_course_1 == "1":
        if len(classes.SpecalityCourse.select("specalitycourse")) == 0:
            print("""
            ------------------------------\n
                MA'LUMOTLAR MAVJUD EMAS
            ------------------------------\n

            """)
        else:
            for i in classes.SpecalityCourse.select("specalitycourse"):
                print(f"""
                    ID: {i[0]}
                    Specality ID: {i[1]}
                    Course ID: {i[2]}
                    Create Date: {i[3]}
                """)

        return specality_course()

    elif speclaity_course_1 == "2":
        specality_id = int(input("Specality ID:"))
        course_id = int(input("Course ID:"))
        speclaity_course_1_1 = classes.SpecalityCourse(specality_id, course_id)
        print(speclaity_course_1_1.insert())
        return specality_course()

    elif speclaity_course_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.SpecalityCourse.update_id(int(old_data), int(new_data)))

        else:
            print(classes.SpecalityCourse.update(column_name.lower(), old_data, new_data))

        return specality_course()

    elif speclaity_course_1 == "4":
        table = "specality_course"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.SpecalityCourse.delete_id(int(old_data)))

        else:
            print(classes.SpecalityCourse.delete(table, column_name.lower(), old_data))

        return specality_course()
    elif speclaity_course_1 == "0":
        return main.main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
            """)
        return specality_course()



def comment():
    comment_1 = input("""
        ______________________________\n
                    SERVICES

        ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>
""")

    if comment_1 == "1":
        if len(classes.Comment.select("comment")) == 0:
            print("""
              ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
              ------------------------------\n

            """)
        else:
            for i in classes.Comment.select("comment"):
                print(f"""
                    ID: {i[0]}
                    Text: {i[1]}
                    Create Date: {i[2]}
                """)
        return comment()

    elif comment_1 == "2":
        text = input("Text: ")
        comment_1_1 = classes.Comment(text)
        print(comment_1_1.insert())
        return comment()

    elif comment_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Comment.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Comment.update(column_name.lower(), old_data, new_data))

        return comment()

    elif comment_1 == "4":
        table = "comment"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Comment.delete_id(int(old_data)))

        else:
            print(classes.Comment.delete(table, column_name.lower(), old_data))

        return comment()
    elif comment_1 == "0":
        return main.main()

    else:
        print("""
                <<<<<<_____________________>>>>>>
                         ERROR COMMAND!
                <<<<<<_____________________>>>>>>
                """)
        return comment()


def course():
    course_1 = input("""
           ______________________________\n
                        SERVICES

           ------------------------------\n
               1. SELECT _>
               2. INSERT _>
               3. UPDATE _>
               4. DELETE _>
               0. Back _>

                               """)

    if course_1 == "1":
        if len(classes.Course.select("course")) == 0:
            print("""
                ------------------------------\n
                    MA'LUMOTLAR MAVJUD EMAS
                ------------------------------\n
                            """)

        else:
            for i in classes.Course.select("course"):
                print(f"""

                    ID: {i[0]}
                    Name: {i[1]}
                    Description: {i[2]}
                    Rating: {i[3]}
                    Course_Status_id: {i[4]}
                    Language_id: {i[5]}
                    Mentor_id: {i[6]}
                    Price: {i[7]}
                    Creata Date: {i[8]}
                            """)

        return mentor()

    elif course_1 == "2":
        name = input("Name: ")
        descrpition = input("Description: ")
        rating = input("Rating: ")
        course_status_id = input("Course Status ID: ")
        language_id = input("Language ID: ")
        mentor_id = input("Mentor ID: ")
        price = input("Price: ")
        course_1_ = classes.Course(name, descrpition, rating, course_status_id, language_id, mentor_id, price)
        print(course_1_.insert())
        return course()

    elif course_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Course.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Course.update(column_name.lower(), old_data, new_data))

        return course()

    elif course_1 == "4":
        table = "course"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Course.delete_id(int(old_data)))

        else:
            print(classes.Course.delete(table, column_name.lower(), old_data))

        return course()
    elif course_1 == "0":
        return main.main()

    else:
        print("""
            <<<<<<_____________________>>>>>>
                     ERROR COMMAND!
            <<<<<<_____________________>>>>>>
                    """)
        return mentor()



def mentor():
    mentor_1 = input("""
       ______________________________\n
                    SERVICES

       ------------------------------\n
           1. SELECT _>
           2. INSERT _>
           3. UPDATE _>
           4. DELETE _>
           0. Back _>

                           """)

    if mentor_1 == "1":
        if len(classes.Mentor.select("mentor")) == 0:
            print("""
                        ------------------------------\n
                            MA'LUMOTLAR MAVJUD EMAS
                        ------------------------------\n
                        """)

        else:
            for i in classes.Mentor.select("mentor"):
                print(f"""

                            ID: {i[0]}
                            First Name: {i[1]}
                            Last Name: {i[2]}
                            Age: {i[3]}
                            email: {i[4]}
                            password: {i[5]}
                            birth Date: {i[6]}
                            Creata Date: {i[7]}
                        """)

        return mentor()

    elif mentor_1 == "2":
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
        mentor_1_ = classes.Users(first_name, last_name, age, city_id, email, password, birth_date)
        print(mentor_1_.insert())
        return mentor()

    elif mentor_1 == "3":
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        new_data = input("New date: ")
        if column_name.lower() == "id":
            print(classes.Mentor.update_id(int(old_data), int(new_data)))

        else:
            print(classes.Mentor.update(column_name.lower(), old_data, new_data))

        return mentor()

    elif mentor_1 == "4":
        table = "mentor"
        column_name = input("Column name: ")
        old_data = input("Now date: ")
        if column_name.lower() == "id":
            print(classes.Mentor.delete_id(int(old_data)))

        else:
            print(classes.Mentor.delete(table, column_name.lower(), old_data))

        return mentor()
    elif mentor_1 == "0":
        return main.main()

    else:
        print("""
                <<<<<<_____________________>>>>>>
                         ERROR COMMAND!
                <<<<<<_____________________>>>>>>
                """)
        return mentor()