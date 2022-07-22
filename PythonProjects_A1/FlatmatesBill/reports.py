import webbrowser
import os

from fpdf import FPDF


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

        # add icon
        my_pdf.image("files/house.png", w=30, h=30)

        # add the title
        my_pdf.set_font(family='Times', size=24, style='B')
        my_pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)

        #
        my_pdf.set_font(family='Times', size=20)
        my_pdf.cell(w=200, h=40, txt="Bill Period", border=1)
        my_pdf.cell(w=338.5, h=40, txt=bill.period, border=1, ln=1)

        # add the flatmates' info
        # flatmate1
        my_pdf.set_font(family="Times", size=14)
        my_pdf.cell(w=200, h=40, txt=flatmate1.name, border=1)
        my_pdf.cell(w=338.5, h=40, txt=str(round(flatmate1.pay(bill, flatmate2), 2)), border=1, ln=1)

        # flatmate2
        my_pdf.cell(w=200, h=40, txt=flatmate2.name, border=1)
        my_pdf.cell(w=338.5, h=40, txt=str(round(flatmate2.pay(bill, flatmate1), 2)), border=1)

        # create the pdf
        my_pdf.output("files/" + self.filename)

        # change directory for webbowser to work
        os.chdir("files")
        # open the pdf auto
        webbrowser.open(self.filename)
