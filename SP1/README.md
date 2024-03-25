## HDS SP1

## Postup řešení

Při zpracování semestrální práce jsem jako základní kámen vzal dodanou fonetickou abecedu,
podle které jsem sestavil základní pravidla.

Pravidla jsem se rozhodl napsat jako slovník, kdy klíčem je vždy regulární výraz a hodnotou pak odpovídající náhrada.

Rugulárními výrazy bylo možné pak uplatnit celou řadu pravidel. Jediná dvě pravidla byla uplatněna vně těchto výrazů.
První je rozdělení slov znakem "|", který byl proveden příkazem split() při předzpracování a následným 
spojením funkcí join() s definovaným oddělovačem "|". Druhé pravidlo je přidání pauzy na začátku věty. Znak 
"|$|" definující pauzu na počátku věty byl přidán díky předpokladu, že každá řádka obsahuje pouze jednu větu, na
počátek věty po přídání mezer mezi slovy ("|").

Pořadí vykonávání pravidel a některá samotná pravidla, která nebyla jasná z tabulky EPA jsem dále upravil dle kapitoly 
2.8 Fonetická transkripce češtiny v publikaci (PSUTKA, J., MÜLLER, L., MATOUŠEK, J., RADOVÁ, V. Mluvíme s počítačem česky. Academia,
Praha, 2006). Dle této knihy jsem přidal i další pravidla jako například použití rázu nebo asimilace.

## Postup spuštění skriptu

Díky použití regulárních výrazů není potřeba žádná speciální knihovna, protože knihovna re je již součástí pythonu.

Spuštění transkripce se tedy provede otevřením souboru "main.py", případnému upravení parametrů a 
následnému spuštění skriptu. 

Po úspěšném proběhnutí transkripce se výstup objeví v definovaném místě, v případě ponechání defaultních hodnot bude k nalezení ve složce "output".
