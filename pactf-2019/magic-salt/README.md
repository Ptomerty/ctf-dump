# The Magic Salt

DOCX files can be treated as ZIP files and unzipped to reveal its XML contents. Looking through the files, we find the string ``<!-- The salt is the name of the card at `s:A25 cn:50` -->`` in `document.xml`. Using the name of the document, `scryfall`, as a hint, we find that the salt is `counterspell`. 

Appending this salt and running a hash cracker through the provided card names yields us our flag.

### Flag: `siege-rhino`
