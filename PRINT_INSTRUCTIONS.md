# 📄 How to Generate Single-Page A3 PDF

The poster is optimized for A3 (420mm × 297mm) landscape format. Due to PDF rendering engine variations, here are the **recommended methods** for generating a perfect single-page PDF:

## ✅ Method 1: Browser Print to PDF (RECOMMENDED)

This method guarantees a single-page A3 PDF:

### Steps:

1. **Start the server:**
   ```bash
   python3 app.py
   ```

2. **Open in browser:**
   ```
   http://localhost:5000/poster
   ```

3. **Print to PDF:**
   - Press `Ctrl+P` (Windows/Linux) or `Cmd+P` (Mac)
   - Or use browser menu: File → Print

4. **Configure print settings:**
   - **Destination:** Save as PDF
   - **Layout:** Landscape
   - **Paper size:** A3
   - **Margins:** None (or Minimum)
   - **Scale:** 100% (or "Fit to page")
   - **Background graphics:** ON (Important!)

5. **Save the PDF**
   - Click "Save" or "Print"
   - Choose location and filename

### Browser-Specific Tips:

**Chrome/Edge:**
- Destination: "Save as PDF"
- More settings → Paper size: A3
- More settings → Margins: None
- More settings → Background graphics: ✓

**Firefox:**
- Print → Destination: "Save to PDF"
- Page Setup → Format & Options: A3, Landscape
- Print Backgrounds: ✓

**Safari:**
- PDF dropdown → "Save as PDF"
- Paper Size: A3
- Scale: 100%

---

## Method 2: Python Script (Alternative)

The `python3 generate_pdf.py` command generates an A3 PDF. Due to WeasyPrint's rendering engine, it may span 2 pages, but the dimensions are correct (420mm × 297mm).

**Note:** When printing this PDF on an A3 printer, it should print correctly as the page dimensions are accurate.

---

## Method 3: Online PDF Converter (If needed)

If you have a 2-page PDF from WeasyPrint:

1. Upload to an online PDF tool (e.g., ilovepdf.com, smallpdf.com)
2. Use "Merge PDF" or "Compress PDF" features
3. Select A3 landscape format
4. Download the optimized single-page result

---

## ✅ Verification

To verify your PDF is A3:

1. Open the PDF
2. Go to File → Properties (or Document Properties)
3. Check "Page Size" should show: **A3 (420 x 297 mm)** or **11.69 x 16.54 inches**

---

## 🎨 Poster Features

- **Size:** A3 Landscape (420mm × 297mm)
- **Borders:** 6mm outer border (dark blue), 1mm inner border (light blue)
- **Layout:** Professional 3-column academic poster
- **Content:** NAVIC Car Crash Detection System
- **Sections:** Problem, Motivation, Objectives, Architecture, Implementation, Results, Challenges, Future Scope
- **Colors:** Color-coded sections for visual clarity
- **Quality:** Print-ready, high-resolution

---

## 🖨️ Printing Tips

- **Paper:** Use A3-sized paper (420mm × 297mm or 11.69" × 16.54")
- **Orientation:** Landscape
- **Quality:** Best/Highest quality setting
- **Color:** Full color
- **Paper type:** Photo paper or heavyweight matte for best results

---

## 💡 Quick Start

**Fastest way to get your PDF:**

```bash
# Start server
python3 app.py

# Open browser to http://localhost:5000/poster

# Press Ctrl+P → Set to A3 Landscape → Save as PDF
```

Done! You now have a professional, single-page A3 PDF poster ready for printing!
