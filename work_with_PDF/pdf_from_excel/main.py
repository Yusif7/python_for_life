import pandas
from fpdf import FPDF

df = pandas.read_excel('data.xlsx')

for index, row in df.iterrows():
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()
    # Add title
    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=50, txt=row['name'], align='C', ln=1)
    # This syntax give us access to columns in Excel file
    for column in df.columns[1:]:
        # Add table
        pdf.set_font(family='Times', style='B', size=16)
        pdf.cell(w=100, h=25, txt=column.capitalize() + ':',)

        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt=row[column], ln=1)

    pdf.output(f"{row['name']}.pdf")
