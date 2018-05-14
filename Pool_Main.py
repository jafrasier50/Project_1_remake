from Tables import PoolTable
import datetime
import time
localtime = time.localtime(time.time())
print(localtime.tm_year)
#-----------------------------Table_Manager_application-------------------------
class Table_Manager_application:
    def __init__(self):
        self.pool_tables =[]
        self.table_class = PoolTable
        self.present_user_options()



    def present_user_options(self):
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
        else:
            if choice >= 6:
                print("Invalid Input")
                self.present_user_options()

    def open_new_table(self):

        hours = int(input("Select number of hours to play: "))
        table_name = input("Please name your table: ")

        new_table = self.table_class(table_name , False)

        if hours >= 8:
            print("Sorry! 8 Hour Maximum.")
        else:
            print(f"You have selected {hours} hours at $30 per hour.")

        new_table.hours = hours

        self.pool_tables.append(new_table)



        self.present_user_options()


    def update_table_status(self):

        selected_table_name = input("enter table name to update ")
        selected_table = None

        for the_table in self.pool_tables:

            if the_table.table_id == selected_table_name:
                selected_table = the_table

        if selected_table != None:

                print('was table occupied ' , selected_table.is_occupied)
                if selected_table.is_occupied == False:
                    selected_table.is_occupied = True

                    time_values = datetime.datetime.now()
                    time_log = time.asctime( time.localtime(time.time()))


                    selected_table.start_time = time_values
                    selected_table.start_time_string = time_log

                else:

                    selected_table.is_occupied = False
                    time_values = datetime.datetime.now()
                    time_log = time.asctime( time.localtime(time.time()))

                    selected_table.end_time = time_values
                    selected_table.end_time_string = time_log
                    a = selected_table.start_time.replace(microsecond=0)
                    b = selected_table.end_time.replace(microsecond=0)
                    total_time = b - a
                    selected_table.total_time = total_time

                    print(total_time)
                    hours_seconds = divmod(total_time.days * 86400 + total_time.seconds, 60)
                    total_minutes = hours_seconds[0]*60 + hours_seconds[1]
                    print(total_minutes)
                    transaction = f"session table: {selected_table.table_id} | session start: {selected_table.start_time_string} | session end: {selected_table.end_time_string} | duration: {str(total_time)} \r\n"
                    self.write_to_file(transaction)
                print('table is occupied' , selected_table.is_occupied)



        self.present_user_options()

    def write_to_file(self, transaction):
       file = open('pool_log.txt','a+')
       file.write(transaction)
       file.close()


    def view_tables_and_Status(self):
        # print(pool_tables(status))

        for table in self.pool_tables:
            print(table)
            print("\n")

        self.present_user_options()

    def close_table(self):
        selected_table_name = input("enter the table name to close: ")
        selected_table = the_table


    def exit_program(self):
        print("Goodbye.")

table_manager = Table_Manager_application()
