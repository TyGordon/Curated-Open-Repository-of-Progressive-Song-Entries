for $x in doc("full_corpus.xml")/bookstore/book
where $x/price>30
order by $x/title
return $x/title