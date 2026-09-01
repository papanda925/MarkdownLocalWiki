from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path


repository_root = Path(__file__).resolve().parent.parent
hta_path = repository_root / "index.hta"
readme_path = repository_root / "README.md"

hta = hta_path.read_text(encoding="cp932")
readme = readme_path.read_text(encoding="utf-8")

inline_scripts = re.findall(
    r"<script(?:\s[^>]*)?>(.*?)</script>",
    hta,
    flags=re.IGNORECASE | re.DOTALL,
)
javascript = "\n".join(script for script in inline_scripts if script.strip())

with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as temp_file:
    temp_file.write(javascript)
    temp_path = Path(temp_file.name)

try:
    subprocess.run(["node", "--check", str(temp_path)], check=True)
finally:
    temp_path.unlink(missing_ok=True)

required_source_patterns = {
    "page-name validation": r"function\s+validatePageName\s*\(",
    "HTA-relative base folder": r"window\.location\.pathname",
    "textarea value saving": r"var\s+content\s*=\s*id\('textarea'\)\.value",
    "scoped current page": r"var\s+pagename\s*=\s*id\('headerH1'\)\.innerText",
    "protected top page": r"pagename\s*===\s*'トップページ'",
}

for label, pattern in required_source_patterns.items():
    if not re.search(pattern, hta):
        raise AssertionError(f"Missing {label}: {pattern}")

for heading in (
    "## 起動方法",
    "## セキュリティ上の注意",
    "## PowerShellローカルサーバー版への移行",
    "## 制限事項",
    "## トラブルシューティング",
):
    if heading not in readme:
        raise AssertionError(f"README is missing {heading}")

print("HTA JavaScript and repository conventions validated.")
