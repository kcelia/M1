<bib>
  {
   for $b in document("bib.xml")/bib/book
    where $b/publisher = "Addison-Wesley" and $b/@year > 1991
    return
      <book year="{ $b/@year }">
        { $b/title }
      </book>
  }
</bib>
