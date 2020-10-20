import sqlite3 as db


class Words_List:
    def __init__(self, words, parts, units):
        self.words = list_of_words
        self.parts = list_of_parts
        self.units = list_of_units

    def starter(self, words, parts, units):
        """ this is starter function and user can choose what section wants to go """

        select_section = input('\nEnter what section you want to go:'
                               '\n1)Looking at units.'
                               '\n2)quiz!'
                               '\n3)Enter a new word!!'
                               '\n0)Exit!'
                               '\n?:')
        if select_section == '1':
            self.list_of_units()
            return self.select_unit_to_show(words, parts, units)
        elif select_section == '2':
            self.list_of_units()
            return self.select_unit_for_quiz(words, parts, units)
        elif select_section == '3':
            return self.add_word(words, parts, units)
        elif select_section == '0':
            print('Bye!!!')
        else:
            print('\nEnter correct number of sections!')
            return self.starter(words, parts, units)

    def list_of_units(self):
        """ this function takes the stored tables name into a list to compare with
         select unit to show chosen unit,

         here must be add some sqlite command to takes units_name table into a list. """
        con = db.connect("wordsdb.db")
        con.row_factory = lambda cursor, row: row[0]
        c = con.cursor()
        command = ''' select * from units '''
        c.execute(command)
        r = c.fetchall()
        for i in r:
            self.units.append(i)
        c.close()
        return

    def fill(self, select):
        if select == '1':
            command = ''' select * from unit1 '''
            return self.fill_words_list(command), self.fill_parts_list(command)
        elif select == '2':
            command = ''' select * from unit2 '''
            return self.fill_words_list(command), self.fill_parts_list(command)
        elif select == '3':
            command = ''' select * from unit3 '''
            return self.fill_words_list(command), self.fill_parts_list(command)
        elif select == '4':
            command = ''' select * from unit4 '''
            return self.fill_words_list(command), self.fill_parts_list(command)
        elif select == '5':
            command = ''' select * from unit5 '''
            return self.fill_words_list(command), self.fill_parts_list(command)
        elif select == '6':
            command = ''' select * from unit6 '''
            return self.fill_words_list(command), self.fill_parts_list(command)
        elif select == '7':
            command = ''' select * from unit7 '''
            return self.fill_words_list(command), self.fill_parts_list(command)
        elif select == '8':
            command = ''' select * from unit8 '''
            return self.fill_words_list(command), self.fill_parts_list(command)
        elif select == '9':
            command = ''' select * from unit9 '''
            return self.fill_words_list(command), self.fill_parts_list(command)
        elif select == '10':
            command = ''' select * from unit10 '''
            return self.fill_words_list(command), self.fill_parts_list(command)
        else:
            command = ''' select * from unit11 '''
            return self.fill_words_list(command), self.fill_parts_list(command)

    def fill_words_list(self, command):
        self.words = []
        con = db.connect('wordsdb.db')
        con.row_factory = lambda cursor, row: row[0]
        c = con.cursor()
        c.execute(command)
        r = c.fetchall()
        con.close()
        self.count = 0
        for i in r:
            self.words.append(i)
            self.count += 1
        return

    def fill_parts_list(self, command):
        self.parts = []
        con = db.connect('wordsdb.db')
        con.row_factory = lambda cursor, row: row[1]
        c = con.cursor()
        c.execute(command)
        r = c.fetchall()
        con.close()
        for j in r:
            self.parts.append(j)
        return

    def select_unit_to_show(self, words, parts, units):
        """ this function takes the unit number that the user wants to see and
         compare with the unit numbers if there is that unit,it call another
         method to shows selected unit that and if there not show a error """

        select_unit = input('\nSelect unit to show, unit 1 to unit 11? (Enter number of unit)'
                            # here must be add last index of unit list
                            '\nto see previous menu enter (Q\q)'
                            '\n: ')
        if select_unit in self.units:
            self.fill(select_unit)
            return self.show(words, parts, units)
        elif select_unit == 'q' or select_unit == 'Q':
            return self.starter(words, parts, units)
        else:
            print('\nthere isn`t unit with this number!')
            return self.select_unit_to_show(words, parts, units)

    def show(self, words, parts, units):
        """ this function print  *** selected ***  unit and after calling starter
        method again at the end,

        in here words and parts lists must be fill by values that stored in database"""

        for i in range(int(self.count)):
            print(self.words[i], ' -> ', self.parts[i])
        return self.starter(words, parts, units)

    def select_unit_for_quiz(self, words, parts, units):
        """ this function shows the interval of units to choose by user """

        print('Select between unit 1 to unit 11'
              '\nTo see previous menu enter (Q\q)')
        select_unit_for_exam = input('Enter number of units: ')
        if select_unit_for_exam in self.units:
            self.fill(select_unit_for_exam)
            return self.quiz(words, parts, units)
        elif select_unit_for_exam == 'q' or select_unit_for_exam == 'Q':
            return self.starter(words, parts, units)
        else:
            print('\nthere isn`t unit with this number!')
            return self.select_unit_for_quiz(words, parts, units)

    def quiz(self, words, parts, units):
        """ this function gets the quiz which  *** chosen ***  by the user and
         after calling starter method again at the end,

         here should be quantify words and parts lists with ((select)) from unit """

        print('Write the part of speech of the shown word,'
              '\nTo see previous menu enter (Q\q)')
        for i in range(int(self.count)):  # inja be andazehe tedad kalamat unit loop mizanad
            guess_time = 3
            while bool(guess_time):
                answer = input(self.words[i] + ' -> ')
                if answer == self.parts[i]:
                    print("correct!")
                    guess_time = False
                elif answer == 'q' or answer == 'Q':
                    return self.select_unit_for_quiz(words, parts, units)
                else:
                    guess_time -= 1
                    if bool(guess_time):
                        print("wrong!!! guess again!")
                    else:
                        print('practice more!!! \nnow guess another word!')
        return self.select_unit_for_quiz(words, parts, units)

    def insert_new_word(self, word, part):
        con = db.connect('wordsdb.db')
        c = con.cursor()
        com = '''INSERT INTO unit11(words, parts) VALUES ('{}', '{}')'''.format(word, part)
        try:
            c.execute(com)
            con.commit()
            print('\nnew word successfully add! ')
        except:
            print('error')
            con.rollback()

        con.close()
        return

    def add_word(self, words, parts, units):
        """ this function get a new word and their part of speech and add it in
         a special unit call *** extra *** and asks user for another word if user
          wants to add,

          here must be get unit extra`s words and takes it to the words list,

          here must be add some sqlite command which appends new word to list of
          words and save it in database. """
        command = ''' select * from unit11 '''
        self.fill_words_list(command)
        self.fill_parts_list(command)
        print('\nFirst you should enter new word and then part of speeches of it.')
        while True:
            print('if you want go back enter (q\Q)!')
            new_word = input('Enter new word: ')
            if new_word == 'q' or new_word == 'Q':
                return self.starter(words, parts, units)
            elif new_word not in self.words:
                new_part = input('Enter part of speech: ')
                self.words.append(new_word)
                self.parts.append(new_part)
                self.insert_new_word(new_word, new_part)
            else:
                print('\nthis word had already added!'
                      '\nadd another word!')


list_of_words = []
list_of_parts = []
list_of_units = []

a = Words_List(list_of_words, list_of_parts, list_of_units)
a.starter(list_of_words, list_of_parts, list_of_units)
