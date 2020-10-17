import argparse

import confcrawl


def norm_conference_name(conference):
    if conference in ['emnlp', 'EMNLP', 'Empirical Methods in Natural Language Processing']:
        conference = 'emnlp'
    elif conference in ['acl', 'ACL', 'Association for Computational Linguistics']:
        raise NotImplementedError(f'{conference} is not supported yet')
    elif conference in ['naacl', 'NAACL', 'The North American Chapter of the Association for Computational Linguistics', 'North American Chapter of the Association for Computational Linguistics']:
        raise NotImplementedError(f'{conference} is not supported yet')
    else:
        raise ValueError(f'{conference} is an invalid input')
    return conference


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--conf', required=True, help="Name of the conference. e.g., emnlp, acl")
    parser.add_argument('--year', '-y', type=str, help="Year when the conference held. 4 digits required", required=True)
    parser.add_argument('--save-dir', '-s', type=str, help="Directory to save crawled table")
    args = parser.parse_args()

    conf = norm_conference_name(args.conf)

    module_name = f'{conf}_{args.year}'
    crawler = getattr(confcrawl, module_name)
    crawler(args.save_dir)
