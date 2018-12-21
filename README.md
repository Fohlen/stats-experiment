# stats-experiment

This is a tiny statistics experiment with data from [GENESIS](https://www-genesis.destatis.de/genesis/online).
I was challenging myself with prediction on data.

In order to use the actual data I had to do some pre-processing manually :unamused:

- strip unecessary and non-compliant CSV lines from the file
- replace broken encodings with `UTF-8`

## Get it running

I use `>= python3.7`
- `git clone https://github.com/Fohlen/stats-experiment.git`
- `cd stats-experiment`
- `python3 -m venv venv`
- `source ./venv/bin/activate`
- `pip install -r requirements.txt`
- `python3 plot.py` (only plotting)
