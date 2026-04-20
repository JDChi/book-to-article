---
name: book-to-article
description: Use when the user provides or points to a book file, especially PDF, EPUB, or TXT, and asks to turn a book into an article, write a learning article from a book, or read a thick nonfiction/social-science book without producing a chapter summary, book review, reading report, rating, or personal reflection.
---

# Book to Article

## Overview

Turn a book into a faithful learning article. The goal is not to summarize, judge, or review the book; the goal is to let a reader who has not read the original learn the book's important ideas through a well-structured article.

Default output: one substantial main article written to a Markdown file, plus optional follow-up article topics only when the book naturally contains several separable themes.

## Input Workflow

1. Confirm the source is a book-like file or path. Supported first-pass formats are PDF, EPUB, and TXT.
2. Extract readable text before analyzing:

```bash
python3 <skill-dir>/scripts/extract_book_text.py /path/to/book.pdf
```

Use `--output /path/to/output.txt` when the output path should be explicit.

3. Inspect the extracted text for front matter, table of contents, chapters, conclusion, notes, obvious OCR damage, and missing sections.
4. If extraction fails or the text is badly damaged, explain the concrete extraction problem and ask for a better source file or a different format.
5. Do not use web search or external background by default. If external context is necessary, label it clearly as external context and keep it separate from the book's own claims.

## Reading Method

Read to reconstruct the book's argument, not to list chapters.

- Identify the problem the book is trying to explain.
- Identify the author's main claims, core concepts, causal mechanisms, and recurring distinctions.
- Track the evidence and cases that are necessary for the argument.
- Mark repetitive examples, long scene-setting, and authorial self-defense as compressible material.
- Preserve important qualifications, tensions, and limits that affect the author's meaning.
- Prefer the author's conceptual structure over your own critique.

For long books, work in passes: first map the structure, then process chapters or sections, then merge the notes into a single article outline before drafting.

## Article Shape

Write the article as a standalone learning piece for a reader who has not read the book.

Use this structure by default:

1. Title that names the central problem or insight, not just the book title.
2. Opening that establishes why the book's question matters.
3. A clear thesis that stays faithful to the original book.
4. Several sections that rebuild the argument in article order.
5. Key cases or examples only where they teach the concept or support the argument.
6. A closing section that explains what way of seeing or thinking the reader should take away.

The article may reorder the book when that improves learning, but it must not distort the author's claims.

## Output Workflow

Write the final article to a file by default. Do not paste a long full article into chat unless the user explicitly asks for inline output.

- Default output format: Markdown.
- Default output location: next to the source book when that directory is writable; otherwise use the current working directory.
- Default file name: `<book-stem>.article.md`, for example `trade-mindfully.article.md`.
- If the user provides an output path, use that path.
- If the article includes follow-up topics, place them at the end of the same Markdown file under `Follow-up article topics`.
- In the chat response, report the output file path and give a short note about extraction quality or any limitations. Do not duplicate the full article in chat.

## Writing Boundaries

Do:

- Write in the language requested by the user. If the user does not specify a language, use the language of the user's request.
- Keep the default main article substantial enough to replace most casual reading of the book: usually 8,000-15,000 Chinese characters for Chinese output, or 4,000-8,000 words for English output, unless the user requests another length.
- Be faithful and lightly editorial: compress and reorganize, but do not replace the author's argument with your own.
- Use connective explanation when needed for readers who have not read the book.
- Prefer paraphrase over quotation.
- Use short quotations only when the original wording is essential.

Do not:

- Output a chapter-by-chapter summary.
- Output a reading judgment report, score, "whether it is worth reading", or "core value" report.
- Write a book review, personal reflection, bullet-point note, or list of golden quotes.
- Add claims that are not in the book unless explicitly marked as external context or your own inference.
- Flatten complex social-science arguments into motivational slogans.
- Reproduce long passages from the book.

## Optional Follow-Up Topics

After the main article, include `Follow-up article topics` only if the book contains themes that would make useful separate articles. Keep this section short: 3-5 titles with one-sentence angles.

Skip this section when it would dilute the main article or when the user only asked for the article.

## Self-Check Before Answering

Before writing the final article file, check:

- Would a reader who has not read the book learn the central argument and the important concepts?
- Is the result an article rather than a summary, report, or review?
- Are repeated examples compressed without losing the reasoning they support?
- Are the author's claims distinguishable from any connective explanation or inference?
- Does the draft avoid long verbatim copying from the book?
- Does the length fit the agreed range or explicitly explain why it does not?
- Was the final article saved to a Markdown file, with the path reported to the user?
