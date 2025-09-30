import pandas as pd

pd.DataFrame()

class RailwayForm:
    formType = "RailwayForm"

    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

divyanshuApplication = RailwayForm()
divyanshuApplication.name = "Divyanshu"
divyanshuApplication.train = "Rajdhani Express"
divyanshuApplication.printData()