from PyPDF2 import PdfFileMerger
import glob

pdfs = glob.glob("*.pdf")
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("MergedSessions.pdf")
merger.close()
