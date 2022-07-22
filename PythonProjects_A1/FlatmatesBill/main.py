<<<<<<< HEAD
<<<<<<< HEAD
from fpdf import FPDF


class Bill:
    """
    data about the bill, the amount and the billing period
    """
=======
from flat import Bill, Flatmate
from reports import PdfReport
>>>>>>> 6d98c4af186bbf39371624e4fab8de64cf01ec22
=======
from flat import Bill, Flatmate
from reports import PdfReport
>>>>>>> 6d98c4af186bbf39371624e4fab8de64cf01ec22

bill_amount = float(input("enter the bill amount: "))
bill_period = input("enter the bill period")
the_bill = Bill(amount=bill_amount, period=bill_period)

flatmate_1_name = input("enter the first flatmates' name")
flatmate_1_days = int(input("enter the first flatmates stay in number of days"))

flatmate_2_name = input("enter the second flatmates' name")
flatmate_2_days = int(input("enter the second flatmates stay in number of days"))

first_flatmate = Flatmate(name=flatmate_1_name, days=flatmate_1_days)
second_flatmate = Flatmate(name=flatmate_2_name, days=flatmate_2_days)

pdf_report = PdfReport(the_bill.period + ".pdf")
pdf_report.generate_report(flatmate1=first_flatmate, flatmate2=second_flatmate, bill=the_bill)

<<<<<<< HEAD
<<<<<<< HEAD

class PdfReport:
    """
    creates a pdf report
    """

    def __init__(self, filename):
        self.filename = filename

    def generate_report(self, flatmate1, flatmate2, bill):
        # create a pdf document
        my_pdf = FPDF(orientation='P', unit='pt', format='A4')
        my_pdf.add_page()

        # add the title
        my_pdf.set_font(family='Times', size=24, style='B')
        my_pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)
        my_pdf.cell(w=200, h=40, txt="Bill Period", border=1)
        my_pdf.cell(w=338.5, h=40, txt=bill.period, border=1, ln=1)

        # add the flatmates info
        #flatmate1
        my_pdf.cell(w=200, h=40, txt=flatmate1.name, border=1)
        my_pdf.cell(w=338.5, h=40, txt=str(round(flatmate1.pay(bill, flatmate2), 2)), border=1, ln=1)

        #flatmate2
        my_pdf.cell(w=200, h=40, txt=flatmate2.name, border=1)
        my_pdf.cell(w=338.5, h=40, txt=str(round(flatmate2.pay(bill, flatmate1), 2)), border=1)
        my_pdf.output(self.filename)


electricity_bill = Bill(amount=130, period="Jun 22")
john = Flatmate("John", 21)
jane = Flatmate("Jane", 27)

print(john.pay(electricity_bill, jane))
print(jane.pay(electricity_bill, john))

pdf_report = PdfReport("report1.pdf")
pdf_report.generate_report(jane, john, electricity_bill)
=======
>>>>>>> 6d98c4af186bbf39371624e4fab8de64cf01ec22
=======
>>>>>>> 6d98c4af186bbf39371624e4fab8de64cf01ec22
