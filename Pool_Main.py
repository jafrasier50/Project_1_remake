from Tables import Pool_Table
#-----------------------------Table_Manager_application-------------------------
class Table_Manager_application: #new class
    def __init__(self):#Table_Manager_application class initiator
        self.pool_tables =[] #attribute that allows tables created to be pushed into
        self.table_class = Pool_Table
        self.present_user_options()



    def present_user_options(self):#function presents users options calls functions
        print("************************************************************************************************")
        choice = int(input("1. Open New Table • 2. View Table All Tables • 3. Close Table • 4. update table • 5. Exit : "))
        print("************************************************************************************************")
        if choice == 1:
            self.open_new_table()
        if choice == 2:
            self.view_tables_and_Status()
        if choice == 3:
            self.close_table()
        if choice == 4:
            self.update_table_status()
        if choice == 5:
            self.exit_program()
        # else:
        #     print("invalid input.")

    def open_new_table(self): #function gives user input on hours to play and table name

        hours = int(input("Select number of hours to play: "))
        table_name = input("Please name your table: ")

        new_table = self.table_class(table_name , "OPEN") #



        if hours >= 8:
            print("Sorry! 8 Hour Maximum.")
        else:
            print(f"You have selected {hours} hours at $30 per hour.")

        new_table.hours = hours

        self.pool_tables.append(new_table)



        self.present_user_options()


    def update_table_status(self): #function updates table

        selected_table_name = input("enter table name to update ") #ask for user input
        selected_table = None #gives table starting value

        for the_table in self.pool_tables: #creates loop for tables

            if the_table.table_id == selected_table_name:
                selected_table = the_table

        if selected_table != None:

                print('table was ' + selected_table.table_status)
                if selected_table.table_status == "OPEN":
                    selected_table.table_status = "OCCUPIED"
                else:
                    selected_table.table_status = "OPEN"
                print('table is now ' + selected_table.table_status)

        self.present_user_options()


    def view_tables_and_Status(self):
        # print(pool_tables(status))
        print(self.pool_tables)
        for table in self.pool_tables:
            print(table)
            print("\n")

        self.present_user_options()

    def close_table(self):
        pass

    def exit_program(self):
        pass

table_manager = Table_Manager_application() #creates instance
