from fpdf import FPDF

pdf = FPDF(orientation="P", format="A4")
pdf.add_page()
pdf.set_font("helvetica", style="B", size=48)
# pdf.text(100,10,"CS50 Certificate") 
pdf.cell(0,text="CS50 Shirtificate",align="C")

# 1. Register the image internally to inspect its dimensions
img_info = pdf.preload_image("https://cs50.harvard.edu/python/psets/8/shirtificate/shirtificate.png")



pdf.image("https://cs50.harvard.edu/python/psets/8/shirtificate/shirtificate.png", x="C", y=70, w=pdf.epw)
name = input("Name: ")
text_to_print = f"{name} took CS50"
pdf.set_font("helvetica", style="B", size=24)
pdf.set_text_color(255,255,255)
pdf.set_y(140)
pdf.cell(0,10,text_to_print, align="C")

pdf.output("Shirtificate.pdf")

