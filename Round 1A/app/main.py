
import fitz
import os, time, json

def is_heading(text, size, font, flags):
    if len(text.strip()) < 2:
        return False
    if size >= 16: return True
    if text.isupper() and size >= 13: return True
    if text.istitle() and size >= 14: return True
    if "bold" in font.lower() and size >= 13: return True
    return False

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    headings = []
    max_size = 0
    title = os.path.splitext(os.path.basename(pdf_path))[0]

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span.get("text", "").strip()
                    size = span.get("size", 0)
                    font = span.get("font", "")
                    flags = span.get("flags", 0)

                    if not text:
                        continue
                    if size > max_size:
                        max_size = size
                        title = text

                    if is_heading(text, size, font, flags):
                        level = "H1" if size >= 16 else "H2" if size >= 14 else "H3"
                        headings.append({"level": level, "text": text, "page": page_num})
    return {"title": title, "outline": headings}

def main():
    for file in os.listdir("input"):
        if file.endswith(".pdf"):
            in_path = os.path.join("input", file)
            start = time.time()
            result = extract_outline(in_path)
            result["execution_time_sec"] = round(time.time() - start, 3)
            out_path = os.path.join("output", os.path.splitext(file)[0] + ".json")
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
