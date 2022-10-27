# JSON Format


## General
```json
{
    "SITE": {
        "SET_NAME_ON_SITE": {
            "normal": "SET_NAME_TO_USE",
            "tokens": "SET_NAME_TO_USE_TOKENS"
        },
        // ...
    }
}
```

|  Name              | Notes               
|--------------------|---------------------
| SITE              | The site you want to associate the data with
| SET_NAME_ON_SITE  | The name of the set that the site uses
| normal | Key, used to identify the regular set to use most of the time
| SET_NAME_TO_USE | The name of the set that you want to use for the site, use Scryfall's naming and sorting convention
| tokens | Key, identify the tokens for the set 
| SET_NAME_TO_USE_TOKENS | Same thing as earlier, but for tokens

> Tokenless: Use ```null```
## Tokenless
```json
{
    "SITE": {
        "SET_NAME_ON_SITE": {
            "normal": "SET_NAME_TO_USE",
            "tokens": null
        },
        // ...
    }
}
```
- ABUGames does not purchase tokens
- CoolStuffInc and CardKingdom do, under the same name as the regular sets

## Example
```json
{
    "csi": {
        "Aether Revolt": {
            "normal": "Aether Revolt", 
            "tokens": "Aether Revolt"
            },
        "Black Bordered (foreign)": {
            "normal": "Foreign Black Border", 
            "tokens": null
            }, 
        "Set Name": {
            "normal": "SET_NAME_TO_USE", 
            "tokens": "SET_NAME_TO_USE_TOKENS"
        }
    },
    "ck": {
        "Aether Revolt": {
            "normal": "Aether Revolt", 
            "tokens": "Aether Revolt"
            },
        "Alara Reborn": {
            "normal": "Alara Reborn", 
            "tokens": "Alara Reborn"
            } 
    }
}
```
> Note: CK or ABU does not purchase Foreign Black Border. CSI has the set as an option on the site, but does not buy any as of 10/26/22