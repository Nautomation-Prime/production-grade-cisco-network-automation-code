# Production-Grade Cisco Network Automation — code

Companion code for the book. Everything here runs; nothing here is a fragment
printed to fill a page.

## Layout

    spine/              one script, evolving from ch4 to ch33
    part2-foundations/  ch5-11
    part3-scaling/      ch12-16
    part4-principles/   ch17-28, one pattern per chapter

Part V's five systems live in their own repositories, linked from each chapter.
They are complete tools with their own history, not excerpts.

## The spine

`spine/` is the thing worth following. It starts in chapter 4 as twelve lines
of Netmiko that collect `show version` from three switches, and ends in chapter
33 as an IOS-XE upgrade orchestrator that can be pointed at four hundred
devices.

Every chapter that changes it has a tag:

    git diff ch04 ch22 -- spine/

That diff is the book's argument in one command — which is the one thing a
website cannot do, because every page has to stand alone.

## Running anything here

Python 3.11 or later.

    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

Chapter 3 covers lab options: Cisco DevNet Sandbox, CML, or Containerlab. Every
example runs against all three. Nothing here needs hardware.

## Conventions

- **Code lines stay under 55 characters.** The book is an ebook, and reflowable
  EPUB destroys Python indentation at large font sizes. CI enforces it.
- **Examples carry the guards the book argues for.** A chapter that argues for
  pre-flight checks is not followed by an example that skips them. Where a
  script would be dangerous in production, it refuses to run outside a lab
  rather than carrying a comment saying so.
- **No real credentials, anywhere.** Not in defaults, not in examples, not in
  tests. Chapter 4's script is the one deliberate exception: it hardcodes a lab
  password because that is one of the things wrong with it, and it carries a
  header saying so.

## Errata

Found a bug? Open an issue. Corrections reach readers quickly — the book is
versioned and revised continuously rather than in editions.

## Licence

MIT. Use any of it in your own estate without attribution.
