# nanoretrotect

## INSTALLATION
```bash
pip install nanoretrotect
```

## USAGE
```bash
nanoretrotect [-h] [-v] [-t THREADS] [-o OUTDIR] [-p PREFIX]
                     [--verbose]
                     [-f {eps,jpeg,jpg,pdf,pgf,png,ps,raw,rgba,svg,svgz,tif,tiff}]
                     [--title TITLE] [--hours HOURS]
                     [--summary files [files ...]] [--bam files [files ...]]

Get detection curve of nanopore experiment.

General options:
  -h, --help            show the help and exit
  -v, --version         Print version and exit.
  -t, --threads THREADS
                        Set the allowed number of threads to be used by the script
  -o, --outdir OUTDIR   Specify directory in which output has to be created.
  -p, --prefix PREFIX   Specify an optional prefix to be used for the output files.

Options for customizing the plots created:
  -f, --format {eps,jpeg,jpg,pdf,pgf,png,ps,raw,rgba,svg,svgz,tif,tiff}
                        Specify the output format of the plots.
  --title TITLE         Add a title to all plots, requires quoting if using spaces
  --hours HOURS         How many hours to plot in the graph

Input data sources, requires a bam and a summary file.:
  --summary files [files ...]
                        Data is a summary file generated by albacore.
  --bam files [files ...]
                        Data as a sorted bam file.
```
