These hooks block Cursor from being added as co-author on commits.

To use them in this repo, run once:

  git config core.hooksPath .githooks

After that, all commits will automatically strip "Co-authored-by: Cursor <cursoragent@cursor.com>" from the message.
