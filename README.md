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


## TODOS
  [ ] extract photos, such as bmp, jpg, png ...etc 
  
  [ ] extract audio and video 


## Metric

CPU: intel i5-8400 CPU @ 2.80GHz

| page count | time cost (second) | speed |
| :--: | :--: | :--: | 
| 20  | 0.028  |   714 page/sec  | 
| 183 |  0.163 |  1122 page/sec  |
| 260 | 0.137  |  1897 page/sec |
