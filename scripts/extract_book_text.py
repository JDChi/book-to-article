#!/usr/bin/env python3
"""Extract readable text from book files for the book-to-article skill."""

from __future__ import annotations

import argparse
import html
import re
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path


SUPPORTED_EXTENSIONS = {".txt", ".pdf", ".epub"}


class ExtractionError(RuntimeError):
    """Raised when a book file cannot be extracted."""


class HTMLTextExtractor(HTMLParser):
    BLOCK_TAGS = {
        "address",
        "article",
        "aside",
        "blockquote",
        "br",
        "div",
        "figcaption",
        "footer",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "li",
        "main",
        "p",
        "section",
        "td",
        "th",
        "tr",
    }

    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "nav"}:
            self.skip_depth += 1
        elif tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "nav"} and self.skip_depth:
            self.skip_depth -= 1
        elif tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.parts.append(data)

    def text(self) -> str:
        return html.unescape("".join(self.parts))


def read_text_file(path: Path) -> str:
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "gb18030", "big5", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    raise ExtractionError("Could not decode text file with common encodings.")


def extract_pdf(path: Path) -> str:
    errors: list[str] = []

    try:
        import pypdf  # type: ignore

        reader = pypdf.PdfReader(str(path))
        pages = []
        for index, page in enumerate(reader.pages, start=1):
            pages.append(f"\n[Page {index}]\n{page.extract_text() or ''}")
        return "\n".join(pages)
    except ImportError as exc:
        errors.append(f"pypdf unavailable: {exc}")
    except Exception as exc:  # pragma: no cover - depends on external PDFs
        errors.append(f"pypdf failed: {exc}")

    try:
        import PyPDF2  # type: ignore

        reader = PyPDF2.PdfReader(str(path))
        pages = []
        for index, page in enumerate(reader.pages, start=1):
            pages.append(f"\n[Page {index}]\n{page.extract_text() or ''}")
        return "\n".join(pages)
    except ImportError as exc:
        errors.append(f"PyPDF2 unavailable: {exc}")
    except Exception as exc:  # pragma: no cover - depends on external PDFs
        errors.append(f"PyPDF2 failed: {exc}")

    raise ExtractionError(
        "Could not extract PDF text. Install pypdf or provide EPUB/TXT. "
        + " | ".join(errors)
    )


def extract_epub(path: Path) -> str:
    try:
        with zipfile.ZipFile(path) as archive:
            names = [
                name
                for name in archive.namelist()
                if name.lower().endswith((".xhtml", ".html", ".htm"))
                and not name.lower().startswith("meta-inf/")
            ]
            if not names:
                raise ExtractionError("EPUB contains no HTML/XHTML content files.")

            sections = []
            for name in sorted(names):
                raw = archive.read(name)
                try:
                    markup = raw.decode("utf-8")
                except UnicodeDecodeError:
                    markup = raw.decode("utf-8", errors="replace")
                parser = HTMLTextExtractor()
                parser.feed(markup)
                text = normalize_text(parser.text())
                if text:
                    sections.append(f"\n[EPUB file: {name}]\n{text}")
            return "\n\n".join(sections)
    except zipfile.BadZipFile as exc:
        raise ExtractionError(f"Invalid EPUB archive: {exc}") from exc


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[\t\f\v ]+", " ", text)
    lines = [line.strip() for line in text.split("\n")]

    paragraphs: list[str] = []
    current: list[str] = []
    for line in lines:
        if not line:
            if current:
                paragraphs.append(" ".join(current).strip())
                current = []
            continue
        current.append(line)
    if current:
        paragraphs.append(" ".join(current).strip())

    return "\n\n".join(paragraph for paragraph in paragraphs if paragraph)


def extract(path: Path) -> str:
    extension = path.suffix.lower()
    if extension not in SUPPORTED_EXTENSIONS:
        supported = ", ".join(sorted(SUPPORTED_EXTENSIONS))
        raise ExtractionError(
            f"Unsupported file type '{extension or '(none)'}'. Supported types: {supported}."
        )

    if extension == ".txt":
        return read_text_file(path)
    if extension == ".pdf":
        return extract_pdf(path)
    if extension == ".epub":
        return extract_epub(path)

    raise ExtractionError(f"Unsupported file type '{extension}'.")


def default_output_path(source: Path) -> Path:
    return source.with_suffix(source.suffix + ".extracted.txt")


def build_output(source: Path, extracted_text: str) -> str:
    body = normalize_text(extracted_text)
    return f"# Extracted text from: {source.name}\n\n{body}\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract normalized plain text from a PDF, EPUB, or TXT book file."
    )
    parser.add_argument("source", type=Path, help="Path to the source book file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output .txt path. Defaults to '<source>.extracted.txt'.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    source = args.source.expanduser()

    if not source.exists():
        print(f"Input file does not exist: {source}", file=sys.stderr)
        return 1
    if not source.is_file():
        print(f"Input path is not a file: {source}", file=sys.stderr)
        return 1

    output = args.output.expanduser() if args.output else default_output_path(source)

    try:
        extracted_text = extract(source)
        output.write_text(build_output(source, extracted_text), encoding="utf-8")
    except ExtractionError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"File operation failed: {exc}", file=sys.stderr)
        return 1

    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
