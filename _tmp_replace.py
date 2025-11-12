# -*- coding: utf-8 -*-
from pathlib import Path
path = Path('DiffTool.html')
text = path.read_text(encoding='utf-8')
start = text.index('  const buildDiff = ')
end = text.index('  const updateStats = ')
block = """  const buildDiff = (beforeObj, afterObj) => {\n    const beforeConds = toArray(beforeObj.conditions);\n    const afterConds = toArray(afterObj.conditions);\n    const { beforeStatus, afterStatus, stats } = evaluateStatuses(beforeConds, afterConds);\n    const summary = `\n      <div class=\"diff-summary\">\n        <span>\u6761\u4ef6\u7ec4\u6570\u91cf\uff1a${stats.before} \u2192 ${stats.after}</span>\n        <span>\u65b0\u589e ${stats.added} \u00b7 \u5220\u9664 ${stats.deleted} \u00b7 \u4fee\u6539 ${stats.modified}</span>\n      </div>\n    `;\n    const html = summary\n      + renderSection(\"\u4fee\u6539\u524d\", beforeConds, beforeStatus)\n      + renderSection(\"\u4fee\u6539\u540e\", afterConds, afterStatus);\n    return { html, stats };\n  };\n\n"""\npath.write_text(text[:start] + block + text[end:], encoding='utf-8')
