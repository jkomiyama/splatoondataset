# Splatoon Dataset

Splatoon dataset consisted of the results of online multi-player games. We gathered the results of about 400,000 Splatoon matches on Stat.ink from October 31, 2015 to January 30, 2016. 

* [Splatoon](https://www.nintendo.com/games/detail/splatoon-wii-u) - An official webpage of the Splatoon online game.
* [Stat.ink](https://stat.ink/) - An unofficial website where Splatoon match results are uploaded.

## Download

* [Match results: splatoon.tsv](https://www.dropbox.com/s/1w9yy5ajvoz2bs4/splatoon.tsv?dl=0) - An official webpage of the Splatoon online game.
* [Converted Patterns: splatoon.label](https://www.dropbox.com/s/7ld9t5jym3kzqdq/splatoon.label?dl=0) - We converted the players' weapons, ranks, and the features related to the battle arena into integers (items in terms of pattern mining).

### Other scripts (in this repo)

The following scripts are used in making the dataset.

* [fetch.sh](./fetch.sh) - A crawler for gathering match results.
* [extract_from_raw_data.py](./extract_from_raw_data.py) - Convert crawled data into splatoon.tsv.

## Acknowledgments

* If you use this dataset, please cite [paper name here](http://www.google.com)

