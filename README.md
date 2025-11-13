# 📊 NAVIC A3 Poster Generator

Professional A3 poster generator for **NAVIC-Based Car Crash Detection System** academic research poster.

## ✨ Features

- ✅ **Guaranteed A3 Dimensions**: Perfect 420mm × 297mm landscape PDF output
- ✅ **Two Generation Methods**: Python (WeasyPrint) or Node.js (Puppeteer)
- ✅ **Professional Academic Design**: Clean layout with proper borders
- ✅ **Print-Ready Quality**: High-resolution output for professional printing
- ✅ **Integrated Logos**: University and organization logos embedded
- ✅ **Professional Borders**: 12mm outer + 2mm inner border

## 🚀 Quick Start (Recommended: Python Method)

### Method 1: Python with Flask (✨ Recommended - Easiest!)

#### Prerequisites
- Python 3.7 or higher
- pip3

#### Installation & Run

**Option A: One-Command Start (Easiest)**
```bash
./start.sh
```

**Option B: Manual Steps**
```bash
# Install dependencies
pip3 install -r requirements.txt

# Start the web server
python3 app.py
```

#### Open Browser
```
http://localhost:5000
```

Click the **"📥 Download A3 PDF"** button and your PDF will download!

---

### Method 2: Command Line (Python - No Web Server)

Generate PDF directly without a web server:

```bash
python3 generate_pdf.py
```

PDF will be saved as `NAVIC_Car_Crash_Detection_Poster_A3.pdf` in the current directory.

---

### Method 3: Node.js with Puppeteer (Advanced)

**Note**: This method requires downloading Chrome and may have more setup issues.

#### Prerequisites
- Node.js 14+ and npm

#### Installation
```bash
npm install
npm start
```

#### Open Browser
```
http://localhost:3000
```

## 📥 Generating the PDF

### Web Interface (Recommended)

1. Start the server (using `./start.sh` or `python3 app.py`)
2. Open `http://localhost:5000` in your browser
3. Click **"📥 Download A3 PDF"**
4. Wait 10-15 seconds
5. PDF downloads automatically!

### Command Line

```bash
python3 generate_pdf.py
```

### Direct API Call

```bash
# Python server
curl http://localhost:5000/generate-pdf --output poster.pdf

# Or open in browser
http://localhost:5000/generate-pdf
```

## 📁 Project Structure

```
A3_Poster/
├── app.py                   # Flask web server (Python) ⭐
├── generate_pdf.py          # CLI PDF generator (Python) ⭐
├── start.sh                 # Quick start script ⭐
├── requirements.txt         # Python dependencies ⭐
├── server.js               # Express server (Node.js - alternative)
├── package.json            # Node.js dependencies
├── README.md               # This file
├── public/
│   ├── index.html         # Main interface with download button
│   └── poster.html        # Clean poster for PDF generation
├── assets/
│   ├── jain-university.png
│   ├── IIT_Tirupati_logo.svg
│   └── national_mission...jpg
└── pnt.html               # Original HTML (backup)
```

## 🎨 Poster Specifications

