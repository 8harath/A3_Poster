const express = require('express');
const puppeteer = require('puppeteer');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));
app.use('/assets', express.static('assets'));

// Serve the main poster page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Generate A3 PDF endpoint
app.get('/generate-pdf', async (req, res) => {
    let browser;
    try {
        console.log('Starting PDF generation...');

        // Launch Puppeteer
        browser = await puppeteer.launch({
            headless: 'new',
            args: [
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-gpu'
            ]
        });

        const page = await browser.newPage();

        // Set viewport to A3 dimensions (at 96 DPI)
        // A3 = 297mm x 420mm = 1123px x 1587px at 96 DPI
        await page.setViewport({
            width: 1587,
            height: 1123,
            deviceScaleFactor: 2
        });

        // Navigate to the poster page
        const posterUrl = `http://localhost:${PORT}/poster`;
        await page.goto(posterUrl, {
            waitUntil: 'networkidle0',
            timeout: 30000
        });

        // Wait for images to load
        await page.waitForSelector('.poster', { timeout: 10000 });
        await page.evaluate(() => {
            return Promise.all(
                Array.from(document.images)
                    .filter(img => !img.complete)
                    .map(img => new Promise(resolve => {
                        img.onload = img.onerror = resolve;
                    }))
            );
        });

        // Generate PDF with A3 dimensions
        const pdf = await page.pdf({
            format: 'A3',
            landscape: true,
            printBackground: true,
            preferCSSPageSize: false,
            margin: {
                top: 0,
                right: 0,
                bottom: 0,
                left: 0
            }
        });

        await browser.close();

        console.log('PDF generated successfully!');

        // Send PDF as download
        res.setHeader('Content-Type', 'application/pdf');
        res.setHeader('Content-Disposition', 'attachment; filename=NAVIC_Car_Crash_Detection_Poster_A3.pdf');
        res.send(pdf);

    } catch (error) {
        console.error('PDF generation error:', error);
        if (browser) await browser.close();
        res.status(500).json({
            error: 'Failed to generate PDF',
            message: error.message
        });
    }
});

// Serve the poster HTML (without download button)
app.get('/poster', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'poster.html'));
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
    console.log(`Generate PDF at http://localhost:${PORT}/generate-pdf`);
});
