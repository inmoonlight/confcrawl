# Conference Paper Crawler (ConfCrawl)

Crawler for lazy paper hunters 😎

## Currently provided conferences

conference | 2020 | 2021
-- | -- | --
EMNLP | Yes | TBD
ACL | No | TBD
NAACL | No | TBD
EACL | TBD | TBD

## Usage

```
$ python crawl.py [-h] --conf CONF --year YEAR [--save-dir SAVE_DIR]

optional arguments:
  -h, --help            show this help message and exit
  --conf CONF           Name of the conference. e.g., emnlp, acl
  --year YEAR, -y YEAR  Year when the conference held. 4 digits required
  --save-dir SAVE_DIR, -s SAVE_DIR
                        Directory to save crawled table
```

## Example

To crawl emnlp 2020 accepted papers, all you need is to type a single command:

```
$ python crawl.py --conf emnlp --year 2020
```
