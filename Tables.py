
class PoolTable:
    def __init__(self, table_id, table_status):
        self.table_id = table_id
        self.is_occupied = table_status
        self.start_time_string = None
        self.end_time_string = None
        self.start_time = None
        self.end_time = None
        self.total_time = None

    def __repr__(self):
        return (f"Table ID: {self.table_id} || Table Satus: {self.is_occupied} || Start Time: {self.start_time_string} || End Time: {self.end_time_string}|| Duration:{self.total_time} ")
