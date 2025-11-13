#!/bin/bash
# Quick Start Script for A3 Poster Generator

echo "======================================"
echo "   A3 Poster Generator - Quick Start"
echo "======================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python 3 is not installed"
    echo "Please install Python 3 first"
    exit 1
fi

echo "✅ Python 3 found"

# Check if Flask is installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "⚠️  Flask not found. Installing dependencies..."
    pip3 install -r requirements.txt --quiet
    echo "✅ Dependencies installed"
else
    echo "✅ Flask found"
fi

# Check if WeasyPrint is installed
if ! python3 -c "import weasyprint" 2>/dev/null; then
    echo "⚠️  WeasyPrint not found. Installing..."
    pip3 install weasyprint --quiet
    echo "✅ WeasyPrint installed"
else
    echo "✅ WeasyPrint found"
fi

echo ""
echo "🚀 Starting server..."
echo ""

python3 app.py
