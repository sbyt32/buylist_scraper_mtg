# Information given by the .json file

|  Name              | Type          | Notes               
|--------------------|---------------|---------------------
|id                  |   str         | ? What ID does this correspond to?
|artist              |   [str]       |
|card_number         |   str         | * Card # in set
|card_style          |   [str]       | ? This might matter with foil / borderless / etc
|layout              |   str         | * This is for if double-faced cards, etc.
|magic_edition       |   [str]       |
|magic_edition_sort  |   str         | ? Why does this differ
|multiverse_id       |   [int]       | * Corresponds to a global method, use scryfall to match?
|display_title       |   str         | * Card title, on the site
|simple_title        |   str         | * Card title, in oracle
|buy_price           |   int         |
|trade_price         |   int         |