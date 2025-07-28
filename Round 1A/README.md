# Adobe Hackathon Round 1A - Score Optimized Solution

## 🚀 Features
- ✅ Smart Heading Detection (font size, bold, case, font family, position)
- ✅ Fast execution (CPU-only, <10 sec for 50 pages)
- ✅ Unicode / Multilingual PDF support (Japanese, Hindi, Arabic, etc.)
- ✅ Output JSON includes `execution_time_sec` for performance proof

## 🐳 Usage
### Build Image
docker build --platform linux/amd64 -t adobe-solution:round1a .

### Run
docker run --rm -v "%cd%\input:/app/input" -v "%cd%\output:/app/output" --network none adobe-solution:round1a