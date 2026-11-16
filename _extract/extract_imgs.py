import os
import pymupdf

base = r"c:\Users\anoyh\.cursor\projects\c-Users-anoyh-Documents-Landing-Page\attachments\bc33861a-2427-4b4d-bf26-2a8e2d1bf9aa"
out = r"c:\Users\anoyh\Documents\Landing Page\_extract\imgs"
os.makedirs(out, exist_ok=True)
files = ["MD_Razeen_DE.pdf", "Project_Suppoting_Documents.pdf", "Razeen_resume_.pdf"]
for fn in files:
    doc = pymupdf.open(os.path.join(base, fn))
    stem = fn.replace(".pdf", "")
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=pymupdf.Matrix(1.4, 1.4))
        pix.save(os.path.join(out, f"{stem}_p{i+1}.png"))
        print(fn, "page", i + 1, "size", page.rect)
        for img in page.get_images(full=True):
            xref = img[0]
            info = doc.extract_image(xref)
            w, h = info.get("width"), info.get("height")
            ext = info.get("ext")
            path = os.path.join(out, f"{stem}_p{i+1}_x{xref}.{ext}")
            with open(path, "wb") as f:
                f.write(info["image"])
            print(f"  xref {xref} {w}x{h} {ext} {len(info['image'])} bytes")
