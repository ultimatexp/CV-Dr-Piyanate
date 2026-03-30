import os
from weasyprint import HTML, CSS

def generate_cv_pdf():
    # Define paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(base_dir, 'cv_template.html')
    css_path = os.path.join(base_dir, 'cv_style.css')
    output_path = os.path.join(base_dir, 'CV_Dr_Piyanate_Redesign.pdf')

    # Load HTML and CSS
    html = HTML(filename=html_path, base_url=base_dir)
    css = CSS(filename=css_path)

    # Generate PDF
    print(f"Generating PDF at {output_path}...")
    html.write_pdf(output_path, stylesheets=[css])
    print("PDF generation complete.")

if __name__ == "__main__":
    generate_cv_pdf()
