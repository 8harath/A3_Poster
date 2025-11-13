#!/usr/bin/env python3
"""
A3 Poster PDF Generator using WeasyPrint
Generates a professional A3 PDF from HTML
"""

import os
import sys
from pathlib import Path

def generate_pdf():
    """Generate A3 PDF from poster HTML"""
    try:
        from weasyprint import HTML, CSS
        print("WeasyPrint loaded successfully!")
    except ImportError:
        print("ERROR: WeasyPrint is not installed.")
        print("Install it with: pip3 install weasyprint")
        sys.exit(1)

    # Paths
    html_file = Path(__file__).parent / "public" / "poster.html"
    output_file = Path(__file__).parent / "NAVIC_Car_Crash_Detection_Poster_A3.pdf"

    if not html_file.exists():
        print(f"ERROR: HTML file not found at {html_file}")
        sys.exit(1)

    print(f"Reading HTML from: {html_file}")
    print(f"Generating PDF...")

    # Read HTML content
    html_content = html_file.read_text()

    # Replace asset paths for proper resolution
    base_url = f"file://{Path(__file__).parent}/"
    html_content = html_content.replace('src="/assets/', f'src="{base_url}assets/')

    # Generate PDF with A3 dimensions (landscape)
    # A3 = 420mm x 297mm (landscape)
    html_obj = HTML(string=html_content, base_url=base_url)

    print("Rendering PDF... (this may take 10-15 seconds)")
    html_obj.write_pdf(
        output_file,
        stylesheets=[CSS(string='@page { size: A3 landscape; margin: 0; }')]
    )

    print(f"\n✅ SUCCESS! PDF generated at:")
    print(f"   {output_file.absolute()}")
    print(f"\nFile size: {output_file.stat().st_size / 1024:.1f} KB")
    print("\nThe PDF is ready for printing!")

    return str(output_file.absolute())

if __name__ == "__main__":
    generate_pdf()
