class Finance:
    def __init__(self, transaction_id, transaction_type, transaction_amount, transaction_category,transaction_description, transaction_date):
        self.transaction_id          = transaction_id
        self.transaction_type        = transaction_type
        self.transactionamount       = transaction_amount
        self.transaction_category    = transaction_category
        self.transaction_description = transaction_description
        self.transaction_date        = transaction_date

    def to_dict(self):
        return {
            "transaction_id"            : self.transaction_id,
            "transaction_type"          : self.transaction_type,
            "transaction_amount"        : self.transactionamount,
            "transaction_category"      : self.transaction_category,
            "transaction_description"   : self.transaction_description,
            "transaction_date"          : self.transaction_date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["transaction_id"],
            data["transaction_type"],
            data["transaction_amount"],
            data["transaction_category"],
            data["transaction_description"],
            data["transaction_date"]
        )
    
    @property
    def transactionamount(self):
        return self.__transaction_amount

    @transactionamount.setter
    def transactionamount(self, value):
        if value < 0:
            raise ValueError("Inavlid Amount cannot be less than zero!")
        elif value == 0:
            raise ValueError("Inavlid Amount cannot be zero!")
        else:
            self.__transaction_amount = value

    def display_transaction(self):
        print("--------Transaction Details---------")
        print(f"ID             :    {self.transaction_id} ")
        print(f"Type           :    {self.transaction_type} ")
        print(f"Amount         :    {self.transactionamount} ")
        print(f"Category       :    {self.transaction_category} ")
        print(f"Description    :    {self.transaction_description} ")
        print(f"Date           :    {self.transaction_date} ")