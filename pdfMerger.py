from PyPDF2 import PdfFileMerger
import glob

pdfs = glob.glob("*.pdf")
if not pdfs:
    print("Error - No PDF's found in Directory")
    exit()
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("MergedSessions.pdf")
merger.close()
