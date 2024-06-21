from typing import Optional
from src.db.models.reader import Reader

class MenuDispaly:

    @staticmethod
    def display_main_menu():
        print(
            """
        Wwelcome to MY READ APP

        MENU
        ------------
        1. DATE MANIPULATION
        2. DATA QUERY
        00.QUIT
            """
        )
    @staticmethod
    def display_MD_menu():
        print(
            """
        1. INSERT READER
        2. INSERT BOOK
        3. INSERT MYREAD
        99. BACK
            """
        )

class DataInput():

    @staticmethod
    def input_for_reader_insert():
        username = input('Enter your username:')
        title = input('Enter title(Mr, Ms, Dr): ')
        first_name = input('Enter first name: ')
        last_name = input('Enter last name:' )

        return{
            "username": username,
            "title": title,
            "first_name": first_name,
            "last_name" : last_name
        }
def main():
    while True:
        MenuDispaly.display_main_menu()
        option: int = int(input('Chose an option to continue: '))

        if option == 1:
            #TODO: OPERATION FOR MANIPULATION
            while True:

                MenuDispaly.display_MD_menu()
                option = int(input('Chose an option to continue: '))

                if option == 1:
                    # INSERT READER
                    reader_detail: dict[str,str] = DataInput.input_for_reader_insert()
                    reader: Optional[Reader] = Reader.insert_data(**reader_detail)

                    if reader:
                        print(f'Reader with username: {reader.username} inserted successfully')
                    
                    else:
                        print('Insertion faild')
                    pass
                elif option ==2:
                    # INSERT BOOK
                    pass
                elif option ==3:
                    # INSERT MYREAD
                    pass
                elif option == 99:
                    break
                else:
                    print('Option not recognized. Please try again')

        elif option == 2:
            #TODO: OPERATION FOR QUERY  
            pass

        elif option == 0:
            print('PROGRAM IS QUITING')
            break
        else:
            print('Option not recognized. please, try again')

if __name__ == '__main__':
    main()