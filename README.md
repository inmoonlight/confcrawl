# Conference Paper Crawler (ConfCrawl)

Crawler for lazy paper hunters 😎 <br>

`A single command line` is all you need to get accepted paper lists along with their arXiv links, if available. <br>
Results are saved in `tsv` in `result` directory if not assigned. Below is an example of EMNLP 2020, which can be found in `result/emnlp_2020.tsv`:


title | author | arxiv | type
-- | -- | -- | -- 
A Bilingual Generative Transformer for Semantic Sentence Embedding | John Wieting, Graham Neubig and Taylor Berg-Kirkpatrick | https://arxiv.org/abs/1911.03895 | long
A Centering Approach for Discourse Structure-aware Coherence Modeling | Sungho Jeon and Michael Strube | N/A | long
A Computational Approach to Understanding Empathy Expressed in Text-Based Mental Health Support | Ashish Sharma, Adam Miner, David Atkins and Tim Althoff | N/A | long
||
Why Skip If You Can Combine: A Simple Knowledge Distillation Technique for Intermediate Layers| Yimeng Wu, Peyman Passban, Mehdi Rezagholizadeh and Qun Liu| https://arxiv.org/abs/2010.03034 | short
Within-Between Lexical Relation Classification using Path-based and Distributional Data| Oren Barkan, Avi Caciularu and Ido Dagan | N/A | short



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

To crawl emnlp 2020 accepted papers, type this single command:

```
$ python crawl.py --conf emnlp --year 2020
```
