from typing import Optional
import logging
from collections import defaultdict
import os

import pandas as pd
import requests
from lxml import html
from tqdm.auto import tqdm

from .utils import search_google, root_dir

logger = logging.getLogger(__name__)


def emnlp_2020(save_dir: Optional[str] = None) -> None:
    """Crawl EMNLP 2020 Main Conference Accepted Papers

    returns crawled papers in tsv dataframe whose columns are "title, author, arxiv link, and type of the paper"
        e.g., A Bilingual Generative Transformer for Semantic Sentence Embedding
        John Wieting, Graham Neubig and Taylor Berg-Kirkpatrick
        https://arxiv.org/abs/1911.03895
        long

    Args:
        save_dir: directory to save result_df
    """
    url = "https://2020.emnlp.org/papers/main"
    result = defaultdict(list)
    save_dir = f'{root_dir}/result' if save_dir is None else save_dir
    os.makedirs(save_dir, exist_ok=True)

    r = requests.get(url)
    if r.ok:
        logger.info("EMNLP 2020 paper crawling successed! Now it is ready to be parsed!")

    root = html.fromstring(r.text)
    long_titles = root.xpath('/html/body/div/div/div/main/article/div/section[2]/section[1]/ul/li/article/span[1]/text()[1]')
    long_authors = root.xpath('/html/body/div/div/div/main/article/div/section[2]/section[1]/ul/li/article/span[2]/text()[1]')
    assert len(long_titles) == len(long_authors)
    short_titles = root.xpath('/html/body/div/div/div/main/article/div/section[2]/section[2]/ul/li/article/span[1]/text()[1]')
    short_authors = root.xpath('/html/body/div/div/div/main/article/div/section[2]/section[2]/ul/li/article/span[2]/text()[1]')
    assert len(short_titles) == len(short_authors)

    for long_title, long_author in tqdm(zip(long_titles, long_authors), desc='Long paper'):
        result['title'].append(long_title)
        result['author'].append(long_author)
        arxiv = search_google(long_title, sleep_time=2)
        result['arxiv'].append(arxiv)
        result['type'].append('long')

    for short_title, short_author in tqdm(zip(short_titles, short_authors), desc='Short paper'):
        result['title'].append(short_title)
        result['author'].append(short_author)
        arxiv = search_google(short_title, sleep_time=2)
        result['arxiv'].append(arxiv)
        result['type'].append('short')

    result_df = pd.DataFrame(result)
    save_path = f"{save_dir}/emnlp_2020.tsv"
    result_df.to_csv(save_path, sep='\t', index=False)
