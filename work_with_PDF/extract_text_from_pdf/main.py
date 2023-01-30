import fitz

with fitz.open("students.pdf") as pdf:
    for page in pdf:
        print(page.get_text())
        print(20 * '-')
    page1 = pdf[0].get_text()
    print(page1)
