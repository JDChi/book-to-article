# Book to Article

`book-to-article` is an agent skill for turning a book file into a faithful learning article.

It is designed for cases where a user provides a nonfiction book, such as a PDF, EPUB, or TXT file, and wants the important argument, concepts, and examples rewritten into a standalone article. It is not meant to produce a chapter summary, book review, reading report, rating, or personal reflection.

## What It Produces

By default, the skill writes one substantial article to a Markdown file:

```text
<book-stem>.article.md
```

The article should:

- Preserve the book's main argument and conceptual structure.
- Compress repeated examples and long setup.
- Rebuild the material into article form instead of following chapters mechanically.
- Prefer paraphrase over quotation.
- Avoid adding claims not present in the book unless clearly marked as external context or inference.

For Chinese output, the default target length is usually 8,000-15,000 Chinese characters. For English output, it is usually 4,000-8,000 words.

## Repository Contents

```text
SKILL.md
agents/openai.yaml
scripts/extract_book_text.py
```

- `SKILL.md`: The actual skill instructions an agent should follow.
- `agents/openai.yaml`: Optional UI metadata for environments that support agent skill metadata.
- `scripts/extract_book_text.py`: A helper script that extracts readable text from supported book files before analysis.

## Text Extraction Script

The helper script supports:

- `.txt`
- `.pdf`
- `.epub`

Usage:

```bash
python3 scripts/extract_book_text.py /path/to/book.epub
```

With an explicit output path:

```bash
python3 scripts/extract_book_text.py /path/to/book.epub --output /tmp/book.extracted.txt
```

The script normalizes whitespace, keeps basic page or EPUB file markers where available, and writes a UTF-8 text file. PDF extraction uses `pypdf` when available and falls back to `PyPDF2`.

## Using the Skill

If this skill is installed in an agent's skills directory, invoke it as:

```text
Use $book-to-article to turn /path/to/book.epub into a learning article.
```

If using it directly from this repository, point the agent at the local skill file:

```text
Use the skill at ./SKILL.md to turn /path/to/book.epub into a learning article.
```

The skill should save the final article as Markdown and report the output path rather than pasting the full article into chat.
