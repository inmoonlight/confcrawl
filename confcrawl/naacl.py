import logging
import os
from collections import defaultdict
from typing import Optional

import pandas as pd
import requests
from lxml import html
from tqdm.auto import tqdm

from .utils import root_dir, search_google

logger = logging.getLogger(__name__)


def naacl_2021(save_dir: Optional[str] = None) -> None:
    """Crawl NAACL 2021 Main Conference Accepted Papers

    returns crawled papers in tsv dataframe whose columns are "title, author, and arxiv link of the paper"
        e.g., A Bilingual Generative Transformer for Semantic Sentence Embedding
        John Wieting, Graham Neubig and Taylor Berg-Kirkpatrick
        https://arxiv.org/abs/1911.03895

    Args:
        save_dir: directory to save result_df
    """
    url = "https://2021.naacl.org/program/accepted/"
    result = defaultdict(list)
    save_dir = f"{root_dir}/result" if save_dir is None else save_dir
    os.makedirs(save_dir, exist_ok=True)

    r = requests.get(url)
    if r.ok:
        logger.info(
            "NAACL 2021 paper crawling successed! Now it is ready to be parsed!"
        )

    root = html.fromstring(r.text)
    titles = root.xpath('//*[@id="main"]/article/div/section/p/strong/text()')
    authors = root.xpath('//*[@id="main"]/article/div/section/p/text()')
    assert len(titles) == len(authors)

    num_main_conference_papers = 472
    titles = titles[:num_main_conference_papers]
    authors = authors[:num_main_conference_papers]

    for title, author in tqdm(zip(titles, authors), total=len(titles)):
        result["title"].append(title)
        result["author"].append(author)
        arxiv = search_google(title, sleep_time=1)
        result["arxiv"].append(arxiv)

    result_df = pd.DataFrame(result)
    save_path = f"{save_dir}/naacl_2021.tsv"
    result_df.to_csv(save_path, sep='\t', index=False)
