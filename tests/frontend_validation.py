from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"

def test_static_site_required_files_exist():
    for name in ("index.html", "style.css", "script.js"):
        assert (SITE / name).is_file()

def test_index_references_local_assets():
    html = (SITE / "index.html").read_text(encoding="utf-8")
    assert 'href="style.css"' in html
    assert 'src="script.js"' in html

def test_index_has_document_structure():
    html = (SITE / "index.html").read_text(encoding="utf-8")
    assert re.search(r"<html\b", html, re.I)
    assert re.search(r"<head\b", html, re.I)
    assert re.search(r"<body\b", html, re.I)
    assert re.search(r"</html>", html, re.I)

def test_visitor_counter_client_code_present():
    js = (SITE / "script.js").read_text(encoding="utf-8")
    assert "fetch(" in js
    assert re.search(r"visitor|counter", js, re.I)
