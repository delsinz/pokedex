pokemon.csv
- importHTML of tables on both http://pokemondb.net/pokedex/all and http://pokemondb.net/pokedex/stats/height-weight
- check rows lineup (by name comparison) and remove the few extra rows in the height-weight table
- add generation information (table is already in generation order, only have to look up start and end ids)

gen5.csv and gen6.csv
- clone pokemon.csv
- remove header
- remove all columns except first 2 (optional)
- swap first 2 columns
- duplicate file into gen5 and rename current gen6
- remove generation 6 pokemon in gen5.csv
- remove generations 1-5 pokemon in gen6.csv

hybrid.csv and separate.csv
- clone pokemon.csv
- use excel find and replace to strip height/weight into metre and kg values
- duplicate file into hybrid and rename current separate

hybrid.csv
- use excel trim+substitute functions to:
-- replace newline (in type) with "-"
-- replace " " (in name) with "-"
-- replace newline (in name) with "("
- use excel if/search functions to append ")" to end of cells containing "("
- search/replace types into standard form (alphabetical), e.g. Fire-Flying & Flying-Fire -> Fire-Flying

separate.csv
- run excel VBA macro (outlined in Excel-VBA-Split-Newline-Macro.txt) to split hybrids into 2 rows