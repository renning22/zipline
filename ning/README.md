## Prerequisites
 * Copy "extension.py" to ~/.zipline/extension.py
 * Make sure data exist: ~/Documents/csvdir/minute/BTC_USD.csv

## Data ingest
```bash
zipline ingest -b custom-csvdir-bundle
```

## Backfill test in command line
```
zipline run -f test_zipline.py -b custom-csvdir-bundle --start 2016-1-1 --end 2016-1-1 --trading-calendar TWENTYFOURSEVEN --data-frequency minute
```

## In IPython Notebook
```python
%load_ext zipline
%pylab inline

%%zipline -b custom-csvdir-bundle --trading-calendar TWENTYFOURSEVEN --data-frequency minute --start 2016-1-1 --end 2016-5-1 --capital-base 1000 -o short_long_btc.pickle
```

## Example

[short_long.ipynb]()
