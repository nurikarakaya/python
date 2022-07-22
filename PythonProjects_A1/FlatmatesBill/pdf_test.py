from fpdf import FPDF

my_pdf = FPDF(orientation='P', unit='pt', format='A4')
my_pdf.add_page()

my_pdf.set_font(family='Times', size=24, style='B')
my_pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)
my_pdf.cell(w=200, h=40, txt="Bill Period", border=1)

my_pdf.cell(w=338.5, h=40, txt="June 2022", border=1)
my_pdf.output("our_bill.pdf")