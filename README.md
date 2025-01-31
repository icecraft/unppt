# unppt
An extremely fast tool which can extract text from MS-PPT file



## Install 

```bash
  git clone  https://github.com:icecraft/unppt
  cd unppt && pip install -r requirements.txt
  chmod +x bin/extractor
```

## Usage

```bash
Usage: main.py [OPTIONS]

Options:
  -p, --path PATH    ppt file path or directory which contains ppt files
                     [required]
  -o, --output PATH  output directory  [required]
  --help             Show this message and exit.

```


```bash 
  python main.py -p some.ppt -o output 
```

or 

```bash 
  python main.py -p some_directory -o output
```



## Metric

| page count | time cost (second) | speed |
| :--: | :--: | :--: | 
| 20 | 0.166|  120 page/sec  | 
| 183 |  7.0 |  26 page/sec  |
| 260 | 2.69  |  96 page/sec |
