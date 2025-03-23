class CommissionEmployee:
    def __init__(self,pdet,data):
        self.pdet=pdet
        self.sales_data=data
        
    @property
    def data(self):
        return self.sales_data
    
    @data.setter
    def data(self,value):
        if value<0:
            raise ValueError("Sales data cannot be negative")
        self.sale_data=value
    
    def earning(self):
        tax=5
        return f"Your annual income is ",self.data*tax/100
        
    def __repr__(self):
        return f"Commission Employee(pdet={self.pdet},sales data is {self.data})"


if __name__=="__main__":
    try:
        ce1=CommissionEmployee("2241003008",50)
        print(ce1)
        #current earning
        print("Earning is ",ce1.earning())

        ce1.data=100
        print("Updated salary is ",ce1.data)
        print("Updated earning is ",ce1.earning())
        try:
            ce1.data = -100
        except ValueError as e:
            print(f"Error: {e}")
    except Exception as e:
        print("An error has occuered: ",e)
        
        
