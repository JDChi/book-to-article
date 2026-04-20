# Book to Article

**把一本厚书，改写成一篇忠实、可读、能真正学到东西的长文章。**

[English](README.md)

Book to Article 是一个面向 AI agent 的 skill。它面向 PDF、EPUB、TXT 这些书籍文件，目标不是写读书笔记、章节总结、书评、评分，也不是提炼几句金句，而是把一本非虚构书里的重要观点、概念、论证和必要案例，重写成一篇可以独立阅读的 Markdown 文章。

它适合这样的场景：你还没读过这本书，但想先获得这本书真正想教给你的东西；或者你觉得很多书篇幅太长、案例重复、铺垫过多，希望保留知识密度，把阅读体验压缩成一篇文章。

## 为什么需要它

很多非虚构书并不是没有价值，而是价值分散在大量铺垫、重复案例和章节结构里。直接总结会太薄，逐章梳理又太像笔记。这个 skill 走中间路线：认真读原书，重建作者的论证，再把它写成一篇自然的长文。

它尤其适合：

- 社科类、商业类、心理学类、方法论类非虚构书。
- 观点有价值但案例重复的书。
- 想先学习一本书的主要理解，再决定是否读原书。
- 想把厚书压缩成一篇更容易读完的文章。

## 它会产出什么

默认会生成一篇 Markdown 文章：

```text
<书名>.article.md
```

这篇文章会尽量做到：

- 忠实保留原书的核心论点和概念结构。
- 把内容重组为一篇文章，而不是逐章摘要。
- 压缩重复案例和过长铺垫。
- 用作者自己的论证逻辑解释关键概念。
- 不输出“是否值得读”“核心价值”“阅读评分”这类读书报告。
- 在最终写作前做一轮文体修订，减少固定句式和模板化表达。

中文输出默认长度通常是 8,000-15,000 字；英文输出通常是 4,000-8,000 words。除非你明确指定其他长度。

## 怎么使用

如果这个 skill 已经安装到 agent 的 skills 目录里，可以这样调用：

```text
Use $book-to-article to turn /path/to/book.epub into a learning article.
```

如果直接在这个仓库里使用，可以让 agent 指向本地 skill 文件：

```text
Use the skill at ./SKILL.md to turn /path/to/book.epub into a learning article.
```

最终文章会保存为 Markdown 文件。agent 只会在对话里告诉你输出路径，不会把整篇长文直接贴到聊天窗口里。

## 支持的输入格式

- `.pdf`
- `.epub`
- `.txt`

仓库里自带一个文本提取脚本：

```bash
python3 scripts/extract_book_text.py /path/to/book.epub
```

也可以指定输出路径：

```bash
python3 scripts/extract_book_text.py /path/to/book.epub --output /tmp/book.extracted.txt
```

PDF 会优先使用 `pypdf` 提取文本，失败时尝试 `PyPDF2`。EPUB 会读取压缩包中的 HTML/XHTML 内容，并整理成纯文本。

## 仓库内容

```text
SKILL.md
agents/openai.yaml
scripts/extract_book_text.py
README.md
README.zh-CN.md
```

- `SKILL.md`：skill 的核心说明，agent 实际执行时会读取它。
- `agents/openai.yaml`：可选的界面元数据，用于支持 skill 展示的环境。
- `scripts/extract_book_text.py`：PDF、EPUB、TXT 文本提取脚本。
