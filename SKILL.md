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

## Inspection Pass

Before drafting, do an internal inspection pass. This is working material, not a user-facing report.

- Classify the book early: practical, theoretical, social-science, history, philosophy, science, memoir, or another dominant mode.
- Read the title, subtitle, preface, table of contents, introduction, conclusion, chapter openings, chapter endings, and any index or notes that reveal the structure.
- State the whole book in one sentence or a few sentences.
- Identify the main questions the author is trying to answer.
- Decide which parts require slow analytical reading and which parts are mainly setup, repetition, examples, or reinforcement.
- Keep moving through difficult passages on the first pass; mark them for return instead of letting them dominate the reading.

## Analytical Reading Method

Read to reconstruct the book's argument, not to list chapters.

- Answer four controlling questions internally: what the book is about as a whole, what the author says in detail and how, whether the claims hold together on the book's own terms, and what understanding the reader should take away.
- Identify the problem the book is trying to explain and any sub-problems the author separates from it.
- Outline the important parts of the book and how those parts compose the whole argument.
- Identify the author's main claims, core concepts, causal mechanisms, propositions, and recurring distinctions.
- Define key terms as the author uses them, especially when ordinary words are used in a specialized way.
- Reconstruct the author's argument chains: claim, reason, evidence, example, qualification, implication.
- Track the evidence and cases that are necessary for the argument.
- Distinguish solved problems, partially solved problems, and tensions the book leaves open.
- Mark repetitive examples, long scene-setting, and authorial self-defense as compressible material.
- Preserve important qualifications, tensions, and limits that affect the author's meaning.
- Do not criticize, modernize, or extend the author's position until the author's own meaning has been reconstructed.
- Prefer the author's conceptual structure over your own critique.

For long books, work in passes: first inspect and classify the whole book, then read analytically by section, then merge the notes into a single argument map before drafting.

## Genre Handling

Adjust reading emphasis to the book type.

- For practical books, preserve the problem, principles, procedures, warnings, and the conditions under which the advice is supposed to work.
- For theoretical books, preserve definitions, propositions, arguments, evidence, and conceptual distinctions.
- For social-science books, be especially careful with familiar terms that may carry the author's own meaning. Do not flatten them into common-sense slogans or import outside assumptions.
- For history and biography, preserve chronology only where it explains causality, development, or interpretation.
- For books with many anecdotes, keep only the cases that teach a concept, carry evidence, or change the reader's understanding.

## Article Shape

Write the article as a standalone learning piece for a reader who has not read the book.

Use this shape by default:

1. Title that names the central problem or insight, not just the book title.
2. Opening that establishes why the book's question matters.
3. A clear thesis that stays faithful to the original book.
4. Several sections that rebuild the argument in article order.
5. Key cases or examples only where they teach the concept or support the argument.
6. A closing section that explains what way of seeing or thinking the reader should take away.

The article may reorder the book when that improves learning, but it must not distort the author's claims.

Draft from the argument map, not from chapter order. The article should feel like a coherent essay that teaches the book's central understanding, while remaining visibly grounded in the book's own structure and claims.

Use the argument map internally, but do not expose it as a rigid outline. The final article should read like polished long-form prose, not lecture notes, study notes, a glossary, or a concept map.

- Prefer essay-like section titles over textbook-style concept labels.
- Introduce technical terms through the reader's problem or the author's reasoning before naming them.
- Avoid stacked definitions. Explain concepts by showing what problem they solve in the author's argument.
- Use transitions that show why the next idea follows, instead of simply moving from one concept to another.
- Keep the author's structure visible underneath the prose, but do not mirror the table of contents unless that is the most natural article order.

## Style Revision Pass

After drafting, revise once for prose variety before saving the file.

- Scan paragraph openings and remove repeated starts such as `The author...`, `The reader...`, `This is why...`, `The real problem is...`, or the same book-specific subject repeated across nearby paragraphs.
- Avoid leaning on a few explanatory frames. Use `not X but Y`, `the real...`, `the key is...`, `in other words`, and `this means...` only when they earn their place; do not let them become the article's rhythm.
- Vary sentence length and movement. Mix direct claims, concrete scenes, causal explanation, contrast, qualification, and short reflective pauses.
- Let adjacent paragraphs connect through meaning, not repeated formula. A transition can come from a question, an example, a consequence, a reversal, or a return to the reader's situation.
- Replace repeated abstract nouns with concrete referents when possible. Do not begin most paragraphs with the same role label, concept name, or author's name.
- Keep technical precision, but loosen the surface. The article should sound like a careful human essay, not a generated explanation optimized for clarity at the expense of cadence.
- If a passage uses the same syntactic pattern three times in close range, rewrite at least two of them.

## Output Workflow

Write the final article to a file by default. Do not paste a long full article into chat unless the user explicitly asks for inline output.

- Default output format: Markdown.
- Default output location: next to the source book when that directory is writable; otherwise use the current working directory.
- Default file name: `<book-stem>.article.md`, for example `trade-mindfully.article.md`.
- If the user provides an output path, use that path.
- Include follow-up topics only when the user explicitly asks for them. If included, place them at the end of the same Markdown file under `Follow-up article topics`.
- In the chat response, report the output file path and give a short note about extraction quality or any limitations. Do not duplicate the full article in chat.

## Writing Boundaries

Do:

- Write in the language requested by the user. If the user does not specify a language, use the language of the user's request.
- Keep the default main article substantial enough to replace most casual reading of the book: usually 8,000-15,000 Chinese characters for Chinese output, or 4,000-8,000 words for English output, unless the user requests another length.
- Be faithful and lightly editorial: compress and reorganize, but do not replace the author's argument with your own.
- Use connective explanation when needed for readers who have not read the book.
- Preserve readability and narrative flow. The article should feel natural to read even when the underlying reading work was analytical.
- Prefer paraphrase over quotation.
- Use short quotations only when the original wording is essential.

Do not:

- Output a chapter-by-chapter summary.
- Output a reading judgment report, score, "whether it is worth reading", or "core value" report.
- Write a book review, personal reflection, bullet-point note, or list of golden quotes.
- Write like a lecture handout, study guide, glossary, or outline.
- Add claims that are not in the book unless explicitly marked as external context or your own inference.
- Flatten complex social-science arguments into motivational slogans.
- Reproduce long passages from the book.

## Optional Follow-Up Topics

Include `Follow-up article topics` only if the user asks for follow-up topics or separate article ideas. Keep this section short: 3-5 titles with one-sentence angles.

Skip this section by default.

## Self-Check Before Answering

Before writing the final article file, check:

- Would a reader who has not read the book learn the central argument and the important concepts?
- Did the reading process answer what the book is about, how the author argues, what the important terms mean, and what understanding the reader should take away?
- Is the draft based on an argument map rather than a mechanical chapter sequence?
- Does the final prose hide the scaffolding well enough to read like an article rather than notes?
- Did the style revision pass reduce repeated paragraph openings, repeated explanatory frames, and repeated sentence shapes?
- Is the result an article rather than a summary, report, or review?
- Are repeated examples compressed without losing the reasoning they support?
- Are the author's claims distinguishable from any connective explanation or inference?
- Does the draft avoid long verbatim copying from the book?
- Does the length fit the agreed range or explicitly explain why it does not?
- Was the final article saved to a Markdown file, with the path reported to the user?