- **Size**: A3 (420mm × 297mm)
- **Orientation**: Landscape
- **Format**: PDF
- **Resolution**: Print-ready quality
- **Borders**:
  - Outer: 12mm solid blue (#1E3A8A)
  - Inner: 2mm solid light blue (#3B82F6)
- **Font**: Arial/Helvetica (widely available)
- **Color Profile**: Print-optimized

## 🛠️ Technical Stack

### Python Stack (Recommended)
- **Backend**: Flask (Python web framework)
- **PDF Generation**: WeasyPrint (reliable HTML to PDF)
- **Frontend**: Pure HTML/CSS/JavaScript

### Node.js Stack (Alternative)
- **Backend**: Node.js + Express
- **PDF Generation**: Puppeteer (headless Chrome)
- **Frontend**: Pure HTML/CSS/JavaScript

## 📋 Requirements

### Python Method (Recommended)
```
Python 3.7+
Flask 3.0+
WeasyPrint 66.0+
```

Install with:
```bash
pip3 install -r requirements.txt
```

### Node.js Method (Alternative)
```
Node.js 14+
npm 6+
```

Install with:
```bash
npm install
```

## 🐛 Troubleshooting

### Python Method

**Problem: Module not found**
```bash
pip3 install flask weasyprint
```

**Problem: Permission denied**
```bash
chmod +x start.sh app.py generate_pdf.py
```

**Problem: Port 5000 already in use**

Edit `app.py` and change port:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Node.js Method

**Problem: Puppeteer Chrome download fails**

The Python method is recommended as it doesn't require downloading Chrome.

### General

**Problem: Logos not showing**

Verify assets folder:
```bash
ls -la assets/
```

**Problem: PDF dimensions wrong**

The PDF is correctly sized to A3. Verify in your PDF viewer:
- File → Properties → Page Size should show "A3 (420 x 297 mm)"

## ⚙️ Configuration

### Change Port (Python)

Edit `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change 5000 to your port
```

### Change Port (Node.js)

Edit `server.js`:
```javascript
const PORT = process.env.PORT || 3000;  // Change 3000 to your port
```

Or use environment variable:
```bash
PORT=8080 npm start
```

## 🎯 Use Cases

- ✅ Academic conference posters
- ✅ Research presentations
- ✅ Internship showcases
- ✅ University project displays
- ✅ Professional printing services
- ✅ Academic portfolio submissions

## 📝 Customization

### Update Content

Edit `public/poster.html`:
- Modify text and data
- Change colors and styling
- Adjust layout and sections
- Update fonts and sizes

### Change Logos

Replace files in `assets/` folder or update paths in `poster.html`.

### Modify Borders

In `poster.html`, adjust the CSS:
```css
.poster {
    border: 12mm solid #1E3A8A;  /* Outer border */
}
.poster-inner {
    border: 2mm solid #3B82F6;   /* Inner border */
}
```

## 🚀 Deployment

### Local Use
```bash
./start.sh
```

### Server Deployment
```bash
# Using Gunicorn (production)
pip3 install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📄 Files Generated

- **PDF File**: `NAVIC_Car_Crash_Detection_Poster_A3.pdf`
- **Size**: ~300-400 KB
- **Format**: PDF/A (archival quality)
- **Dimensions**: Exactly 420mm × 297mm (A3 landscape)

## 🎓 Academic Information

**Project**: NAVIC-Based Car Crash Detection System
**Author**: Bharath K (23BCAR0252)
**Institution**: JAIN (Deemed-to-be University)
**Program**: PNT Internship 2025
**Guides**: Dr. K. Suneetha & Dr. Zion Ramdinthara

## 📞 Support

### Check Status
```bash
# Python method
python3 -c "import flask, weasyprint; print('✅ All dependencies OK')"

# Node.js method
node -v && npm -v
```

### Get Help
1. Read troubleshooting section above
2. Check server logs in terminal
3. Verify file structure with `ls -la`
4. Contact: bharath.k@jainuniversity.ac.in

## 🙏 Acknowledgments

- **IIT Tirupati** - National Institute of Fabrication
- **JAIN University** - School of Computer Science & IT
- **NM-ICPS Program** - Department of Science & Technology
- **Guides**: Dr. K. Suneetha & Dr. Zion Ramdinthara

## 📄 License

MIT License - Free for academic use

---

## 🏃 Quick Commands Cheat Sheet

```bash
# Start web server (easiest)
./start.sh

# Generate PDF without server
python3 generate_pdf.py

# Start Flask server manually
python3 app.py

# Start Node.js server (alternative)
npm start

# Install Python dependencies
pip3 install -r requirements.txt

# Install Node.js dependencies
npm install

# Check if everything works
python3 -c "import flask, weasyprint; print('✅ Ready!')"
```

---

**Made with ❤️ for NAVIC Car Crash Detection System Research**

**⭐ Star this repository if it helped you!**
