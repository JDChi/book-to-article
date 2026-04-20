# Book to Article

**Turn a dense nonfiction book into a faithful long-form article.**

[简体中文](README.zh-CN.md)

Book to Article is an agent skill for reading book files and rewriting the important ideas into one substantial article. It is built for readers who want to learn from a book without receiving a chapter summary, a review, a score, or a list of quotes.

Give it a PDF, EPUB, or TXT book. It extracts the text, reads for the book's argument, compresses repetition, preserves the author's core claims, and writes a standalone Markdown article that can replace most casual reading of the original.

## Why It Exists

Many nonfiction books contain valuable ideas wrapped in repeated examples, long setup, and chapter structures designed for a full reading experience. This skill keeps the learning value and removes the drag.

It is especially useful for:

- Social-science and practical nonfiction.
- Books with strong concepts but repetitive examples.
- Turning a long book into an article you can actually finish.
- Learning the author's argument before deciding whether to read the full book.

## What You Get

By default, the skill writes one Markdown article:

```text
<book-stem>.article.md
```

The article is designed to:

- Stay faithful to the book's argument and conceptual structure.
- Rebuild the material as a readable essay, not a chapter-by-chapter summary.
- Compress repeated cases and long scene-setting.
- Explain key concepts through the author's reasoning.
- Avoid review-style judgments such as whether the book is worth reading.
- Reduce formulaic prose through a dedicated style revision pass.

For Chinese output, the default target length is usually 8,000-15,000 Chinese characters. For English output, it is usually 4,000-8,000 words.

## How To Use

If the skill is installed in an agent's skills directory:

```text
Use $book-to-article to turn /path/to/book.epub into a learning article.
```

If you are using this repository directly:

```text
Use the skill at ./SKILL.md to turn /path/to/book.epub into a learning article.
```

The final article is saved as Markdown, and the agent reports the output path instead of pasting the full article into chat.

## Supported Inputs

- `.pdf`
- `.epub`
- `.txt`

The bundled extraction helper can also be used directly:

```bash
python3 scripts/extract_book_text.py /path/to/book.epub
```

With an explicit output path:

```bash
python3 scripts/extract_book_text.py /path/to/book.epub --output /tmp/book.extracted.txt
```

PDF extraction uses `pypdf` when available and falls back to `PyPDF2`. EPUB extraction reads the archive's HTML/XHTML content and normalizes it into plain text.

## Repository Contents

```text
SKILL.md
agents/openai.yaml
scripts/extract_book_text.py
README.md
README.zh-CN.md
```

- `SKILL.md`: The actual skill instructions.
- `agents/openai.yaml`: Optional UI metadata for skill-aware environments.
- `scripts/extract_book_text.py`: Text extraction helper for PDF, EPUB, and TXT files.
