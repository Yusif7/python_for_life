from fpdf import FPDF

# P = portrait, l = landscape ;
pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()
