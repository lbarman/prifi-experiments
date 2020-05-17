# PriFi plots

This repository contains all raw data (and their derived plots) about experiments and benchmarks of [PriFi](https://github.com/dedis/prifi).

## Structure of this repo.

Please ignore the root folder! It only contains a bunch of scripts used by the sub-folders.

Go to, e.g., `fig3a-e2e-latency` (the numbering of the figures follow [the paper](https://arxiv.org/abs/1710.10237)) and examinate the `Makefile` to understand what is going on.

Structure of each subfolder:
- `config` : a copy of the `sda/simul` folder (in [PriFi](https://github.com/dedis/prifi)) at the time of the experiment; it contains all parameters
- `logs` : raw logs exported from the relay. Raw logs are `.txt` files

Most `Makefile`s do the same thing: 
1. parse the raw log into `JSON` format
2. extract the relevant lines (e.g., latency) into a separate files (e.g., `measured-latency.compiled`). Note: this is just a fancy `grep`, and the output is text
3. compute statistics (often: simply the mean of the value after the steady-state occurs, excluding obvious failures such as runs with timeouts, etc). This runs the `aggregate.js` main script with a `.json` (data source) and a `.js` (processor script). Creates a `yyy.gnudata` file that can be plotted
4. eps (runs gnuplot using the `xxx.gnuplot` script and the `yyy.gnudata` formatted input)
5. pdf (converts eps to pdf)

Author: Ludovic Barman
