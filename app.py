#!/usr/bin/env python3
"""
Flask Web Application for A3 Poster PDF Generation
Simple and reliable PDF generation using WeasyPrint
"""

from flask import Flask, send_file, render_template, send_from_directory
from pathlib import Path
import os
import tempfile
from datetime import datetime

app = Flask(__name__,
            static_folder='assets',
            static_url_path='/assets',
            template_folder='public')

@app.route('/')
def index():
    """Serve the main page with download button"""
    return send_file('public/index.html')

@app.route('/poster')
def poster():
    """Serve the poster HTML for preview"""
    return send_file('public/poster.html')

@app.route('/generate-pdf')
def generate_pdf():
    """Generate and download A3 PDF"""
    try:
        from weasyprint import HTML, CSS

        # Read HTML content
        html_file = Path(__file__).parent / "public" / "poster.html"
        html_content = html_file.read_text()

        # Update asset paths
        base_url = f"file://{Path(__file__).parent}/"
        html_content = html_content.replace('src="/assets/', f'src="{base_url}assets/')

        # Create temporary PDF file
        temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
        temp_path = temp_pdf.name
        temp_pdf.close()

        # Generate PDF
        html_obj = HTML(string=html_content, base_url=base_url)
        html_obj.write_pdf(
            temp_path,
            stylesheets=[CSS(string='@page { size: A3 landscape; margin: 0; }')]
        )

        # Send file and clean up
        response = send_file(
            temp_path,
            mimetype='application/pdf',
            as_attachment=True,
            download_name='NAVIC_Car_Crash_Detection_Poster_A3.pdf'
        )

        # Schedule cleanup after sending
        @response.call_on_close
        def cleanup():
            try:
                os.unlink(temp_path)
            except:
                pass

        return response

    except Exception as e:
        return f"Error generating PDF: {str(e)}", 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 A3 Poster Generator Server Starting...")
    print("="*60)
    print(f"\n📊 Open your browser and visit:")
    print(f"   http://localhost:5000")
    print(f"\n📥 Direct PDF download:")
    print(f"   http://localhost:5000/generate-pdf")
    print(f"\n👁️  Preview poster:")
    print(f"   http://localhost:5000/poster")
    print("\n" + "="*60 + "\n")

    app.run(debug=True, host='0.0.0.0', port=5000)
