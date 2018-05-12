


class Pool_Table:
    def __init__(self, table_id, table_status):
        self.table_id = table_id
        self.table_status = table_status

    def table_status(self):
        pass
        # table_occupied = True
        # table_open = False

    def __repr__(self):
        return (f"table id: {self.table_id} table satus: {self.table_status}")
