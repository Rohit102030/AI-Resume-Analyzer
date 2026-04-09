from reportlab.platypus import SimpleDocTemplate, Paragraph

def generate_report(filename, content):
    doc = SimpleDocTemplate(filename)
    elements = []

    for line in content:
        elements.append(Paragraph(line))

    doc.build(elements)