from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"

class FrontendValidationTests(unittest.TestCase):
    def test_static_site_required_files_exist(self):
        for name in ("index.html", "style.css", "script.js"):
            self.assertTrue((SITE / name).is_file(), name)

    def test_index_references_local_assets(self):
        html = (SITE / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="style.css"', html)
        self.assertIn('src="script.js"', html)

    def test_index_has_document_structure(self):
        html = (SITE / "index.html").read_text(encoding="utf-8")
        self.assertRegex(html, r"<html\b")
        self.assertRegex(html, r"<head\b")
        self.assertRegex(html, r"<body\b")
        self.assertRegex(html, r"</html>")

    def test_visitor_counter_client_code_present(self):
        js = (SITE / "script.js").read_text(encoding="utf-8")
        self.assertIn("fetch(", js)
        self.assertRegex(js, r"visitor|counter")

if __name__ == "__main__":
    unittest.main()
