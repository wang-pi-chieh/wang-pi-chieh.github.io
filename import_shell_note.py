"""Import the saved HackMD Markdown as a static content entry (no runtime dependency)."""
import json
import re
import struct
from pathlib import Path
from markdown_it import MarkdownIt

source = Path('notes/shell-script.md').read_text(encoding='utf-8')
body = re.sub(r'^# Shell Script\s*\n', '', source, count=1)
body = re.sub(r'^### ', '## ', body, flags=re.M)
body = re.sub(r'^#### ', '### ', body, flags=re.M)
body = '## 基礎指令\n\n' + body
images = {
    'rJFGmXDHzl': 'shell-sed-trailing-slash',
    'ByZ4QmwrGl': 'shell-sed-result',
    'HJfaT1vBfl': 'shell-sed-spaces',
    'S1Z8xfDHGl': 'shell-terminal-test',
}
for image_id, name in images.items():
    body = body.replace(f'https://hackmd.io/_uploads/{image_id}.png', f'assets/notes/{name}.png')
html = MarkdownIt('commonmark', {'html': False, 'breaks': True}).render(body)
html = html.replace('<img ', '<img loading="lazy" ')
for name in images.values():
    data = Path(f'assets/notes/{name}.png').read_bytes()
    width, height = struct.unpack('>II', data[16:24])
    html = html.replace(f'src="assets/notes/{name}.png"', f'src="assets/notes/{name}.png" width="{width}" height="{height}"')
entry = {
    'id': 2,
    'title': 'Shell Script',
    'topic': 'Linux / Shell',
    'date': '自學筆記',
    'description': '整理 Shell 基礎指令、awk、grep、sed、測試條件、特殊變數與 find，用範例記下操作方式。',
    'featured': True,
    'sourceUrl': 'https://hackmd.io/@j6Nk1gJzRkKJDWn2RB3x3w/r1MSwoBrMg',
    'body': html,
}
p = Path('content.js')
text = p.read_text(encoding='utf-8')
marker = '// Imported Shell Script note; edit notes/shell-script.md and rerun import_shell_note.py.'
text = text.split('\n' + marker)[0].rstrip()
text += '\n' + marker + '\nportfolio.notes.push(' + json.dumps(entry, ensure_ascii=False) + ');\n'
p.write_text(text, encoding='utf-8')
print('Imported Shell Script note with', len(re.findall(r'<h[234]>', html)), 'headings.')
