from fpdf import FPDF

# P = portrait, l = landscape ;
pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()
# x = 500 add attribute to image method to move image to the x position
pdf.image('tiger.jpeg', w=80, h=50)

# Add title
# First define text font
# Then use cell method to add title
# border = 1 add attribute to cell method to add border in your title
# ln = 1 add break line between paragraphs, if space between paragraphs is too big, you need to decrease 'h' attribute
pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt='Malayan Tiger', align='C', ln=1)

# Add next paragraph
pdf.set_font(family='Times', style='B', size=16)
pdf.cell(w=0, h=25, txt='Description', ln=1)

# Add next paragraph

pdf.set_font(family='Times', size=12)
# Do not use fill the paragraph in IDE it will give the wrong result
text = """The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native to Peninsular Malaysia.[2] This population inhabits the southern and central parts of the Malay Peninsula and has been classified as critically endangered on the IUCN Red List since 2015. As of April 2014, the population was estimated at 80 to 120 mature individuals with a continuous declining trend.[3]"""

# Use this method if you add multiline paragraphs
pdf.multi_cell(w=0, h=20, txt=text)

# Add table title
pdf.set_font(family='Times', style='B', size=16)
pdf.cell(w=0, h=50, txt='Scientific classification', ln=1)

# Add table row
pdf.set_font(family='Times', style='B', size=16)
pdf.cell(w=100, h=25, txt='Kingdom:')

pdf.set_font(family='Times', size=16)
pdf.cell(w=100, h=25, txt='Animalia', ln=1)

# Add table row
pdf.set_font(family='Times', style='B', size=16)
pdf.cell(w=100, h=25, txt='Phylum:')

pdf.set_font(family='Times', size=16)
pdf.cell(w=100, h=25, txt='Chordata', ln=1)

pdf.output('output.pdf')
