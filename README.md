# A3 Poster Generator

**Professional Academic Research Poster Generation Tool**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![Node.js](https://img.shields.io/badge/Node.js-14%2B-green.svg)](https://nodejs.org/)

---

## Overview

The **A3 Poster Generator** is a production-ready web application designed to generate print-quality, professional academic research posters in A3 landscape format (420mm × 297mm). Built for the **NAVIC-Based Car Crash Detection System** research project, this tool provides a flexible, dual-architecture approach to PDF generation with both Python and Node.js implementations.

This project addresses the common challenge of creating consistent, print-ready academic posters by automating the rendering and PDF generation process while maintaining precise dimensional specifications and professional visual design standards.

### Key Highlights

- **Guaranteed A3 dimensions** with exact 420mm × 297mm landscape output
- **Dual implementation architectures** supporting both Python (WeasyPrint) and Node.js (Puppeteer)
- **Print-ready quality** with proper color profiles and high-resolution rendering
- **Professional academic design** featuring institutional logos, structured sections, and visual hierarchy
- **Multiple generation methods** including web interface, CLI, and direct API access
- **Zero-dependency frontend** using pure HTML/CSS/JavaScript

---

## Table of Contents

- [Features](#features)
- [System Architecture](#system-architecture)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technical Specifications](#technical-specifications)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Use Cases](#use-cases)
- [Customization](#customization)
- [Contributing](#contributing)
- [Academic Context](#academic-context)
- [License](#license)

---

## Features

### Core Functionality

- ✅ **Precise A3 Dimensions**: Guaranteed 420mm × 297mm landscape PDF output meeting international standards
- ✅ **Dual Backend Support**: Choose between Python (Flask + WeasyPrint) or Node.js (Express + Puppeteer)
- ✅ **Multiple Access Methods**: Web interface, command-line tool, or direct HTTP API
- ✅ **Print-Ready Output**: High-resolution rendering optimized for professional printing services
- ✅ **Professional Border Design**: Dual-layer border system (12mm outer + 2mm inner) for visual polish
- ✅ **Embedded Assets**: Integrated university and organization logos with proper resolution handling
- ✅ **Responsive Interface**: Clean, modern web UI with real-time status feedback
- ✅ **Error Handling**: Comprehensive error management with fallback mechanisms
- ✅ **Health Monitoring**: Built-in health check endpoints for production deployments

### Technical Features

- **Server-side PDF generation** eliminating browser-specific rendering inconsistencies
- **Temporary file management** with automatic cleanup after delivery
- **CORS support** for cross-origin API requests
- **Static asset optimization** with efficient file serving
- **Modular architecture** allowing easy extension and customization
- **Cross-platform compatibility** running on Linux, macOS, and Windows

---

## System Architecture

### Architecture Overview

The application follows a modular, layered architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                        Client Layer                          │
│  (Web Browser - HTML/CSS/JavaScript Interface)              │
└─────────────────┬───────────────────────────────────────────┘
                  │ HTTP/HTTPS
                  ▼
┌─────────────────────────────────────────────────────────────┐
│                     Application Layer                        │
│  ┌──────────────────┐         ┌──────────────────┐         │
│  │   Flask Server   │   OR    │  Express Server  │         │
│  │   (Python 3.7+)  │         │   (Node.js 14+)  │         │
│  └────────┬─────────┘         └─────────┬────────┘         │
│           │                               │                  │
│           ▼                               ▼                  │
│  ┌──────────────────┐         ┌──────────────────┐         │
│  │   WeasyPrint     │         │    Puppeteer     │         │
│  │  (HTML to PDF)   │         │ (Headless Chrome)│         │
│  └────────┬─────────┘         └─────────┬────────┘         │
└───────────┼───────────────────────────────┼──────────────────┘
            │                               │
            ▼                               ▼
┌─────────────────────────────────────────────────────────────┐
│                      Rendering Layer                         │
│  • HTML Template Processing (poster.html)                   │
│  • CSS Styling & Layout Engine                              │
│  • Asset Resolution (logos, images)                         │
│  • Page Size Configuration (A3 landscape)                   │
└─────────────────┬───────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│                       Output Layer                           │
│         PDF File (420mm × 297mm, print-ready)               │
└─────────────────────────────────────────────────────────────┘
```

### Component Interaction Flow

1. **User Request**: Client initiates PDF generation via web interface or direct API call
2. **Server Processing**: Flask or Express server receives request and loads HTML template
3. **Asset Resolution**: Server resolves all asset paths (logos, stylesheets) to absolute URLs
4. **PDF Rendering**: WeasyPrint or Puppeteer renders HTML to PDF with A3 specifications
5. **File Delivery**: Generated PDF is sent to client as downloadable attachment
6. **Cleanup**: Temporary files are automatically removed post-delivery

### Technology Stack Comparison

| Component | Python Stack (Recommended) | Node.js Stack (Alternative) |
|-----------|---------------------------|----------------------------|
| **Web Framework** | Flask 3.0+ | Express 4.18+ |
| **PDF Engine** | WeasyPrint 66.0+ | Puppeteer 21.6+ |
| **Rendering** | Cairo graphics library | Chrome DevTools Protocol |
| **Installation Size** | ~50-100 MB | ~300-400 MB (includes Chromium) |
| **Startup Time** | Fast (~1-2 seconds) | Moderate (~3-5 seconds) |
| **Memory Usage** | Low (~50-100 MB) | Moderate (~150-300 MB) |
| **Dependencies** | System libraries (Cairo, Pango) | Bundled Chromium browser |
| **Best For** | Production servers, Linux environments | Development, Windows/macOS |

---

## Quick Start

### Method 1: Python Flask Server (Recommended)

**One-Command Start:**

```bash
./start.sh
```

The script automatically:
- Checks Python 3 installation
- Installs required dependencies if missing
- Starts the Flask server on port 5000

**Access the application:**

```
http://localhost:5000
```

Click **"Download A3 PDF"** and your poster will be generated and downloaded automatically.

---

### Method 2: Command-Line Generation (No Web Server)

For direct PDF generation without starting a web server:

```bash
python3 generate_pdf.py
```

**Output:**
- File: `NAVIC_Car_Crash_Detection_Poster_A3.pdf`
- Location: Current working directory
- Size: ~300-400 KB

---

### Method 3: Node.js Server (Alternative)

For environments where Node.js is preferred:

```bash
npm install
npm start
```

**Access the application:**

```
http://localhost:3000
```

---

## Installation

### Prerequisites

#### For Python Method (Recommended)

- **Python**: 3.7 or higher
- **pip**: Python package manager (usually bundled with Python)
- **System Libraries** (auto-installed on most systems):
  - Cairo (graphics rendering)
  - Pango (text layout)
  - GDK-PixBuf (image loading)

#### For Node.js Method

- **Node.js**: 14.0 or higher
- **npm**: 6.0 or higher (bundled with Node.js)

### Installation Steps

#### Python Installation

**1. Clone the repository:**

```bash
git clone https://github.com/8harath/A3_Poster.git
cd A3_Poster
```

**2. Install Python dependencies:**

```bash
pip3 install -r requirements.txt
```

**Dependencies installed:**
- `Flask==3.0.0` - Web framework
- `weasyprint==66.0` - PDF generation library
- `Werkzeug==3.0.1` - WSGI utility library

**3. Verify installation:**

```bash
python3 -c "import flask, weasyprint; print('✅ All dependencies installed successfully')"
```

#### Node.js Installation

**1. Clone the repository:**

```bash
git clone https://github.com/8harath/A3_Poster.git
cd A3_Poster
```

**2. Install Node.js dependencies:**

```bash
npm install
```

**Dependencies installed:**
- `express` - Web framework
- `puppeteer` - Headless Chrome automation
- `cors` - Cross-origin resource sharing middleware

**3. Verify installation:**

```bash
node -v && npm -v
```

---

## Usage

### Web Interface Usage

#### Starting the Server

**Python:**
```bash
python3 app.py
```

**Node.js:**
```bash
npm start
```

#### Generating PDFs via Web UI

1. Navigate to `http://localhost:5000` (Python) or `http://localhost:3000` (Node.js)
2. Review poster specifications and features
3. Click **"Download A3 PDF"** button
4. Wait 10-15 seconds for generation
5. PDF downloads automatically to your default downloads folder

**Expected Generation Time:**
- Python (WeasyPrint): 8-12 seconds
- Node.js (Puppeteer): 10-15 seconds

#### Previewing the Poster

To preview the poster in your browser before generating the PDF:

```
http://localhost:5000/poster
```

This displays the exact poster layout that will be converted to PDF.

---

### Command-Line Usage

#### Direct PDF Generation

```bash
python3 generate_pdf.py
```

**Output:**
```
WeasyPrint loaded successfully!
Reading HTML from: /path/to/public/poster.html
Generating PDF...
Rendering PDF... (this may take 10-15 seconds)

✅ SUCCESS! PDF generated at:
   /path/to/NAVIC_Car_Crash_Detection_Poster_A3.pdf

File size: 328.4 KB

The PDF is ready for printing!
```

---

### API Usage

#### Direct API Endpoint

**Python Server:**

```bash
# Download via curl
curl http://localhost:5000/generate-pdf -o poster.pdf

# Or open directly in browser
open http://localhost:5000/generate-pdf
```

**Node.js Server:**

```bash
curl http://localhost:3000/generate-pdf -o poster.pdf
```

#### Health Check Endpoint (Python Only)

```bash
curl http://localhost:5000/health
```

**Response:**
```json
{
  "status": "ok",
  "timestamp": "2025-01-20T10:30:45.123456"
}
```

---

## Project Structure

```
A3_Poster/
│
├── app.py                      # Flask web server (Python) - Primary backend
├── generate_pdf.py             # CLI PDF generator (Python) - Standalone tool
├── server.js                   # Express server (Node.js) - Alternative backend
├── start.sh                    # Quick start automation script
│
├── requirements.txt            # Python dependencies
├── package.json                # Node.js dependencies and metadata
│
├── README.md                   # Comprehensive project documentation
├── PRINT_INSTRUCTIONS.md       # Detailed printing guidelines
├── .gitignore                  # Git exclusion rules
│
├── public/                     # Frontend files
│   ├── index.html             # Main web interface with download UI
│   └── poster.html            # Clean poster template for PDF generation
│
├── assets/                     # Static resources
│   ├── jain-university.png            # JAIN University logo
│   ├── IIT_Tirupati_logo.svg          # IIT Tirupati logo
│   └── national_mission_...jpg        # NM-ICPS program logo
│
└── pnt.html                    # Original HTML (archived backup)
```

### Key Files Explained

- **app.py**: Flask application serving the web interface and handling PDF generation via WeasyPrint
- **generate_pdf.py**: Standalone Python script for command-line PDF generation without server
- **server.js**: Node.js alternative using Express and Puppeteer for PDF generation
- **start.sh**: Automated setup and launch script with dependency checking
- **public/index.html**: User-facing web interface with download button and status indicators
- **public/poster.html**: Poster template with embedded CSS and structured content layout
- **assets/**: Institutional logos and branding assets embedded in the poster

---

## Technical Specifications

### PDF Output Specifications

| Property | Value |
|----------|-------|
| **Format** | PDF (Portable Document Format) |
| **Page Size** | A3 (ISO 216 standard) |
| **Dimensions** | 420mm × 297mm (16.54" × 11.69") |
| **Orientation** | Landscape |
| **Margins** | 0mm (full bleed) |
| **Resolution** | Print-ready (300+ DPI equivalent) |
| **Color Space** | RGB (optimized for digital printing) |
| **File Size** | ~300-400 KB (typical) |
| **Compatibility** | PDF/A compliant for archival |

### Poster Design Specifications

| Element | Specification |
|---------|--------------|
| **Outer Border** | 12mm solid, color #1E3A8A (navy blue) |
| **Inner Border** | 2mm solid, color #3B82F6 (light blue) |
| **Font Family** | Arial, Helvetica, sans-serif |
| **Title Font Size** | 19pt, weight 900 (extra bold) |
| **Section Headers** | 7-8.5pt, weight 800 (bold) |
| **Body Text** | 5.5pt, line-height 1.1 |
| **Layout** | 3-column grid with flexible content areas |
| **Color Coding** | Semantic colors for different section types |
| **Logo Height** | 11-12mm optimized for print visibility |

### Browser Compatibility

The web interface is tested and compatible with:

- ✅ Google Chrome 90+
- ✅ Mozilla Firefox 88+
- ✅ Microsoft Edge 90+
- ✅ Safari 14+
- ✅ Opera 76+

### Server Requirements

**Minimum Requirements:**
- **CPU**: 1 core, 1.5 GHz
- **RAM**: 512 MB available memory
- **Storage**: 200 MB free space
- **Network**: Port 5000 (Python) or 3000 (Node.js) available

**Recommended for Production:**
- **CPU**: 2+ cores, 2.0+ GHz
- **RAM**: 1 GB+ available memory
- **Storage**: 500 MB+ free space
- **OS**: Linux (Ubuntu 20.04+, Debian 10+, CentOS 8+)

---

## Configuration

### Port Configuration

#### Python Flask

Edit `app.py` (line 92):

```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

Change `port=5000` to your desired port number.

#### Node.js Express

Edit `server.js` (line 7):

```javascript
const PORT = process.env.PORT || 3000;
```

Or use environment variable:

```bash
PORT=8080 npm start
```

### Debug Mode

#### Python

To disable debug mode for production:

```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

#### Node.js

Set NODE_ENV environment variable:

```bash
NODE_ENV=production npm start
```

### Asset Path Configuration

If you move the assets folder or use external asset URLs, update `public/poster.html`:

```html
<!-- Change from: -->
<img src="/assets/jain-university.png" alt="JAIN">

<!-- To: -->
<img src="https://example.com/path/to/logo.png" alt="JAIN">
```

---

## Deployment

### Local Development

**Quick start for development:**

```bash
./start.sh
```

### Production Deployment with Gunicorn

For production environments, use Gunicorn WSGI server:

**1. Install Gunicorn:**

```bash
pip3 install gunicorn
```

**2. Run with Gunicorn:**

```bash
# 4 worker processes, bind to all interfaces
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**3. With logging:**

```bash
gunicorn -w 4 -b 0.0.0.0:5000 \
  --access-logfile access.log \
  --error-logfile error.log \
  app:app
```

### Docker Deployment

**Create Dockerfile:**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

**Build and run:**

```bash
docker build -t a3-poster-generator .
docker run -p 5000:5000 a3-poster-generator
```

### systemd Service (Linux)

**Create service file** `/etc/systemd/system/poster-generator.service`:

```ini
[Unit]
Description=A3 Poster Generator
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/opt/A3_Poster
Environment="PATH=/usr/local/bin:/usr/bin"
ExecStart=/usr/local/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
```

**Enable and start:**

```bash
sudo systemctl daemon-reload
sudo systemctl enable poster-generator
sudo systemctl start poster-generator
```

---

## Troubleshooting

### Python Method Issues

#### Error: Module not found

**Problem:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
pip3 install flask weasyprint
# Or install all dependencies
pip3 install -r requirements.txt
```

#### Error: WeasyPrint dependencies missing

**Problem:**
```
OSError: cannot load library 'gobject-2.0-0'
```

**Solution (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install -y \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    shared-mime-info
```

**Solution (macOS):**
```bash
brew install cairo pango gdk-pixbuf
```

#### Error: Permission denied

**Problem:**
```bash
-bash: ./start.sh: Permission denied
```

**Solution:**
```bash
chmod +x start.sh app.py generate_pdf.py
```

#### Error: Port already in use

**Problem:**
```
OSError: [Errno 48] Address already in use
```

**Solution:**

Find and kill the process using port 5000:
```bash
lsof -ti:5000 | xargs kill -9
```

Or change the port in `app.py`.

### Node.js Method Issues

#### Error: Puppeteer Chrome download fails

**Problem:**
Puppeteer fails to download Chromium during npm install.

**Solution:**

Use the Python method, which doesn't require downloading Chrome. Alternatively:

```bash
npm install puppeteer --unsafe-perm=true
```

#### Error: No usable sandbox

**Problem:**
```
Error: Failed to launch chrome! No usable sandbox!
```

**Solution:**

The Node.js server already includes `--no-sandbox` flag. If issues persist, verify Node.js version:

```bash
node --version  # Should be 14+
```

### General Issues

#### Problem: Logos not displaying

**Verify assets folder:**
```bash
ls -la assets/
```

Expected output:
```
jain-university.png
IIT_Tirupati_logo.svg
national_mission_in_interdisciplinary_cyber_physical_systems_nm_icps-scaled.jpg
```

If files are missing, ensure you cloned the complete repository.

#### Problem: PDF dimensions incorrect

**Verification:**

Open the generated PDF in a viewer, go to **File → Properties**, and verify:
- **Page Size**: A3 (420 x 297 mm) or (16.54 x 11.69 in)

The dimensions are correctly configured in the code. If your viewer shows different dimensions, the PDF itself is correct—this may be a display issue in the viewer.

#### Problem: Generated PDF is blank or incomplete

**Common causes:**
1. **Assets not loading**: Check asset paths in `poster.html`
2. **Font issues**: Ensure Arial/Helvetica fonts are available
3. **Rendering timeout**: Increase timeout values in the code

**Debug:**
```bash
# Test poster HTML directly
python3 app.py
# Visit http://localhost:5000/poster in browser
```

---

## Use Cases

### Academic Applications

- ✅ **Conference Presentations**: Research posters for academic conferences and symposia
- ✅ **Internship Showcases**: Project demonstrations for internship programs
- ✅ **University Project Displays**: Final year projects and capstone presentations
- ✅ **Research Lab Exhibitions**: Laboratory open houses and research showcases
- ✅ **Academic Portfolios**: Professional portfolio submissions for graduate programs
- ✅ **Thesis Defenses**: Visual aids for thesis and dissertation presentations

### Professional Applications

- ✅ **Industry Conferences**: Technical presentations at industry events
- ✅ **Trade Shows**: Product and technology demonstrations
- ✅ **Scientific Publications**: Supplementary visual materials for papers
- ✅ **Grant Proposals**: Visual summaries for funding applications
- ✅ **Educational Materials**: Teaching aids and instructional posters

### Customization for Other Projects

This tool can be adapted for any project requiring A3 poster generation:

1. Edit `public/poster.html` with your content
2. Replace logos in `assets/` folder
3. Adjust colors and styling in the CSS section
4. Generate your custom poster

---

## Customization

### Updating Content

Edit `public/poster.html` to modify:

- **Title and subtitle** (lines 75-76)
- **Author information** (line 78)
- **Section content** (lines 84-162)
- **Footer contact info** (line 166)

### Changing Colors

Modify color variables in `public/poster.html` CSS section:

```css
/* Primary colors */
.poster { background: #1E3A8A; }  /* Outer border color */
.inner { border: 1mm solid #3B82F6; }  /* Inner border color */

/* Section color coding */
.prob { border-left-color: #DC2626; background: #FEF2F2; }  /* Problem - Red */
.motv { border-left-color: #F59E0B; background: #FFFBEB; }  /* Motivation - Orange */
.impl { border-left-color: #10B981; background: #F0FDF4; }  /* Implementation - Green */
.fut { border-left-color: #8B5CF6; background: #F5F3FF; }   /* Future - Purple */
```

### Modifying Layout

The poster uses a responsive grid layout:

```css
.grid {
    display: grid;
    grid-template-columns: 1fr 1.5fr 1fr;  /* Adjust column widths */
    gap: 2mm;  /* Adjust spacing */
}
```

Change `grid-template-columns` to adjust column proportions:
- `1fr 1fr 1fr` = Equal three columns
- `2fr 1fr 1fr` = Wider left column
- `1fr 2fr` = Two-column layout

### Replacing Logos

**Option 1: Replace files**

Replace existing files in `assets/` folder with same filenames:
```bash
cp new-logo.png assets/jain-university.png
```

**Option 2: Update paths**

Edit `public/poster.html` (lines 69-71):

```html
<img src="/assets/your-logo-1.png" alt="Organization 1">
<img src="/assets/your-logo-2.svg" alt="Organization 2">
<img src="/assets/your-logo-3.jpg" alt="Organization 3">
```

### Adjusting Font Sizes

For better readability or to fit more content, adjust font sizes in CSS:

```css
.ttl { font-size: 19pt; }      /* Title - increase for prominence */
.sub { font-size: 9pt; }       /* Subtitle */
.sec h3 { font-size: 7pt; }    /* Section headers */
.sec p, .sec li { font-size: 5.5pt; }  /* Body text */
```

### Modifying Borders

Adjust border thickness and style:

```css
.poster {
    padding: 6mm;  /* Outer border thickness */
}

.inner {
    border: 1mm solid #3B82F6;  /* Inner border: thickness, style, color */
}
```

---

## Contributing

Contributions are welcome! This project can be improved in several ways:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature`
3. **Make your changes** with clear, descriptive commits
4. **Test thoroughly** with both Python and Node.js methods
5. **Submit a pull request** with detailed description

### Areas for Contribution

- **Additional poster templates** for different research domains
- **Enhanced customization interface** (web-based editor)
- **Batch processing capabilities** for multiple posters
- **Additional export formats** (PNG, SVG, etc.)
- **Internationalization** support for multiple languages
- **Performance optimizations** for faster PDF generation
- **Additional deployment guides** (Heroku, AWS, Azure, etc.)

---

## Academic Context

### Project Information

**Research Project**: NAVIC-Based Car Crash Detection System
**Focus Area**: Communication Pipeline & Android Prototype Development
**Domain**: Position, Navigation & Timing (PNT) Systems
**Program**: National Mission on Interdisciplinary Cyber-Physical Systems (NM-ICPS)

### Author

**Name**: Bharath K
**Student ID**: 23BCAR0252
**Institution**: JAIN (Deemed-to-be University)
**School**: School of Computer Science & Information Technology
**Email**: bharath.k@jainuniversity.ac.in

### Academic Supervision

**Primary Guide**: Dr. K. Suneetha (JAIN University)
**Co-Guide**: Dr. Zion Ramdinthara (IIT Tirupati)

### Collaborating Institutions

- **JAIN (Deemed-to-be University)** - School of Computer Science & IT
- **Indian Institute of Technology (IIT) Tirupati** - National Institute of Fabrication
- **National Mission on Interdisciplinary Cyber-Physical Systems (NM-ICPS)** - Department of Science & Technology, Government of India

### Project Metrics

- **GitHub Commits**: 416+
- **Development Duration**: Internship 2025
- **Implementation Status**: Phase-1 Prototype Validated
- **Repository**: [github.com/8harath/Car_Crash_Detection](https://github.com/8harath/Car_Crash_Detection)

---

## License

MIT License

Copyright (c) 2025 Bharath K

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Acknowledgments

This project was developed as part of the PNT Internship 2025 program under the National Mission on Interdisciplinary Cyber-Physical Systems (NM-ICPS), supported by the Department of Science & Technology, Government of India.

**Special thanks to:**

- **Dr. K. Suneetha** - Primary research guide and mentor
- **Dr. Zion Ramdinthara** - Co-guide and technical supervisor
- **IIT Tirupati** - National Institute of Fabrication for infrastructure and support
- **JAIN University** - School of Computer Science & IT for institutional support
- **NM-ICPS Program** - Financial and programmatic support

---

## Support and Contact

### Technical Support

For technical issues, please:

1. Check the [Troubleshooting](#troubleshooting) section
2. Verify your installation with provided commands
3. Review server logs for error messages

### Contact Information

**Email**: bharath.k@jainuniversity.ac.in
**GitHub**: [@8harath](https://github.com/8harath)
**Project Repository**: [A3_Poster](https://github.com/8harath/A3_Poster)

---

## Quick Reference

### Essential Commands

```bash
# Start Python server (recommended)
./start.sh
# or
python3 app.py

# Generate PDF without server
python3 generate_pdf.py

# Start Node.js server (alternative)
npm install && npm start

# Install Python dependencies
pip3 install -r requirements.txt

# Check Python setup
python3 -c "import flask, weasyprint; print('✅ Ready!')"

# Production deployment
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Quick Links

- **Web Interface**: http://localhost:5000
- **Poster Preview**: http://localhost:5000/poster
- **Direct PDF Download**: http://localhost:5000/generate-pdf
- **Health Check**: http://localhost:5000/health

---

<div align="center">

**⭐ If this project helped you, please consider giving it a star on GitHub! ⭐**

Made with ❤️ for the NAVIC Car Crash Detection System Research Project

</div>
